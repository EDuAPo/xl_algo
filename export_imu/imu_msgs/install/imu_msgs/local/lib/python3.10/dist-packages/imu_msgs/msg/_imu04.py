# generated from rosidl_generator_py/resource/_idl.py.em
# with input from imu_msgs:msg/Imu04.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# Member 'gps_message'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Imu04(type):
    """Metaclass of message 'Imu04'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('imu_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'imu_msgs.msg.Imu04')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__imu04
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__imu04
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__imu04
            cls._TYPE_SUPPORT = module.type_support_msg__msg__imu04
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__imu04

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Imu04(metaclass=Metaclass_Imu04):
    """Message class 'Imu04'."""

    __slots__ = [
        '_header',
        '_roll',
        '_pitch',
        '_yaw',
        '_gx',
        '_gy',
        '_gz',
        '_ax',
        '_ay',
        '_az',
        '_temperature',
        '_time',
        '_gps_message',
        '_gps_heading_status',
        '_ptype',
        '_pdata',
        '_ver_pos',
        '_ver_vel',
        '_info_byte',
        '_msg_type',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'roll': 'float',
        'pitch': 'float',
        'yaw': 'float',
        'gx': 'float',
        'gy': 'float',
        'gz': 'float',
        'ax': 'float',
        'ay': 'float',
        'az': 'float',
        'temperature': 'float',
        'time': 'float',
        'gps_message': 'uint8[14]',
        'gps_heading_status': 'uint8',
        'ptype': 'uint8',
        'pdata': 'uint16',
        'ver_pos': 'float',
        'ver_vel': 'float',
        'info_byte': 'uint16',
        'msg_type': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('uint8'), 14),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.roll = kwargs.get('roll', float())
        self.pitch = kwargs.get('pitch', float())
        self.yaw = kwargs.get('yaw', float())
        self.gx = kwargs.get('gx', float())
        self.gy = kwargs.get('gy', float())
        self.gz = kwargs.get('gz', float())
        self.ax = kwargs.get('ax', float())
        self.ay = kwargs.get('ay', float())
        self.az = kwargs.get('az', float())
        self.temperature = kwargs.get('temperature', float())
        self.time = kwargs.get('time', float())
        if 'gps_message' not in kwargs:
            self.gps_message = numpy.zeros(14, dtype=numpy.uint8)
        else:
            self.gps_message = numpy.array(kwargs.get('gps_message'), dtype=numpy.uint8)
            assert self.gps_message.shape == (14, )
        self.gps_heading_status = kwargs.get('gps_heading_status', int())
        self.ptype = kwargs.get('ptype', int())
        self.pdata = kwargs.get('pdata', int())
        self.ver_pos = kwargs.get('ver_pos', float())
        self.ver_vel = kwargs.get('ver_vel', float())
        self.info_byte = kwargs.get('info_byte', int())
        self.msg_type = kwargs.get('msg_type', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.roll != other.roll:
            return False
        if self.pitch != other.pitch:
            return False
        if self.yaw != other.yaw:
            return False
        if self.gx != other.gx:
            return False
        if self.gy != other.gy:
            return False
        if self.gz != other.gz:
            return False
        if self.ax != other.ax:
            return False
        if self.ay != other.ay:
            return False
        if self.az != other.az:
            return False
        if self.temperature != other.temperature:
            return False
        if self.time != other.time:
            return False
        if any(self.gps_message != other.gps_message):
            return False
        if self.gps_heading_status != other.gps_heading_status:
            return False
        if self.ptype != other.ptype:
            return False
        if self.pdata != other.pdata:
            return False
        if self.ver_pos != other.ver_pos:
            return False
        if self.ver_vel != other.ver_vel:
            return False
        if self.info_byte != other.info_byte:
            return False
        if self.msg_type != other.msg_type:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def roll(self):
        """Message field 'roll'."""
        return self._roll

    @roll.setter
    def roll(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'roll' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'roll' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._roll = value

    @builtins.property
    def pitch(self):
        """Message field 'pitch'."""
        return self._pitch

    @pitch.setter
    def pitch(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pitch' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pitch' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pitch = value

    @builtins.property
    def yaw(self):
        """Message field 'yaw'."""
        return self._yaw

    @yaw.setter
    def yaw(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw = value

    @builtins.property
    def gx(self):
        """Message field 'gx'."""
        return self._gx

    @gx.setter
    def gx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gx' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'gx' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._gx = value

    @builtins.property
    def gy(self):
        """Message field 'gy'."""
        return self._gy

    @gy.setter
    def gy(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gy' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'gy' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._gy = value

    @builtins.property
    def gz(self):
        """Message field 'gz'."""
        return self._gz

    @gz.setter
    def gz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gz' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'gz' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._gz = value

    @builtins.property
    def ax(self):
        """Message field 'ax'."""
        return self._ax

    @ax.setter
    def ax(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ax' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ax' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ax = value

    @builtins.property
    def ay(self):
        """Message field 'ay'."""
        return self._ay

    @ay.setter
    def ay(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ay' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ay' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ay = value

    @builtins.property
    def az(self):
        """Message field 'az'."""
        return self._az

    @az.setter
    def az(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'az' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'az' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._az = value

    @builtins.property
    def temperature(self):
        """Message field 'temperature'."""
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'temperature' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'temperature' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._temperature = value

    @builtins.property
    def time(self):
        """Message field 'time'."""
        return self._time

    @time.setter
    def time(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'time' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._time = value

    @builtins.property
    def gps_message(self):
        """Message field 'gps_message'."""
        return self._gps_message

    @gps_message.setter
    def gps_message(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.uint8, \
                "The 'gps_message' numpy.ndarray() must have the dtype of 'numpy.uint8'"
            assert value.size == 14, \
                "The 'gps_message' numpy.ndarray() must have a size of 14"
            self._gps_message = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 14 and
                 all(isinstance(v, int) for v in value) and
                 all(val >= 0 and val < 256 for val in value)), \
                "The 'gps_message' field must be a set or sequence with length 14 and each value of type 'int' and each unsigned integer in [0, 255]"
        self._gps_message = numpy.array(value, dtype=numpy.uint8)

    @builtins.property
    def gps_heading_status(self):
        """Message field 'gps_heading_status'."""
        return self._gps_heading_status

    @gps_heading_status.setter
    def gps_heading_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'gps_heading_status' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'gps_heading_status' field must be an unsigned integer in [0, 255]"
        self._gps_heading_status = value

    @builtins.property
    def ptype(self):
        """Message field 'ptype'."""
        return self._ptype

    @ptype.setter
    def ptype(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'ptype' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'ptype' field must be an unsigned integer in [0, 255]"
        self._ptype = value

    @builtins.property
    def pdata(self):
        """Message field 'pdata'."""
        return self._pdata

    @pdata.setter
    def pdata(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'pdata' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'pdata' field must be an unsigned integer in [0, 65535]"
        self._pdata = value

    @builtins.property
    def ver_pos(self):
        """Message field 'ver_pos'."""
        return self._ver_pos

    @ver_pos.setter
    def ver_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ver_pos' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ver_pos' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ver_pos = value

    @builtins.property
    def ver_vel(self):
        """Message field 'ver_vel'."""
        return self._ver_vel

    @ver_vel.setter
    def ver_vel(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ver_vel' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ver_vel' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ver_vel = value

    @builtins.property
    def info_byte(self):
        """Message field 'info_byte'."""
        return self._info_byte

    @info_byte.setter
    def info_byte(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'info_byte' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'info_byte' field must be an unsigned integer in [0, 65535]"
        self._info_byte = value

    @builtins.property
    def msg_type(self):
        """Message field 'msg_type'."""
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'msg_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'msg_type' field must be an unsigned integer in [0, 255]"
        self._msg_type = value
