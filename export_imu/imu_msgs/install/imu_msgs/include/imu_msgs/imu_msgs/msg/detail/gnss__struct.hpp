// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from imu_msgs:msg/Gnss.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__GNSS__STRUCT_HPP_
#define IMU_MSGS__MSG__DETAIL__GNSS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__imu_msgs__msg__Gnss __attribute__((deprecated))
#else
# define DEPRECATED__imu_msgs__msg__Gnss __declspec(deprecated)
#endif

namespace imu_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Gnss_
{
  using Type = Gnss_<ContainerAllocator>;

  explicit Gnss_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->longitude = 0.0;
      this->lon_sigma = 0.0f;
      this->latitude = 0.0;
      this->lat_sigma = 0.0f;
      this->altitude = 0.0;
      this->alt_sigma = 0.0f;
      this->gps_fix = 0;
      this->rtk_age = 0;
      this->flags_pos = 0;
      this->flags_vel = 0;
      this->flags_attitude = 0;
      this->flags_time = 0;
      this->hor_vel = 0.0f;
      this->track_angle = 0.0f;
      this->ver_vel = 0.0f;
      this->latency_vel = 0.0f;
      this->base_length = 0.0f;
      this->yaw = 0.0f;
      this->yaw_sigma = 0.0f;
      this->pitch = 0.0f;
      this->pitch_sigma = 0.0f;
      this->utc_time = "";
      this->ts_pos = 0ul;
      this->ts_vel = 0ul;
      this->ts_heading = 0ul;
      this->state = 0;
      this->num_master = 0;
      this->gdop = 0.0f;
      this->pdop = 0.0f;
      this->hdop = 0.0f;
      this->htdop = 0.0f;
      this->tdop = 0.0f;
      this->num_reserve = 0;
    }
  }

  explicit Gnss_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    utc_time(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->longitude = 0.0;
      this->lon_sigma = 0.0f;
      this->latitude = 0.0;
      this->lat_sigma = 0.0f;
      this->altitude = 0.0;
      this->alt_sigma = 0.0f;
      this->gps_fix = 0;
      this->rtk_age = 0;
      this->flags_pos = 0;
      this->flags_vel = 0;
      this->flags_attitude = 0;
      this->flags_time = 0;
      this->hor_vel = 0.0f;
      this->track_angle = 0.0f;
      this->ver_vel = 0.0f;
      this->latency_vel = 0.0f;
      this->base_length = 0.0f;
      this->yaw = 0.0f;
      this->yaw_sigma = 0.0f;
      this->pitch = 0.0f;
      this->pitch_sigma = 0.0f;
      this->utc_time = "";
      this->ts_pos = 0ul;
      this->ts_vel = 0ul;
      this->ts_heading = 0ul;
      this->state = 0;
      this->num_master = 0;
      this->gdop = 0.0f;
      this->pdop = 0.0f;
      this->hdop = 0.0f;
      this->htdop = 0.0f;
      this->tdop = 0.0f;
      this->num_reserve = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _longitude_type =
    double;
  _longitude_type longitude;
  using _lon_sigma_type =
    float;
  _lon_sigma_type lon_sigma;
  using _latitude_type =
    double;
  _latitude_type latitude;
  using _lat_sigma_type =
    float;
  _lat_sigma_type lat_sigma;
  using _altitude_type =
    double;
  _altitude_type altitude;
  using _alt_sigma_type =
    float;
  _alt_sigma_type alt_sigma;
  using _gps_fix_type =
    uint16_t;
  _gps_fix_type gps_fix;
  using _rtk_age_type =
    uint16_t;
  _rtk_age_type rtk_age;
  using _flags_pos_type =
    uint8_t;
  _flags_pos_type flags_pos;
  using _flags_vel_type =
    uint8_t;
  _flags_vel_type flags_vel;
  using _flags_attitude_type =
    uint8_t;
  _flags_attitude_type flags_attitude;
  using _flags_time_type =
    uint8_t;
  _flags_time_type flags_time;
  using _hor_vel_type =
    float;
  _hor_vel_type hor_vel;
  using _track_angle_type =
    float;
  _track_angle_type track_angle;
  using _ver_vel_type =
    float;
  _ver_vel_type ver_vel;
  using _latency_vel_type =
    float;
  _latency_vel_type latency_vel;
  using _base_length_type =
    float;
  _base_length_type base_length;
  using _yaw_type =
    float;
  _yaw_type yaw;
  using _yaw_sigma_type =
    float;
  _yaw_sigma_type yaw_sigma;
  using _pitch_type =
    float;
  _pitch_type pitch;
  using _pitch_sigma_type =
    float;
  _pitch_sigma_type pitch_sigma;
  using _utc_time_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _utc_time_type utc_time;
  using _ts_pos_type =
    uint32_t;
  _ts_pos_type ts_pos;
  using _ts_vel_type =
    uint32_t;
  _ts_vel_type ts_vel;
  using _ts_heading_type =
    uint32_t;
  _ts_heading_type ts_heading;
  using _state_type =
    uint8_t;
  _state_type state;
  using _num_master_type =
    uint8_t;
  _num_master_type num_master;
  using _gdop_type =
    float;
  _gdop_type gdop;
  using _pdop_type =
    float;
  _pdop_type pdop;
  using _hdop_type =
    float;
  _hdop_type hdop;
  using _htdop_type =
    float;
  _htdop_type htdop;
  using _tdop_type =
    float;
  _tdop_type tdop;
  using _num_reserve_type =
    uint8_t;
  _num_reserve_type num_reserve;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__longitude(
    const double & _arg)
  {
    this->longitude = _arg;
    return *this;
  }
  Type & set__lon_sigma(
    const float & _arg)
  {
    this->lon_sigma = _arg;
    return *this;
  }
  Type & set__latitude(
    const double & _arg)
  {
    this->latitude = _arg;
    return *this;
  }
  Type & set__lat_sigma(
    const float & _arg)
  {
    this->lat_sigma = _arg;
    return *this;
  }
  Type & set__altitude(
    const double & _arg)
  {
    this->altitude = _arg;
    return *this;
  }
  Type & set__alt_sigma(
    const float & _arg)
  {
    this->alt_sigma = _arg;
    return *this;
  }
  Type & set__gps_fix(
    const uint16_t & _arg)
  {
    this->gps_fix = _arg;
    return *this;
  }
  Type & set__rtk_age(
    const uint16_t & _arg)
  {
    this->rtk_age = _arg;
    return *this;
  }
  Type & set__flags_pos(
    const uint8_t & _arg)
  {
    this->flags_pos = _arg;
    return *this;
  }
  Type & set__flags_vel(
    const uint8_t & _arg)
  {
    this->flags_vel = _arg;
    return *this;
  }
  Type & set__flags_attitude(
    const uint8_t & _arg)
  {
    this->flags_attitude = _arg;
    return *this;
  }
  Type & set__flags_time(
    const uint8_t & _arg)
  {
    this->flags_time = _arg;
    return *this;
  }
  Type & set__hor_vel(
    const float & _arg)
  {
    this->hor_vel = _arg;
    return *this;
  }
  Type & set__track_angle(
    const float & _arg)
  {
    this->track_angle = _arg;
    return *this;
  }
  Type & set__ver_vel(
    const float & _arg)
  {
    this->ver_vel = _arg;
    return *this;
  }
  Type & set__latency_vel(
    const float & _arg)
  {
    this->latency_vel = _arg;
    return *this;
  }
  Type & set__base_length(
    const float & _arg)
  {
    this->base_length = _arg;
    return *this;
  }
  Type & set__yaw(
    const float & _arg)
  {
    this->yaw = _arg;
    return *this;
  }
  Type & set__yaw_sigma(
    const float & _arg)
  {
    this->yaw_sigma = _arg;
    return *this;
  }
  Type & set__pitch(
    const float & _arg)
  {
    this->pitch = _arg;
    return *this;
  }
  Type & set__pitch_sigma(
    const float & _arg)
  {
    this->pitch_sigma = _arg;
    return *this;
  }
  Type & set__utc_time(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->utc_time = _arg;
    return *this;
  }
  Type & set__ts_pos(
    const uint32_t & _arg)
  {
    this->ts_pos = _arg;
    return *this;
  }
  Type & set__ts_vel(
    const uint32_t & _arg)
  {
    this->ts_vel = _arg;
    return *this;
  }
  Type & set__ts_heading(
    const uint32_t & _arg)
  {
    this->ts_heading = _arg;
    return *this;
  }
  Type & set__state(
    const uint8_t & _arg)
  {
    this->state = _arg;
    return *this;
  }
  Type & set__num_master(
    const uint8_t & _arg)
  {
    this->num_master = _arg;
    return *this;
  }
  Type & set__gdop(
    const float & _arg)
  {
    this->gdop = _arg;
    return *this;
  }
  Type & set__pdop(
    const float & _arg)
  {
    this->pdop = _arg;
    return *this;
  }
  Type & set__hdop(
    const float & _arg)
  {
    this->hdop = _arg;
    return *this;
  }
  Type & set__htdop(
    const float & _arg)
  {
    this->htdop = _arg;
    return *this;
  }
  Type & set__tdop(
    const float & _arg)
  {
    this->tdop = _arg;
    return *this;
  }
  Type & set__num_reserve(
    const uint8_t & _arg)
  {
    this->num_reserve = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    imu_msgs::msg::Gnss_<ContainerAllocator> *;
  using ConstRawPtr =
    const imu_msgs::msg::Gnss_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<imu_msgs::msg::Gnss_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<imu_msgs::msg::Gnss_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::Gnss_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::Gnss_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::Gnss_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::Gnss_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<imu_msgs::msg::Gnss_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<imu_msgs::msg::Gnss_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__imu_msgs__msg__Gnss
    std::shared_ptr<imu_msgs::msg::Gnss_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__imu_msgs__msg__Gnss
    std::shared_ptr<imu_msgs::msg::Gnss_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Gnss_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->longitude != other.longitude) {
      return false;
    }
    if (this->lon_sigma != other.lon_sigma) {
      return false;
    }
    if (this->latitude != other.latitude) {
      return false;
    }
    if (this->lat_sigma != other.lat_sigma) {
      return false;
    }
    if (this->altitude != other.altitude) {
      return false;
    }
    if (this->alt_sigma != other.alt_sigma) {
      return false;
    }
    if (this->gps_fix != other.gps_fix) {
      return false;
    }
    if (this->rtk_age != other.rtk_age) {
      return false;
    }
    if (this->flags_pos != other.flags_pos) {
      return false;
    }
    if (this->flags_vel != other.flags_vel) {
      return false;
    }
    if (this->flags_attitude != other.flags_attitude) {
      return false;
    }
    if (this->flags_time != other.flags_time) {
      return false;
    }
    if (this->hor_vel != other.hor_vel) {
      return false;
    }
    if (this->track_angle != other.track_angle) {
      return false;
    }
    if (this->ver_vel != other.ver_vel) {
      return false;
    }
    if (this->latency_vel != other.latency_vel) {
      return false;
    }
    if (this->base_length != other.base_length) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    if (this->yaw_sigma != other.yaw_sigma) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    if (this->pitch_sigma != other.pitch_sigma) {
      return false;
    }
    if (this->utc_time != other.utc_time) {
      return false;
    }
    if (this->ts_pos != other.ts_pos) {
      return false;
    }
    if (this->ts_vel != other.ts_vel) {
      return false;
    }
    if (this->ts_heading != other.ts_heading) {
      return false;
    }
    if (this->state != other.state) {
      return false;
    }
    if (this->num_master != other.num_master) {
      return false;
    }
    if (this->gdop != other.gdop) {
      return false;
    }
    if (this->pdop != other.pdop) {
      return false;
    }
    if (this->hdop != other.hdop) {
      return false;
    }
    if (this->htdop != other.htdop) {
      return false;
    }
    if (this->tdop != other.tdop) {
      return false;
    }
    if (this->num_reserve != other.num_reserve) {
      return false;
    }
    return true;
  }
  bool operator!=(const Gnss_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Gnss_

// alias to use template instance with default allocator
using Gnss =
  imu_msgs::msg::Gnss_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__GNSS__STRUCT_HPP_
