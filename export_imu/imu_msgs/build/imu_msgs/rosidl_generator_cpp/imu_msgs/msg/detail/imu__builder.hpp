// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from imu_msgs:msg/Imu.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU__BUILDER_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "imu_msgs/msg/detail/imu__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace imu_msgs
{

namespace msg
{

namespace builder
{

class Init_Imu_imu_msg
{
public:
  explicit Init_Imu_imu_msg(::imu_msgs::msg::Imu & msg)
  : msg_(msg)
  {}
  ::imu_msgs::msg::Imu imu_msg(::imu_msgs::msg::Imu::_imu_msg_type arg)
  {
    msg_.imu_msg = std::move(arg);
    return std::move(msg_);
  }

private:
  ::imu_msgs::msg::Imu msg_;
};

class Init_Imu_header
{
public:
  Init_Imu_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Imu_imu_msg header(::imu_msgs::msg::Imu::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Imu_imu_msg(msg_);
  }

private:
  ::imu_msgs::msg::Imu msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::imu_msgs::msg::Imu>()
{
  return imu_msgs::msg::builder::Init_Imu_header();
}

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__IMU__BUILDER_HPP_
