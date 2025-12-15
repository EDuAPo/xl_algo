// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from imu_msgs:msg/Gnss.idl
// generated code does not contain a copyright notice
#include "imu_msgs/msg/detail/gnss__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "imu_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "imu_msgs/msg/detail/gnss__struct.h"
#include "imu_msgs/msg/detail/gnss__functions.h"
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

#include "rosidl_runtime_c/string.h"  // utc_time
#include "rosidl_runtime_c/string_functions.h"  // utc_time
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


using _Gnss__ros_msg_type = imu_msgs__msg__Gnss;

static bool _Gnss__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Gnss__ros_msg_type * ros_message = static_cast<const _Gnss__ros_msg_type *>(untyped_ros_message);
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

  // Field name: longitude
  {
    cdr << ros_message->longitude;
  }

  // Field name: lon_sigma
  {
    cdr << ros_message->lon_sigma;
  }

  // Field name: latitude
  {
    cdr << ros_message->latitude;
  }

  // Field name: lat_sigma
  {
    cdr << ros_message->lat_sigma;
  }

  // Field name: altitude
  {
    cdr << ros_message->altitude;
  }

  // Field name: alt_sigma
  {
    cdr << ros_message->alt_sigma;
  }

  // Field name: gps_fix
  {
    cdr << ros_message->gps_fix;
  }

  // Field name: rtk_age
  {
    cdr << ros_message->rtk_age;
  }

  // Field name: flags_pos
  {
    cdr << ros_message->flags_pos;
  }

  // Field name: flags_vel
  {
    cdr << ros_message->flags_vel;
  }

  // Field name: flags_attitude
  {
    cdr << ros_message->flags_attitude;
  }

  // Field name: flags_time
  {
    cdr << ros_message->flags_time;
  }

  // Field name: hor_vel
  {
    cdr << ros_message->hor_vel;
  }

  // Field name: track_angle
  {
    cdr << ros_message->track_angle;
  }

  // Field name: ver_vel
  {
    cdr << ros_message->ver_vel;
  }

  // Field name: latency_vel
  {
    cdr << ros_message->latency_vel;
  }

  // Field name: base_length
  {
    cdr << ros_message->base_length;
  }

  // Field name: yaw
  {
    cdr << ros_message->yaw;
  }

  // Field name: yaw_sigma
  {
    cdr << ros_message->yaw_sigma;
  }

  // Field name: pitch
  {
    cdr << ros_message->pitch;
  }

  // Field name: pitch_sigma
  {
    cdr << ros_message->pitch_sigma;
  }

  // Field name: utc_time
  {
    const rosidl_runtime_c__String * str = &ros_message->utc_time;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: ts_pos
  {
    cdr << ros_message->ts_pos;
  }

  // Field name: ts_vel
  {
    cdr << ros_message->ts_vel;
  }

  // Field name: ts_heading
  {
    cdr << ros_message->ts_heading;
  }

  // Field name: state
  {
    cdr << ros_message->state;
  }

  // Field name: num_master
  {
    cdr << ros_message->num_master;
  }

  // Field name: gdop
  {
    cdr << ros_message->gdop;
  }

  // Field name: pdop
  {
    cdr << ros_message->pdop;
  }

  // Field name: hdop
  {
    cdr << ros_message->hdop;
  }

  // Field name: htdop
  {
    cdr << ros_message->htdop;
  }

  // Field name: tdop
  {
    cdr << ros_message->tdop;
  }

  // Field name: num_reserve
  {
    cdr << ros_message->num_reserve;
  }

  return true;
}

