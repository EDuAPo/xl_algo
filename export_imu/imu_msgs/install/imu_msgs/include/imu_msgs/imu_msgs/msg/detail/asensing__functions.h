// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from imu_msgs:msg/ASENSING.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__ASENSING__FUNCTIONS_H_
#define IMU_MSGS__MSG__DETAIL__ASENSING__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "imu_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "imu_msgs/msg/detail/asensing__struct.h"

/// Initialize msg/ASENSING message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * imu_msgs__msg__ASENSING
 * )) before or use
 * imu_msgs__msg__ASENSING__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ASENSING__init(imu_msgs__msg__ASENSING * msg);

/// Finalize msg/ASENSING message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
void
imu_msgs__msg__ASENSING__fini(imu_msgs__msg__ASENSING * msg);

/// Create msg/ASENSING message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * imu_msgs__msg__ASENSING__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
imu_msgs__msg__ASENSING *
imu_msgs__msg__ASENSING__create();

/// Destroy msg/ASENSING message.
/**
 * It calls
 * imu_msgs__msg__ASENSING__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
void
imu_msgs__msg__ASENSING__destroy(imu_msgs__msg__ASENSING * msg);

/// Check for msg/ASENSING message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ASENSING__are_equal(const imu_msgs__msg__ASENSING * lhs, const imu_msgs__msg__ASENSING * rhs);

/// Copy a msg/ASENSING message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ASENSING__copy(
  const imu_msgs__msg__ASENSING * input,
  imu_msgs__msg__ASENSING * output);

/// Initialize array of msg/ASENSING messages.
/**
 * It allocates the memory for the number of elements and calls
 * imu_msgs__msg__ASENSING__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ASENSING__Sequence__init(imu_msgs__msg__ASENSING__Sequence * array, size_t size);

/// Finalize array of msg/ASENSING messages.
/**
 * It calls
 * imu_msgs__msg__ASENSING__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
void
imu_msgs__msg__ASENSING__Sequence__fini(imu_msgs__msg__ASENSING__Sequence * array);

/// Create array of msg/ASENSING messages.
/**
 * It allocates the memory for the array and calls
 * imu_msgs__msg__ASENSING__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
imu_msgs__msg__ASENSING__Sequence *
imu_msgs__msg__ASENSING__Sequence__create(size_t size);

/// Destroy array of msg/ASENSING messages.
/**
 * It calls
 * imu_msgs__msg__ASENSING__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
void
imu_msgs__msg__ASENSING__Sequence__destroy(imu_msgs__msg__ASENSING__Sequence * array);

/// Check for msg/ASENSING message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ASENSING__Sequence__are_equal(const imu_msgs__msg__ASENSING__Sequence * lhs, const imu_msgs__msg__ASENSING__Sequence * rhs);

/// Copy an array of msg/ASENSING messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ASENSING__Sequence__copy(
  const imu_msgs__msg__ASENSING__Sequence * input,
  imu_msgs__msg__ASENSING__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__ASENSING__FUNCTIONS_H_
