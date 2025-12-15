// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from imu_msgs:msg/Odom.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ODOM__STRUCT_HPP_
#define IMU_MSGS__MSG__DETAIL__ODOM__STRUCT_HPP_

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
# define DEPRECATED__imu_msgs__msg__Odom __attribute__((deprecated))
#else
# define DEPRECATED__imu_msgs__msg__Odom __declspec(deprecated)
#endif

namespace imu_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Odom_
{
  using Type = Odom_<ContainerAllocator>;

  explicit Odom_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->q0_w = 0.0f;
      this->q1_x = 0.0f;
      this->q2_y = 0.0f;
      this->q3_z = 0.0f;
      this->pos_x = 0.0f;
      this->pos_y = 0.0f;
      this->pos_z = 0.0f;
      this->vel_x = 0.0f;
      this->vel_y = 0.0f;
      this->vel_z = 0.0f;
      this->vel = 0.0f;
      this->ang_vel_x = 0.0f;
      this->ang_vel_y = 0.0f;
      this->ang_vel_z = 0.0f;
      this->acc_x = 0.0f;
      this->acc_y = 0.0f;
      this->acc_z = 0.0f;
      this->status = 0;
      this->sensor_status = 0ul;
      this->pos_x_std = 0.0f;
      this->pos_y_std = 0.0f;
      this->pos_z_std = 0.0f;
      this->vel_x_std = 0.0f;
      this->vel_y_std = 0.0f;
      this->vel_z_std = 0.0f;
      this->roll_std = 0.0f;
      this->pitch_std = 0.0f;
      this->yaw_std = 0.0f;
      this->tow_ms = 0ul;
    }
  }

  explicit Odom_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->q0_w = 0.0f;
      this->q1_x = 0.0f;
      this->q2_y = 0.0f;
      this->q3_z = 0.0f;
      this->pos_x = 0.0f;
      this->pos_y = 0.0f;
      this->pos_z = 0.0f;
      this->vel_x = 0.0f;
      this->vel_y = 0.0f;
      this->vel_z = 0.0f;
      this->vel = 0.0f;
      this->ang_vel_x = 0.0f;
      this->ang_vel_y = 0.0f;
      this->ang_vel_z = 0.0f;
      this->acc_x = 0.0f;
      this->acc_y = 0.0f;
      this->acc_z = 0.0f;
      this->status = 0;
      this->sensor_status = 0ul;
      this->pos_x_std = 0.0f;
      this->pos_y_std = 0.0f;
      this->pos_z_std = 0.0f;
      this->vel_x_std = 0.0f;
      this->vel_y_std = 0.0f;
      this->vel_z_std = 0.0f;
      this->roll_std = 0.0f;
      this->pitch_std = 0.0f;
      this->yaw_std = 0.0f;
      this->tow_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _q0_w_type =
    float;
  _q0_w_type q0_w;
  using _q1_x_type =
    float;
  _q1_x_type q1_x;
  using _q2_y_type =
    float;
  _q2_y_type q2_y;
  using _q3_z_type =
    float;
  _q3_z_type q3_z;
  using _pos_x_type =
    float;
  _pos_x_type pos_x;
  using _pos_y_type =
    float;
  _pos_y_type pos_y;
  using _pos_z_type =
    float;
  _pos_z_type pos_z;
  using _vel_x_type =
    float;
  _vel_x_type vel_x;
  using _vel_y_type =
    float;
  _vel_y_type vel_y;
  using _vel_z_type =
    float;
  _vel_z_type vel_z;
  using _vel_type =
    float;
  _vel_type vel;
  using _ang_vel_x_type =
    float;
  _ang_vel_x_type ang_vel_x;
  using _ang_vel_y_type =
    float;
  _ang_vel_y_type ang_vel_y;
  using _ang_vel_z_type =
    float;
  _ang_vel_z_type ang_vel_z;
  using _acc_x_type =
    float;
  _acc_x_type acc_x;
  using _acc_y_type =
    float;
  _acc_y_type acc_y;
  using _acc_z_type =
    float;
  _acc_z_type acc_z;
  using _status_type =
    uint8_t;
  _status_type status;
  using _sensor_status_type =
    uint32_t;
  _sensor_status_type sensor_status;
  using _pos_x_std_type =
    float;
  _pos_x_std_type pos_x_std;
  using _pos_y_std_type =
    float;
  _pos_y_std_type pos_y_std;
  using _pos_z_std_type =
    float;
  _pos_z_std_type pos_z_std;
  using _vel_x_std_type =
    float;
  _vel_x_std_type vel_x_std;
  using _vel_y_std_type =
    float;
  _vel_y_std_type vel_y_std;
  using _vel_z_std_type =
    float;
  _vel_z_std_type vel_z_std;
  using _roll_std_type =
    float;
  _roll_std_type roll_std;
  using _pitch_std_type =
    float;
  _pitch_std_type pitch_std;
  using _yaw_std_type =
    float;
  _yaw_std_type yaw_std;
  using _tow_ms_type =
    uint32_t;
  _tow_ms_type tow_ms;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__q0_w(
    const float & _arg)
  {
    this->q0_w = _arg;
    return *this;
  }
  Type & set__q1_x(
    const float & _arg)
  {
    this->q1_x = _arg;
    return *this;
  }
  Type & set__q2_y(
    const float & _arg)
  {
    this->q2_y = _arg;
    return *this;
  }
  Type & set__q3_z(
    const float & _arg)
  {
    this->q3_z = _arg;
    return *this;
  }
  Type & set__pos_x(
    const float & _arg)
  {
    this->pos_x = _arg;
    return *this;
  }
  Type & set__pos_y(
    const float & _arg)
  {
    this->pos_y = _arg;
    return *this;
  }
  Type & set__pos_z(
    const float & _arg)
  {
    this->pos_z = _arg;
    return *this;
  }
  Type & set__vel_x(
    const float & _arg)
  {
    this->vel_x = _arg;
    return *this;
  }
  Type & set__vel_y(
    const float & _arg)
  {
    this->vel_y = _arg;
    return *this;
  }
  Type & set__vel_z(
    const float & _arg)
  {
    this->vel_z = _arg;
    return *this;
  }
  Type & set__vel(
    const float & _arg)
  {
    this->vel = _arg;
    return *this;
  }
  Type & set__ang_vel_x(
    const float & _arg)
  {
    this->ang_vel_x = _arg;
    return *this;
  }
  Type & set__ang_vel_y(
    const float & _arg)
  {
    this->ang_vel_y = _arg;
    return *this;
  }
  Type & set__ang_vel_z(
    const float & _arg)
  {
    this->ang_vel_z = _arg;
    return *this;
  }
  Type & set__acc_x(
    const float & _arg)
  {
    this->acc_x = _arg;
    return *this;
  }
  Type & set__acc_y(
    const float & _arg)
  {
    this->acc_y = _arg;
    return *this;
  }
  Type & set__acc_z(
    const float & _arg)
  {
    this->acc_z = _arg;
    return *this;
  }
  Type & set__status(
    const uint8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__sensor_status(
    const uint32_t & _arg)
  {
    this->sensor_status = _arg;
    return *this;
  }
  Type & set__pos_x_std(
    const float & _arg)
  {
    this->pos_x_std = _arg;
    return *this;
  }
  Type & set__pos_y_std(
    const float & _arg)
  {
    this->pos_y_std = _arg;
    return *this;
  }
  Type & set__pos_z_std(
    const float & _arg)
  {
    this->pos_z_std = _arg;
    return *this;
  }
  Type & set__vel_x_std(
    const float & _arg)
  {
    this->vel_x_std = _arg;
    return *this;
  }
  Type & set__vel_y_std(
    const float & _arg)
  {
    this->vel_y_std = _arg;
    return *this;
  }
  Type & set__vel_z_std(
    const float & _arg)
  {
    this->vel_z_std = _arg;
    return *this;
  }
  Type & set__roll_std(
    const float & _arg)
  {
    this->roll_std = _arg;
    return *this;
  }
  Type & set__pitch_std(
    const float & _arg)
  {
    this->pitch_std = _arg;
    return *this;
  }
  Type & set__yaw_std(
    const float & _arg)
  {
    this->yaw_std = _arg;
    return *this;
  }
  Type & set__tow_ms(
    const uint32_t & _arg)
  {
    this->tow_ms = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    imu_msgs::msg::Odom_<ContainerAllocator> *;
  using ConstRawPtr =
    const imu_msgs::msg::Odom_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<imu_msgs::msg::Odom_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<imu_msgs::msg::Odom_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::Odom_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::Odom_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::Odom_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::Odom_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<imu_msgs::msg::Odom_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<imu_msgs::msg::Odom_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__imu_msgs__msg__Odom
    std::shared_ptr<imu_msgs::msg::Odom_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__imu_msgs__msg__Odom
    std::shared_ptr<imu_msgs::msg::Odom_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Odom_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->q0_w != other.q0_w) {
      return false;
    }
    if (this->q1_x != other.q1_x) {
      return false;
    }
    if (this->q2_y != other.q2_y) {
      return false;
    }
    if (this->q3_z != other.q3_z) {
      return false;
    }
    if (this->pos_x != other.pos_x) {
      return false;
    }
    if (this->pos_y != other.pos_y) {
      return false;
    }
    if (this->pos_z != other.pos_z) {
      return false;
    }
    if (this->vel_x != other.vel_x) {
      return false;
    }
    if (this->vel_y != other.vel_y) {
      return false;
    }
    if (this->vel_z != other.vel_z) {
      return false;
    }
    if (this->vel != other.vel) {
      return false;
    }
    if (this->ang_vel_x != other.ang_vel_x) {
      return false;
    }
    if (this->ang_vel_y != other.ang_vel_y) {
      return false;
    }
    if (this->ang_vel_z != other.ang_vel_z) {
      return false;
    }
    if (this->acc_x != other.acc_x) {
      return false;
    }
    if (this->acc_y != other.acc_y) {
      return false;
    }
    if (this->acc_z != other.acc_z) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    if (this->sensor_status != other.sensor_status) {
      return false;
    }
    if (this->pos_x_std != other.pos_x_std) {
      return false;
    }
    if (this->pos_y_std != other.pos_y_std) {
      return false;
    }
    if (this->pos_z_std != other.pos_z_std) {
      return false;
    }
    if (this->vel_x_std != other.vel_x_std) {
      return false;
    }
    if (this->vel_y_std != other.vel_y_std) {
      return false;
    }
    if (this->vel_z_std != other.vel_z_std) {
      return false;
    }
    if (this->roll_std != other.roll_std) {
      return false;
    }
    if (this->pitch_std != other.pitch_std) {
      return false;
    }
    if (this->yaw_std != other.yaw_std) {
      return false;
    }
    if (this->tow_ms != other.tow_ms) {
      return false;
    }
    return true;
  }
  bool operator!=(const Odom_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Odom_

// alias to use template instance with default allocator
using Odom =
  imu_msgs::msg::Odom_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__ODOM__STRUCT_HPP_
