// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from imu_msgs:msg/ImuInitial.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU_INITIAL__BUILDER_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU_INITIAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "imu_msgs/msg/detail/imu_initial__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace imu_msgs
{

namespace msg
{

namespace builder
{

class Init_ImuInitial_imu_time_stamp
{
public:
  explicit Init_ImuInitial_imu_time_stamp(::imu_msgs::msg::ImuInitial & msg)
  : msg_(msg)
  {}
  ::imu_msgs::msg::ImuInitial imu_time_stamp(::imu_msgs::msg::ImuInitial::_imu_time_stamp_type arg)
  {
    msg_.imu_time_stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

class Init_ImuInitial_temperature
{
public:
  explicit Init_ImuInitial_temperature(::imu_msgs::msg::ImuInitial & msg)
  : msg_(msg)
  {}
  Init_ImuInitial_imu_time_stamp temperature(::imu_msgs::msg::ImuInitial::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_ImuInitial_imu_time_stamp(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

class Init_ImuInitial_az
{
public:
  explicit Init_ImuInitial_az(::imu_msgs::msg::ImuInitial & msg)
  : msg_(msg)
  {}
  Init_ImuInitial_temperature az(::imu_msgs::msg::ImuInitial::_az_type arg)
  {
    msg_.az = std::move(arg);
    return Init_ImuInitial_temperature(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

class Init_ImuInitial_ay
{
public:
  explicit Init_ImuInitial_ay(::imu_msgs::msg::ImuInitial & msg)
  : msg_(msg)
  {}
  Init_ImuInitial_az ay(::imu_msgs::msg::ImuInitial::_ay_type arg)
  {
    msg_.ay = std::move(arg);
    return Init_ImuInitial_az(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

class Init_ImuInitial_ax
{
public:
  explicit Init_ImuInitial_ax(::imu_msgs::msg::ImuInitial & msg)
  : msg_(msg)
  {}
  Init_ImuInitial_ay ax(::imu_msgs::msg::ImuInitial::_ax_type arg)
  {
    msg_.ax = std::move(arg);
    return Init_ImuInitial_ay(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

class Init_ImuInitial_gz
{
public:
  explicit Init_ImuInitial_gz(::imu_msgs::msg::ImuInitial & msg)
  : msg_(msg)
  {}
  Init_ImuInitial_ax gz(::imu_msgs::msg::ImuInitial::_gz_type arg)
  {
    msg_.gz = std::move(arg);
    return Init_ImuInitial_ax(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

class Init_ImuInitial_gy
{
public:
  explicit Init_ImuInitial_gy(::imu_msgs::msg::ImuInitial & msg)
  : msg_(msg)
  {}
  Init_ImuInitial_gz gy(::imu_msgs::msg::ImuInitial::_gy_type arg)
  {
    msg_.gy = std::move(arg);
    return Init_ImuInitial_gz(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

class Init_ImuInitial_gx
{
public:
  explicit Init_ImuInitial_gx(::imu_msgs::msg::ImuInitial & msg)
  : msg_(msg)
  {}
  Init_ImuInitial_gy gx(::imu_msgs::msg::ImuInitial::_gx_type arg)
  {
    msg_.gx = std::move(arg);
    return Init_ImuInitial_gy(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

class Init_ImuInitial_header
{
public:
  Init_ImuInitial_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImuInitial_gx header(::imu_msgs::msg::ImuInitial::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ImuInitial_gx(msg_);
  }

private:
  ::imu_msgs::msg::ImuInitial msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::imu_msgs::msg::ImuInitial>()
{
  return imu_msgs::msg::builder::Init_ImuInitial_header();
}

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__IMU_INITIAL__BUILDER_HPP_
