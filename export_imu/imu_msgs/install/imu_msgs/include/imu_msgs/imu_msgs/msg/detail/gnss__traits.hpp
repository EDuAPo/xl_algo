// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from imu_msgs:msg/Gnss.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__GNSS__TRAITS_HPP_
#define IMU_MSGS__MSG__DETAIL__GNSS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "imu_msgs/msg/detail/gnss__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace imu_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Gnss & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: longitude
  {
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << ", ";
  }

  // member: lon_sigma
  {
    out << "lon_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.lon_sigma, out);
    out << ", ";
  }

  // member: latitude
  {
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << ", ";
  }

  // member: lat_sigma
  {
    out << "lat_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.lat_sigma, out);
    out << ", ";
  }

  // member: altitude
  {
    out << "altitude: ";
    rosidl_generator_traits::value_to_yaml(msg.altitude, out);
    out << ", ";
  }

  // member: alt_sigma
  {
    out << "alt_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.alt_sigma, out);
    out << ", ";
  }

  // member: gps_fix
  {
    out << "gps_fix: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_fix, out);
    out << ", ";
  }

  // member: rtk_age
  {
    out << "rtk_age: ";
    rosidl_generator_traits::value_to_yaml(msg.rtk_age, out);
    out << ", ";
  }

  // member: flags_pos
  {
    out << "flags_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flags_pos, out);
    out << ", ";
  }

  // member: flags_vel
  {
    out << "flags_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.flags_vel, out);
    out << ", ";
  }

  // member: flags_attitude
  {
    out << "flags_attitude: ";
    rosidl_generator_traits::value_to_yaml(msg.flags_attitude, out);
    out << ", ";
  }

  // member: flags_time
  {
    out << "flags_time: ";
    rosidl_generator_traits::value_to_yaml(msg.flags_time, out);
    out << ", ";
  }

  // member: hor_vel
  {
    out << "hor_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.hor_vel, out);
    out << ", ";
  }

  // member: track_angle
  {
    out << "track_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.track_angle, out);
    out << ", ";
  }

  // member: ver_vel
  {
    out << "ver_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.ver_vel, out);
    out << ", ";
  }

  // member: latency_vel
  {
    out << "latency_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.latency_vel, out);
    out << ", ";
  }

  // member: base_length
  {
    out << "base_length: ";
    rosidl_generator_traits::value_to_yaml(msg.base_length, out);
    out << ", ";
  }

  // member: yaw
  {
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << ", ";
  }

  // member: yaw_sigma
  {
    out << "yaw_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_sigma, out);
    out << ", ";
  }

  // member: pitch
  {
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << ", ";
  }

  // member: pitch_sigma
  {
    out << "pitch_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch_sigma, out);
    out << ", ";
  }

  // member: utc_time
  {
    out << "utc_time: ";
    rosidl_generator_traits::value_to_yaml(msg.utc_time, out);
    out << ", ";
  }

  // member: ts_pos
  {
    out << "ts_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.ts_pos, out);
    out << ", ";
  }

  // member: ts_vel
  {
    out << "ts_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.ts_vel, out);
    out << ", ";
  }

  // member: ts_heading
  {
    out << "ts_heading: ";
    rosidl_generator_traits::value_to_yaml(msg.ts_heading, out);
    out << ", ";
  }

  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << ", ";
  }

  // member: num_master
  {
    out << "num_master: ";
    rosidl_generator_traits::value_to_yaml(msg.num_master, out);
    out << ", ";
  }

  // member: gdop
  {
    out << "gdop: ";
    rosidl_generator_traits::value_to_yaml(msg.gdop, out);
    out << ", ";
  }

  // member: pdop
  {
    out << "pdop: ";
    rosidl_generator_traits::value_to_yaml(msg.pdop, out);
    out << ", ";
  }

  // member: hdop
  {
    out << "hdop: ";
    rosidl_generator_traits::value_to_yaml(msg.hdop, out);
    out << ", ";
  }

  // member: htdop
  {
    out << "htdop: ";
    rosidl_generator_traits::value_to_yaml(msg.htdop, out);
    out << ", ";
  }

  // member: tdop
  {
    out << "tdop: ";
    rosidl_generator_traits::value_to_yaml(msg.tdop, out);
    out << ", ";
  }

  // member: num_reserve
  {
    out << "num_reserve: ";
    rosidl_generator_traits::value_to_yaml(msg.num_reserve, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Gnss & msg,
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

  // member: longitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "longitude: ";
    rosidl_generator_traits::value_to_yaml(msg.longitude, out);
    out << "\n";
  }

  // member: lon_sigma
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lon_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.lon_sigma, out);
    out << "\n";
  }

  // member: latitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latitude: ";
    rosidl_generator_traits::value_to_yaml(msg.latitude, out);
    out << "\n";
  }

  // member: lat_sigma
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lat_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.lat_sigma, out);
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

  // member: alt_sigma
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "alt_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.alt_sigma, out);
    out << "\n";
  }

  // member: gps_fix
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gps_fix: ";
    rosidl_generator_traits::value_to_yaml(msg.gps_fix, out);
    out << "\n";
  }

  // member: rtk_age
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rtk_age: ";
    rosidl_generator_traits::value_to_yaml(msg.rtk_age, out);
    out << "\n";
  }

  // member: flags_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flags_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flags_pos, out);
    out << "\n";
  }

  // member: flags_vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flags_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.flags_vel, out);
    out << "\n";
  }

  // member: flags_attitude
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flags_attitude: ";
    rosidl_generator_traits::value_to_yaml(msg.flags_attitude, out);
    out << "\n";
  }

  // member: flags_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flags_time: ";
    rosidl_generator_traits::value_to_yaml(msg.flags_time, out);
    out << "\n";
  }

  // member: hor_vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "hor_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.hor_vel, out);
    out << "\n";
  }

  // member: track_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "track_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.track_angle, out);
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

  // member: latency_vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "latency_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.latency_vel, out);
    out << "\n";
  }

  // member: base_length
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "base_length: ";
    rosidl_generator_traits::value_to_yaml(msg.base_length, out);
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

  // member: yaw_sigma
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw_sigma, out);
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

  // member: pitch_sigma
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch_sigma: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch_sigma, out);
    out << "\n";
  }

  // member: utc_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "utc_time: ";
    rosidl_generator_traits::value_to_yaml(msg.utc_time, out);
    out << "\n";
  }

  // member: ts_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ts_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.ts_pos, out);
    out << "\n";
  }

  // member: ts_vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ts_vel: ";
    rosidl_generator_traits::value_to_yaml(msg.ts_vel, out);
    out << "\n";
  }

  // member: ts_heading
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ts_heading: ";
    rosidl_generator_traits::value_to_yaml(msg.ts_heading, out);
    out << "\n";
  }

  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << "\n";
  }

  // member: num_master
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "num_master: ";
    rosidl_generator_traits::value_to_yaml(msg.num_master, out);
    out << "\n";
  }

  // member: gdop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gdop: ";
    rosidl_generator_traits::value_to_yaml(msg.gdop, out);
    out << "\n";
  }

  // member: pdop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pdop: ";
    rosidl_generator_traits::value_to_yaml(msg.pdop, out);
    out << "\n";
  }

  // member: hdop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "hdop: ";
    rosidl_generator_traits::value_to_yaml(msg.hdop, out);
    out << "\n";
  }

  // member: htdop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "htdop: ";
    rosidl_generator_traits::value_to_yaml(msg.htdop, out);
    out << "\n";
  }

  // member: tdop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tdop: ";
    rosidl_generator_traits::value_to_yaml(msg.tdop, out);
    out << "\n";
  }

  // member: num_reserve
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "num_reserve: ";
    rosidl_generator_traits::value_to_yaml(msg.num_reserve, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Gnss & msg, bool use_flow_style = false)
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
  const imu_msgs::msg::Gnss & msg,
  std::ostream & out, size_t indentation = 0)
{
  imu_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use imu_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const imu_msgs::msg::Gnss & msg)
{
  return imu_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<imu_msgs::msg::Gnss>()
{
  return "imu_msgs::msg::Gnss";
}

template<>
inline const char * name<imu_msgs::msg::Gnss>()
{
  return "imu_msgs/msg/Gnss";
}

template<>
struct has_fixed_size<imu_msgs::msg::Gnss>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<imu_msgs::msg::Gnss>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<imu_msgs::msg::Gnss>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // IMU_MSGS__MSG__DETAIL__GNSS__TRAITS_HPP_
