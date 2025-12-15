// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from imu_msgs:msg/Odom.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "imu_msgs/msg/detail/odom__struct.h"
#include "imu_msgs/msg/detail/odom__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool imu_msgs__msg__odom__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[24];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("imu_msgs.msg._odom.Odom", full_classname_dest, 23) == 0);
  }
  imu_msgs__msg__Odom * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // q0_w
    PyObject * field = PyObject_GetAttrString(_pymsg, "q0_w");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->q0_w = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // q1_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "q1_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->q1_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // q2_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "q2_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->q2_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // q3_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "q3_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->q3_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pos_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pos_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pos_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pos_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pos_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pos_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vel_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "vel_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vel_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vel_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "vel_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vel_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vel_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "vel_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vel_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "vel");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vel = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ang_vel_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "ang_vel_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ang_vel_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ang_vel_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "ang_vel_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ang_vel_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ang_vel_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "ang_vel_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ang_vel_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // acc_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "acc_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->acc_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // acc_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "acc_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->acc_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // acc_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "acc_z");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->acc_z = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // status
    PyObject * field = PyObject_GetAttrString(_pymsg, "status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->status = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // sensor_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "sensor_status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->sensor_status = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // pos_x_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos_x_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pos_x_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pos_y_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos_y_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pos_y_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pos_z_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "pos_z_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pos_z_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vel_x_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "vel_x_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vel_x_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vel_y_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "vel_y_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vel_y_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // vel_z_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "vel_z_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->vel_z_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // roll_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "roll_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->roll_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pitch_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "pitch_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pitch_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // tow_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "tow_ms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->tow_ms = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * imu_msgs__msg__odom__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Odom */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("imu_msgs.msg._odom");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Odom");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  imu_msgs__msg__Odom * ros_message = (imu_msgs__msg__Odom *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // q0_w
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->q0_w);
    {
      int rc = PyObject_SetAttrString(_pymessage, "q0_w", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // q1_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->q1_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "q1_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // q2_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->q2_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "q2_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // q3_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->q3_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "q3_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pos_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pos_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pos_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pos_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pos_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pos_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pos_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pos_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pos_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vel_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vel_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vel_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vel_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vel_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vel_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vel_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vel_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vel_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vel
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vel);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ang_vel_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ang_vel_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ang_vel_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ang_vel_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ang_vel_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ang_vel_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ang_vel_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ang_vel_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ang_vel_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // acc_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->acc_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "acc_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // acc_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->acc_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "acc_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // acc_z
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->acc_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "acc_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // status
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // sensor_status
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->sensor_status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sensor_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pos_x_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pos_x_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pos_x_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pos_y_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pos_y_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pos_y_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pos_z_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pos_z_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pos_z_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vel_x_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vel_x_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vel_x_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vel_y_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vel_y_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vel_y_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // vel_z_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->vel_z_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "vel_z_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // roll_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->roll_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "roll_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pitch_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pitch_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pitch_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tow_ms
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->tow_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tow_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
