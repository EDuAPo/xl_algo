// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imu_msgs:msg/Odom.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ODOM__STRUCT_H_
#define IMU_MSGS__MSG__DETAIL__ODOM__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/Odom in the package imu_msgs.
typedef struct imu_msgs__msg__Odom
{
  std_msgs__msg__Header header;
  /// 四元数q0~q3
  float q0_w;
  float q1_x;
  float q2_y;
  float q3_z;
  /// 位置坐标
  float pos_x;
  float pos_y;
  float pos_z;
  /// 速度
  float vel_x;
  float vel_y;
  float vel_z;
  /// XYZ3个方向合速度
  float vel;
  /// 角速度
  float ang_vel_x;
  float ang_vel_y;
  float ang_vel_z;
  /// 加速度
  float acc_x;
  float acc_y;
  float acc_z;
  /// odom状态
  uint8_t status;
  /// 传感器状态
  uint32_t sensor_status;
  /// 位置信息精度
  float pos_x_std;
  float pos_y_std;
  float pos_z_std;
  /// 速度信息精度
  float vel_x_std;
  float vel_y_std;
  float vel_z_std;
  /// 姿态信息精度
  float roll_std;
  float pitch_std;
  float yaw_std;
  /// 周内秒毫秒
  uint32_t tow_ms;
} imu_msgs__msg__Odom;

// Struct for a sequence of imu_msgs__msg__Odom.
typedef struct imu_msgs__msg__Odom__Sequence
{
  imu_msgs__msg__Odom * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imu_msgs__msg__Odom__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__ODOM__STRUCT_H_
