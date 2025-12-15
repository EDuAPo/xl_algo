// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imu_msgs:msg/Imu.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU__STRUCT_H_
#define IMU_MSGS__MSG__DETAIL__IMU__STRUCT_H_

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
// Member 'imu_msg'
#include "imu_msgs/msg/detail/asensing__struct.h"

/// Struct defined in msg/Imu in the package imu_msgs.
typedef struct imu_msgs__msg__Imu
{
  std_msgs__msg__Header header;
  imu_msgs__msg__ASENSING imu_msg;
} imu_msgs__msg__Imu;

// Struct for a sequence of imu_msgs__msg__Imu.
typedef struct imu_msgs__msg__Imu__Sequence
{
  imu_msgs__msg__Imu * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imu_msgs__msg__Imu__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__IMU__STRUCT_H_
