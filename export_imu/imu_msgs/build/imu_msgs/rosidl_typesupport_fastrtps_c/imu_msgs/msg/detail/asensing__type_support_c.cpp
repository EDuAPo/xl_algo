// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from imu_msgs:msg/ASENSING.idl
// generated code does not contain a copyright notice
#include "imu_msgs/msg/detail/asensing__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "imu_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "imu_msgs/msg/detail/asensing__struct.h"
#include "imu_msgs/msg/detail/asensing__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _ASENSING__ros_msg_type = imu_msgs__msg__ASENSING;

static bool _ASENSING__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ASENSING__ros_msg_type * ros_message = static_cast<const _ASENSING__ros_msg_type *>(untyped_ros_message);
  // Field name: latitude
  {
    cdr << ros_message->latitude;
  }

  // Field name: longitude
  {
    cdr << ros_message->longitude;
  }

  // Field name: altitude
  {
    cdr << ros_message->altitude;
  }

  // Field name: north_velocity
  {
    cdr << ros_message->north_velocity;
  }

  // Field name: east_velocity
  {
    cdr << ros_message->east_velocity;
  }

  // Field name: ground_velocity
  {
    cdr << ros_message->ground_velocity;
  }

  // Field name: roll
  {
    cdr << ros_message->roll;
  }

  // Field name: pitch
  {
    cdr << ros_message->pitch;
  }

  // Field name: azimuth
  {
    cdr << ros_message->azimuth;
  }

  // Field name: x_angular_velocity
  {
    cdr << ros_message->x_angular_velocity;
  }

  // Field name: y_angular_velocity
  {
    cdr << ros_message->y_angular_velocity;
  }

  // Field name: z_angular_velocity
  {
    cdr << ros_message->z_angular_velocity;
  }

  // Field name: x_acc
  {
    cdr << ros_message->x_acc;
  }

  // Field name: y_acc
  {
    cdr << ros_message->y_acc;
  }

  // Field name: z_acc
  {
    cdr << ros_message->z_acc;
  }

  // Field name: latitude_std
  {
    cdr << ros_message->latitude_std;
  }

  // Field name: longitude_std
  {
    cdr << ros_message->longitude_std;
  }

  // Field name: altitude_std
  {
    cdr << ros_message->altitude_std;
  }

  // Field name: north_velocity_std
  {
    cdr << ros_message->north_velocity_std;
  }

  // Field name: east_velocity_std
  {
    cdr << ros_message->east_velocity_std;
  }

  // Field name: ground_velocity_std
  {
    cdr << ros_message->ground_velocity_std;
  }

  // Field name: roll_std
  {
    cdr << ros_message->roll_std;
  }

  // Field name: pitch_std
  {
    cdr << ros_message->pitch_std;
  }

  // Field name: azimuth_std
  {
    cdr << ros_message->azimuth_std;
  }

  // Field name: ins_status
  {
    cdr << ros_message->ins_status;
  }

  // Field name: position_type
  {
    cdr << ros_message->position_type;
  }

  // Field name: sec_of_week
  {
    cdr << ros_message->sec_of_week;
  }

  // Field name: gps_week_number
  {
    cdr << ros_message->gps_week_number;
  }

  // Field name: temperature
  {
    cdr << ros_message->temperature;
  }

  // Field name: wheel_speed_status
  {
    cdr << ros_message->wheel_speed_status;
  }

  // Field name: heading_type
  {
    cdr << ros_message->heading_type;
  }

  // Field name: numsv
  {
    cdr << ros_message->numsv;
  }

  // Field name: is_available
  {
    cdr << (ros_message->is_available ? true : false);
  }

  // Field name: utm_x
  {
    cdr << ros_message->utm_x;
  }

  // Field name: utm_y
  {
    cdr << ros_message->utm_y;
  }

  return true;
}

