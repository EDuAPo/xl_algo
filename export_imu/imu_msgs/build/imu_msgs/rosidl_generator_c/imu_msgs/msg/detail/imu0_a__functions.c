// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from imu_msgs:msg/Imu0A.idl
// generated code does not contain a copyright notice
#include "imu_msgs/msg/detail/imu0_a__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
imu_msgs__msg__Imu0A__init(imu_msgs__msg__Imu0A * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    imu_msgs__msg__Imu0A__fini(msg);
    return false;
  }
  // gx
  // gy
  // gz
  // ax
  // ay
  // az
  // temperature
  // imu_time_stamp
  // status
  // frame_count
  return true;
}

void
imu_msgs__msg__Imu0A__fini(imu_msgs__msg__Imu0A * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // gx
  // gy
  // gz
  // ax
  // ay
  // az
  // temperature
  // imu_time_stamp
  // status
  // frame_count
}

bool
imu_msgs__msg__Imu0A__are_equal(const imu_msgs__msg__Imu0A * lhs, const imu_msgs__msg__Imu0A * rhs)
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
  // gx
  if (lhs->gx != rhs->gx) {
    return false;
  }
  // gy
  if (lhs->gy != rhs->gy) {
    return false;
  }
  // gz
  if (lhs->gz != rhs->gz) {
    return false;
  }
  // ax
  if (lhs->ax != rhs->ax) {
    return false;
  }
  // ay
  if (lhs->ay != rhs->ay) {
    return false;
  }
  // az
  if (lhs->az != rhs->az) {
    return false;
  }
  // temperature
  if (lhs->temperature != rhs->temperature) {
    return false;
  }
  // imu_time_stamp
  if (lhs->imu_time_stamp != rhs->imu_time_stamp) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // frame_count
  if (lhs->frame_count != rhs->frame_count) {
    return false;
  }
  return true;
}

bool
imu_msgs__msg__Imu0A__copy(
  const imu_msgs__msg__Imu0A * input,
  imu_msgs__msg__Imu0A * output)
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
  // gx
  output->gx = input->gx;
  // gy
  output->gy = input->gy;
  // gz
  output->gz = input->gz;
  // ax
  output->ax = input->ax;
  // ay
  output->ay = input->ay;
  // az
  output->az = input->az;
  // temperature
  output->temperature = input->temperature;
  // imu_time_stamp
  output->imu_time_stamp = input->imu_time_stamp;
  // status
  output->status = input->status;
  // frame_count
  output->frame_count = input->frame_count;
  return true;
}

imu_msgs__msg__Imu0A *
imu_msgs__msg__Imu0A__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Imu0A * msg = (imu_msgs__msg__Imu0A *)allocator.allocate(sizeof(imu_msgs__msg__Imu0A), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(imu_msgs__msg__Imu0A));
  bool success = imu_msgs__msg__Imu0A__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
imu_msgs__msg__Imu0A__destroy(imu_msgs__msg__Imu0A * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    imu_msgs__msg__Imu0A__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
imu_msgs__msg__Imu0A__Sequence__init(imu_msgs__msg__Imu0A__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Imu0A * data = NULL;

  if (size) {
    data = (imu_msgs__msg__Imu0A *)allocator.zero_allocate(size, sizeof(imu_msgs__msg__Imu0A), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = imu_msgs__msg__Imu0A__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        imu_msgs__msg__Imu0A__fini(&data[i - 1]);
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
imu_msgs__msg__Imu0A__Sequence__fini(imu_msgs__msg__Imu0A__Sequence * array)
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
      imu_msgs__msg__Imu0A__fini(&array->data[i]);
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

imu_msgs__msg__Imu0A__Sequence *
imu_msgs__msg__Imu0A__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  imu_msgs__msg__Imu0A__Sequence * array = (imu_msgs__msg__Imu0A__Sequence *)allocator.allocate(sizeof(imu_msgs__msg__Imu0A__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = imu_msgs__msg__Imu0A__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
imu_msgs__msg__Imu0A__Sequence__destroy(imu_msgs__msg__Imu0A__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    imu_msgs__msg__Imu0A__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
imu_msgs__msg__Imu0A__Sequence__are_equal(const imu_msgs__msg__Imu0A__Sequence * lhs, const imu_msgs__msg__Imu0A__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!imu_msgs__msg__Imu0A__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
imu_msgs__msg__Imu0A__Sequence__copy(
  const imu_msgs__msg__Imu0A__Sequence * input,
  imu_msgs__msg__Imu0A__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(imu_msgs__msg__Imu0A);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    imu_msgs__msg__Imu0A * data =
      (imu_msgs__msg__Imu0A *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!imu_msgs__msg__Imu0A__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          imu_msgs__msg__Imu0A__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!imu_msgs__msg__Imu0A__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
