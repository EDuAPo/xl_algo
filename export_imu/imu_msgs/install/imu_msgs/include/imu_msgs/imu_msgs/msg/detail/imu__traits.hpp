// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from imu_msgs:msg/Imu.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU__TRAITS_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "imu_msgs/msg/detail/imu__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'imu_msg'
#include "imu_msgs/msg/detail/asensing__traits.hpp"

namespace imu_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Imu & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: imu_msg
  {
    out << "imu_msg: ";
    to_flow_style_yaml(msg.imu_msg, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Imu & msg,
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

  // member: imu_msg
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "imu_msg:\n";
    to_block_style_yaml(msg.imu_msg, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Imu & msg, bool use_flow_style = false)
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
  const imu_msgs::msg::Imu & msg,
  std::ostream & out, size_t indentation = 0)
{
  imu_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use imu_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const imu_msgs::msg::Imu & msg)
{
  return imu_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<imu_msgs::msg::Imu>()
{
  return "imu_msgs::msg::Imu";
}

template<>
inline const char * name<imu_msgs::msg::Imu>()
{
  return "imu_msgs/msg/Imu";
}

template<>
struct has_fixed_size<imu_msgs::msg::Imu>
  : std::integral_constant<bool, has_fixed_size<imu_msgs::msg::ASENSING>::value && has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<imu_msgs::msg::Imu>
  : std::integral_constant<bool, has_bounded_size<imu_msgs::msg::ASENSING>::value && has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<imu_msgs::msg::Imu>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // IMU_MSGS__MSG__DETAIL__IMU__TRAITS_HPP_