static bool _ASENSING__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ASENSING__ros_msg_type * ros_message = static_cast<_ASENSING__ros_msg_type *>(untyped_ros_message);
  // Field name: latitude
  {
    cdr >> ros_message->latitude;
  }

  // Field name: longitude
  {
    cdr >> ros_message->longitude;
  }

  // Field name: altitude
  {
    cdr >> ros_message->altitude;
  }

  // Field name: north_velocity
  {
    cdr >> ros_message->north_velocity;
  }

  // Field name: east_velocity
  {
    cdr >> ros_message->east_velocity;
  }

  // Field name: ground_velocity
  {
    cdr >> ros_message->ground_velocity;
  }

  // Field name: roll
  {
    cdr >> ros_message->roll;
  }

  // Field name: pitch
  {
    cdr >> ros_message->pitch;
  }

  // Field name: azimuth
  {
    cdr >> ros_message->azimuth;
  }

  // Field name: x_angular_velocity
  {
    cdr >> ros_message->x_angular_velocity;
  }

  // Field name: y_angular_velocity
  {
    cdr >> ros_message->y_angular_velocity;
  }

  // Field name: z_angular_velocity
  {
    cdr >> ros_message->z_angular_velocity;
  }

  // Field name: x_acc
  {
    cdr >> ros_message->x_acc;
  }

  // Field name: y_acc
  {
    cdr >> ros_message->y_acc;
  }

  // Field name: z_acc
  {
    cdr >> ros_message->z_acc;
  }

  // Field name: latitude_std
  {
    cdr >> ros_message->latitude_std;
  }

  // Field name: longitude_std
  {
    cdr >> ros_message->longitude_std;
  }

  // Field name: altitude_std
  {
    cdr >> ros_message->altitude_std;
  }

  // Field name: north_velocity_std
  {
    cdr >> ros_message->north_velocity_std;
  }

  // Field name: east_velocity_std
  {
    cdr >> ros_message->east_velocity_std;
  }

  // Field name: ground_velocity_std
  {
    cdr >> ros_message->ground_velocity_std;
  }

  // Field name: roll_std
  {
    cdr >> ros_message->roll_std;
  }

  // Field name: pitch_std
  {
    cdr >> ros_message->pitch_std;
  }

  // Field name: azimuth_std
  {
    cdr >> ros_message->azimuth_std;
  }

  // Field name: ins_status
  {
    cdr >> ros_message->ins_status;
  }

  // Field name: position_type
  {
    cdr >> ros_message->position_type;
  }

  // Field name: sec_of_week
  {
    cdr >> ros_message->sec_of_week;
  }

  // Field name: gps_week_number
  {
    cdr >> ros_message->gps_week_number;
  }

  // Field name: temperature
  {
    cdr >> ros_message->temperature;
  }

  // Field name: wheel_speed_status
  {
    cdr >> ros_message->wheel_speed_status;
  }

  // Field name: heading_type
  {
    cdr >> ros_message->heading_type;
  }

  // Field name: numsv
  {
    cdr >> ros_message->numsv;
  }

  // Field name: is_available
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->is_available = tmp ? true : false;
  }

  // Field name: utm_x
  {
    cdr >> ros_message->utm_x;
  }

  // Field name: utm_y
  {
    cdr >> ros_message->utm_y;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_imu_msgs
size_t get_serialized_size_imu_msgs__msg__ASENSING(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ASENSING__ros_msg_type * ros_message = static_cast<const _ASENSING__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name latitude
  {
    size_t item_size = sizeof(ros_message->latitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name longitude
  {
    size_t item_size = sizeof(ros_message->longitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name altitude
  {
    size_t item_size = sizeof(ros_message->altitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name north_velocity
  {
    size_t item_size = sizeof(ros_message->north_velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name east_velocity
  {
    size_t item_size = sizeof(ros_message->east_velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ground_velocity
  {
    size_t item_size = sizeof(ros_message->ground_velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name roll
  {
    size_t item_size = sizeof(ros_message->roll);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pitch
  {
    size_t item_size = sizeof(ros_message->pitch);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name azimuth
  {
    size_t item_size = sizeof(ros_message->azimuth);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name x_angular_velocity
  {
    size_t item_size = sizeof(ros_message->x_angular_velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name y_angular_velocity
  {
    size_t item_size = sizeof(ros_message->y_angular_velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name z_angular_velocity
  {
    size_t item_size = sizeof(ros_message->z_angular_velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name x_acc
  {
    size_t item_size = sizeof(ros_message->x_acc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name y_acc
  {
    size_t item_size = sizeof(ros_message->y_acc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name z_acc
  {
    size_t item_size = sizeof(ros_message->z_acc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name latitude_std
  {
    size_t item_size = sizeof(ros_message->latitude_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name longitude_std
  {
    size_t item_size = sizeof(ros_message->longitude_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name altitude_std
  {
    size_t item_size = sizeof(ros_message->altitude_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name north_velocity_std
  {
    size_t item_size = sizeof(ros_message->north_velocity_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name east_velocity_std
  {
    size_t item_size = sizeof(ros_message->east_velocity_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ground_velocity_std
  {
    size_t item_size = sizeof(ros_message->ground_velocity_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name roll_std
  {
    size_t item_size = sizeof(ros_message->roll_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pitch_std
  {
    size_t item_size = sizeof(ros_message->pitch_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name azimuth_std
  {
    size_t item_size = sizeof(ros_message->azimuth_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ins_status
  {
    size_t item_size = sizeof(ros_message->ins_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position_type
  {
    size_t item_size = sizeof(ros_message->position_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name sec_of_week
  {
    size_t item_size = sizeof(ros_message->sec_of_week);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name gps_week_number
  {
    size_t item_size = sizeof(ros_message->gps_week_number);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name temperature
  {
    size_t item_size = sizeof(ros_message->temperature);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name wheel_speed_status
  {
    size_t item_size = sizeof(ros_message->wheel_speed_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name heading_type
  {
    size_t item_size = sizeof(ros_message->heading_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name numsv
  {
    size_t item_size = sizeof(ros_message->numsv);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name is_available
  {
    size_t item_size = sizeof(ros_message->is_available);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name utm_x
  {
    size_t item_size = sizeof(ros_message->utm_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name utm_y
  {
    size_t item_size = sizeof(ros_message->utm_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _ASENSING__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_imu_msgs__msg__ASENSING(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_imu_msgs
size_t max_serialized_size_imu_msgs__msg__ASENSING(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: latitude
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: longitude
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: altitude
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: north_velocity
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: east_velocity
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ground_velocity
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: roll
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: pitch
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: azimuth
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: x_angular_velocity
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: y_angular_velocity
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: z_angular_velocity
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: x_acc
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: y_acc
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: z_acc
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: latitude_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: longitude_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: altitude_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: north_velocity_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: east_velocity_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ground_velocity_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: roll_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pitch_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: azimuth_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ins_status
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: position_type
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: sec_of_week
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: gps_week_number
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: temperature
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: wheel_speed_status
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: heading_type
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: numsv
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: is_available
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: utm_x
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: utm_y
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = imu_msgs__msg__ASENSING;
    is_plain =
      (
      offsetof(DataType, utm_y) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _ASENSING__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_imu_msgs__msg__ASENSING(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_ASENSING = {
  "imu_msgs::msg",
  "ASENSING",
  _ASENSING__cdr_serialize,
  _ASENSING__cdr_deserialize,
  _ASENSING__get_serialized_size,
  _ASENSING__max_serialized_size
};

static rosidl_message_type_support_t _ASENSING__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ASENSING,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, imu_msgs, msg, ASENSING)() {
  return &_ASENSING__type_support;
}

#if defined(__cplusplus)
}
#endif
