// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from imu_msgs:msg/ASENSING.idl
// generated code does not contain a copyright notice
#include "imu_msgs/msg/detail/asensing__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
imu_msgs__msg__ASENSING__init(imu_msgs__msg__ASENSING * msg)
{
  if (!msg) {
    return false;
  }
  // latitude
  // longitude
  // altitude
  // north_velocity
  // east_velocity
  // ground_velocity
  // roll
  // pitch
  // azimuth
  // x_angular_velocity
  // y_angular_velocity
  // z_angular_velocity
  // x_acc
  // y_acc
  // z_acc
  // latitude_std
  // longitude_std
  // altitude_std
  // north_velocity_std
  // east_velocity_std
  // ground_velocity_std
  // roll_std
  // pitch_std
  // azimuth_std
  // ins_status
  // position_type
  // sec_of_week
  // gps_week_number
  // temperature
  // wheel_speed_status
  // heading_type
  // numsv
  // is_available
  // utm_x
  // utm_y
  return true;
}

void
imu_msgs__msg__ASENSING__fini(imu_msgs__msg__ASENSING * msg)
{
  if (!msg) {
    return;
  }
  // latitude
  // longitude
  // altitude
  // north_velocity
  // east_velocity
  // ground_velocity
  // roll
  // pitch
  // azimuth
  // x_angular_velocity
  // y_angular_velocity
  // z_angular_velocity
  // x_acc
  // y_acc
  // z_acc
  // latitude_std
  // longitude_std
  // altitude_std
  // north_velocity_std
  // east_velocity_std
  // ground_velocity_std
  // roll_std
  // pitch_std
  // azimuth_std
  // ins_status
  // position_type
  // sec_of_week
  // gps_week_number
  // temperature
  // wheel_speed_status
  // heading_type
  // numsv
  // is_available
  // utm_x
  // utm_y
}

bool
imu_msgs__msg__ASENSING__are_equal(const imu_msgs__msg__ASENSING * lhs, const imu_msgs__msg__ASENSING * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // latitude
  if (lhs->latitude != rhs->latitude) {
    return false;
  }
  // longitude
  if (lhs->longitude != rhs->longitude) {
    return false;
  }
  // altitude
  if (lhs->altitude != rhs->altitude) {
    return false;
  }
  // north_velocity
  if (lhs->north_velocity != rhs->north_velocity) {
    return false;
  }
  // east_velocity
  if (lhs->east_velocity != rhs->east_velocity) {
    return false;
  }
  // ground_velocity
  if (lhs->ground_velocity != rhs->ground_velocity) {
    return false;
  }
  // roll
  if (lhs->roll != rhs->roll) {
    return false;
  }
  // pitch
  if (lhs->pitch != rhs->pitch) {
    return false;
  }
  // azimuth
  if (lhs->azimuth != rhs->azimuth) {
    return false;
  }
  // x_angular_velocity
  if (lhs->x_angular_velocity != rhs->x_angular_velocity) {
    return false;
  }
  // y_angular_velocity
  if (lhs->y_angular_velocity != rhs->y_angular_velocity) {
    return false;
  }
  // z_angular_velocity
  if (lhs->z_angular_velocity != rhs->z_angular_velocity) {
    return false;
  }
  // x_acc
  if (lhs->x_acc != rhs->x_acc) {
    return false;
  }
  // y_acc
  if (lhs->y_acc != rhs->y_acc) {
    return false;
  }
  // z_acc
  if (lhs->z_acc != rhs->z_acc) {
    return false;
  }
  // latitude_std
  if (lhs->latitude_std != rhs->latitude_std) {
    return false;
  }
  // longitude_std
  if (lhs->longitude_std != rhs->longitude_std) {
    return false;
  }
  // altitude_std
  if (lhs->altitude_std != rhs->altitude_std) {
    return false;
  }
  // north_velocity_std
  if (lhs->north_velocity_std != rhs->north_velocity_std) {
    return false;
  }
  // east_velocity_std
  if (lhs->east_velocity_std != rhs->east_velocity_std) {
    return false;
  }
  // ground_velocity_std
  if (lhs->ground_velocity_std != rhs->ground_velocity_std) {
    return false;
  }
  // roll_std
  if (lhs->roll_std != rhs->roll_std) {
    return false;
  }
  // pitch_std
  if (lhs->pitch_std != rhs->pitch_std) {
    return false;
  }
  // azimuth_std
  if (lhs->azimuth_std != rhs->azimuth_std) {
    return false;
  }
  // ins_status
  if (lhs->ins_status != rhs->ins_status) {
    return false;
  }
  // position_type
  if (lhs->position_type != rhs->position_type) {
    return false;
  }
  // sec_of_week
  if (lhs->sec_of_week != rhs->sec_of_week) {
    return false;
  }
  // gps_week_number
  if (lhs->gps_week_number != rhs->gps_week_number) {
    return false;
  }
  // temperature
  if (lhs->temperature != rhs->temperature) {
    return false;
  }
  // wheel_speed_status
  if (lhs->wheel_speed_status != rhs->wheel_speed_status) {
    return false;
  }
  // heading_type
  if (lhs->heading_type != rhs->heading_type) {
    return false;
  }
  // numsv
  if (lhs->numsv != rhs->numsv) {
    return false;
  }
  // is_available
  if (lhs->is_available != rhs->is_available) {
    return false;
  }
  // utm_x
  if (lhs->utm_x != rhs->utm_x) {
    return false;
  }
  // utm_y
  if (lhs->utm_y != rhs->utm_y) {
    return false;
  }
  return true;
}

