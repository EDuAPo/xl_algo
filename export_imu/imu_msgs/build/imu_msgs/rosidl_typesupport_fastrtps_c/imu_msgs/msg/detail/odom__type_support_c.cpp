// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from imu_msgs:msg/Odom.idl
// generated code does not contain a copyright notice
#include "imu_msgs/msg/detail/odom__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "imu_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "imu_msgs/msg/detail/odom__struct.h"
#include "imu_msgs/msg/detail/odom__functions.h"
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

#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_imu_msgs
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_imu_msgs
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_imu_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _Odom__ros_msg_type = imu_msgs__msg__Odom;

static bool _Odom__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Odom__ros_msg_type * ros_message = static_cast<const _Odom__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->header, cdr))
    {
      return false;
    }
  }

  // Field name: q0_w
  {
    cdr << ros_message->q0_w;
  }

  // Field name: q1_x
  {
    cdr << ros_message->q1_x;
  }

  // Field name: q2_y
  {
    cdr << ros_message->q2_y;
  }

  // Field name: q3_z
  {
    cdr << ros_message->q3_z;
  }

  // Field name: pos_x
  {
    cdr << ros_message->pos_x;
  }

  // Field name: pos_y
  {
    cdr << ros_message->pos_y;
  }

  // Field name: pos_z
  {
    cdr << ros_message->pos_z;
  }

  // Field name: vel_x
  {
    cdr << ros_message->vel_x;
  }

  // Field name: vel_y
  {
    cdr << ros_message->vel_y;
  }

  // Field name: vel_z
  {
    cdr << ros_message->vel_z;
  }

  // Field name: vel
  {
    cdr << ros_message->vel;
  }

  // Field name: ang_vel_x
  {
    cdr << ros_message->ang_vel_x;
  }

  // Field name: ang_vel_y
  {
    cdr << ros_message->ang_vel_y;
  }

  // Field name: ang_vel_z
  {
    cdr << ros_message->ang_vel_z;
  }

  // Field name: acc_x
  {
    cdr << ros_message->acc_x;
  }

  // Field name: acc_y
  {
    cdr << ros_message->acc_y;
  }

  // Field name: acc_z
  {
    cdr << ros_message->acc_z;
  }

  // Field name: status
  {
    cdr << ros_message->status;
  }

  // Field name: sensor_status
  {
    cdr << ros_message->sensor_status;
  }

  // Field name: pos_x_std
  {
    cdr << ros_message->pos_x_std;
  }

  // Field name: pos_y_std
  {
    cdr << ros_message->pos_y_std;
  }

  // Field name: pos_z_std
  {
    cdr << ros_message->pos_z_std;
  }

  // Field name: vel_x_std
  {
    cdr << ros_message->vel_x_std;
  }

  // Field name: vel_y_std
  {
    cdr << ros_message->vel_y_std;
  }

  // Field name: vel_z_std
  {
    cdr << ros_message->vel_z_std;
  }

  // Field name: roll_std
  {
    cdr << ros_message->roll_std;
  }

  // Field name: pitch_std
  {
    cdr << ros_message->pitch_std;
  }

  // Field name: yaw_std
  {
    cdr << ros_message->yaw_std;
  }

  // Field name: tow_ms
  {
    cdr << ros_message->tow_ms;
  }

  return true;
}

