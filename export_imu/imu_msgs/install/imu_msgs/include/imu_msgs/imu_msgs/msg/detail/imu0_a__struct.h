// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imu_msgs:msg/Imu0A.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU0_A__STRUCT_H_
#define IMU_MSGS__MSG__DETAIL__IMU0_A__STRUCT_H_

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

/// Struct defined in msg/Imu0A in the package imu_msgs.
typedef struct imu_msgs__msg__Imu0A
{
  std_msgs__msg__Header header;
  float gx;
  float gy;
  float gz;
  float ax;
  float ay;
  float az;
  float temperature;
  double imu_time_stamp;
  uint8_t status;
  uint16_t frame_count;
} imu_msgs__msg__Imu0A;

// Struct for a sequence of imu_msgs__msg__Imu0A.
typedef struct imu_msgs__msg__Imu0A__Sequence
{
  imu_msgs__msg__Imu0A * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imu_msgs__msg__Imu0A__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__IMU0_A__STRUCT_H_
