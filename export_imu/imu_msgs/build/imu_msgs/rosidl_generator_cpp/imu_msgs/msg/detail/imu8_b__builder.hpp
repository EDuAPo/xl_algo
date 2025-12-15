// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from imu_msgs:msg/Imu8B.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU8_B__BUILDER_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU8_B__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "imu_msgs/msg/detail/imu8_b__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace imu_msgs
{

namespace msg
{

namespace builder
{

class Init_Imu8B_status
{
public:
  explicit Init_Imu8B_status(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  ::imu_msgs::msg::Imu8B status(::imu_msgs::msg::Imu8B::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_temperature
{
public:
  explicit Init_Imu8B_temperature(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_status temperature(::imu_msgs::msg::Imu8B::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_Imu8B_status(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_az
{
public:
  explicit Init_Imu8B_az(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_temperature az(::imu_msgs::msg::Imu8B::_az_type arg)
  {
    msg_.az = std::move(arg);
    return Init_Imu8B_temperature(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_ay
{
public:
  explicit Init_Imu8B_ay(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_az ay(::imu_msgs::msg::Imu8B::_ay_type arg)
  {
    msg_.ay = std::move(arg);
    return Init_Imu8B_az(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_ax
{
public:
  explicit Init_Imu8B_ax(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_ay ax(::imu_msgs::msg::Imu8B::_ax_type arg)
  {
    msg_.ax = std::move(arg);
    return Init_Imu8B_ay(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_gz
{
public:
  explicit Init_Imu8B_gz(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_ax gz(::imu_msgs::msg::Imu8B::_gz_type arg)
  {
    msg_.gz = std::move(arg);
    return Init_Imu8B_ax(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_gy
{
public:
  explicit Init_Imu8B_gy(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_gz gy(::imu_msgs::msg::Imu8B::_gy_type arg)
  {
    msg_.gy = std::move(arg);
    return Init_Imu8B_gz(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_gx
{
public:
  explicit Init_Imu8B_gx(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_gy gx(::imu_msgs::msg::Imu8B::_gx_type arg)
  {
    msg_.gx = std::move(arg);
    return Init_Imu8B_gy(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_serial_number
{
public:
  explicit Init_Imu8B_serial_number(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_gx serial_number(::imu_msgs::msg::Imu8B::_serial_number_type arg)
  {
    msg_.serial_number = std::move(arg);
    return Init_Imu8B_gx(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_frame_count
{
public:
  explicit Init_Imu8B_frame_count(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_serial_number frame_count(::imu_msgs::msg::Imu8B::_frame_count_type arg)
  {
    msg_.frame_count = std::move(arg);
    return Init_Imu8B_serial_number(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_data_length
{
public:
  explicit Init_Imu8B_data_length(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_frame_count data_length(::imu_msgs::msg::Imu8B::_data_length_type arg)
  {
    msg_.data_length = std::move(arg);
    return Init_Imu8B_frame_count(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_type
{
public:
  explicit Init_Imu8B_type(::imu_msgs::msg::Imu8B & msg)
  : msg_(msg)
  {}
  Init_Imu8B_data_length type(::imu_msgs::msg::Imu8B::_type_type arg)
  {
    msg_.type = std::move(arg);
    return Init_Imu8B_data_length(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

class Init_Imu8B_header
{
public:
  Init_Imu8B_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Imu8B_type header(::imu_msgs::msg::Imu8B::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Imu8B_type(msg_);
  }

private:
  ::imu_msgs::msg::Imu8B msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::imu_msgs::msg::Imu8B>()
{
  return imu_msgs::msg::builder::Init_Imu8B_header();
}

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__IMU8_B__BUILDER_HPP_
