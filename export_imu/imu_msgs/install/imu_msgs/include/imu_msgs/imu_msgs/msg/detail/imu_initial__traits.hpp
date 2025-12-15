// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from imu_msgs:msg/ImuInitial.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU_INITIAL__TRAITS_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU_INITIAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "imu_msgs/msg/detail/imu_initial__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace imu_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ImuInitial & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: gx
  {
    out << "gx: ";
    rosidl_generator_traits::value_to_yaml(msg.gx, out);
    out << ", ";
  }

  // member: gy
  {
    out << "gy: ";
    rosidl_generator_traits::value_to_yaml(msg.gy, out);
    out << ", ";
  }

  // member: gz
  {
    out << "gz: ";
    rosidl_generator_traits::value_to_yaml(msg.gz, out);
    out << ", ";
  }

  // member: ax
  {
    out << "ax: ";
    rosidl_generator_traits::value_to_yaml(msg.ax, out);
    out << ", ";
  }

  // member: ay
  {
    out << "ay: ";
    rosidl_generator_traits::value_to_yaml(msg.ay, out);
    out << ", ";
  }

  // member: az
  {
    out << "az: ";
    rosidl_generator_traits::value_to_yaml(msg.az, out);
    out << ", ";
  }

  // member: temperature
  {
    out << "temperature: ";
    rosidl_generator_traits::value_to_yaml(msg.temperature, out);
    out << ", ";
  }

  // member: imu_time_stamp
  {
    out << "imu_time_stamp: ";
    rosidl_generator_traits::value_to_yaml(msg.imu_time_stamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ImuInitial & msg,
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

  // member: gx
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gx: ";
    rosidl_generator_traits::value_to_yaml(msg.gx, out);
    out << "\n";
  }

  // member: gy
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gy: ";
    rosidl_generator_traits::value_to_yaml(msg.gy, out);
    out << "\n";
  }

  // member: gz
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gz: ";
    rosidl_generator_traits::value_to_yaml(msg.gz, out);
    out << "\n";
  }

  // member: ax
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ax: ";
    rosidl_generator_traits::value_to_yaml(msg.ax, out);
    out << "\n";
  }

  // member: ay
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ay: ";
    rosidl_generator_traits::value_to_yaml(msg.ay, out);
    out << "\n";
  }

  // member: az
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "az: ";
    rosidl_generator_traits::value_to_yaml(msg.az, out);
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

  // member: imu_time_stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "imu_time_stamp: ";
    rosidl_generator_traits::value_to_yaml(msg.imu_time_stamp, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ImuInitial & msg, bool use_flow_style = false)
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
  const imu_msgs::msg::ImuInitial & msg,
  std::ostream & out, size_t indentation = 0)
{
  imu_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use imu_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const imu_msgs::msg::ImuInitial & msg)
{
  return imu_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<imu_msgs::msg::ImuInitial>()
{
  return "imu_msgs::msg::ImuInitial";
}

template<>
inline const char * name<imu_msgs::msg::ImuInitial>()
{
  return "imu_msgs/msg/ImuInitial";
}

template<>
struct has_fixed_size<imu_msgs::msg::ImuInitial>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<imu_msgs::msg::ImuInitial>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<imu_msgs::msg::ImuInitial>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // IMU_MSGS__MSG__DETAIL__IMU_INITIAL__TRAITS_HPP_
