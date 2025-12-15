// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imu_msgs:msg/Imu04.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU04__STRUCT_H_
#define IMU_MSGS__MSG__DETAIL__IMU04__STRUCT_H_

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

/// Struct defined in msg/Imu04 in the package imu_msgs.
typedef struct imu_msgs__msg__Imu04
{
  std_msgs__msg__Header header;
  float roll;
  float pitch;
  float yaw;
  float gx;
  float gy;
  float gz;
  float ax;
  float ay;
  float az;
  float temperature;
  float time;
  uint8_t gps_message[14];
  uint8_t gps_heading_status;
  uint8_t ptype;
  uint16_t pdata;
  float ver_pos;
  float ver_vel;
  uint16_t info_byte;
  /// 0x00:deinit
  /// 0x01:动中通版本数据帧
  /// 0x02:VG版本数据帧
  /// 0x03:升沉版本数据帧
  uint8_t msg_type;
} imu_msgs__msg__Imu04;

// Struct for a sequence of imu_msgs__msg__Imu04.
typedef struct imu_msgs__msg__Imu04__Sequence
{
  imu_msgs__msg__Imu04 * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imu_msgs__msg__Imu04__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__IMU04__STRUCT_H_
