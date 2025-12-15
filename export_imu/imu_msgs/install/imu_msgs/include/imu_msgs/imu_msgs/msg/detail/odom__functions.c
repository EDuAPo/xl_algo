// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from imu_msgs:msg/Odom.idl
// generated code does not contain a copyright notice
#include "imu_msgs/msg/detail/odom__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
imu_msgs__msg__Odom__init(imu_msgs__msg__Odom * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    imu_msgs__msg__Odom__fini(msg);
    return false;
  }
  // q0_w
  // q1_x
  // q2_y
  // q3_z
  // pos_x
  // pos_y
  // pos_z
  // vel_x
  // vel_y
  // vel_z
  // vel
  // ang_vel_x
  // ang_vel_y
  // ang_vel_z
  // acc_x
  // acc_y
  // acc_z
  // status
  // sensor_status
  // pos_x_std
  // pos_y_std
  // pos_z_std
  // vel_x_std
  // vel_y_std
  // vel_z_std
  // roll_std
  // pitch_std
  // yaw_std
  // tow_ms
  return true;
}

void
imu_msgs__msg__Odom__fini(imu_msgs__msg__Odom * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // q0_w
  // q1_x
  // q2_y
  // q3_z
  // pos_x
  // pos_y
  // pos_z
  // vel_x
  // vel_y
  // vel_z
  // vel
  // ang_vel_x
  // ang_vel_y
  // ang_vel_z
  // acc_x
  // acc_y
  // acc_z
  // status
  // sensor_status
  // pos_x_std
  // pos_y_std
  // pos_z_std
  // vel_x_std
  // vel_y_std
  // vel_z_std
  // roll_std
  // pitch_std
  // yaw_std
  // tow_ms
}

bool
imu_msgs__msg__Odom__are_equal(const imu_msgs__msg__Odom * lhs, const imu_msgs__msg__Odom * rhs)
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
  // q0_w
  if (lhs->q0_w != rhs->q0_w) {
    return false;
  }
  // q1_x
  if (lhs->q1_x != rhs->q1_x) {
    return false;
  }
  // q2_y
  if (lhs->q2_y != rhs->q2_y) {
    return false;
  }
  // q3_z
  if (lhs->q3_z != rhs->q3_z) {
    return false;
  }
  // pos_x
  if (lhs->pos_x != rhs->pos_x) {
    return false;
  }
  // pos_y
  if (lhs->pos_y != rhs->pos_y) {
    return false;
  }
  // pos_z
  if (lhs->pos_z != rhs->pos_z) {
    return false;
  }
  // vel_x
  if (lhs->vel_x != rhs->vel_x) {
    return false;
  }
  // vel_y
  if (lhs->vel_y != rhs->vel_y) {
    return false;
  }
  // vel_z
  if (lhs->vel_z != rhs->vel_z) {
    return false;
  }
  // vel
  if (lhs->vel != rhs->vel) {
    return false;
  }
  // ang_vel_x
  if (lhs->ang_vel_x != rhs->ang_vel_x) {
    return false;
  }
  // ang_vel_y
  if (lhs->ang_vel_y != rhs->ang_vel_y) {
    return false;
  }
  // ang_vel_z
  if (lhs->ang_vel_z != rhs->ang_vel_z) {
    return false;
  }
  // acc_x
  if (lhs->acc_x != rhs->acc_x) {
    return false;
  }
  // acc_y
  if (lhs->acc_y != rhs->acc_y) {
    return false;
  }
  // acc_z
  if (lhs->acc_z != rhs->acc_z) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // sensor_status
  if (lhs->sensor_status != rhs->sensor_status) {
    return false;
  }
  // pos_x_std
  if (lhs->pos_x_std != rhs->pos_x_std) {
    return false;
  }
  // pos_y_std
  if (lhs->pos_y_std != rhs->pos_y_std) {
    return false;
  }
  // pos_z_std
  if (lhs->pos_z_std != rhs->pos_z_std) {
    return false;
  }
  // vel_x_std
  if (lhs->vel_x_std != rhs->vel_x_std) {
    return false;
  }
  // vel_y_std
  if (lhs->vel_y_std != rhs->vel_y_std) {
    return false;
  }
  // vel_z_std
  if (lhs->vel_z_std != rhs->vel_z_std) {
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
  // yaw_std
  if (lhs->yaw_std != rhs->yaw_std) {
    return false;
  }
  // tow_ms
  if (lhs->tow_ms != rhs->tow_ms) {
    return false;
  }
  return true;
}

