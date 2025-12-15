# generated from rosidl_generator_py/resource/_idl.py.em
# with input from imu_msgs:msg/ImuInitial.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ImuInitial(type):
    """Metaclass of message 'ImuInitial'."""

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
                'imu_msgs.msg.ImuInitial')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__imu_initial
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__imu_initial
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__imu_initial
            cls._TYPE_SUPPORT = module.type_support_msg__msg__imu_initial
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__imu_initial

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


class ImuInitial(metaclass=Metaclass_ImuInitial):
    """Message class 'ImuInitial'."""

    __slots__ = [
        '_header',
        '_gx',
        '_gy',
        '_gz',
        '_ax',
        '_ay',
        '_az',
        '_temperature',
        '_imu_time_stamp',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'gx': 'float',
        'gy': 'float',
        'gz': 'float',
        'ax': 'float',
        'ay': 'float',
        'az': 'float',
        'temperature': 'float',
        'imu_time_stamp': 'double',
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
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.gx = kwargs.get('gx', float())
        self.gy = kwargs.get('gy', float())
        self.gz = kwargs.get('gz', float())
        self.ax = kwargs.get('ax', float())
        self.ay = kwargs.get('ay', float())
        self.az = kwargs.get('az', float())
        self.temperature = kwargs.get('temperature', float())
        self.imu_time_stamp = kwargs.get('imu_time_stamp', float())

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
        if self.imu_time_stamp != other.imu_time_stamp:
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
    def imu_time_stamp(self):
        """Message field 'imu_time_stamp'."""
        return self._imu_time_stamp

    @imu_time_stamp.setter
    def imu_time_stamp(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'imu_time_stamp' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'imu_time_stamp' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._imu_time_stamp = value