static bool _Odom__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Odom__ros_msg_type * ros_message = static_cast<_Odom__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->header))
    {
      return false;
    }
  }

  // Field name: q0_w
  {
    cdr >> ros_message->q0_w;
  }

  // Field name: q1_x
  {
    cdr >> ros_message->q1_x;
  }

  // Field name: q2_y
  {
    cdr >> ros_message->q2_y;
  }

  // Field name: q3_z
  {
    cdr >> ros_message->q3_z;
  }

  // Field name: pos_x
  {
    cdr >> ros_message->pos_x;
  }

  // Field name: pos_y
  {
    cdr >> ros_message->pos_y;
  }

  // Field name: pos_z
  {
    cdr >> ros_message->pos_z;
  }

  // Field name: vel_x
  {
    cdr >> ros_message->vel_x;
  }

  // Field name: vel_y
  {
    cdr >> ros_message->vel_y;
  }

  // Field name: vel_z
  {
    cdr >> ros_message->vel_z;
  }

  // Field name: vel
  {
    cdr >> ros_message->vel;
  }

  // Field name: ang_vel_x
  {
    cdr >> ros_message->ang_vel_x;
  }

  // Field name: ang_vel_y
  {
    cdr >> ros_message->ang_vel_y;
  }

  // Field name: ang_vel_z
  {
    cdr >> ros_message->ang_vel_z;
  }

  // Field name: acc_x
  {
    cdr >> ros_message->acc_x;
  }

  // Field name: acc_y
  {
    cdr >> ros_message->acc_y;
  }

  // Field name: acc_z
  {
    cdr >> ros_message->acc_z;
  }

  // Field name: status
  {
    cdr >> ros_message->status;
  }

  // Field name: sensor_status
  {
    cdr >> ros_message->sensor_status;
  }

  // Field name: pos_x_std
  {
    cdr >> ros_message->pos_x_std;
  }

  // Field name: pos_y_std
  {
    cdr >> ros_message->pos_y_std;
  }

  // Field name: pos_z_std
  {
    cdr >> ros_message->pos_z_std;
  }

  // Field name: vel_x_std
  {
    cdr >> ros_message->vel_x_std;
  }

  // Field name: vel_y_std
  {
    cdr >> ros_message->vel_y_std;
  }

  // Field name: vel_z_std
  {
    cdr >> ros_message->vel_z_std;
  }

  // Field name: roll_std
  {
    cdr >> ros_message->roll_std;
  }

  // Field name: pitch_std
  {
    cdr >> ros_message->pitch_std;
  }

  // Field name: yaw_std
  {
    cdr >> ros_message->yaw_std;
  }

  // Field name: tow_ms
  {
    cdr >> ros_message->tow_ms;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_imu_msgs
size_t get_serialized_size_imu_msgs__msg__Odom(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Odom__ros_msg_type * ros_message = static_cast<const _Odom__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name q0_w
  {
    size_t item_size = sizeof(ros_message->q0_w);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name q1_x
  {
    size_t item_size = sizeof(ros_message->q1_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name q2_y
  {
    size_t item_size = sizeof(ros_message->q2_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name q3_z
  {
    size_t item_size = sizeof(ros_message->q3_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pos_x
  {
    size_t item_size = sizeof(ros_message->pos_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pos_y
  {
    size_t item_size = sizeof(ros_message->pos_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pos_z
  {
    size_t item_size = sizeof(ros_message->pos_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vel_x
  {
    size_t item_size = sizeof(ros_message->vel_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vel_y
  {
    size_t item_size = sizeof(ros_message->vel_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vel_z
  {
    size_t item_size = sizeof(ros_message->vel_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vel
  {
    size_t item_size = sizeof(ros_message->vel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ang_vel_x
  {
    size_t item_size = sizeof(ros_message->ang_vel_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ang_vel_y
  {
    size_t item_size = sizeof(ros_message->ang_vel_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ang_vel_z
  {
    size_t item_size = sizeof(ros_message->ang_vel_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name acc_x
  {
    size_t item_size = sizeof(ros_message->acc_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name acc_y
  {
    size_t item_size = sizeof(ros_message->acc_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name acc_z
  {
    size_t item_size = sizeof(ros_message->acc_z);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name status
  {
    size_t item_size = sizeof(ros_message->status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name sensor_status
  {
    size_t item_size = sizeof(ros_message->sensor_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pos_x_std
  {
    size_t item_size = sizeof(ros_message->pos_x_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pos_y_std
  {
    size_t item_size = sizeof(ros_message->pos_y_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pos_z_std
  {
    size_t item_size = sizeof(ros_message->pos_z_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vel_x_std
  {
    size_t item_size = sizeof(ros_message->vel_x_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vel_y_std
  {
    size_t item_size = sizeof(ros_message->vel_y_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vel_z_std
  {
    size_t item_size = sizeof(ros_message->vel_z_std);
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
  // field.name yaw_std
  {
    size_t item_size = sizeof(ros_message->yaw_std);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tow_ms
  {
    size_t item_size = sizeof(ros_message->tow_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Odom__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_imu_msgs__msg__Odom(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_imu_msgs
size_t max_serialized_size_imu_msgs__msg__Odom(
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

  // member: header
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_std_msgs__msg__Header(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: q0_w
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: q1_x
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: q2_y
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: q3_z
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pos_x
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pos_y
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pos_z
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vel_x
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vel_y
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vel_z
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vel
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ang_vel_x
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ang_vel_y
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ang_vel_z
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: acc_x
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: acc_y
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: acc_z
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: status
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: sensor_status
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pos_x_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pos_y_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pos_z_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vel_x_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vel_y_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vel_z_std
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
  // member: yaw_std
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: tow_ms
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = imu_msgs__msg__Odom;
    is_plain =
      (
      offsetof(DataType, tow_ms) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _Odom__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_imu_msgs__msg__Odom(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Odom = {
  "imu_msgs::msg",
  "Odom",
  _Odom__cdr_serialize,
  _Odom__cdr_deserialize,
  _Odom__get_serialized_size,
  _Odom__max_serialized_size
};

static rosidl_message_type_support_t _Odom__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Odom,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, imu_msgs, msg, Odom)() {
  return &_Odom__type_support;
}

#if defined(__cplusplus)
}
#endif
