// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imu_msgs:msg/Imu8B.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU8_B__STRUCT_H_
#define IMU_MSGS__MSG__DETAIL__IMU8_B__STRUCT_H_

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

/// Struct defined in msg/Imu8B in the package imu_msgs.
typedef struct imu_msgs__msg__Imu8B
{
  std_msgs__msg__Header header;
  uint8_t type;
  uint16_t data_length;
  uint32_t frame_count;
  uint8_t serial_number;
  float gx;
  float gy;
  float gz;
  float ax;
  float ay;
  float az;
  float temperature;
  uint8_t status;
} imu_msgs__msg__Imu8B;

// Struct for a sequence of imu_msgs__msg__Imu8B.
typedef struct imu_msgs__msg__Imu8B__Sequence
{
  imu_msgs__msg__Imu8B * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imu_msgs__msg__Imu8B__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__IMU8_B__STRUCT_H_
