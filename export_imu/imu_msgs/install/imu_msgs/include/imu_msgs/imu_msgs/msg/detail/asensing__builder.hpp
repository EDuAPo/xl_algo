// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from imu_msgs:msg/ASENSING.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ASENSING__BUILDER_HPP_
#define IMU_MSGS__MSG__DETAIL__ASENSING__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "imu_msgs/msg/detail/asensing__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace imu_msgs
{

namespace msg
{

namespace builder
{

class Init_ASENSING_utm_y
{
public:
  explicit Init_ASENSING_utm_y(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  ::imu_msgs::msg::ASENSING utm_y(::imu_msgs::msg::ASENSING::_utm_y_type arg)
  {
    msg_.utm_y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_utm_x
{
public:
  explicit Init_ASENSING_utm_x(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_utm_y utm_x(::imu_msgs::msg::ASENSING::_utm_x_type arg)
  {
    msg_.utm_x = std::move(arg);
    return Init_ASENSING_utm_y(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_is_available
{
public:
  explicit Init_ASENSING_is_available(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_utm_x is_available(::imu_msgs::msg::ASENSING::_is_available_type arg)
  {
    msg_.is_available = std::move(arg);
    return Init_ASENSING_utm_x(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_numsv
{
public:
  explicit Init_ASENSING_numsv(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_is_available numsv(::imu_msgs::msg::ASENSING::_numsv_type arg)
  {
    msg_.numsv = std::move(arg);
    return Init_ASENSING_is_available(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_heading_type
{
public:
  explicit Init_ASENSING_heading_type(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_numsv heading_type(::imu_msgs::msg::ASENSING::_heading_type_type arg)
  {
    msg_.heading_type = std::move(arg);
    return Init_ASENSING_numsv(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_wheel_speed_status
{
public:
  explicit Init_ASENSING_wheel_speed_status(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_heading_type wheel_speed_status(::imu_msgs::msg::ASENSING::_wheel_speed_status_type arg)
  {
    msg_.wheel_speed_status = std::move(arg);
    return Init_ASENSING_heading_type(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_temperature
{
public:
  explicit Init_ASENSING_temperature(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_wheel_speed_status temperature(::imu_msgs::msg::ASENSING::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_ASENSING_wheel_speed_status(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_gps_week_number
{
public:
  explicit Init_ASENSING_gps_week_number(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_temperature gps_week_number(::imu_msgs::msg::ASENSING::_gps_week_number_type arg)
  {
    msg_.gps_week_number = std::move(arg);
    return Init_ASENSING_temperature(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_sec_of_week
{
public:
  explicit Init_ASENSING_sec_of_week(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_gps_week_number sec_of_week(::imu_msgs::msg::ASENSING::_sec_of_week_type arg)
  {
    msg_.sec_of_week = std::move(arg);
    return Init_ASENSING_gps_week_number(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_position_type
{
public:
  explicit Init_ASENSING_position_type(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_sec_of_week position_type(::imu_msgs::msg::ASENSING::_position_type_type arg)
  {
    msg_.position_type = std::move(arg);
    return Init_ASENSING_sec_of_week(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_ins_status
{
public:
  explicit Init_ASENSING_ins_status(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_position_type ins_status(::imu_msgs::msg::ASENSING::_ins_status_type arg)
  {
    msg_.ins_status = std::move(arg);
    return Init_ASENSING_position_type(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_azimuth_std
{
public:
  explicit Init_ASENSING_azimuth_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_ins_status azimuth_std(::imu_msgs::msg::ASENSING::_azimuth_std_type arg)
  {
    msg_.azimuth_std = std::move(arg);
    return Init_ASENSING_ins_status(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_pitch_std
{
public:
  explicit Init_ASENSING_pitch_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_azimuth_std pitch_std(::imu_msgs::msg::ASENSING::_pitch_std_type arg)
  {
    msg_.pitch_std = std::move(arg);
    return Init_ASENSING_azimuth_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_roll_std
{
public:
  explicit Init_ASENSING_roll_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_pitch_std roll_std(::imu_msgs::msg::ASENSING::_roll_std_type arg)
  {
    msg_.roll_std = std::move(arg);
    return Init_ASENSING_pitch_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_ground_velocity_std
{
public:
  explicit Init_ASENSING_ground_velocity_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_roll_std ground_velocity_std(::imu_msgs::msg::ASENSING::_ground_velocity_std_type arg)
  {
    msg_.ground_velocity_std = std::move(arg);
    return Init_ASENSING_roll_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_east_velocity_std
{
public:
  explicit Init_ASENSING_east_velocity_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_ground_velocity_std east_velocity_std(::imu_msgs::msg::ASENSING::_east_velocity_std_type arg)
  {
    msg_.east_velocity_std = std::move(arg);
    return Init_ASENSING_ground_velocity_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_north_velocity_std
{
public:
  explicit Init_ASENSING_north_velocity_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_east_velocity_std north_velocity_std(::imu_msgs::msg::ASENSING::_north_velocity_std_type arg)
  {
    msg_.north_velocity_std = std::move(arg);
    return Init_ASENSING_east_velocity_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_altitude_std
{
public:
  explicit Init_ASENSING_altitude_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_north_velocity_std altitude_std(::imu_msgs::msg::ASENSING::_altitude_std_type arg)
  {
    msg_.altitude_std = std::move(arg);
    return Init_ASENSING_north_velocity_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_longitude_std
{
public:
  explicit Init_ASENSING_longitude_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_altitude_std longitude_std(::imu_msgs::msg::ASENSING::_longitude_std_type arg)
  {
    msg_.longitude_std = std::move(arg);
    return Init_ASENSING_altitude_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_latitude_std
{
public:
  explicit Init_ASENSING_latitude_std(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_longitude_std latitude_std(::imu_msgs::msg::ASENSING::_latitude_std_type arg)
  {
    msg_.latitude_std = std::move(arg);
    return Init_ASENSING_longitude_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_z_acc
{
public:
  explicit Init_ASENSING_z_acc(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_latitude_std z_acc(::imu_msgs::msg::ASENSING::_z_acc_type arg)
  {
    msg_.z_acc = std::move(arg);
    return Init_ASENSING_latitude_std(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_y_acc
{
public:
  explicit Init_ASENSING_y_acc(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_z_acc y_acc(::imu_msgs::msg::ASENSING::_y_acc_type arg)
  {
    msg_.y_acc = std::move(arg);
    return Init_ASENSING_z_acc(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_x_acc
{
public:
  explicit Init_ASENSING_x_acc(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_y_acc x_acc(::imu_msgs::msg::ASENSING::_x_acc_type arg)
  {
    msg_.x_acc = std::move(arg);
    return Init_ASENSING_y_acc(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_z_angular_velocity
{
public:
  explicit Init_ASENSING_z_angular_velocity(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_x_acc z_angular_velocity(::imu_msgs::msg::ASENSING::_z_angular_velocity_type arg)
  {
    msg_.z_angular_velocity = std::move(arg);
    return Init_ASENSING_x_acc(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_y_angular_velocity
{
public:
  explicit Init_ASENSING_y_angular_velocity(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_z_angular_velocity y_angular_velocity(::imu_msgs::msg::ASENSING::_y_angular_velocity_type arg)
  {
    msg_.y_angular_velocity = std::move(arg);
    return Init_ASENSING_z_angular_velocity(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_x_angular_velocity
{
public:
  explicit Init_ASENSING_x_angular_velocity(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_y_angular_velocity x_angular_velocity(::imu_msgs::msg::ASENSING::_x_angular_velocity_type arg)
  {
    msg_.x_angular_velocity = std::move(arg);
    return Init_ASENSING_y_angular_velocity(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_azimuth
{
public:
  explicit Init_ASENSING_azimuth(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_x_angular_velocity azimuth(::imu_msgs::msg::ASENSING::_azimuth_type arg)
  {
    msg_.azimuth = std::move(arg);
    return Init_ASENSING_x_angular_velocity(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_pitch
{
public:
  explicit Init_ASENSING_pitch(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_azimuth pitch(::imu_msgs::msg::ASENSING::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_ASENSING_azimuth(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_roll
{
public:
  explicit Init_ASENSING_roll(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_pitch roll(::imu_msgs::msg::ASENSING::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_ASENSING_pitch(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_ground_velocity
{
public:
  explicit Init_ASENSING_ground_velocity(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_roll ground_velocity(::imu_msgs::msg::ASENSING::_ground_velocity_type arg)
  {
    msg_.ground_velocity = std::move(arg);
    return Init_ASENSING_roll(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_east_velocity
{
public:
  explicit Init_ASENSING_east_velocity(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_ground_velocity east_velocity(::imu_msgs::msg::ASENSING::_east_velocity_type arg)
  {
    msg_.east_velocity = std::move(arg);
    return Init_ASENSING_ground_velocity(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_north_velocity
{
public:
  explicit Init_ASENSING_north_velocity(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_east_velocity north_velocity(::imu_msgs::msg::ASENSING::_north_velocity_type arg)
  {
    msg_.north_velocity = std::move(arg);
    return Init_ASENSING_east_velocity(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_altitude
{
public:
  explicit Init_ASENSING_altitude(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_north_velocity altitude(::imu_msgs::msg::ASENSING::_altitude_type arg)
  {
    msg_.altitude = std::move(arg);
    return Init_ASENSING_north_velocity(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_longitude
{
public:
  explicit Init_ASENSING_longitude(::imu_msgs::msg::ASENSING & msg)
  : msg_(msg)
  {}
  Init_ASENSING_altitude longitude(::imu_msgs::msg::ASENSING::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_ASENSING_altitude(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

class Init_ASENSING_latitude
{
public:
  Init_ASENSING_latitude()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ASENSING_longitude latitude(::imu_msgs::msg::ASENSING::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_ASENSING_longitude(msg_);
  }

private:
  ::imu_msgs::msg::ASENSING msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::imu_msgs::msg::ASENSING>()
{
  return imu_msgs::msg::builder::Init_ASENSING_latitude();
}

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__ASENSING__BUILDER_HPP_
