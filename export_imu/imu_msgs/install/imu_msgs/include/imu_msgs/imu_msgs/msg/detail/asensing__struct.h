// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from imu_msgs:msg/ASENSING.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ASENSING__STRUCT_H_
#define IMU_MSGS__MSG__DETAIL__ASENSING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ASENSING in the package imu_msgs.
typedef struct imu_msgs__msg__ASENSING
{
  double latitude;
  double longitude;
  double altitude;
  double north_velocity;
  double east_velocity;
  double ground_velocity;
  /// deg
  double roll;
  /// [-180,180]deg
  double pitch;
  /// [-180,180]deg,正北顺时针到正南为正0-180°
  double azimuth;
  double x_angular_velocity;
  double y_angular_velocity;
  double z_angular_velocity;
  double x_acc;
  double y_acc;
  double z_acc;
  float latitude_std;
  float longitude_std;
  float altitude_std;
  float north_velocity_std;
  float east_velocity_std;
  float ground_velocity_std;
  float roll_std;
  float pitch_std;
  float azimuth_std;
  uint32_t ins_status;
  uint32_t position_type;
  double sec_of_week;
  double gps_week_number;
  float temperature;
  uint32_t wheel_speed_status;
  uint32_t heading_type;
  uint32_t numsv;
  bool is_available;
  double utm_x;
  double utm_y;
} imu_msgs__msg__ASENSING;

// Struct for a sequence of imu_msgs__msg__ASENSING.
typedef struct imu_msgs__msg__ASENSING__Sequence
{
  imu_msgs__msg__ASENSING * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} imu_msgs__msg__ASENSING__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__ASENSING__STRUCT_H_
