// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from imu_msgs:msg/Gnss.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__GNSS__BUILDER_HPP_
#define IMU_MSGS__MSG__DETAIL__GNSS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "imu_msgs/msg/detail/gnss__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace imu_msgs
{

namespace msg
{

namespace builder
{

class Init_Gnss_num_reserve
{
public:
  explicit Init_Gnss_num_reserve(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  ::imu_msgs::msg::Gnss num_reserve(::imu_msgs::msg::Gnss::_num_reserve_type arg)
  {
    msg_.num_reserve = std::move(arg);
    return std::move(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_tdop
{
public:
  explicit Init_Gnss_tdop(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_num_reserve tdop(::imu_msgs::msg::Gnss::_tdop_type arg)
  {
    msg_.tdop = std::move(arg);
    return Init_Gnss_num_reserve(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_htdop
{
public:
  explicit Init_Gnss_htdop(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_tdop htdop(::imu_msgs::msg::Gnss::_htdop_type arg)
  {
    msg_.htdop = std::move(arg);
    return Init_Gnss_tdop(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_hdop
{
public:
  explicit Init_Gnss_hdop(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_htdop hdop(::imu_msgs::msg::Gnss::_hdop_type arg)
  {
    msg_.hdop = std::move(arg);
    return Init_Gnss_htdop(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_pdop
{
public:
  explicit Init_Gnss_pdop(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_hdop pdop(::imu_msgs::msg::Gnss::_pdop_type arg)
  {
    msg_.pdop = std::move(arg);
    return Init_Gnss_hdop(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_gdop
{
public:
  explicit Init_Gnss_gdop(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_pdop gdop(::imu_msgs::msg::Gnss::_gdop_type arg)
  {
    msg_.gdop = std::move(arg);
    return Init_Gnss_pdop(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_num_master
{
public:
  explicit Init_Gnss_num_master(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_gdop num_master(::imu_msgs::msg::Gnss::_num_master_type arg)
  {
    msg_.num_master = std::move(arg);
    return Init_Gnss_gdop(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_state
{
public:
  explicit Init_Gnss_state(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_num_master state(::imu_msgs::msg::Gnss::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_Gnss_num_master(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_ts_heading
{
public:
  explicit Init_Gnss_ts_heading(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_state ts_heading(::imu_msgs::msg::Gnss::_ts_heading_type arg)
  {
    msg_.ts_heading = std::move(arg);
    return Init_Gnss_state(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_ts_vel
{
public:
  explicit Init_Gnss_ts_vel(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_ts_heading ts_vel(::imu_msgs::msg::Gnss::_ts_vel_type arg)
  {
    msg_.ts_vel = std::move(arg);
    return Init_Gnss_ts_heading(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_ts_pos
{
public:
  explicit Init_Gnss_ts_pos(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_ts_vel ts_pos(::imu_msgs::msg::Gnss::_ts_pos_type arg)
  {
    msg_.ts_pos = std::move(arg);
    return Init_Gnss_ts_vel(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_utc_time
{
public:
  explicit Init_Gnss_utc_time(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_ts_pos utc_time(::imu_msgs::msg::Gnss::_utc_time_type arg)
  {
    msg_.utc_time = std::move(arg);
    return Init_Gnss_ts_pos(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_pitch_sigma
{
public:
  explicit Init_Gnss_pitch_sigma(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_utc_time pitch_sigma(::imu_msgs::msg::Gnss::_pitch_sigma_type arg)
  {
    msg_.pitch_sigma = std::move(arg);
    return Init_Gnss_utc_time(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_pitch
{
public:
  explicit Init_Gnss_pitch(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_pitch_sigma pitch(::imu_msgs::msg::Gnss::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_Gnss_pitch_sigma(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_yaw_sigma
{
public:
  explicit Init_Gnss_yaw_sigma(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_pitch yaw_sigma(::imu_msgs::msg::Gnss::_yaw_sigma_type arg)
  {
    msg_.yaw_sigma = std::move(arg);
    return Init_Gnss_pitch(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_yaw
{
public:
  explicit Init_Gnss_yaw(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_yaw_sigma yaw(::imu_msgs::msg::Gnss::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return Init_Gnss_yaw_sigma(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_base_length
{
public:
  explicit Init_Gnss_base_length(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_yaw base_length(::imu_msgs::msg::Gnss::_base_length_type arg)
  {
    msg_.base_length = std::move(arg);
    return Init_Gnss_yaw(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_latency_vel
{
public:
  explicit Init_Gnss_latency_vel(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_base_length latency_vel(::imu_msgs::msg::Gnss::_latency_vel_type arg)
  {
    msg_.latency_vel = std::move(arg);
    return Init_Gnss_base_length(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_ver_vel
{
public:
  explicit Init_Gnss_ver_vel(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_latency_vel ver_vel(::imu_msgs::msg::Gnss::_ver_vel_type arg)
  {
    msg_.ver_vel = std::move(arg);
    return Init_Gnss_latency_vel(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_track_angle
{
public:
  explicit Init_Gnss_track_angle(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_ver_vel track_angle(::imu_msgs::msg::Gnss::_track_angle_type arg)
  {
    msg_.track_angle = std::move(arg);
    return Init_Gnss_ver_vel(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_hor_vel
{
public:
  explicit Init_Gnss_hor_vel(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_track_angle hor_vel(::imu_msgs::msg::Gnss::_hor_vel_type arg)
  {
    msg_.hor_vel = std::move(arg);
    return Init_Gnss_track_angle(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_flags_time
{
public:
  explicit Init_Gnss_flags_time(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_hor_vel flags_time(::imu_msgs::msg::Gnss::_flags_time_type arg)
  {
    msg_.flags_time = std::move(arg);
    return Init_Gnss_hor_vel(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_flags_attitude
{
public:
  explicit Init_Gnss_flags_attitude(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_flags_time flags_attitude(::imu_msgs::msg::Gnss::_flags_attitude_type arg)
  {
    msg_.flags_attitude = std::move(arg);
    return Init_Gnss_flags_time(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_flags_vel
{
public:
  explicit Init_Gnss_flags_vel(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_flags_attitude flags_vel(::imu_msgs::msg::Gnss::_flags_vel_type arg)
  {
    msg_.flags_vel = std::move(arg);
    return Init_Gnss_flags_attitude(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_flags_pos
{
public:
  explicit Init_Gnss_flags_pos(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_flags_vel flags_pos(::imu_msgs::msg::Gnss::_flags_pos_type arg)
  {
    msg_.flags_pos = std::move(arg);
    return Init_Gnss_flags_vel(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_rtk_age
{
public:
  explicit Init_Gnss_rtk_age(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_flags_pos rtk_age(::imu_msgs::msg::Gnss::_rtk_age_type arg)
  {
    msg_.rtk_age = std::move(arg);
    return Init_Gnss_flags_pos(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_gps_fix
{
public:
  explicit Init_Gnss_gps_fix(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_rtk_age gps_fix(::imu_msgs::msg::Gnss::_gps_fix_type arg)
  {
    msg_.gps_fix = std::move(arg);
    return Init_Gnss_rtk_age(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_alt_sigma
{
public:
  explicit Init_Gnss_alt_sigma(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_gps_fix alt_sigma(::imu_msgs::msg::Gnss::_alt_sigma_type arg)
  {
    msg_.alt_sigma = std::move(arg);
    return Init_Gnss_gps_fix(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_altitude
{
public:
  explicit Init_Gnss_altitude(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_alt_sigma altitude(::imu_msgs::msg::Gnss::_altitude_type arg)
  {
    msg_.altitude = std::move(arg);
    return Init_Gnss_alt_sigma(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_lat_sigma
{
public:
  explicit Init_Gnss_lat_sigma(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_altitude lat_sigma(::imu_msgs::msg::Gnss::_lat_sigma_type arg)
  {
    msg_.lat_sigma = std::move(arg);
    return Init_Gnss_altitude(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_latitude
{
public:
  explicit Init_Gnss_latitude(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_lat_sigma latitude(::imu_msgs::msg::Gnss::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_Gnss_lat_sigma(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_lon_sigma
{
public:
  explicit Init_Gnss_lon_sigma(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_latitude lon_sigma(::imu_msgs::msg::Gnss::_lon_sigma_type arg)
  {
    msg_.lon_sigma = std::move(arg);
    return Init_Gnss_latitude(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_longitude
{
public:
  explicit Init_Gnss_longitude(::imu_msgs::msg::Gnss & msg)
  : msg_(msg)
  {}
  Init_Gnss_lon_sigma longitude(::imu_msgs::msg::Gnss::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_Gnss_lon_sigma(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

class Init_Gnss_header
{
public:
  Init_Gnss_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Gnss_longitude header(::imu_msgs::msg::Gnss::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Gnss_longitude(msg_);
  }

private:
  ::imu_msgs::msg::Gnss msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::imu_msgs::msg::Gnss>()
{
  return imu_msgs::msg::builder::Init_Gnss_header();
}

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__GNSS__BUILDER_HPP_
