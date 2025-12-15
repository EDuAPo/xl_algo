
python3 ./export_camera.py --bag /home/shucdong/workspace/dataset/test/camera_bags/ --out /home/shucdong/workspace/dataset/test/test_export_camera/

python3 ./export_lidar.py --bag /home/shucdong/workspace/dataset/test/camera_bags/ --out /home/shucdong/workspace/dataset/test/test_export_camera/ --format pcd_binary

python3 ./export_imu.py --bag /home/shucdong/workspace/dataset/test/camera_bags/ --out /home/shucdong/workspace/dataset/test/test_export_camera/ins.json

python3 ./undistortion.py --images /home/shucdong/workspace/dataset/test/test_export_camera --params /home/shucdong/workspace/xl/bag_parser/export_ros2bag/export_camera/undistortion/intrinsic_param --vehicle vehicle_000 --out /home/shucdong/workspace/dataset/test/test_export_camera/undistorted --scale_min 0.2 --logtime 20251104_160012


adjust dir

extract sampl