#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import argparse
from datetime import datetime
import os
from pathlib import Path
import threading
import queue
import sys
from concurrent.futures import ThreadPoolExecutor

import cv2
import gi
import numpy as np
import time  # 用于时间戳fallback和性能监控
from datetime import datetime as dt_datetime  # 用于性能统计

from rosbags.highlevel import AnyReader
from rosbags.serde import deserialize_cdr

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

Gst.init(None)


ALL_CAMERA_H265_TOPICS = [
    '/camera/cam_8M_wa_front',
    '/camera/cam_8M_pt_front',
    '/camera/cam_3M_front',
    '/camera/cam_3M_left',
    '/camera/cam_3M_right',
    '/camera/cam_3M_rear',
]

def create_pipeline(topic_name_sanitized, use_hw_accel="auto"):
    """
    为每个topic创建一个GStreamer解码管道。
    use_hw_accel: 'nvidia', 'vaapi', or 'none'
    """
    # 软件解码（默认和备用选项）
    decoder = "avdec_h265"
    
    # 尝试选择硬件解码器
    if use_hw_accel == "nvidia":
        # 注意: NVIDIA管道可能需要更复杂的元素，如nvvidconv
        # 这只是一个基础示例，可能需要根据具体驱动和GStreamer版本微调
        decoder = "nvv4l2decoder"
        print(f"[{topic_name_sanitized}] Using NVIDIA hardware decoder.")
    elif use_hw_accel == "vaapi":
        decoder = "vaapih265dec"
        print(f"[{topic_name_sanitized}] Using VA-API hardware decoder.")
    else:
        print(f"[{topic_name_sanitized}] Using software decoder (avdec_h265).")

    pipeline_str = (
        f"appsrc name={topic_name_sanitized} format=time stream-type=stream caps=video/x-h265,stream-format=byte-stream,alignment=au ! "
        f"h265parse config-interval=1 ! {decoder} ! "
        "videoconvert ! video/x-raw,format=BGR ! "
        "appsink name=sink emit-signals=True max-buffers=1000 drop=True sync=false"
    )
    return Gst.parse_launch(pipeline_str)

def save_image_task(filepath, frame):
    """用于在线程池中执行的图像保存任务"""
    cv2.imwrite(filepath, frame)

def on_new_sample(sink, user_data):
    """appsink的回调函数，现在将保存任务提交给线程池"""
    output_dir, topic_name, counters, writer_pool = user_data  # 移除timestamps

    sample = sink.emit('pull-sample')
    if not sample: return Gst.FlowReturn.OK

    buf, caps = sample.get_buffer(), sample.get_caps()
    height = caps.get_structure(0).get_value('height')
    width = caps.get_structure(0).get_value('width')

    result, mapinfo = buf.map(Gst.MapFlags.READ)
    if result:
        try:
            timestamp = buf.pts  # 从PTS获取timestamp
            if timestamp == Gst.CLOCK_TIME_NONE:
                # Fallback: 如果PTS无效，用当前系统时间（纳秒）
                print(f"\n[{topic_name}] Warning: Invalid PTS, using current time.")
                timestamp = int(time.time_ns())  # 需要import time

            sec, nsec = timestamp // 1_000_000_000, timestamp % 1_000_000_000
            timestamp_sec = timestamp / 1e9
            dt = datetime.fromtimestamp(timestamp_sec)
            timestamp_str = dt.strftime("%Y%m%d_%H%M%S_%f")[:-3]  # 精确到毫秒

            filename = f"{timestamp_str}.jpg"
            filepath = os.path.join(output_dir, filename)
            
            frame = np.ndarray((height, width, 3), buffer=mapinfo.data, dtype=np.uint8)
            
            # 异步写入，必须复制frame
            writer_pool.submit(save_image_task, filepath, frame.copy())
            
            counters['decoded'] += 1
            if counters['decoded'] % 50 == 0:  # 优化：每50帧打印一次
                current_time = time.time()
                elapsed = current_time - counters['start_time']
                interval = current_time - counters['last_print_time']
                frames_in_interval = counters['decoded'] - counters['last_decoded_count']
                
                # 计算速率
                overall_fps = counters['decoded'] / elapsed if elapsed > 0 else 0
                interval_fps = frames_in_interval / interval if interval > 0 else 0
                
                print(f"\r[{topic_name}] 已解码: {counters['decoded']} 帧 | "
                      f"总速率: {overall_fps:.2f} fps | "
                      f"当前速率: {interval_fps:.2f} fps | "
                      f"总耗时: {elapsed:.1f}s", end='')
                
                counters['last_print_time'] = current_time
                counters['last_decoded_count'] = counters['decoded']
        except Exception as e:  # 通用捕获，替换原Empty异常
            print(f"\n[{topic_name}] Error in callback: {e}", file=sys.stderr)
        finally:
            buf.unmap(mapinfo)
    return Gst.FlowReturn.OK

