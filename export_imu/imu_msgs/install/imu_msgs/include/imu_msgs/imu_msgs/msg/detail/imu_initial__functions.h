// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from imu_msgs:msg/ImuInitial.idl
// generated code does not contain a copyright notice

#ifndef IMU_MSGS__MSG__DETAIL__IMU_INITIAL__FUNCTIONS_H_
#define IMU_MSGS__MSG__DETAIL__IMU_INITIAL__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "imu_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "imu_msgs/msg/detail/imu_initial__struct.h"

/// Initialize msg/ImuInitial message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * imu_msgs__msg__ImuInitial
 * )) before or use
 * imu_msgs__msg__ImuInitial__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ImuInitial__init(imu_msgs__msg__ImuInitial * msg);

/// Finalize msg/ImuInitial message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
void
imu_msgs__msg__ImuInitial__fini(imu_msgs__msg__ImuInitial * msg);

/// Create msg/ImuInitial message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * imu_msgs__msg__ImuInitial__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
imu_msgs__msg__ImuInitial *
imu_msgs__msg__ImuInitial__create();

/// Destroy msg/ImuInitial message.
/**
 * It calls
 * imu_msgs__msg__ImuInitial__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
void
imu_msgs__msg__ImuInitial__destroy(imu_msgs__msg__ImuInitial * msg);

/// Check for msg/ImuInitial message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ImuInitial__are_equal(const imu_msgs__msg__ImuInitial * lhs, const imu_msgs__msg__ImuInitial * rhs);

/// Copy a msg/ImuInitial message.
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
imu_msgs__msg__ImuInitial__copy(
  const imu_msgs__msg__ImuInitial * input,
  imu_msgs__msg__ImuInitial * output);

/// Initialize array of msg/ImuInitial messages.
/**
 * It allocates the memory for the number of elements and calls
 * imu_msgs__msg__ImuInitial__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ImuInitial__Sequence__init(imu_msgs__msg__ImuInitial__Sequence * array, size_t size);

/// Finalize array of msg/ImuInitial messages.
/**
 * It calls
 * imu_msgs__msg__ImuInitial__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
void
imu_msgs__msg__ImuInitial__Sequence__fini(imu_msgs__msg__ImuInitial__Sequence * array);

/// Create array of msg/ImuInitial messages.
/**
 * It allocates the memory for the array and calls
 * imu_msgs__msg__ImuInitial__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
imu_msgs__msg__ImuInitial__Sequence *
imu_msgs__msg__ImuInitial__Sequence__create(size_t size);

/// Destroy array of msg/ImuInitial messages.
/**
 * It calls
 * imu_msgs__msg__ImuInitial__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
void
imu_msgs__msg__ImuInitial__Sequence__destroy(imu_msgs__msg__ImuInitial__Sequence * array);

/// Check for msg/ImuInitial message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_imu_msgs
bool
imu_msgs__msg__ImuInitial__Sequence__are_equal(const imu_msgs__msg__ImuInitial__Sequence * lhs, const imu_msgs__msg__ImuInitial__Sequence * rhs);

/// Copy an array of msg/ImuInitial messages.
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
imu_msgs__msg__ImuInitial__Sequence__copy(
  const imu_msgs__msg__ImuInitial__Sequence * input,
  imu_msgs__msg__ImuInitial__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // IMU_MSGS__MSG__DETAIL__IMU_INITIAL__FUNCTIONS_H_
