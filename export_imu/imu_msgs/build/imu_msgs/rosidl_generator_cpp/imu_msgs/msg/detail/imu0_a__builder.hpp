// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from imu_msgs:msg/Imu0A.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU0_A__BUILDER_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU0_A__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "imu_msgs/msg/detail/imu0_a__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace imu_msgs
{

namespace msg
{

namespace builder
{

class Init_Imu0A_frame_count
{
public:
  explicit Init_Imu0A_frame_count(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  ::imu_msgs::msg::Imu0A frame_count(::imu_msgs::msg::Imu0A::_frame_count_type arg)
  {
    msg_.frame_count = std::move(arg);
    return std::move(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_status
{
public:
  explicit Init_Imu0A_status(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_frame_count status(::imu_msgs::msg::Imu0A::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Imu0A_frame_count(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_imu_time_stamp
{
public:
  explicit Init_Imu0A_imu_time_stamp(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_status imu_time_stamp(::imu_msgs::msg::Imu0A::_imu_time_stamp_type arg)
  {
    msg_.imu_time_stamp = std::move(arg);
    return Init_Imu0A_status(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_temperature
{
public:
  explicit Init_Imu0A_temperature(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_imu_time_stamp temperature(::imu_msgs::msg::Imu0A::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_Imu0A_imu_time_stamp(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_az
{
public:
  explicit Init_Imu0A_az(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_temperature az(::imu_msgs::msg::Imu0A::_az_type arg)
  {
    msg_.az = std::move(arg);
    return Init_Imu0A_temperature(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_ay
{
public:
  explicit Init_Imu0A_ay(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_az ay(::imu_msgs::msg::Imu0A::_ay_type arg)
  {
    msg_.ay = std::move(arg);
    return Init_Imu0A_az(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_ax
{
public:
  explicit Init_Imu0A_ax(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_ay ax(::imu_msgs::msg::Imu0A::_ax_type arg)
  {
    msg_.ax = std::move(arg);
    return Init_Imu0A_ay(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_gz
{
public:
  explicit Init_Imu0A_gz(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_ax gz(::imu_msgs::msg::Imu0A::_gz_type arg)
  {
    msg_.gz = std::move(arg);
    return Init_Imu0A_ax(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_gy
{
public:
  explicit Init_Imu0A_gy(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_gz gy(::imu_msgs::msg::Imu0A::_gy_type arg)
  {
    msg_.gy = std::move(arg);
    return Init_Imu0A_gz(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_gx
{
public:
  explicit Init_Imu0A_gx(::imu_msgs::msg::Imu0A & msg)
  : msg_(msg)
  {}
  Init_Imu0A_gy gx(::imu_msgs::msg::Imu0A::_gx_type arg)
  {
    msg_.gx = std::move(arg);
    return Init_Imu0A_gy(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

class Init_Imu0A_header
{
public:
  Init_Imu0A_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Imu0A_gx header(::imu_msgs::msg::Imu0A::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Imu0A_gx(msg_);
  }

private:
  ::imu_msgs::msg::Imu0A msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::imu_msgs::msg::Imu0A>()
{
  return imu_msgs::msg::builder::Init_Imu0A_header();
}

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__IMU0_A__BUILDER_HPP_