bool
imu_msgs__msg__ASENSING__copy(
  const imu_msgs__msg__ASENSING * input,
  imu_msgs__msg__ASENSING * output)
{
  if (!input || !output) {
    return false;
  }
  // latitude
  output->latitude = input->latitude;
  // longitude
  output->longitude = input->longitude;
  // altitude
  output->altitude = input->altitude;
  // north_velocity
  output->north_velocity = input->north_velocity;
  // east_velocity
  output->east_velocity = input->east_velocity;
  // ground_velocity
  output->ground_velocity = input->ground_velocity;
  // roll
  output->roll = input->roll;
  // pitch
  output->pitch = input->pitch;
  // azimuth
  output->azimuth = input->azimuth;
  // x_angular_velocity
  output->x_angular_velocity = input->x_angular_velocity;
  // y_angular_velocity
  output->y_angular_velocity = input->y_angular_velocity;
  // z_angular_velocity
  output->z_angular_velocity = input->z_angular_velocity;
  // x_acc
  output->x_acc = input->x_acc;
  // y_acc
  output->y_acc = input->y_acc;
  // z_acc
  output->z_acc = input->z_acc;
  // latitude_std
  output->latitude_std = input->latitude_std;
  // longitude_std
  output->longitude_std = input->longitude_std;
  // altitude_std
  output->altitude_std = input->altitude_std;
  // north_velocity_std
  output->north_velocity_std = input->north_velocity_std;
  // east_velocity_std
  output->east_velocity_std = input->east_velocity_std;
  // ground_velocity_std
  output->ground_velocity_std = input->ground_velocity_std;
  // roll_std
  output->roll_std = input->roll_std;
  // pitch_std
  output->pitch_std = input->pitch_std;
  // azimuth_std
  output->azimuth_std = input->azimuth_std;
  // ins_status
  output->ins_status = input->ins_status;
  // position_type
  output->position_type = input->position_type;
  // sec_of_week
  output->sec_of_week = input->sec_of_week;
  // gps_week_number
  output->gps_week_number = input->gps_week_number;
  // temperature
  output->temperature = input->temperature;
  // wheel_speed_status
  output->wheel_speed_status = input->wheel_speed_status;
  // heading_type
  output->heading_type = input->heading_type;
  // numsv
  output->numsv = input->numsv;
  // is_available
  output->is_available = input->is_available;
  // utm_x
  output->utm_x = input->utm_x;
  // utm_y
  output->utm_y = input->utm_y;
  return true;
}

imu_msgs__msg__ASENSING *
imu_msgs__msg__ASENSING__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__ASENSING * msg = (imu_msgs__msg__ASENSING *)allocator.allocate(sizeof(imu_msgs__msg__ASENSING), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(imu_msgs__msg__ASENSING));
  bool success = imu_msgs__msg__ASENSING__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
imu_msgs__msg__ASENSING__destroy(imu_msgs__msg__ASENSING * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    imu_msgs__msg__ASENSING__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
imu_msgs__msg__ASENSING__Sequence__init(imu_msgs__msg__ASENSING__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__ASENSING * data = NULL;

  if (size) {
    data = (imu_msgs__msg__ASENSING *)allocator.zero_allocate(size, sizeof(imu_msgs__msg__ASENSING), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = imu_msgs__msg__ASENSING__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        imu_msgs__msg__ASENSING__fini(&data[i - 1]);
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
imu_msgs__msg__ASENSING__Sequence__fini(imu_msgs__msg__ASENSING__Sequence * array)
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
      imu_msgs__msg__ASENSING__fini(&array->data[i]);
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

imu_msgs__msg__ASENSING__Sequence *
imu_msgs__msg__ASENSING__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__ASENSING__Sequence * array = (imu_msgs__msg__ASENSING__Sequence *)allocator.allocate(sizeof(imu_msgs__msg__ASENSING__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = imu_msgs__msg__ASENSING__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
imu_msgs__msg__ASENSING__Sequence__destroy(imu_msgs__msg__ASENSING__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    imu_msgs__msg__ASENSING__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
imu_msgs__msg__ASENSING__Sequence__are_equal(const imu_msgs__msg__ASENSING__Sequence * lhs, const imu_msgs__msg__ASENSING__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!imu_msgs__msg__ASENSING__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
imu_msgs__msg__ASENSING__Sequence__copy(
  const imu_msgs__msg__ASENSING__Sequence * input,
  imu_msgs__msg__ASENSING__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(imu_msgs__msg__ASENSING);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    imu_msgs__msg__ASENSING * data =
      (imu_msgs__msg__ASENSING *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!imu_msgs__msg__ASENSING__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          imu_msgs__msg__ASENSING__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!imu_msgs__msg__ASENSING__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
