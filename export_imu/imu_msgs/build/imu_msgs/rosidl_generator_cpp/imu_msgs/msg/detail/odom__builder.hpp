// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from imu_msgs:msg/Odom.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ODOM__BUILDER_HPP_
#define IMU_MSGS__MSG__DETAIL__ODOM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "imu_msgs/msg/detail/odom__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace imu_msgs
{

namespace msg
{

namespace builder
{

class Init_Odom_tow_ms
{
public:
  explicit Init_Odom_tow_ms(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  ::imu_msgs::msg::Odom tow_ms(::imu_msgs::msg::Odom::_tow_ms_type arg)
  {
    msg_.tow_ms = std::move(arg);
    return std::move(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_yaw_std
{
public:
  explicit Init_Odom_yaw_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_tow_ms yaw_std(::imu_msgs::msg::Odom::_yaw_std_type arg)
  {
    msg_.yaw_std = std::move(arg);
    return Init_Odom_tow_ms(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_pitch_std
{
public:
  explicit Init_Odom_pitch_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_yaw_std pitch_std(::imu_msgs::msg::Odom::_pitch_std_type arg)
  {
    msg_.pitch_std = std::move(arg);
    return Init_Odom_yaw_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_roll_std
{
public:
  explicit Init_Odom_roll_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_pitch_std roll_std(::imu_msgs::msg::Odom::_roll_std_type arg)
  {
    msg_.roll_std = std::move(arg);
    return Init_Odom_pitch_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_vel_z_std
{
public:
  explicit Init_Odom_vel_z_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_roll_std vel_z_std(::imu_msgs::msg::Odom::_vel_z_std_type arg)
  {
    msg_.vel_z_std = std::move(arg);
    return Init_Odom_roll_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_vel_y_std
{
public:
  explicit Init_Odom_vel_y_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_vel_z_std vel_y_std(::imu_msgs::msg::Odom::_vel_y_std_type arg)
  {
    msg_.vel_y_std = std::move(arg);
    return Init_Odom_vel_z_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_vel_x_std
{
public:
  explicit Init_Odom_vel_x_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_vel_y_std vel_x_std(::imu_msgs::msg::Odom::_vel_x_std_type arg)
  {
    msg_.vel_x_std = std::move(arg);
    return Init_Odom_vel_y_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_pos_z_std
{
public:
  explicit Init_Odom_pos_z_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_vel_x_std pos_z_std(::imu_msgs::msg::Odom::_pos_z_std_type arg)
  {
    msg_.pos_z_std = std::move(arg);
    return Init_Odom_vel_x_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_pos_y_std
{
public:
  explicit Init_Odom_pos_y_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_pos_z_std pos_y_std(::imu_msgs::msg::Odom::_pos_y_std_type arg)
  {
    msg_.pos_y_std = std::move(arg);
    return Init_Odom_pos_z_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_pos_x_std
{
public:
  explicit Init_Odom_pos_x_std(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_pos_y_std pos_x_std(::imu_msgs::msg::Odom::_pos_x_std_type arg)
  {
    msg_.pos_x_std = std::move(arg);
    return Init_Odom_pos_y_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_sensor_status
{
public:
  explicit Init_Odom_sensor_status(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_pos_x_std sensor_status(::imu_msgs::msg::Odom::_sensor_status_type arg)
  {
    msg_.sensor_status = std::move(arg);
    return Init_Odom_pos_x_std(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_status
{
public:
  explicit Init_Odom_status(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_sensor_status status(::imu_msgs::msg::Odom::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Odom_sensor_status(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_acc_z
{
public:
  explicit Init_Odom_acc_z(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_status acc_z(::imu_msgs::msg::Odom::_acc_z_type arg)
  {
    msg_.acc_z = std::move(arg);
    return Init_Odom_status(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_acc_y
{
public:
  explicit Init_Odom_acc_y(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_acc_z acc_y(::imu_msgs::msg::Odom::_acc_y_type arg)
  {
    msg_.acc_y = std::move(arg);
    return Init_Odom_acc_z(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_acc_x
{
public:
  explicit Init_Odom_acc_x(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_acc_y acc_x(::imu_msgs::msg::Odom::_acc_x_type arg)
  {
    msg_.acc_x = std::move(arg);
    return Init_Odom_acc_y(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_ang_vel_z
{
public:
  explicit Init_Odom_ang_vel_z(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_acc_x ang_vel_z(::imu_msgs::msg::Odom::_ang_vel_z_type arg)
  {
    msg_.ang_vel_z = std::move(arg);
    return Init_Odom_acc_x(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_ang_vel_y
{
public:
  explicit Init_Odom_ang_vel_y(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_ang_vel_z ang_vel_y(::imu_msgs::msg::Odom::_ang_vel_y_type arg)
  {
    msg_.ang_vel_y = std::move(arg);
    return Init_Odom_ang_vel_z(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_ang_vel_x
{
public:
  explicit Init_Odom_ang_vel_x(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_ang_vel_y ang_vel_x(::imu_msgs::msg::Odom::_ang_vel_x_type arg)
  {
    msg_.ang_vel_x = std::move(arg);
    return Init_Odom_ang_vel_y(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_vel
{
public:
  explicit Init_Odom_vel(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_ang_vel_x vel(::imu_msgs::msg::Odom::_vel_type arg)
  {
    msg_.vel = std::move(arg);
    return Init_Odom_ang_vel_x(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_vel_z
{
public:
  explicit Init_Odom_vel_z(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_vel vel_z(::imu_msgs::msg::Odom::_vel_z_type arg)
  {
    msg_.vel_z = std::move(arg);
    return Init_Odom_vel(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_vel_y
{
public:
  explicit Init_Odom_vel_y(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_vel_z vel_y(::imu_msgs::msg::Odom::_vel_y_type arg)
  {
    msg_.vel_y = std::move(arg);
    return Init_Odom_vel_z(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_vel_x
{
public:
  explicit Init_Odom_vel_x(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_vel_y vel_x(::imu_msgs::msg::Odom::_vel_x_type arg)
  {
    msg_.vel_x = std::move(arg);
    return Init_Odom_vel_y(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_pos_z
{
public:
  explicit Init_Odom_pos_z(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_vel_x pos_z(::imu_msgs::msg::Odom::_pos_z_type arg)
  {
    msg_.pos_z = std::move(arg);
    return Init_Odom_vel_x(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_pos_y
{
public:
  explicit Init_Odom_pos_y(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_pos_z pos_y(::imu_msgs::msg::Odom::_pos_y_type arg)
  {
    msg_.pos_y = std::move(arg);
    return Init_Odom_pos_z(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_pos_x
{
public:
  explicit Init_Odom_pos_x(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_pos_y pos_x(::imu_msgs::msg::Odom::_pos_x_type arg)
  {
    msg_.pos_x = std::move(arg);
    return Init_Odom_pos_y(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_q3_z
{
public:
  explicit Init_Odom_q3_z(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_pos_x q3_z(::imu_msgs::msg::Odom::_q3_z_type arg)
  {
    msg_.q3_z = std::move(arg);
    return Init_Odom_pos_x(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_q2_y
{
public:
  explicit Init_Odom_q2_y(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_q3_z q2_y(::imu_msgs::msg::Odom::_q2_y_type arg)
  {
    msg_.q2_y = std::move(arg);
    return Init_Odom_q3_z(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_q1_x
{
public:
  explicit Init_Odom_q1_x(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_q2_y q1_x(::imu_msgs::msg::Odom::_q1_x_type arg)
  {
    msg_.q1_x = std::move(arg);
    return Init_Odom_q2_y(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_q0_w
{
public:
  explicit Init_Odom_q0_w(::imu_msgs::msg::Odom & msg)
  : msg_(msg)
  {}
  Init_Odom_q1_x q0_w(::imu_msgs::msg::Odom::_q0_w_type arg)
  {
    msg_.q0_w = std::move(arg);
    return Init_Odom_q1_x(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

class Init_Odom_header
{
public:
  Init_Odom_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Odom_q0_w header(::imu_msgs::msg::Odom::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Odom_q0_w(msg_);
  }

private:
  ::imu_msgs::msg::Odom msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::imu_msgs::msg::Odom>()
{
  return imu_msgs::msg::builder::Init_Odom_header();
}

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__ODOM__BUILDER_HPP_