def decode_worker(topic_name, data_queue, base_output_dir, hw_accel_flag):
    """解码工作线程，现在包含一个用于写入的线程池"""
    topic_name_sanitized = topic_name.replace('/', '_')
    topic_name_sanitized = topic_name_sanitized.lstrip('_')
    output_dir = os.path.join(base_output_dir, topic_name_sanitized)
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"[{topic_name}] Worker started. Outputting to: {output_dir}")

    main_loop = GLib.MainLoop()
    counters = {
        'pushed': 0, 
        'decoded': 0,
        'start_time': time.time(),  # 性能监控：开始时间
        'last_print_time': time.time(),  # 性能监控：上次打印时间
        'last_decoded_count': 0  # 性能监控：上次解码数量
    }
    # 创建一个最多有12个线程的写入池，限制队列大小防止内存泄漏
    from concurrent.futures import ThreadPoolExecutor
    import threading
    writer_pool = ThreadPoolExecutor(max_workers=12, thread_name_prefix="ImgWriter")
    
    pipeline = create_pipeline(topic_name_sanitized, hw_accel_flag)
    
    user_data_for_callback = (output_dir, topic_name, counters, writer_pool)  # 移除timestamps
    sink = pipeline.get_by_name('sink')
    sink.connect("new-sample", on_new_sample, user_data_for_callback)

    bus = pipeline.get_bus()
    bus.add_signal_watch()
    def on_bus_message(bus, message):
        t = message.type
        if t == Gst.MessageType.EOS:
            print(f"\n[{topic_name}] Received EOS from pipeline.")
            main_loop.quit()
        elif t == Gst.MessageType.ERROR:
            err, debug = message.parse_error()
            print(f"\n[{topic_name}] GStreamer Error: {err}. {debug}", file=sys.stderr)
            main_loop.quit()
        return True
    bus.connect("message", on_bus_message)

    appsrc = pipeline.get_by_name(topic_name_sanitized)
    appsrc.set_property('is-live', False)
    appsrc.set_property('max-bytes', 10485760)  # 优化：10MB缓冲区，减少内存碎片
    appsrc.set_property('block', True)   # push-buffer 阻塞直到消费
    appsrc.set_property('format', Gst.Format.TIME)
    appsrc.set_property('emit-signals', True)

    pipeline.set_state(Gst.State.PLAYING)
    loop_thread = threading.Thread(target=main_loop.run, daemon=True)
    loop_thread.start()

    try:
        while True:
            item = data_queue.get()
            if item is None: break
            
            timestamp, h265_data = item
            counters['pushed'] += 1
            buf = Gst.Buffer.new_wrapped(h265_data)
            buf.pts = timestamp  # 设置PTS（纳秒单位，直接赋值）
            buf.dts = Gst.CLOCK_TIME_NONE  # 可选：decode timestamp，通常不需设置
            appsrc.emit('push-buffer', buf)
    except Exception as e:
        print(f"[{topic_name}] Error in push loop: {e}", file=sys.stderr)

    print(f"[{topic_name}] Sending EOS to appsrc...")
    appsrc.emit('end-of-stream')

    print(f"[{topic_name}] Waiting for pipeline to finish (max 10s)...")
    loop_thread.join(timeout=10.0)

    if loop_thread.is_alive():
        print(f"[{topic_name}] Pipeline did not exit in time. Forcing quit...")
        main_loop.quit()
        loop_thread.join(timeout=2.0)

    # 等待所有写入任务完成
    writer_pool.shutdown(wait=True)

    pipeline.set_state(Gst.State.NULL)
    
    total_time = time.time() - counters['start_time']
    avg_fps = counters['decoded'] / total_time if total_time > 0 else 0
    
    print(f"\r[{topic_name}] Finalizing...")
    print(f"\n{'='*60}")
    print(f"📊 性能统计 - Topic: {topic_name}")
    print(f"{'='*60}")
    print(f"  推送帧数: {counters['pushed']}")
    print(f"  解码成功: {counters['decoded']}")
    print(f"  总耗时: {total_time:.2f} 秒")
    print(f"  平均速率: {avg_fps:.2f} fps")
    print(f"  平均每帧: {1000/avg_fps:.2f} ms" if avg_fps > 0 else "  平均每帧: N/A")
    print(f"{'='*60}")

