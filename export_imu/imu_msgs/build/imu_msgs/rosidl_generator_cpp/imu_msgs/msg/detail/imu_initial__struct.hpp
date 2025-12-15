// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from imu_msgs:msg/ImuInitial.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU_INITIAL__STRUCT_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU_INITIAL__STRUCT_HPP_

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
# define DEPRECATED__imu_msgs__msg__ImuInitial __attribute__((deprecated))
#else
# define DEPRECATED__imu_msgs__msg__ImuInitial __declspec(deprecated)
#endif

namespace imu_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ImuInitial_
{
  using Type = ImuInitial_<ContainerAllocator>;

  explicit ImuInitial_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->gx = 0.0f;
      this->gy = 0.0f;
      this->gz = 0.0f;
      this->ax = 0.0f;
      this->ay = 0.0f;
      this->az = 0.0f;
      this->temperature = 0.0f;
      this->imu_time_stamp = 0.0;
    }
  }

  explicit ImuInitial_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->gx = 0.0f;
      this->gy = 0.0f;
      this->gz = 0.0f;
      this->ax = 0.0f;
      this->ay = 0.0f;
      this->az = 0.0f;
      this->temperature = 0.0f;
      this->imu_time_stamp = 0.0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
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
  using _imu_time_stamp_type =
    double;
  _imu_time_stamp_type imu_time_stamp;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
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
  Type & set__imu_time_stamp(
    const double & _arg)
  {
    this->imu_time_stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    imu_msgs::msg::ImuInitial_<ContainerAllocator> *;
  using ConstRawPtr =
    const imu_msgs::msg::ImuInitial_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<imu_msgs::msg::ImuInitial_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<imu_msgs::msg::ImuInitial_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::ImuInitial_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::ImuInitial_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::ImuInitial_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::ImuInitial_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<imu_msgs::msg::ImuInitial_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<imu_msgs::msg::ImuInitial_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__imu_msgs__msg__ImuInitial
    std::shared_ptr<imu_msgs::msg::ImuInitial_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__imu_msgs__msg__ImuInitial
    std::shared_ptr<imu_msgs::msg::ImuInitial_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ImuInitial_ & other) const
  {
    if (this->header != other.header) {
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
    if (this->imu_time_stamp != other.imu_time_stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const ImuInitial_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ImuInitial_

// alias to use template instance with default allocator
using ImuInitial =
  imu_msgs::msg::ImuInitial_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__IMU_INITIAL__STRUCT_HPP_
