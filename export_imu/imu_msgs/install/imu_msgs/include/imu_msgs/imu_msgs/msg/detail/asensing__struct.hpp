// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from imu_msgs:msg/ASENSING.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ASENSING__STRUCT_HPP_
#define IMU_MSGS__MSG__DETAIL__ASENSING__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__imu_msgs__msg__ASENSING __attribute__((deprecated))
#else
# define DEPRECATED__imu_msgs__msg__ASENSING __declspec(deprecated)
#endif

namespace imu_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ASENSING_
{
  using Type = ASENSING_<ContainerAllocator>;

  explicit ASENSING_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->latitude = 0.0;
      this->longitude = 0.0;
      this->altitude = 0.0;
      this->north_velocity = 0.0;
      this->east_velocity = 0.0;
      this->ground_velocity = 0.0;
      this->roll = 0.0;
      this->pitch = 0.0;
      this->azimuth = 0.0;
      this->x_angular_velocity = 0.0;
      this->y_angular_velocity = 0.0;
      this->z_angular_velocity = 0.0;
      this->x_acc = 0.0;
      this->y_acc = 0.0;
      this->z_acc = 0.0;
      this->latitude_std = 0.0f;
      this->longitude_std = 0.0f;
      this->altitude_std = 0.0f;
      this->north_velocity_std = 0.0f;
      this->east_velocity_std = 0.0f;
      this->ground_velocity_std = 0.0f;
      this->roll_std = 0.0f;
      this->pitch_std = 0.0f;
      this->azimuth_std = 0.0f;
      this->ins_status = 0ul;
      this->position_type = 0ul;
      this->sec_of_week = 0.0;
      this->gps_week_number = 0.0;
      this->temperature = 0.0f;
      this->wheel_speed_status = 0ul;
      this->heading_type = 0ul;
      this->numsv = 0ul;
      this->is_available = false;
      this->utm_x = 0.0;
      this->utm_y = 0.0;
    }
  }

  explicit ASENSING_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->latitude = 0.0;
      this->longitude = 0.0;
      this->altitude = 0.0;
      this->north_velocity = 0.0;
      this->east_velocity = 0.0;
      this->ground_velocity = 0.0;
      this->roll = 0.0;
      this->pitch = 0.0;
      this->azimuth = 0.0;
      this->x_angular_velocity = 0.0;
      this->y_angular_velocity = 0.0;
      this->z_angular_velocity = 0.0;
      this->x_acc = 0.0;
      this->y_acc = 0.0;
      this->z_acc = 0.0;
      this->latitude_std = 0.0f;
      this->longitude_std = 0.0f;
      this->altitude_std = 0.0f;
      this->north_velocity_std = 0.0f;
      this->east_velocity_std = 0.0f;
      this->ground_velocity_std = 0.0f;
      this->roll_std = 0.0f;
      this->pitch_std = 0.0f;
      this->azimuth_std = 0.0f;
      this->ins_status = 0ul;
      this->position_type = 0ul;
      this->sec_of_week = 0.0;
      this->gps_week_number = 0.0;
      this->temperature = 0.0f;
      this->wheel_speed_status = 0ul;
      this->heading_type = 0ul;
      this->numsv = 0ul;
      this->is_available = false;
      this->utm_x = 0.0;
      this->utm_y = 0.0;
    }
  }

  // field types and members
  using _latitude_type =
    double;
  _latitude_type latitude;
  using _longitude_type =
    double;
  _longitude_type longitude;
  using _altitude_type =
    double;
  _altitude_type altitude;
  using _north_velocity_type =
    double;
  _north_velocity_type north_velocity;
  using _east_velocity_type =
    double;
  _east_velocity_type east_velocity;
  using _ground_velocity_type =
    double;
  _ground_velocity_type ground_velocity;
  using _roll_type =
    double;
  _roll_type roll;
  using _pitch_type =
    double;
  _pitch_type pitch;
  using _azimuth_type =
    double;
  _azimuth_type azimuth;
  using _x_angular_velocity_type =
    double;
  _x_angular_velocity_type x_angular_velocity;
  using _y_angular_velocity_type =
    double;
  _y_angular_velocity_type y_angular_velocity;
  using _z_angular_velocity_type =
    double;
  _z_angular_velocity_type z_angular_velocity;
  using _x_acc_type =
    double;
  _x_acc_type x_acc;
  using _y_acc_type =
    double;
  _y_acc_type y_acc;
  using _z_acc_type =
    double;
  _z_acc_type z_acc;
  using _latitude_std_type =
    float;
  _latitude_std_type latitude_std;
  using _longitude_std_type =
    float;
  _longitude_std_type longitude_std;
  using _altitude_std_type =
    float;
  _altitude_std_type altitude_std;
  using _north_velocity_std_type =
    float;
  _north_velocity_std_type north_velocity_std;
  using _east_velocity_std_type =
    float;
  _east_velocity_std_type east_velocity_std;
  using _ground_velocity_std_type =
    float;
  _ground_velocity_std_type ground_velocity_std;
  using _roll_std_type =
    float;
  _roll_std_type roll_std;
  using _pitch_std_type =
    float;
  _pitch_std_type pitch_std;
  using _azimuth_std_type =
    float;
  _azimuth_std_type azimuth_std;
  using _ins_status_type =
    uint32_t;
  _ins_status_type ins_status;
  using _position_type_type =
    uint32_t;
  _position_type_type position_type;
  using _sec_of_week_type =
    double;
  _sec_of_week_type sec_of_week;
  using _gps_week_number_type =
    double;
  _gps_week_number_type gps_week_number;
  using _temperature_type =
    float;
  _temperature_type temperature;
  using _wheel_speed_status_type =
    uint32_t;
  _wheel_speed_status_type wheel_speed_status;
  using _heading_type_type =
    uint32_t;
  _heading_type_type heading_type;
  using _numsv_type =
    uint32_t;
  _numsv_type numsv;
  using _is_available_type =
    bool;
  _is_available_type is_available;
  using _utm_x_type =
    double;
  _utm_x_type utm_x;
  using _utm_y_type =
    double;
  _utm_y_type utm_y;

  // setters for named parameter idiom
  Type & set__latitude(
    const double & _arg)
  {
    this->latitude = _arg;
    return *this;
  }
  Type & set__longitude(
    const double & _arg)
  {
    this->longitude = _arg;
    return *this;
  }
  Type & set__altitude(
    const double & _arg)
  {
    this->altitude = _arg;
    return *this;
  }
  Type & set__north_velocity(
    const double & _arg)
  {
    this->north_velocity = _arg;
    return *this;
  }
  Type & set__east_velocity(
    const double & _arg)
  {
    this->east_velocity = _arg;
    return *this;
  }
  Type & set__ground_velocity(
    const double & _arg)
  {
    this->ground_velocity = _arg;
    return *this;
  }
  Type & set__roll(
    const double & _arg)
  {
    this->roll = _arg;
    return *this;
  }
  Type & set__pitch(
    const double & _arg)
  {
    this->pitch = _arg;
    return *this;
  }
  Type & set__azimuth(
    const double & _arg)
  {
    this->azimuth = _arg;
    return *this;
  }
  Type & set__x_angular_velocity(
    const double & _arg)
  {
    this->x_angular_velocity = _arg;
    return *this;
  }
  Type & set__y_angular_velocity(
    const double & _arg)
  {
    this->y_angular_velocity = _arg;
    return *this;
  }
  Type & set__z_angular_velocity(
    const double & _arg)
  {
    this->z_angular_velocity = _arg;
    return *this;
  }
  Type & set__x_acc(
    const double & _arg)
  {
    this->x_acc = _arg;
    return *this;
  }
  Type & set__y_acc(
    const double & _arg)
  {
    this->y_acc = _arg;
    return *this;
  }
  Type & set__z_acc(
    const double & _arg)
  {
    this->z_acc = _arg;
    return *this;
  }
  Type & set__latitude_std(
    const float & _arg)
  {
    this->latitude_std = _arg;
    return *this;
  }
  Type & set__longitude_std(
    const float & _arg)
  {
    this->longitude_std = _arg;
    return *this;
  }
  Type & set__altitude_std(
    const float & _arg)
  {
    this->altitude_std = _arg;
    return *this;
  }
  Type & set__north_velocity_std(
    const float & _arg)
  {
    this->north_velocity_std = _arg;
    return *this;
  }
  Type & set__east_velocity_std(
    const float & _arg)
  {
    this->east_velocity_std = _arg;
    return *this;
  }
  Type & set__ground_velocity_std(
    const float & _arg)
  {
    this->ground_velocity_std = _arg;
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
  Type & set__azimuth_std(
    const float & _arg)
  {
    this->azimuth_std = _arg;
    return *this;
  }
  Type & set__ins_status(
    const uint32_t & _arg)
  {
    this->ins_status = _arg;
    return *this;
  }
  Type & set__position_type(
    const uint32_t & _arg)
  {
    this->position_type = _arg;
    return *this;
  }
  Type & set__sec_of_week(
    const double & _arg)
  {
    this->sec_of_week = _arg;
    return *this;
  }
  Type & set__gps_week_number(
    const double & _arg)
  {
    this->gps_week_number = _arg;
    return *this;
  }
  Type & set__temperature(
    const float & _arg)
  {
    this->temperature = _arg;
    return *this;
  }
  Type & set__wheel_speed_status(
    const uint32_t & _arg)
  {
    this->wheel_speed_status = _arg;
    return *this;
  }
  Type & set__heading_type(
    const uint32_t & _arg)
  {
    this->heading_type = _arg;
    return *this;
  }
  Type & set__numsv(
    const uint32_t & _arg)
  {
    this->numsv = _arg;
    return *this;
  }
  Type & set__is_available(
    const bool & _arg)
  {
    this->is_available = _arg;
    return *this;
  }
  Type & set__utm_x(
    const double & _arg)
  {
    this->utm_x = _arg;
    return *this;
  }
  Type & set__utm_y(
    const double & _arg)
  {
    this->utm_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    imu_msgs::msg::ASENSING_<ContainerAllocator> *;
  using ConstRawPtr =
    const imu_msgs::msg::ASENSING_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<imu_msgs::msg::ASENSING_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<imu_msgs::msg::ASENSING_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::ASENSING_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::ASENSING_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      imu_msgs::msg::ASENSING_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<imu_msgs::msg::ASENSING_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<imu_msgs::msg::ASENSING_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<imu_msgs::msg::ASENSING_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__imu_msgs__msg__ASENSING
    std::shared_ptr<imu_msgs::msg::ASENSING_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__imu_msgs__msg__ASENSING
    std::shared_ptr<imu_msgs::msg::ASENSING_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ASENSING_ & other) const
  {
    if (this->latitude != other.latitude) {
      return false;
    }
    if (this->longitude != other.longitude) {
      return false;
    }
    if (this->altitude != other.altitude) {
      return false;
    }
    if (this->north_velocity != other.north_velocity) {
      return false;
    }
    if (this->east_velocity != other.east_velocity) {
      return false;
    }
    if (this->ground_velocity != other.ground_velocity) {
      return false;
    }
    if (this->roll != other.roll) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    if (this->azimuth != other.azimuth) {
      return false;
    }
    if (this->x_angular_velocity != other.x_angular_velocity) {
      return false;
    }
    if (this->y_angular_velocity != other.y_angular_velocity) {
      return false;
    }
    if (this->z_angular_velocity != other.z_angular_velocity) {
      return false;
    }
    if (this->x_acc != other.x_acc) {
      return false;
    }
    if (this->y_acc != other.y_acc) {
      return false;
    }
    if (this->z_acc != other.z_acc) {
      return false;
    }
    if (this->latitude_std != other.latitude_std) {
      return false;
    }
    if (this->longitude_std != other.longitude_std) {
      return false;
    }
    if (this->altitude_std != other.altitude_std) {
      return false;
    }
    if (this->north_velocity_std != other.north_velocity_std) {
      return false;
    }
    if (this->east_velocity_std != other.east_velocity_std) {
      return false;
    }
    if (this->ground_velocity_std != other.ground_velocity_std) {
      return false;
    }
    if (this->roll_std != other.roll_std) {
      return false;
    }
    if (this->pitch_std != other.pitch_std) {
      return false;
    }
    if (this->azimuth_std != other.azimuth_std) {
      return false;
    }
    if (this->ins_status != other.ins_status) {
      return false;
    }
    if (this->position_type != other.position_type) {
      return false;
    }
    if (this->sec_of_week != other.sec_of_week) {
      return false;
    }
    if (this->gps_week_number != other.gps_week_number) {
      return false;
    }
    if (this->temperature != other.temperature) {
      return false;
    }
    if (this->wheel_speed_status != other.wheel_speed_status) {
      return false;
    }
    if (this->heading_type != other.heading_type) {
      return false;
    }
    if (this->numsv != other.numsv) {
      return false;
    }
    if (this->is_available != other.is_available) {
      return false;
    }
    if (this->utm_x != other.utm_x) {
      return false;
    }
    if (this->utm_y != other.utm_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const ASENSING_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ASENSING_

// alias to use template instance with default allocator
using ASENSING =
  imu_msgs::msg::ASENSING_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace imu_msgs

#endif  // IMU_MSGS__MSG__DETAIL__ASENSING__STRUCT_HPP_