def get_all_bags(input_path):
    """获取所有bag目录，支持单目录和多目录模式"""
    bag_root = os.path.abspath(input_path)
    bag_paths = []
    
    # 检查输入路径本身是否是一个bag目录（包含metadata.yaml）
    meta_file = os.path.join(bag_root, "metadata.yaml")
    if os.path.exists(meta_file):
        print(f"✅ 输入路径是单个bag目录：{bag_root}")
        bag_paths.append(Path(bag_root))
        return bag_paths
    
    # 否则，按原逻辑遍历子目录
    print(f"📁 按多目录模式处理：遍历 {bag_root} 的子目录")
    for entry in sorted(os.listdir(bag_root)):
        bag_path = os.path.join(bag_root, entry)
        if not os.path.isdir(bag_path):
            continue
        
        meta_file = os.path.join(bag_path, "metadata.yaml")
        if not os.path.exists(meta_file):
            continue
        
        bag_paths.append(Path(bag_path))
    
    print(f"找到 {len(bag_paths)} 个bag目录")
    return bag_paths

def rename_topic(topic_name):
    topic_name_sanitized = topic_name.replace('/', '_')
    topic_name_sanitized = topic_name_sanitized.lstrip('_')
    return topic_name_sanitized

def main():
    parser = argparse.ArgumentParser(
        description="Decode H.265 data from multiple continuous ROS2 bags.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("--bag", required=True, help="要导出ROS2 bag 的根目录，里面包含多个 bag 子目录")
    parser.add_argument("--out", required=True, help="输出根目录,目录若存在将会删除")

    parser.add_argument("--hwaccel", type=str, default="none", choices=['none', 'nvidia', 'vaapi'], 
                        help="Specify hardware acceleration method.")
    args = parser.parse_args()

    threads, data_queues = {}, {}

    print(f"Starting bag file processing with hardware acceleration: {args.hwaccel}")
    # 打印将要按顺序处理的所有bag文件
    print(f"Input bags (will be processed in this order): {args.bag}")

    out_dir = os.path.abspath(args.out)
    input_bag_dir = os.path.abspath(args.bag)
    if input_bag_dir == out_dir:
        print(f"Error: Output directory '{out_dir}' cannot be the same as input bag directory '{input_bag_dir}'.", file=sys.stderr)
        sys.exit(1)

    # 如果输出目录存在，则先删除
    for topic in ALL_CAMERA_H265_TOPICS:
        topic_name_sanitized = rename_topic(topic)
        topic_output_dir = os.path.join(out_dir, topic_name_sanitized)
        if os.path.exists(topic_output_dir):
            print(f"Output directory for topic '{topic}' exists at '{topic_output_dir}'. Deleting...")
            import shutil
            shutil.rmtree(topic_output_dir)
            os.makedirs(topic_output_dir, exist_ok=True)

    bag_paths = get_all_bags(args.bag)

    try:
        with AnyReader(bag_paths) as reader:
            
            # 这个循环现在会无缝地遍历所有bag文件中的所有消息
            for connection, timestamp, rawdata in reader.messages():
                if connection.msgtype != 'sensor_msgs/msg/Image': continue
                topic_name = connection.topic
                if topic_name not in ALL_CAMERA_H265_TOPICS:
                    print(f"\nSkipping topic: {topic_name}")
                    continue
                
                # 线程和管线只在第一次遇到topic时创建
                if topic_name not in threads:
                    print(f"\nDiscovered new topic: {topic_name}. Starting worker thread.")
                    q = queue.Queue(maxsize=1000)
                    data_queues[topic_name] = q
                    # 这个线程将存活，直到所有bag文件都被处理完毕
                    thread = threading.Thread(target=decode_worker, args=(topic_name, q, args.out, args.hwaccel))
                    threads[topic_name] = thread
                    thread.start()

                msg = reader.deserialize(rawdata, connection.msgtype)  # 修复DeprecationWarning
                # 持续推送数据，无需关心它来自哪个bag文件
                data_queues[topic_name].put((timestamp, msg.data.tobytes()))

    except Exception as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
    finally:
        # 这个 'finally' 块只在所有bag文件都被处理完毕后才会执行
        print("\nEnd of all bag files reached. Signaling worker threads to finalize...")
        for q in data_queues.values(): q.put(None)
        for t in threads.values(): t.join()
        print(f"\nAll decoding threads have finished. Program terminated. Output is in '{args.out}'")

if __name__ == '__main__':
    main()