bool
imu_msgs__msg__Odom__copy(
  const imu_msgs__msg__Odom * input,
  imu_msgs__msg__Odom * output)
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
  // q0_w
  output->q0_w = input->q0_w;
  // q1_x
  output->q1_x = input->q1_x;
  // q2_y
  output->q2_y = input->q2_y;
  // q3_z
  output->q3_z = input->q3_z;
  // pos_x
  output->pos_x = input->pos_x;
  // pos_y
  output->pos_y = input->pos_y;
  // pos_z
  output->pos_z = input->pos_z;
  // vel_x
  output->vel_x = input->vel_x;
  // vel_y
  output->vel_y = input->vel_y;
  // vel_z
  output->vel_z = input->vel_z;
  // vel
  output->vel = input->vel;
  // ang_vel_x
  output->ang_vel_x = input->ang_vel_x;
  // ang_vel_y
  output->ang_vel_y = input->ang_vel_y;
  // ang_vel_z
  output->ang_vel_z = input->ang_vel_z;
  // acc_x
  output->acc_x = input->acc_x;
  // acc_y
  output->acc_y = input->acc_y;
  // acc_z
  output->acc_z = input->acc_z;
  // status
  output->status = input->status;
  // sensor_status
  output->sensor_status = input->sensor_status;
  // pos_x_std
  output->pos_x_std = input->pos_x_std;
  // pos_y_std
  output->pos_y_std = input->pos_y_std;
  // pos_z_std
  output->pos_z_std = input->pos_z_std;
  // vel_x_std
  output->vel_x_std = input->vel_x_std;
  // vel_y_std
  output->vel_y_std = input->vel_y_std;
  // vel_z_std
  output->vel_z_std = input->vel_z_std;
  // roll_std
  output->roll_std = input->roll_std;
  // pitch_std
  output->pitch_std = input->pitch_std;
  // yaw_std
  output->yaw_std = input->yaw_std;
  // tow_ms
  output->tow_ms = input->tow_ms;
  return true;
}

imu_msgs__msg__Odom *
imu_msgs__msg__Odom__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Odom * msg = (imu_msgs__msg__Odom *)allocator.allocate(sizeof(imu_msgs__msg__Odom), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(imu_msgs__msg__Odom));
  bool success = imu_msgs__msg__Odom__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
imu_msgs__msg__Odom__destroy(imu_msgs__msg__Odom * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    imu_msgs__msg__Odom__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
imu_msgs__msg__Odom__Sequence__init(imu_msgs__msg__Odom__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Odom * data = NULL;

  if (size) {
    data = (imu_msgs__msg__Odom *)allocator.zero_allocate(size, sizeof(imu_msgs__msg__Odom), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = imu_msgs__msg__Odom__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        imu_msgs__msg__Odom__fini(&data[i - 1]);
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
imu_msgs__msg__Odom__Sequence__fini(imu_msgs__msg__Odom__Sequence * array)
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
      imu_msgs__msg__Odom__fini(&array->data[i]);
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

imu_msgs__msg__Odom__Sequence *
imu_msgs__msg__Odom__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Odom__Sequence * array = (imu_msgs__msg__Odom__Sequence *)allocator.allocate(sizeof(imu_msgs__msg__Odom__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = imu_msgs__msg__Odom__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
imu_msgs__msg__Odom__Sequence__destroy(imu_msgs__msg__Odom__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    imu_msgs__msg__Odom__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
imu_msgs__msg__Odom__Sequence__are_equal(const imu_msgs__msg__Odom__Sequence * lhs, const imu_msgs__msg__Odom__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!imu_msgs__msg__Odom__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
imu_msgs__msg__Odom__Sequence__copy(
  const imu_msgs__msg__Odom__Sequence * input,
  imu_msgs__msg__Odom__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(imu_msgs__msg__Odom);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    imu_msgs__msg__Odom * data =
      (imu_msgs__msg__Odom *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!imu_msgs__msg__Odom__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          imu_msgs__msg__Odom__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!imu_msgs__msg__Odom__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