static bool _Gnss__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Gnss__ros_msg_type * ros_message = static_cast<_Gnss__ros_msg_type *>(untyped_ros_message);
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

  // Field name: longitude
  {
    cdr >> ros_message->longitude;
  }

  // Field name: lon_sigma
  {
    cdr >> ros_message->lon_sigma;
  }

  // Field name: latitude
  {
    cdr >> ros_message->latitude;
  }

  // Field name: lat_sigma
  {
    cdr >> ros_message->lat_sigma;
  }

  // Field name: altitude
  {
    cdr >> ros_message->altitude;
  }

  // Field name: alt_sigma
  {
    cdr >> ros_message->alt_sigma;
  }

  // Field name: gps_fix
  {
    cdr >> ros_message->gps_fix;
  }

  // Field name: rtk_age
  {
    cdr >> ros_message->rtk_age;
  }

  // Field name: flags_pos
  {
    cdr >> ros_message->flags_pos;
  }

  // Field name: flags_vel
  {
    cdr >> ros_message->flags_vel;
  }

  // Field name: flags_attitude
  {
    cdr >> ros_message->flags_attitude;
  }

  // Field name: flags_time
  {
    cdr >> ros_message->flags_time;
  }

  // Field name: hor_vel
  {
    cdr >> ros_message->hor_vel;
  }

  // Field name: track_angle
  {
    cdr >> ros_message->track_angle;
  }

  // Field name: ver_vel
  {
    cdr >> ros_message->ver_vel;
  }

  // Field name: latency_vel
  {
    cdr >> ros_message->latency_vel;
  }

  // Field name: base_length
  {
    cdr >> ros_message->base_length;
  }

  // Field name: yaw
  {
    cdr >> ros_message->yaw;
  }

  // Field name: yaw_sigma
  {
    cdr >> ros_message->yaw_sigma;
  }

  // Field name: pitch
  {
    cdr >> ros_message->pitch;
  }

  // Field name: pitch_sigma
  {
    cdr >> ros_message->pitch_sigma;
  }

  // Field name: utc_time
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->utc_time.data) {
      rosidl_runtime_c__String__init(&ros_message->utc_time);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->utc_time,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'utc_time'\n");
      return false;
    }
  }

  // Field name: ts_pos
  {
    cdr >> ros_message->ts_pos;
  }

  // Field name: ts_vel
  {
    cdr >> ros_message->ts_vel;
  }

  // Field name: ts_heading
  {
    cdr >> ros_message->ts_heading;
  }

  // Field name: state
  {
    cdr >> ros_message->state;
  }

  // Field name: num_master
  {
    cdr >> ros_message->num_master;
  }

  // Field name: gdop
  {
    cdr >> ros_message->gdop;
  }

  // Field name: pdop
  {
    cdr >> ros_message->pdop;
  }

  // Field name: hdop
  {
    cdr >> ros_message->hdop;
  }

  // Field name: htdop
  {
    cdr >> ros_message->htdop;
  }

  // Field name: tdop
  {
    cdr >> ros_message->tdop;
  }

  // Field name: num_reserve
  {
    cdr >> ros_message->num_reserve;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_imu_msgs
size_t get_serialized_size_imu_msgs__msg__Gnss(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Gnss__ros_msg_type * ros_message = static_cast<const _Gnss__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name longitude
  {
    size_t item_size = sizeof(ros_message->longitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name lon_sigma
  {
    size_t item_size = sizeof(ros_message->lon_sigma);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name latitude
  {
    size_t item_size = sizeof(ros_message->latitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name lat_sigma
  {
    size_t item_size = sizeof(ros_message->lat_sigma);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name altitude
  {
    size_t item_size = sizeof(ros_message->altitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name alt_sigma
  {
    size_t item_size = sizeof(ros_message->alt_sigma);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name gps_fix
  {
    size_t item_size = sizeof(ros_message->gps_fix);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rtk_age
  {
    size_t item_size = sizeof(ros_message->rtk_age);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flags_pos
  {
    size_t item_size = sizeof(ros_message->flags_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flags_vel
  {
    size_t item_size = sizeof(ros_message->flags_vel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flags_attitude
  {
    size_t item_size = sizeof(ros_message->flags_attitude);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flags_time
  {
    size_t item_size = sizeof(ros_message->flags_time);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name hor_vel
  {
    size_t item_size = sizeof(ros_message->hor_vel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name track_angle
  {
    size_t item_size = sizeof(ros_message->track_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ver_vel
  {
    size_t item_size = sizeof(ros_message->ver_vel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name latency_vel
  {
    size_t item_size = sizeof(ros_message->latency_vel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name base_length
  {
    size_t item_size = sizeof(ros_message->base_length);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yaw
  {
    size_t item_size = sizeof(ros_message->yaw);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yaw_sigma
  {
    size_t item_size = sizeof(ros_message->yaw_sigma);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pitch
  {
    size_t item_size = sizeof(ros_message->pitch);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pitch_sigma
  {
    size_t item_size = sizeof(ros_message->pitch_sigma);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name utc_time
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->utc_time.size + 1);
  // field.name ts_pos
  {
    size_t item_size = sizeof(ros_message->ts_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ts_vel
  {
    size_t item_size = sizeof(ros_message->ts_vel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ts_heading
  {
    size_t item_size = sizeof(ros_message->ts_heading);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name state
  {
    size_t item_size = sizeof(ros_message->state);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name num_master
  {
    size_t item_size = sizeof(ros_message->num_master);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name gdop
  {
    size_t item_size = sizeof(ros_message->gdop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pdop
  {
    size_t item_size = sizeof(ros_message->pdop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name hdop
  {
    size_t item_size = sizeof(ros_message->hdop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name htdop
  {
    size_t item_size = sizeof(ros_message->htdop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tdop
  {
    size_t item_size = sizeof(ros_message->tdop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name num_reserve
  {
    size_t item_size = sizeof(ros_message->num_reserve);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Gnss__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_imu_msgs__msg__Gnss(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_imu_msgs
size_t max_serialized_size_imu_msgs__msg__Gnss(
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
  // member: longitude
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: lon_sigma
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: latitude
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: lat_sigma
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: altitude
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: alt_sigma
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: gps_fix
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: rtk_age
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint16_t);
    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: flags_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: flags_vel
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: flags_attitude
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: flags_time
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: hor_vel
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: track_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ver_vel
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: latency_vel
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: base_length
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: yaw
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: yaw_sigma
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pitch
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pitch_sigma
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: utc_time
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: ts_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ts_vel
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ts_heading
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: state
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: num_master
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: gdop
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pdop
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: hdop
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: htdop
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: tdop
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: num_reserve
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = imu_msgs__msg__Gnss;
    is_plain =
      (
      offsetof(DataType, num_reserve) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _Gnss__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_imu_msgs__msg__Gnss(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Gnss = {
  "imu_msgs::msg",
  "Gnss",
  _Gnss__cdr_serialize,
  _Gnss__cdr_deserialize,
  _Gnss__get_serialized_size,
  _Gnss__max_serialized_size
};

static rosidl_message_type_support_t _Gnss__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Gnss,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, imu_msgs, msg, Gnss)() {
  return &_Gnss__type_support;
}

#if defined(__cplusplus)
}
#endif
