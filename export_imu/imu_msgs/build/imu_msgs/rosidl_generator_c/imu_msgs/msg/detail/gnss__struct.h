// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imu_msgs:msg/Gnss.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__GNSS__STRUCT_H_
#define IMU_MSGS__MSG__DETAIL__GNSS__STRUCT_H_

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
// Member 'utc_time'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Gnss in the package imu_msgs.
typedef struct imu_msgs__msg__Gnss
{
  std_msgs__msg__Header header;
  double longitude;
  float lon_sigma;
  double latitude;
  float lat_sigma;
  double altitude;
  float alt_sigma;
  uint16_t gps_fix;
  uint16_t rtk_age;
  uint8_t flags_pos;
  uint8_t flags_vel;
  uint8_t flags_attitude;
  uint8_t flags_time;
  float hor_vel;
  float track_angle;
  float ver_vel;
  float latency_vel;
  float base_length;
  float yaw;
  float yaw_sigma;
  float pitch;
  float pitch_sigma;
  rosidl_runtime_c__String utc_time;
  uint32_t ts_pos;
  uint32_t ts_vel;
  uint32_t ts_heading;
  uint8_t state;
  uint8_t num_master;
  float gdop;
  float pdop;
  float hdop;
  float htdop;
  float tdop;
  uint8_t num_reserve;
} imu_msgs__msg__Gnss;

// Struct for a sequence of imu_msgs__msg__Gnss.
typedef struct imu_msgs__msg__Gnss__Sequence
{
  imu_msgs__msg__Gnss * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imu_msgs__msg__Gnss__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__GNSS__STRUCT_H_
