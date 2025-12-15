// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from imu_msgs:msg/Odom.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ODOM__TRAITS_HPP_
#define IMU_MSGS__MSG__DETAIL__ODOM__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "imu_msgs/msg/detail/odom__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace imu_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Odom & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: q0_w
  {
    out << "q0_w: ";
    rosidl_generator_traits::value_to_yaml(msg.q0_w, out);
    out << ", ";
  }

  // member: q1_x
  {
    out << "q1_x: ";
    rosidl_generator_traits::value_to_yaml(msg.q1_x, out);
    out << ", ";
  }

  // member: q2_y
  {
    out << "q2_y: ";
    rosidl_generator_traits::value_to_yaml(msg.q2_y, out);
    out << ", ";
  }

  // member: q3_z
  {
    out << "q3_z: ";
    rosidl_generator_traits::value_to_yaml(msg.q3_z, out);
    out << ", ";
  }

  // member: pos_x
  {
    out << "pos_x: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x, out);
    out << ", ";
  }

  // member: pos_y
  {
    out << "pos_y: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y, out);
    out << ", ";
  }

  // member: pos_z
  {
    out << "pos_z: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_z, out);
    out << ", ";
  }

  // member: vel_x
  {
    out << "vel_x: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_x, out);
    out << ", ";
  }

  // member: vel_y
  {
    out << "vel_y: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_y, out);
    out << ", ";
  }

  // member: vel_z
  {
    out << "vel_z: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_z, out);
    out << ", ";
  }

  // member: vel
  {
    out << "vel: ";
    rosidl_generator_traits::value_to_yaml(msg.vel, out);
    out << ", ";
  }

  // member: ang_vel_x
  {
    out << "ang_vel_x: ";
    rosidl_generator_traits::value_to_yaml(msg.ang_vel_x, out);
    out << ", ";
  }

  // member: ang_vel_y
  {
    out << "ang_vel_y: ";
    rosidl_generator_traits::value_to_yaml(msg.ang_vel_y, out);
    out << ", ";
  }

  // member: ang_vel_z
  {
    out << "ang_vel_z: ";
    rosidl_generator_traits::value_to_yaml(msg.ang_vel_z, out);
    out << ", ";
  }

  // member: acc_x
  {
    out << "acc_x: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_x, out);
    out << ", ";
  }

  // member: acc_y
  {
    out << "acc_y: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_y, out);
    out << ", ";
  }

  // member: acc_z
  {
    out << "acc_z: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_z, out);
    out << ", ";
  }

  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: sensor_status
  {
    out << "sensor_status: ";
    rosidl_generator_traits::value_to_yaml(msg.sensor_status, out);
    out << ", ";
  }

  // member: pos_x_std
  {
    out << "pos_x_std: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x_std, out);
    out << ", ";
  }

  // member: pos_y_std
  {
    out << "pos_y_std: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y_std, out);
    out << ", ";
  }

  // member: pos_z_std
  {
    out << "pos_z_std: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_z_std, out);
    out << ", ";
  }

  // member: vel_x_std
  {
    out << "vel_x_std: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_x_std, out);
    out << ", ";
  }

  // member: vel_y_std
  {
    out << "vel_y_std: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_y_std, out);
    out << ", ";
  }

  // member: vel_z_std
  {
    out << "vel_z_std: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_z_std, out);
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

  // member: yaw_std
  {
    out << "yaw_std: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_std, out);
    out << ", ";
  }

  // member: tow_ms
  {
    out << "tow_ms: ";
    rosidl_generator_traits::value_to_yaml(msg.tow_ms, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Odom & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: q0_w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "q0_w: ";
    rosidl_generator_traits::value_to_yaml(msg.q0_w, out);
    out << "\n";
  }

  // member: q1_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "q1_x: ";
    rosidl_generator_traits::value_to_yaml(msg.q1_x, out);
    out << "\n";
  }

  // member: q2_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "q2_y: ";
    rosidl_generator_traits::value_to_yaml(msg.q2_y, out);
    out << "\n";
  }

  // member: q3_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "q3_z: ";
    rosidl_generator_traits::value_to_yaml(msg.q3_z, out);
    out << "\n";
  }

  // member: pos_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_x: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x, out);
    out << "\n";
  }

  // member: pos_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_y: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y, out);
    out << "\n";
  }

  // member: pos_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_z: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_z, out);
    out << "\n";
  }

  // member: vel_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vel_x: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_x, out);
    out << "\n";
  }

  // member: vel_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vel_y: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_y, out);
    out << "\n";
  }

  // member: vel_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vel_z: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_z, out);
    out << "\n";
  }

  // member: vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vel: ";
    rosidl_generator_traits::value_to_yaml(msg.vel, out);
    out << "\n";
  }

  // member: ang_vel_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ang_vel_x: ";
    rosidl_generator_traits::value_to_yaml(msg.ang_vel_x, out);
    out << "\n";
  }

  // member: ang_vel_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ang_vel_y: ";
    rosidl_generator_traits::value_to_yaml(msg.ang_vel_y, out);
    out << "\n";
  }

  // member: ang_vel_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ang_vel_z: ";
    rosidl_generator_traits::value_to_yaml(msg.ang_vel_z, out);
    out << "\n";
  }

  // member: acc_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acc_x: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_x, out);
    out << "\n";
  }

  // member: acc_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acc_y: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_y, out);
    out << "\n";
  }

  // member: acc_z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acc_z: ";
    rosidl_generator_traits::value_to_yaml(msg.acc_z, out);
    out << "\n";
  }

  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: sensor_status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sensor_status: ";
    rosidl_generator_traits::value_to_yaml(msg.sensor_status, out);
    out << "\n";
  }

  // member: pos_x_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_x_std: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_x_std, out);
    out << "\n";
  }

  // member: pos_y_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_y_std: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_y_std, out);
    out << "\n";
  }

  // member: pos_z_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos_z_std: ";
    rosidl_generator_traits::value_to_yaml(msg.pos_z_std, out);
    out << "\n";
  }

  // member: vel_x_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vel_x_std: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_x_std, out);
    out << "\n";
  }

  // member: vel_y_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vel_y_std: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_y_std, out);
    out << "\n";
  }

  // member: vel_z_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vel_z_std: ";
    rosidl_generator_traits::value_to_yaml(msg.vel_z_std, out);
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

  // member: yaw_std
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_std: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_std, out);
    out << "\n";
  }

  // member: tow_ms
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tow_ms: ";
    rosidl_generator_traits::value_to_yaml(msg.tow_ms, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Odom & msg, bool use_flow_style = false)
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
  const imu_msgs::msg::Odom & msg,
  std::ostream & out, size_t indentation = 0)
{
  imu_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use imu_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const imu_msgs::msg::Odom & msg)
{
  return imu_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<imu_msgs::msg::Odom>()
{
  return "imu_msgs::msg::Odom";
}

template<>
inline const char * name<imu_msgs::msg::Odom>()
{
  return "imu_msgs/msg/Odom";
}

template<>
struct has_fixed_size<imu_msgs::msg::Odom>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<imu_msgs::msg::Odom>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<imu_msgs::msg::Odom>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // IMU_MSGS__MSG__DETAIL__ODOM__TRAITS_HPP_
