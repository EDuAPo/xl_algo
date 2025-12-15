// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from imu_msgs:msg/Gnss.idl
// generated code does not contain a copyright notice
#include "imu_msgs/msg/detail/gnss__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `utc_time`
#include "rosidl_runtime_c/string_functions.h"

bool
imu_msgs__msg__Gnss__init(imu_msgs__msg__Gnss * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    imu_msgs__msg__Gnss__fini(msg);
    return false;
  }
  // longitude
  // lon_sigma
  // latitude
  // lat_sigma
  // altitude
  // alt_sigma
  // gps_fix
  // rtk_age
  // flags_pos
  // flags_vel
  // flags_attitude
  // flags_time
  // hor_vel
  // track_angle
  // ver_vel
  // latency_vel
  // base_length
  // yaw
  // yaw_sigma
  // pitch
  // pitch_sigma
  // utc_time
  if (!rosidl_runtime_c__String__init(&msg->utc_time)) {
    imu_msgs__msg__Gnss__fini(msg);
    return false;
  }
  // ts_pos
  // ts_vel
  // ts_heading
  // state
  // num_master
  // gdop
  // pdop
  // hdop
  // htdop
  // tdop
  // num_reserve
  return true;
}

void
imu_msgs__msg__Gnss__fini(imu_msgs__msg__Gnss * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // longitude
  // lon_sigma
  // latitude
  // lat_sigma
  // altitude
  // alt_sigma
  // gps_fix
  // rtk_age
  // flags_pos
  // flags_vel
  // flags_attitude
  // flags_time
  // hor_vel
  // track_angle
  // ver_vel
  // latency_vel
  // base_length
  // yaw
  // yaw_sigma
  // pitch
  // pitch_sigma
  // utc_time
  rosidl_runtime_c__String__fini(&msg->utc_time);
  // ts_pos
  // ts_vel
  // ts_heading
  // state
  // num_master
  // gdop
  // pdop
  // hdop
  // htdop
  // tdop
  // num_reserve
}

bool
imu_msgs__msg__Gnss__are_equal(const imu_msgs__msg__Gnss * lhs, const imu_msgs__msg__Gnss * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // longitude
  if (lhs->longitude != rhs->longitude) {
    return false;
  }
  // lon_sigma
  if (lhs->lon_sigma != rhs->lon_sigma) {
    return false;
  }
  // latitude
  if (lhs->latitude != rhs->latitude) {
    return false;
  }
  // lat_sigma
  if (lhs->lat_sigma != rhs->lat_sigma) {
    return false;
  }
  // altitude
  if (lhs->altitude != rhs->altitude) {
    return false;
  }
  // alt_sigma
  if (lhs->alt_sigma != rhs->alt_sigma) {
    return false;
  }
  // gps_fix
  if (lhs->gps_fix != rhs->gps_fix) {
    return false;
  }
  // rtk_age
  if (lhs->rtk_age != rhs->rtk_age) {
    return false;
  }
  // flags_pos
  if (lhs->flags_pos != rhs->flags_pos) {
    return false;
  }
  // flags_vel
  if (lhs->flags_vel != rhs->flags_vel) {
    return false;
  }
  // flags_attitude
  if (lhs->flags_attitude != rhs->flags_attitude) {
    return false;
  }
  // flags_time
  if (lhs->flags_time != rhs->flags_time) {
    return false;
  }
  // hor_vel
  if (lhs->hor_vel != rhs->hor_vel) {
    return false;
  }
  // track_angle
  if (lhs->track_angle != rhs->track_angle) {
    return false;
  }
  // ver_vel
  if (lhs->ver_vel != rhs->ver_vel) {
    return false;
  }
  // latency_vel
  if (lhs->latency_vel != rhs->latency_vel) {
    return false;
  }
  // base_length
  if (lhs->base_length != rhs->base_length) {
    return false;
  }
  // yaw
  if (lhs->yaw != rhs->yaw) {
    return false;
  }
  // yaw_sigma
  if (lhs->yaw_sigma != rhs->yaw_sigma) {
    return false;
  }
  // pitch
  if (lhs->pitch != rhs->pitch) {
    return false;
  }
  // pitch_sigma
  if (lhs->pitch_sigma != rhs->pitch_sigma) {
    return false;
  }
  // utc_time
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->utc_time), &(rhs->utc_time)))
  {
    return false;
  }
  // ts_pos
  if (lhs->ts_pos != rhs->ts_pos) {
    return false;
  }
  // ts_vel
  if (lhs->ts_vel != rhs->ts_vel) {
    return false;
  }
  // ts_heading
  if (lhs->ts_heading != rhs->ts_heading) {
    return false;
  }
  // state
  if (lhs->state != rhs->state) {
    return false;
  }
  // num_master
  if (lhs->num_master != rhs->num_master) {
    return false;
  }
  // gdop
  if (lhs->gdop != rhs->gdop) {
    return false;
  }
  // pdop
  if (lhs->pdop != rhs->pdop) {
    return false;
  }
  // hdop
  if (lhs->hdop != rhs->hdop) {
    return false;
  }
  // htdop
  if (lhs->htdop != rhs->htdop) {
    return false;
  }
  // tdop
  if (lhs->tdop != rhs->tdop) {
    return false;
  }
  // num_reserve
  if (lhs->num_reserve != rhs->num_reserve) {
    return false;
  }
  return true;
}

