// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from imu_msgs:msg/Imu04.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU04__TRAITS_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU04__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "imu_msgs/msg/detail/imu04__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace imu_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Imu04 & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
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

  // member: yaw
  {
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
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

  // member: time
  {
    out << "time: ";
    rosidl_generator_traits::value_to_yaml(msg.time, out);
    out << ", ";
  }

  // member: gps_message
  {
    if (msg.gps_message.size() == 0) {
      out << "gps_message: []";
    } else {
      out << "gps_message: [";
      size_t pending_items = msg.gps_message.size();
      for (auto item : msg.gps_message) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: gps_heading_status
  {
    out << "gps_heading_status: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_heading_status, out);
    out << ", ";
  }

  // member: ptype
  {
    out << "ptype: ";
    rosidl_generator_traits::value_to_yaml(msg.ptype, out);
    out << ", ";
  }

  // member: pdata
  {
    out << "pdata: ";
    rosidl_generator_traits::value_to_yaml(msg.pdata, out);
    out << ", ";
  }

  // member: ver_pos
  {
    out << "ver_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.ver_pos, out);
    out << ", ";
  }

  // member: ver_vel
  {
    out << "ver_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.ver_vel, out);
    out << ", ";
  }

  // member: info_byte
  {
    out << "info_byte: ";
    rosidl_generator_traits::value_to_yaml(msg.info_byte, out);
    out << ", ";
  }

  // member: msg_type
  {
    out << "msg_type: ";
    rosidl_generator_traits::value_to_yaml(msg.msg_type, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Imu04 & msg,
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

  // member: yaw
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << "\n";
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

  // member: time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "time: ";
    rosidl_generator_traits::value_to_yaml(msg.time, out);
    out << "\n";
  }

  // member: gps_message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.gps_message.size() == 0) {
      out << "gps_message: []\n";
    } else {
      out << "gps_message:\n";
      for (auto item : msg.gps_message) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: gps_heading_status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gps_heading_status: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_heading_status, out);
    out << "\n";
  }

  // member: ptype
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ptype: ";
    rosidl_generator_traits::value_to_yaml(msg.ptype, out);
    out << "\n";
  }

  // member: pdata
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pdata: ";
    rosidl_generator_traits::value_to_yaml(msg.pdata, out);
    out << "\n";
  }

  // member: ver_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ver_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.ver_pos, out);
    out << "\n";
  }

  // member: ver_vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ver_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.ver_vel, out);
    out << "\n";
  }

  // member: info_byte
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info_byte: ";
    rosidl_generator_traits::value_to_yaml(msg.info_byte, out);
    out << "\n";
  }

  // member: msg_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "msg_type: ";
    rosidl_generator_traits::value_to_yaml(msg.msg_type, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Imu04 & msg, bool use_flow_style = false)
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
  const imu_msgs::msg::Imu04 & msg,
  std::ostream & out, size_t indentation = 0)
{
  imu_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use imu_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const imu_msgs::msg::Imu04 & msg)
{
  return imu_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<imu_msgs::msg::Imu04>()
{
  return "imu_msgs::msg::Imu04";
}

template<>
inline const char * name<imu_msgs::msg::Imu04>()
{
  return "imu_msgs/msg/Imu04";
}

template<>
struct has_fixed_size<imu_msgs::msg::Imu04>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<imu_msgs::msg::Imu04>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<imu_msgs::msg::Imu04>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // IMU_MSGS__MSG__DETAIL__IMU04__TRAITS_HPP_
