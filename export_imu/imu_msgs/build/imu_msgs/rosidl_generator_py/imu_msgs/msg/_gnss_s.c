// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from imu_msgs:msg/Gnss.idl
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
#include "imu_msgs/msg/detail/gnss__struct.h"
#include "imu_msgs/msg/detail/gnss__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool imu_msgs__msg__gnss__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("imu_msgs.msg._gnss.Gnss", full_classname_dest, 23) == 0);
  }
  imu_msgs__msg__Gnss * ros_message = _ros_message;
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
  {  // longitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "longitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->longitude = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // lon_sigma
    PyObject * field = PyObject_GetAttrString(_pymsg, "lon_sigma");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lon_sigma = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // latitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "latitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latitude = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // lat_sigma
    PyObject * field = PyObject_GetAttrString(_pymsg, "lat_sigma");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lat_sigma = (float)PyFloat_AS_DOUBLE(field);
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
  {  // alt_sigma
    PyObject * field = PyObject_GetAttrString(_pymsg, "alt_sigma");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->alt_sigma = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // gps_fix
    PyObject * field = PyObject_GetAttrString(_pymsg, "gps_fix");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->gps_fix = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // rtk_age
    PyObject * field = PyObject_GetAttrString(_pymsg, "rtk_age");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->rtk_age = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // flags_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "flags_pos");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->flags_pos = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // flags_vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "flags_vel");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->flags_vel = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // flags_attitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "flags_attitude");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->flags_attitude = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // flags_time
    PyObject * field = PyObject_GetAttrString(_pymsg, "flags_time");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->flags_time = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // hor_vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "hor_vel");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->hor_vel = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // track_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "track_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->track_angle = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ver_vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "ver_vel");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ver_vel = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // latency_vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "latency_vel");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latency_vel = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // base_length
    PyObject * field = PyObject_GetAttrString(_pymsg, "base_length");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->base_length = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw_sigma
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw_sigma");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw_sigma = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pitch
    PyObject * field = PyObject_GetAttrString(_pymsg, "pitch");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pitch = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pitch_sigma
    PyObject * field = PyObject_GetAttrString(_pymsg, "pitch_sigma");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pitch_sigma = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // utc_time
    PyObject * field = PyObject_GetAttrString(_pymsg, "utc_time");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->utc_time, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // ts_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "ts_pos");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ts_pos = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ts_vel
    PyObject * field = PyObject_GetAttrString(_pymsg, "ts_vel");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ts_vel = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // ts_heading
    PyObject * field = PyObject_GetAttrString(_pymsg, "ts_heading");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ts_heading = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // state
    PyObject * field = PyObject_GetAttrString(_pymsg, "state");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->state = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // num_master
    PyObject * field = PyObject_GetAttrString(_pymsg, "num_master");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->num_master = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // gdop
    PyObject * field = PyObject_GetAttrString(_pymsg, "gdop");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->gdop = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pdop
    PyObject * field = PyObject_GetAttrString(_pymsg, "pdop");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pdop = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // hdop
    PyObject * field = PyObject_GetAttrString(_pymsg, "hdop");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->hdop = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // htdop
    PyObject * field = PyObject_GetAttrString(_pymsg, "htdop");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->htdop = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // tdop
    PyObject * field = PyObject_GetAttrString(_pymsg, "tdop");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->tdop = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // num_reserve
    PyObject * field = PyObject_GetAttrString(_pymsg, "num_reserve");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->num_reserve = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * imu_msgs__msg__gnss__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Gnss */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("imu_msgs.msg._gnss");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Gnss");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  imu_msgs__msg__Gnss * ros_message = (imu_msgs__msg__Gnss *)raw_ros_message;
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
  {  // lon_sigma
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lon_sigma);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lon_sigma", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
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
  {  // lat_sigma
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lat_sigma);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lat_sigma", field);
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
  {  // alt_sigma
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->alt_sigma);
    {
      int rc = PyObject_SetAttrString(_pymessage, "alt_sigma", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gps_fix
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->gps_fix);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gps_fix", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rtk_age
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->rtk_age);
    {
      int rc = PyObject_SetAttrString(_pymessage, "rtk_age", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flags_pos
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->flags_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flags_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flags_vel
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->flags_vel);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flags_vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flags_attitude
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->flags_attitude);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flags_attitude", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flags_time
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->flags_time);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flags_time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // hor_vel
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->hor_vel);
    {
      int rc = PyObject_SetAttrString(_pymessage, "hor_vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // track_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->track_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "track_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ver_vel
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ver_vel);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ver_vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // latency_vel
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->latency_vel);
    {
      int rc = PyObject_SetAttrString(_pymessage, "latency_vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // base_length
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->base_length);
    {
      int rc = PyObject_SetAttrString(_pymessage, "base_length", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw_sigma
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw_sigma);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw_sigma", field);
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
  {  // pitch_sigma
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pitch_sigma);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pitch_sigma", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // utc_time
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->utc_time.data,
      strlen(ros_message->utc_time.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "utc_time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ts_pos
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ts_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ts_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ts_vel
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ts_vel);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ts_vel", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ts_heading
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ts_heading);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ts_heading", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // state
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->state);
    {
      int rc = PyObject_SetAttrString(_pymessage, "state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // num_master
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->num_master);
    {
      int rc = PyObject_SetAttrString(_pymessage, "num_master", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gdop
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->gdop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gdop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pdop
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pdop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pdop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // hdop
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->hdop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "hdop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // htdop
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->htdop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "htdop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tdop
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->tdop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tdop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // num_reserve
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->num_reserve);
    {
      int rc = PyObject_SetAttrString(_pymessage, "num_reserve", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
