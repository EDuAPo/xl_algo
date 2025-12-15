// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from imu_msgs:msg/ASENSING.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ASENSING__TRAITS_HPP_
#define IMU_MSGS__MSG__DETAIL__ASENSING__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "imu_msgs/msg/detail/asensing__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace imu_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ASENSING & msg,
  std::ostream & out)
{
  out << "{";
  // member: latitude
  {
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << ", ";
  }

  // member: longitude
  {
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << ", ";
  }

  // member: altitude
  {
    out << "altitude: ";
    rosidl_generator_traits::value_to_yaml(msg.altitude, out);
    out << ", ";
  }

  // member: north_velocity
  {
    out << "north_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.north_velocity, out);
    out << ", ";
  }

  // member: east_velocity
  {
    out << "east_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.east_velocity, out);
    out << ", ";
  }

  // member: ground_velocity
  {
    out << "ground_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.ground_velocity, out);
    out << ", ";
  }

  // member: roll
  {
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << ", ";
  }

  // member: pitch
  {
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << ", ";
  }

  // member: azimuth
  {
    out << "azimuth: ";
    rosidl_generator_traits::value_to_yaml(msg.azimuth, out);
    out << ", ";
  }

  // member: x_angular_velocity
  {
    out << "x_angular_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.x_angular_velocity, out);
    out << ", ";
  }

  // member: y_angular_velocity
  {
    out << "y_angular_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.y_angular_velocity, out);
    out << ", ";
  }

  // member: z_angular_velocity
  {
    out << "z_angular_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.z_angular_velocity, out);
    out << ", ";
  }

  // member: x_acc
  {
    out << "x_acc: ";
    rosidl_generator_traits::value_to_yaml(msg.x_acc, out);
    out << ", ";
  }

  // member: y_acc
  {
    out << "y_acc: ";
    rosidl_generator_traits::value_to_yaml(msg.y_acc, out);
    out << ", ";
  }

  // member: z_acc
  {
    out << "z_acc: ";
    rosidl_generator_traits::value_to_yaml(msg.z_acc, out);
    out << ", ";
  }

  // member: latitude_std
  {
    out << "latitude_std: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude_std, out);
    out << ", ";
  }

  // member: longitude_std
  {
    out << "longitude_std: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude_std, out);
    out << ", ";
  }

  // member: altitude_std
  {
    out << "altitude_std: ";
    rosidl_generator_traits::value_to_yaml(msg.altitude_std, out);
    out << ", ";
  }

  // member: north_velocity_std
  {
    out << "north_velocity_std: ";
    rosidl_generator_traits::value_to_yaml(msg.north_velocity_std, out);
    out << ", ";
  }

  // member: east_velocity_std
  {
    out << "east_velocity_std: ";
    rosidl_generator_traits::value_to_yaml(msg.east_velocity_std, out);
    out << ", ";
  }

  // member: ground_velocity_std
  {
    out << "ground_velocity_std: ";
    rosidl_generator_traits::value_to_yaml(msg.ground_velocity_std, out);
    out << ", ";
  }

  // member: roll_std
  {
    out << "roll_std: ";
    rosidl_generator_traits::value_to_yaml(msg.roll_std, out);
    out << ", ";
  }

  // member: pitch_std
  {
    out << "pitch_std: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch_std, out);
    out << ", ";
  }

  // member: azimuth_std
  {
    out << "azimuth_std: ";
    rosidl_generator_traits::value_to_yaml(msg.azimuth_std, out);
    out << ", ";
  }

  // member: ins_status
  {
    out << "ins_status: ";
    rosidl_generator_traits::value_to_yaml(msg.ins_status, out);
    out << ", ";
  }

  // member: position_type
  {
    out << "position_type: ";
    rosidl_generator_traits::value_to_yaml(msg.position_type, out);
    out << ", ";
  }

  // member: sec_of_week
  {
    out << "sec_of_week: ";
    rosidl_generator_traits::value_to_yaml(msg.sec_of_week, out);
    out << ", ";
  }

  // member: gps_week_number
  {
    out << "gps_week_number: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_week_number, out);
    out << ", ";
  }

  // member: temperature
  {
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
    out << ", ";
  }

  // member: wheel_speed_status
  {
    out << "wheel_speed_status: ";
    rosidl_generator_traits::value_to_yaml(msg.wheel_speed_status, out);
    out << ", ";
  }

  // member: heading_type
  {
    out << "heading_type: ";
    rosidl_generator_traits::value_to_yaml(msg.heading_type, out);
    out << ", ";
  }

  // member: numsv
  {
    out << "numsv: ";
    rosidl_generator_traits::value_to_yaml(msg.numsv, out);
    out << ", ";
  }

  // member: is_available
  {
    out << "is_available: ";
    rosidl_generator_traits::value_to_yaml(msg.is_available, out);
    out << ", ";
  }

  // member: utm_x
  {
    out << "utm_x: ";
    rosidl_generator_traits::value_to_yaml(msg.utm_x, out);
    out << ", ";
  }

  // member: utm_y
  {
    out << "utm_y: ";
    rosidl_generator_traits::value_to_yaml(msg.utm_y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ASENSING & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: latitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << "\n";
  }

  // member: longitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << "\n";
  }

  // member: altitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "altitude: ";
    rosidl_generator_traits::value_to_yaml(msg.altitude, out);
    out << "\n";
  }

  // member: north_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "north_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.north_velocity, out);
    out << "\n";
  }

  // member: east_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "east_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.east_velocity, out);
    out << "\n";
  }

  // member: ground_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ground_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.ground_velocity, out);
    out << "\n";
  }

  // member: roll
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << "\n";
  }

  // member: pitch
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << "\n";
  }

  // member: azimuth
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "azimuth: ";
    rosidl_generator_traits::value_to_yaml(msg.azimuth, out);
    out << "\n";
  }

  // member: x_angular_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_angular_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.x_angular_velocity, out);
    out << "\n";
  }

  // member: y_angular_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_angular_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.y_angular_velocity, out);
    out << "\n";
  }

  // member: z_angular_velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "z_angular_velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.z_angular_velocity, out);
    out << "\n";
  }

  // member: x_acc
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_acc: ";
    rosidl_generator_traits::value_to_yaml(msg.x_acc, out);
    out << "\n";
  }

  // member: y_acc
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_acc: ";
    rosidl_generator_traits::value_to_yaml(msg.y_acc, out);
    out << "\n";
  }

  // member: z_acc
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "z_acc: ";
    rosidl_generator_traits::value_to_yaml(msg.z_acc, out);
    out << "\n";
  }

  // member: latitude_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude_std: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude_std, out);
    out << "\n";
  }

  // member: longitude_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude_std: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude_std, out);
    out << "\n";
  }

  // member: altitude_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "altitude_std: ";
    rosidl_generator_traits::value_to_yaml(msg.altitude_std, out);
    out << "\n";
  }

  // member: north_velocity_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "north_velocity_std: ";
    rosidl_generator_traits::value_to_yaml(msg.north_velocity_std, out);
    out << "\n";
  }

  // member: east_velocity_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "east_velocity_std: ";
    rosidl_generator_traits::value_to_yaml(msg.east_velocity_std, out);
    out << "\n";
  }

  // member: ground_velocity_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ground_velocity_std: ";
    rosidl_generator_traits::value_to_yaml(msg.ground_velocity_std, out);
    out << "\n";
  }

  // member: roll_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "roll_std: ";
    rosidl_generator_traits::value_to_yaml(msg.roll_std, out);
    out << "\n";
  }

  // member: pitch_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch_std: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch_std, out);
    out << "\n";
  }

  // member: azimuth_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "azimuth_std: ";
    rosidl_generator_traits::value_to_yaml(msg.azimuth_std, out);
    out << "\n";
  }

  // member: ins_status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ins_status: ";
    rosidl_generator_traits::value_to_yaml(msg.ins_status, out);
    out << "\n";
  }

  // member: position_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position_type: ";
    rosidl_generator_traits::value_to_yaml(msg.position_type, out);
    out << "\n";
  }

  // member: sec_of_week
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sec_of_week: ";
    rosidl_generator_traits::value_to_yaml(msg.sec_of_week, out);
    out << "\n";
  }

  // member: gps_week_number
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gps_week_number: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_week_number, out);
    out << "\n";
  }

  // member: temperature
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
    out << "\n";
  }

  // member: wheel_speed_status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "wheel_speed_status: ";
    rosidl_generator_traits::value_to_yaml(msg.wheel_speed_status, out);
    out << "\n";
  }

  // member: heading_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "heading_type: ";
    rosidl_generator_traits::value_to_yaml(msg.heading_type, out);
    out << "\n";
  }

  // member: numsv
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "numsv: ";
    rosidl_generator_traits::value_to_yaml(msg.numsv, out);
    out << "\n";
  }

  // member: is_available
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_available: ";
    rosidl_generator_traits::value_to_yaml(msg.is_available, out);
    out << "\n";
  }

  // member: utm_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "utm_x: ";
    rosidl_generator_traits::value_to_yaml(msg.utm_x, out);
    out << "\n";
  }

  // member: utm_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "utm_y: ";
    rosidl_generator_traits::value_to_yaml(msg.utm_y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ASENSING & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace imu_msgs

namespace rosidl_generator_traits
{

[[deprecated("use imu_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const imu_msgs::msg::ASENSING & msg,
  std::ostream & out, size_t indentation = 0)
{
  imu_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use imu_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const imu_msgs::msg::ASENSING & msg)
{
  return imu_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<imu_msgs::msg::ASENSING>()
{
  return "imu_msgs::msg::ASENSING";
}

template<>
inline const char * name<imu_msgs::msg::ASENSING>()
{
  return "imu_msgs/msg/ASENSING";
}

template<>
struct has_fixed_size<imu_msgs::msg::ASENSING>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<imu_msgs::msg::ASENSING>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<imu_msgs::msg::ASENSING>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // IMU_MSGS__MSG__DETAIL__ASENSING__TRAITS_HPP_