bool
imu_msgs__msg__Gnss__copy(
  const imu_msgs__msg__Gnss * input,
  imu_msgs__msg__Gnss * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // longitude
  output->longitude = input->longitude;
  // lon_sigma
  output->lon_sigma = input->lon_sigma;
  // latitude
  output->latitude = input->latitude;
  // lat_sigma
  output->lat_sigma = input->lat_sigma;
  // altitude
  output->altitude = input->altitude;
  // alt_sigma
  output->alt_sigma = input->alt_sigma;
  // gps_fix
  output->gps_fix = input->gps_fix;
  // rtk_age
  output->rtk_age = input->rtk_age;
  // flags_pos
  output->flags_pos = input->flags_pos;
  // flags_vel
  output->flags_vel = input->flags_vel;
  // flags_attitude
  output->flags_attitude = input->flags_attitude;
  // flags_time
  output->flags_time = input->flags_time;
  // hor_vel
  output->hor_vel = input->hor_vel;
  // track_angle
  output->track_angle = input->track_angle;
  // ver_vel
  output->ver_vel = input->ver_vel;
  // latency_vel
  output->latency_vel = input->latency_vel;
  // base_length
  output->base_length = input->base_length;
  // yaw
  output->yaw = input->yaw;
  // yaw_sigma
  output->yaw_sigma = input->yaw_sigma;
  // pitch
  output->pitch = input->pitch;
  // pitch_sigma
  output->pitch_sigma = input->pitch_sigma;
  // utc_time
  if (!rosidl_runtime_c__String__copy(
      &(input->utc_time), &(output->utc_time)))
  {
    return false;
  }
  // ts_pos
  output->ts_pos = input->ts_pos;
  // ts_vel
  output->ts_vel = input->ts_vel;
  // ts_heading
  output->ts_heading = input->ts_heading;
  // state
  output->state = input->state;
  // num_master
  output->num_master = input->num_master;
  // gdop
  output->gdop = input->gdop;
  // pdop
  output->pdop = input->pdop;
  // hdop
  output->hdop = input->hdop;
  // htdop
  output->htdop = input->htdop;
  // tdop
  output->tdop = input->tdop;
  // num_reserve
  output->num_reserve = input->num_reserve;
  return true;
}

imu_msgs__msg__Gnss *
imu_msgs__msg__Gnss__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Gnss * msg = (imu_msgs__msg__Gnss *)allocator.allocate(sizeof(imu_msgs__msg__Gnss), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(imu_msgs__msg__Gnss));
  bool success = imu_msgs__msg__Gnss__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
imu_msgs__msg__Gnss__destroy(imu_msgs__msg__Gnss * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    imu_msgs__msg__Gnss__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
imu_msgs__msg__Gnss__Sequence__init(imu_msgs__msg__Gnss__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Gnss * data = NULL;

  if (size) {
    data = (imu_msgs__msg__Gnss *)allocator.zero_allocate(size, sizeof(imu_msgs__msg__Gnss), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = imu_msgs__msg__Gnss__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        imu_msgs__msg__Gnss__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
imu_msgs__msg__Gnss__Sequence__fini(imu_msgs__msg__Gnss__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      imu_msgs__msg__Gnss__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

imu_msgs__msg__Gnss__Sequence *
imu_msgs__msg__Gnss__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Gnss__Sequence * array = (imu_msgs__msg__Gnss__Sequence *)allocator.allocate(sizeof(imu_msgs__msg__Gnss__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = imu_msgs__msg__Gnss__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
imu_msgs__msg__Gnss__Sequence__destroy(imu_msgs__msg__Gnss__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    imu_msgs__msg__Gnss__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
imu_msgs__msg__Gnss__Sequence__are_equal(const imu_msgs__msg__Gnss__Sequence * lhs, const imu_msgs__msg__Gnss__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!imu_msgs__msg__Gnss__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
imu_msgs__msg__Gnss__Sequence__copy(
  const imu_msgs__msg__Gnss__Sequence * input,
  imu_msgs__msg__Gnss__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(imu_msgs__msg__Gnss);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    imu_msgs__msg__Gnss * data =
      (imu_msgs__msg__Gnss *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!imu_msgs__msg__Gnss__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          imu_msgs__msg__Gnss__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!imu_msgs__msg__Gnss__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
