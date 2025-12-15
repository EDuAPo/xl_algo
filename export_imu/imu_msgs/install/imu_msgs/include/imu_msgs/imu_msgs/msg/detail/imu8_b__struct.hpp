// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from imu_msgs:msg/Imu8B.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU8_B__STRUCT_HPP_
#define IMU_MSGS__MSG__DETAIL__IMU8_B__STRUCT_HPP_

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
# define DEPRECATED__imu_msgs__msg__Imu8B __attribute__((deprecated))
#else
# define DEPRECATED__imu_msgs__msg__Imu8B __declspec(deprecated)
#endif

namespace imu_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Imu8B_
{
  using Type = Imu8B_<ContainerAllocator>;

  explicit Imu8B_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->type = 0;
      this->data_length = 0;
      this->frame_count = 0ul;
      this->serial_number = 0;
      this->gx = 0.0f;
      this->gy = 0.0f;
      this->gz = 0.0f;
      this->ax = 0.0f;
      this->ay = 0.0f;
      this->az = 0.0f;
      this->temperature = 0.0f;
      this->status = 0;
    }
  }

  explicit Imu8B_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->type = 0;
      this->data_length = 0;
      this->frame_count = 0ul;
      this->serial_number = 0;
      this->gx = 0.0f;
      this->gy = 0.0f;
      this->gz = 0.0f;
      this->ax = 0.0f;
      this->ay = 0.0f;
      this->az = 0.0f;
      this->temperature = 0.0f;
      this->status = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _type_type =
    uint8_t;
  _type_type type;
  using _data_length_type =
    uint16_t;
  _data_length_type data_length;
  using _frame_count_type =
    uint32_t;
  _frame_count_type frame_count;
  using _serial_number_type =
    uint8_t;
  _serial_number_type serial_number;
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
  using _status_type =
    uint8_t;
  _status_type status;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__type(
    const uint8_t & _arg)
  {
    this->type = _arg;
    return *this;
  }
  Type & set__data_length(
    const uint16_t & _arg)
  {
    this->data_length = _arg;
    return *this;
  }
  Type & set__frame_count(
    const uint32_t & _arg)
  {
    this->frame_count = _arg;
    return *this;
  }
  Type & set__serial_number(
    const uint8_t & _arg)
  {
    this->serial_number = _arg;
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
  Type & set__status(
    const uint8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    imu_msgs::msg::Imu8B_<ContainerAllocator> *;
  using ConstRawPtr =
    const imu_msgs::msg::Imu8B_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<imu_msgs::msg::Imu8B_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<imu_msgs::msg::Imu8B_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::Imu8B_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::Imu8B_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::Imu8B_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::Imu8B_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<imu_msgs::msg::Imu8B_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<imu_msgs::msg::Imu8B_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__imu_msgs__msg__Imu8B
    std::shared_ptr<imu_msgs::msg::Imu8B_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__imu_msgs__msg__Imu8B
    std::shared_ptr<imu_msgs::msg::Imu8B_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Imu8B_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->type != other.type) {
      return false;
    }
    if (this->data_length != other.data_length) {
      return false;
    }
    if (this->frame_count != other.frame_count) {
      return false;
    }
    if (this->serial_number != other.serial_number) {
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
    if (this->status != other.status) {
      return false;
    }
    return true;
  }
  bool operator!=(const Imu8B_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Imu8B_

// alias to use template instance with default allocator
using Imu8B =
  imu_msgs::msg::Imu8B_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__IMU8_B__STRUCT_HPP_
