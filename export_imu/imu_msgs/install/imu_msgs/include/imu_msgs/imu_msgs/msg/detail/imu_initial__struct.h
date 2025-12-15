// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imu_msgs:msg/ImuInitial.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU_INITIAL__STRUCT_H_
#define IMU_MSGS__MSG__DETAIL__IMU_INITIAL__STRUCT_H_

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

/// Struct defined in msg/ImuInitial in the package imu_msgs.
typedef struct imu_msgs__msg__ImuInitial
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
} imu_msgs__msg__ImuInitial;

// Struct for a sequence of imu_msgs__msg__ImuInitial.
typedef struct imu_msgs__msg__ImuInitial__Sequence
{
  imu_msgs__msg__ImuInitial * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imu_msgs__msg__ImuInitial__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__IMU_INITIAL__STRUCT_H_
