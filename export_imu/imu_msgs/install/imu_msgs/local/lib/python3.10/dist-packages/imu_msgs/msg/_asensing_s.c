// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from imu_msgs:msg/ASENSING.idl
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
#include "imu_msgs/msg/detail/asensing__struct.h"
#include "imu_msgs/msg/detail/asensing__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool imu_msgs__msg__asensing__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[32];
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
    assert(strncmp("imu_msgs.msg._asensing.ASENSING", full_classname_dest, 31) == 0);
  }
  imu_msgs__msg__ASENSING * ros_message = _ros_message;
  {  // latitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "latitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latitude = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // longitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "longitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->longitude = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // altitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "altitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->altitude = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // north_velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "north_velocity");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->north_velocity = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // east_velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "east_velocity");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->east_velocity = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ground_velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "ground_velocity");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ground_velocity = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // roll
    PyObject * field = PyObject_GetAttrString(_pymsg, "roll");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->roll = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pitch
    PyObject * field = PyObject_GetAttrString(_pymsg, "pitch");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pitch = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // azimuth
    PyObject * field = PyObject_GetAttrString(_pymsg, "azimuth");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->azimuth = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // x_angular_velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_angular_velocity");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_angular_velocity = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_angular_velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_angular_velocity");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_angular_velocity = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // z_angular_velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "z_angular_velocity");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->z_angular_velocity = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // x_acc
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_acc");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_acc = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_acc
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_acc");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_acc = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // z_acc
    PyObject * field = PyObject_GetAttrString(_pymsg, "z_acc");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->z_acc = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // latitude_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "latitude_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latitude_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // longitude_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "longitude_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->longitude_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // altitude_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "altitude_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->altitude_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // north_velocity_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "north_velocity_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->north_velocity_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // east_velocity_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "east_velocity_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->east_velocity_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ground_velocity_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "ground_velocity_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ground_velocity_std = (float)PyFloat_AS_DOUBLE(field);
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
  {  // azimuth_std
    PyObject * field = PyObject_GetAttrString(_pymsg, "azimuth_std");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->azimuth_std = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ins_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "ins_status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ins_status = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // position_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "position_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->position_type = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // sec_of_week
    PyObject * field = PyObject_GetAttrString(_pymsg, "sec_of_week");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->sec_of_week = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // gps_week_number
    PyObject * field = PyObject_GetAttrString(_pymsg, "gps_week_number");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->gps_week_number = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // temperature
    PyObject * field = PyObject_GetAttrString(_pymsg, "temperature");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->temperature = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // wheel_speed_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "wheel_speed_status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->wheel_speed_status = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // heading_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "heading_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->heading_type = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // numsv
    PyObject * field = PyObject_GetAttrString(_pymsg, "numsv");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->numsv = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // is_available
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_available");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_available = (Py_True == field);
    Py_DECREF(field);
  }
  {  // utm_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "utm_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->utm_x = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // utm_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "utm_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->utm_y = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * imu_msgs__msg__asensing__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ASENSING */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("imu_msgs.msg._asensing");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ASENSING");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  imu_msgs__msg__ASENSING * ros_message = (imu_msgs__msg__ASENSING *)raw_ros_message;
  {  // latitude
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->latitude);
    {
      int rc = PyObject_SetAttrString(_pymessage, "latitude", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // longitude
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->longitude);
    {
      int rc = PyObject_SetAttrString(_pymessage, "longitude", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // altitude
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->altitude);
    {
      int rc = PyObject_SetAttrString(_pymessage, "altitude", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // north_velocity
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->north_velocity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "north_velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // east_velocity
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->east_velocity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "east_velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ground_velocity
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ground_velocity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ground_velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // roll
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->roll);
    {
      int rc = PyObject_SetAttrString(_pymessage, "roll", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pitch
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pitch);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pitch", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // azimuth
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->azimuth);
    {
      int rc = PyObject_SetAttrString(_pymessage, "azimuth", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_angular_velocity
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_angular_velocity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_angular_velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_angular_velocity
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_angular_velocity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_angular_velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // z_angular_velocity
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->z_angular_velocity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "z_angular_velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_acc
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_acc);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_acc", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_acc
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_acc);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_acc", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // z_acc
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->z_acc);
    {
      int rc = PyObject_SetAttrString(_pymessage, "z_acc", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // latitude_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->latitude_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "latitude_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // longitude_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->longitude_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "longitude_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // altitude_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->altitude_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "altitude_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // north_velocity_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->north_velocity_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "north_velocity_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // east_velocity_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->east_velocity_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "east_velocity_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ground_velocity_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ground_velocity_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ground_velocity_std", field);
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
  {  // azimuth_std
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->azimuth_std);
    {
      int rc = PyObject_SetAttrString(_pymessage, "azimuth_std", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ins_status
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ins_status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ins_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position_type
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->position_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // sec_of_week
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->sec_of_week);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sec_of_week", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gps_week_number
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->gps_week_number);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gps_week_number", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // temperature
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->temperature);
    {
      int rc = PyObject_SetAttrString(_pymessage, "temperature", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // wheel_speed_status
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->wheel_speed_status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "wheel_speed_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // heading_type
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->heading_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "heading_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // numsv
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->numsv);
    {
      int rc = PyObject_SetAttrString(_pymessage, "numsv", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_available
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_available ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_available", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // utm_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->utm_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "utm_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // utm_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->utm_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "utm_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
