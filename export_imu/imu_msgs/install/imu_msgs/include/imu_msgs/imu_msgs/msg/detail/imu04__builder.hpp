// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from imu_msgs:msg/Imu04.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU04__BUILDER_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU04__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "imu_msgs/msg/detail/imu04__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace imu_msgs
{

namespace msg
{

namespace builder
{

class Init_Imu04_msg_type
{
public:
  explicit Init_Imu04_msg_type(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  ::imu_msgs::msg::Imu04 msg_type(::imu_msgs::msg::Imu04::_msg_type_type arg)
  {
    msg_.msg_type = std::move(arg);
    return std::move(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_info_byte
{
public:
  explicit Init_Imu04_info_byte(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_msg_type info_byte(::imu_msgs::msg::Imu04::_info_byte_type arg)
  {
    msg_.info_byte = std::move(arg);
    return Init_Imu04_msg_type(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_ver_vel
{
public:
  explicit Init_Imu04_ver_vel(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_info_byte ver_vel(::imu_msgs::msg::Imu04::_ver_vel_type arg)
  {
    msg_.ver_vel = std::move(arg);
    return Init_Imu04_info_byte(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_ver_pos
{
public:
  explicit Init_Imu04_ver_pos(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_ver_vel ver_pos(::imu_msgs::msg::Imu04::_ver_pos_type arg)
  {
    msg_.ver_pos = std::move(arg);
    return Init_Imu04_ver_vel(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_pdata
{
public:
  explicit Init_Imu04_pdata(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_ver_pos pdata(::imu_msgs::msg::Imu04::_pdata_type arg)
  {
    msg_.pdata = std::move(arg);
    return Init_Imu04_ver_pos(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_ptype
{
public:
  explicit Init_Imu04_ptype(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_pdata ptype(::imu_msgs::msg::Imu04::_ptype_type arg)
  {
    msg_.ptype = std::move(arg);
    return Init_Imu04_pdata(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_gps_heading_status
{
public:
  explicit Init_Imu04_gps_heading_status(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_ptype gps_heading_status(::imu_msgs::msg::Imu04::_gps_heading_status_type arg)
  {
    msg_.gps_heading_status = std::move(arg);
    return Init_Imu04_ptype(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_gps_message
{
public:
  explicit Init_Imu04_gps_message(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_gps_heading_status gps_message(::imu_msgs::msg::Imu04::_gps_message_type arg)
  {
    msg_.gps_message = std::move(arg);
    return Init_Imu04_gps_heading_status(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_time
{
public:
  explicit Init_Imu04_time(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_gps_message time(::imu_msgs::msg::Imu04::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_Imu04_gps_message(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_temperature
{
public:
  explicit Init_Imu04_temperature(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_time temperature(::imu_msgs::msg::Imu04::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_Imu04_time(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_az
{
public:
  explicit Init_Imu04_az(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_temperature az(::imu_msgs::msg::Imu04::_az_type arg)
  {
    msg_.az = std::move(arg);
    return Init_Imu04_temperature(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_ay
{
public:
  explicit Init_Imu04_ay(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_az ay(::imu_msgs::msg::Imu04::_ay_type arg)
  {
    msg_.ay = std::move(arg);
    return Init_Imu04_az(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_ax
{
public:
  explicit Init_Imu04_ax(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_ay ax(::imu_msgs::msg::Imu04::_ax_type arg)
  {
    msg_.ax = std::move(arg);
    return Init_Imu04_ay(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_gz
{
public:
  explicit Init_Imu04_gz(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_ax gz(::imu_msgs::msg::Imu04::_gz_type arg)
  {
    msg_.gz = std::move(arg);
    return Init_Imu04_ax(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_gy
{
public:
  explicit Init_Imu04_gy(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_gz gy(::imu_msgs::msg::Imu04::_gy_type arg)
  {
    msg_.gy = std::move(arg);
    return Init_Imu04_gz(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_gx
{
public:
  explicit Init_Imu04_gx(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_gy gx(::imu_msgs::msg::Imu04::_gx_type arg)
  {
    msg_.gx = std::move(arg);
    return Init_Imu04_gy(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_yaw
{
public:
  explicit Init_Imu04_yaw(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_gx yaw(::imu_msgs::msg::Imu04::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return Init_Imu04_gx(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_pitch
{
public:
  explicit Init_Imu04_pitch(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_yaw pitch(::imu_msgs::msg::Imu04::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_Imu04_yaw(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_roll
{
public:
  explicit Init_Imu04_roll(::imu_msgs::msg::Imu04 & msg)
  : msg_(msg)
  {}
  Init_Imu04_pitch roll(::imu_msgs::msg::Imu04::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_Imu04_pitch(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

class Init_Imu04_header
{
public:
  Init_Imu04_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Imu04_roll header(::imu_msgs::msg::Imu04::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Imu04_roll(msg_);
  }

private:
  ::imu_msgs::msg::Imu04 msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::imu_msgs::msg::Imu04>()
{
  return imu_msgs::msg::builder::Init_Imu04_header();
}

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__IMU04__BUILDER_HPP_
