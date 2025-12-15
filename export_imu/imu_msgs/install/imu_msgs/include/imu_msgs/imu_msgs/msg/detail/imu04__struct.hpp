// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from imu_msgs:msg/Imu04.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU04__STRUCT_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU04__STRUCT_HPP_

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
# define DEPRECATED__imu_msgs__msg__Imu04 __attribute__((deprecated))
#else
# define DEPRECATED__imu_msgs__msg__Imu04 __declspec(deprecated)
#endif

namespace imu_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Imu04_
{
  using Type = Imu04_<ContainerAllocator>;

  explicit Imu04_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->roll = 0.0f;
      this->pitch = 0.0f;
      this->yaw = 0.0f;
      this->gx = 0.0f;
      this->gy = 0.0f;
      this->gz = 0.0f;
      this->ax = 0.0f;
      this->ay = 0.0f;
      this->az = 0.0f;
      this->temperature = 0.0f;
      this->time = 0.0f;
      std::fill<typename std::array<uint8_t, 14>::iterator, uint8_t>(this->gps_message.begin(), this->gps_message.end(), 0);
      this->gps_heading_status = 0;
      this->ptype = 0;
      this->pdata = 0;
      this->ver_pos = 0.0f;
      this->ver_vel = 0.0f;
      this->info_byte = 0;
      this->msg_type = 0;
    }
  }

  explicit Imu04_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    gps_message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->roll = 0.0f;
      this->pitch = 0.0f;
      this->yaw = 0.0f;
      this->gx = 0.0f;
      this->gy = 0.0f;
      this->gz = 0.0f;
      this->ax = 0.0f;
      this->ay = 0.0f;
      this->az = 0.0f;
      this->temperature = 0.0f;
      this->time = 0.0f;
      std::fill<typename std::array<uint8_t, 14>::iterator, uint8_t>(this->gps_message.begin(), this->gps_message.end(), 0);
      this->gps_heading_status = 0;
      this->ptype = 0;
      this->pdata = 0;
      this->ver_pos = 0.0f;
      this->ver_vel = 0.0f;
      this->info_byte = 0;
      this->msg_type = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _roll_type =
    float;
  _roll_type roll;
  using _pitch_type =
    float;
  _pitch_type pitch;
  using _yaw_type =
    float;
  _yaw_type yaw;
  using _gx_type =
    float;
  _gx_type gx;
  using _gy_type =
    float;
  _gy_type gy;
  using _gz_type =
    float;
  _gz_type gz;
  using _ax_type =
    float;
  _ax_type ax;
  using _ay_type =
    float;
  _ay_type ay;
  using _az_type =
    float;
  _az_type az;
  using _temperature_type =
    float;
  _temperature_type temperature;
  using _time_type =
    float;
  _time_type time;
  using _gps_message_type =
    std::array<uint8_t, 14>;
  _gps_message_type gps_message;
  using _gps_heading_status_type =
    uint8_t;
  _gps_heading_status_type gps_heading_status;
  using _ptype_type =
    uint8_t;
  _ptype_type ptype;
  using _pdata_type =
    uint16_t;
  _pdata_type pdata;
  using _ver_pos_type =
    float;
  _ver_pos_type ver_pos;
  using _ver_vel_type =
    float;
  _ver_vel_type ver_vel;
  using _info_byte_type =
    uint16_t;
  _info_byte_type info_byte;
  using _msg_type_type =
    uint8_t;
  _msg_type_type msg_type;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__roll(
    const float & _arg)
  {
    this->roll = _arg;
    return *this;
  }
  Type & set__pitch(
    const float & _arg)
  {
    this->pitch = _arg;
    return *this;
  }
  Type & set__yaw(
    const float & _arg)
  {
    this->yaw = _arg;
    return *this;
  }
  Type & set__gx(
    const float & _arg)
  {
    this->gx = _arg;
    return *this;
  }
  Type & set__gy(
    const float & _arg)
  {
    this->gy = _arg;
    return *this;
  }
  Type & set__gz(
    const float & _arg)
  {
    this->gz = _arg;
    return *this;
  }
  Type & set__ax(
    const float & _arg)
  {
    this->ax = _arg;
    return *this;
  }
  Type & set__ay(
    const float & _arg)
  {
    this->ay = _arg;
    return *this;
  }
  Type & set__az(
    const float & _arg)
  {
    this->az = _arg;
    return *this;
  }
  Type & set__temperature(
    const float & _arg)
  {
    this->temperature = _arg;
    return *this;
  }
  Type & set__time(
    const float & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__gps_message(
    const std::array<uint8_t, 14> & _arg)
  {
    this->gps_message = _arg;
    return *this;
  }
  Type & set__gps_heading_status(
    const uint8_t & _arg)
  {
    this->gps_heading_status = _arg;
    return *this;
  }
  Type & set__ptype(
    const uint8_t & _arg)
  {
    this->ptype = _arg;
    return *this;
  }
  Type & set__pdata(
    const uint16_t & _arg)
  {
    this->pdata = _arg;
    return *this;
  }
  Type & set__ver_pos(
    const float & _arg)
  {
    this->ver_pos = _arg;
    return *this;
  }
  Type & set__ver_vel(
    const float & _arg)
  {
    this->ver_vel = _arg;
    return *this;
  }
  Type & set__info_byte(
    const uint16_t & _arg)
  {
    this->info_byte = _arg;
    return *this;
  }
  Type & set__msg_type(
    const uint8_t & _arg)
  {
    this->msg_type = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    imu_msgs::msg::Imu04_<ContainerAllocator> *;
  using ConstRawPtr =
    const imu_msgs::msg::Imu04_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<imu_msgs::msg::Imu04_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<imu_msgs::msg::Imu04_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::Imu04_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::Imu04_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::Imu04_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::Imu04_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<imu_msgs::msg::Imu04_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<imu_msgs::msg::Imu04_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__imu_msgs__msg__Imu04
    std::shared_ptr<imu_msgs::msg::Imu04_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__imu_msgs__msg__Imu04
    std::shared_ptr<imu_msgs::msg::Imu04_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Imu04_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->roll != other.roll) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    if (this->gx != other.gx) {
      return false;
    }
    if (this->gy != other.gy) {
      return false;
    }
    if (this->gz != other.gz) {
      return false;
    }
    if (this->ax != other.ax) {
      return false;
    }
    if (this->ay != other.ay) {
      return false;
    }
    if (this->az != other.az) {
      return false;
    }
    if (this->temperature != other.temperature) {
      return false;
    }
    if (this->time != other.time) {
      return false;
    }
    if (this->gps_message != other.gps_message) {
      return false;
    }
    if (this->gps_heading_status != other.gps_heading_status) {
      return false;
    }
    if (this->ptype != other.ptype) {
      return false;
    }
    if (this->pdata != other.pdata) {
      return false;
    }
    if (this->ver_pos != other.ver_pos) {
      return false;
    }
    if (this->ver_vel != other.ver_vel) {
      return false;
    }
    if (this->info_byte != other.info_byte) {
      return false;
    }
    if (this->msg_type != other.msg_type) {
      return false;
    }
    return true;
  }
  bool operator!=(const Imu04_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Imu04_

// alias to use template instance with default allocator
using Imu04 =
  imu_msgs::msg::Imu04_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__IMU04__STRUCT_HPP_
