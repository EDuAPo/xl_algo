# generated from rosidl_generator_py/resource/_idl.py.em
# with input from imu_msgs:msg/Odom.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Odom(type):
    """Metaclass of message 'Odom'."""

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
                'imu_msgs.msg.Odom')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__odom
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__odom
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__odom
            cls._TYPE_SUPPORT = module.type_support_msg__msg__odom
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__odom

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


class Odom(metaclass=Metaclass_Odom):
    """Message class 'Odom'."""

    __slots__ = [
        '_header',
        '_q0_w',
        '_q1_x',
        '_q2_y',
        '_q3_z',
        '_pos_x',
        '_pos_y',
        '_pos_z',
        '_vel_x',
        '_vel_y',
        '_vel_z',
        '_vel',
        '_ang_vel_x',
        '_ang_vel_y',
        '_ang_vel_z',
        '_acc_x',
        '_acc_y',
        '_acc_z',
        '_status',
        '_sensor_status',
        '_pos_x_std',
        '_pos_y_std',
        '_pos_z_std',
        '_vel_x_std',
        '_vel_y_std',
        '_vel_z_std',
        '_roll_std',
        '_pitch_std',
        '_yaw_std',
        '_tow_ms',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'q0_w': 'float',
        'q1_x': 'float',
        'q2_y': 'float',
        'q3_z': 'float',
        'pos_x': 'float',
        'pos_y': 'float',
        'pos_z': 'float',
        'vel_x': 'float',
        'vel_y': 'float',
        'vel_z': 'float',
        'vel': 'float',
        'ang_vel_x': 'float',
        'ang_vel_y': 'float',
        'ang_vel_z': 'float',
        'acc_x': 'float',
        'acc_y': 'float',
        'acc_z': 'float',
        'status': 'uint8',
        'sensor_status': 'uint32',
        'pos_x_std': 'float',
        'pos_y_std': 'float',
        'pos_z_std': 'float',
        'vel_x_std': 'float',
        'vel_y_std': 'float',
        'vel_z_std': 'float',
        'roll_std': 'float',
        'pitch_std': 'float',
        'yaw_std': 'float',
        'tow_ms': 'uint32',
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
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.q0_w = kwargs.get('q0_w', float())
        self.q1_x = kwargs.get('q1_x', float())
        self.q2_y = kwargs.get('q2_y', float())
        self.q3_z = kwargs.get('q3_z', float())
        self.pos_x = kwargs.get('pos_x', float())
        self.pos_y = kwargs.get('pos_y', float())
        self.pos_z = kwargs.get('pos_z', float())
        self.vel_x = kwargs.get('vel_x', float())
        self.vel_y = kwargs.get('vel_y', float())
        self.vel_z = kwargs.get('vel_z', float())
        self.vel = kwargs.get('vel', float())
        self.ang_vel_x = kwargs.get('ang_vel_x', float())
        self.ang_vel_y = kwargs.get('ang_vel_y', float())
        self.ang_vel_z = kwargs.get('ang_vel_z', float())
        self.acc_x = kwargs.get('acc_x', float())
        self.acc_y = kwargs.get('acc_y', float())
        self.acc_z = kwargs.get('acc_z', float())
        self.status = kwargs.get('status', int())
        self.sensor_status = kwargs.get('sensor_status', int())
        self.pos_x_std = kwargs.get('pos_x_std', float())
        self.pos_y_std = kwargs.get('pos_y_std', float())
        self.pos_z_std = kwargs.get('pos_z_std', float())
        self.vel_x_std = kwargs.get('vel_x_std', float())
        self.vel_y_std = kwargs.get('vel_y_std', float())
        self.vel_z_std = kwargs.get('vel_z_std', float())
        self.roll_std = kwargs.get('roll_std', float())
        self.pitch_std = kwargs.get('pitch_std', float())
        self.yaw_std = kwargs.get('yaw_std', float())
        self.tow_ms = kwargs.get('tow_ms', int())

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
        if self.q0_w != other.q0_w:
            return False
        if self.q1_x != other.q1_x:
            return False
        if self.q2_y != other.q2_y:
            return False
        if self.q3_z != other.q3_z:
            return False
        if self.pos_x != other.pos_x:
            return False
        if self.pos_y != other.pos_y:
            return False
        if self.pos_z != other.pos_z:
            return False
        if self.vel_x != other.vel_x:
            return False
        if self.vel_y != other.vel_y:
            return False
        if self.vel_z != other.vel_z:
            return False
        if self.vel != other.vel:
            return False
        if self.ang_vel_x != other.ang_vel_x:
            return False
        if self.ang_vel_y != other.ang_vel_y:
            return False
        if self.ang_vel_z != other.ang_vel_z:
            return False
        if self.acc_x != other.acc_x:
            return False
        if self.acc_y != other.acc_y:
            return False
        if self.acc_z != other.acc_z:
            return False
        if self.status != other.status:
            return False
        if self.sensor_status != other.sensor_status:
            return False
        if self.pos_x_std != other.pos_x_std:
            return False
        if self.pos_y_std != other.pos_y_std:
            return False
        if self.pos_z_std != other.pos_z_std:
            return False
        if self.vel_x_std != other.vel_x_std:
            return False
        if self.vel_y_std != other.vel_y_std:
            return False
        if self.vel_z_std != other.vel_z_std:
            return False
        if self.roll_std != other.roll_std:
            return False
        if self.pitch_std != other.pitch_std:
            return False
        if self.yaw_std != other.yaw_std:
            return False
        if self.tow_ms != other.tow_ms:
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
    def q0_w(self):
        """Message field 'q0_w'."""
        return self._q0_w

    @q0_w.setter
    def q0_w(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'q0_w' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'q0_w' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._q0_w = value

    @builtins.property
    def q1_x(self):
        """Message field 'q1_x'."""
        return self._q1_x

    @q1_x.setter
    def q1_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'q1_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'q1_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._q1_x = value

    @builtins.property
    def q2_y(self):
        """Message field 'q2_y'."""
        return self._q2_y

    @q2_y.setter
    def q2_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'q2_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'q2_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._q2_y = value

    @builtins.property
    def q3_z(self):
        """Message field 'q3_z'."""
        return self._q3_z

    @q3_z.setter
    def q3_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'q3_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'q3_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._q3_z = value

    @builtins.property
    def pos_x(self):
        """Message field 'pos_x'."""
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pos_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pos_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pos_x = value

    @builtins.property
    def pos_y(self):
        """Message field 'pos_y'."""
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pos_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pos_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pos_y = value

    @builtins.property
    def pos_z(self):
        """Message field 'pos_z'."""
        return self._pos_z

    @pos_z.setter
    def pos_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pos_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pos_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pos_z = value

    @builtins.property
    def vel_x(self):
        """Message field 'vel_x'."""
        return self._vel_x

    @vel_x.setter
    def vel_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vel_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'vel_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._vel_x = value

    @builtins.property
    def vel_y(self):
        """Message field 'vel_y'."""
        return self._vel_y

    @vel_y.setter
    def vel_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vel_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'vel_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._vel_y = value

    @builtins.property
    def vel_z(self):
        """Message field 'vel_z'."""
        return self._vel_z

    @vel_z.setter
    def vel_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vel_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'vel_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._vel_z = value

    @builtins.property
    def vel(self):
        """Message field 'vel'."""
        return self._vel

    @vel.setter
    def vel(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vel' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'vel' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._vel = value

    @builtins.property
    def ang_vel_x(self):
        """Message field 'ang_vel_x'."""
        return self._ang_vel_x

    @ang_vel_x.setter
    def ang_vel_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ang_vel_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ang_vel_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ang_vel_x = value

    @builtins.property
    def ang_vel_y(self):
        """Message field 'ang_vel_y'."""
        return self._ang_vel_y

    @ang_vel_y.setter
    def ang_vel_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ang_vel_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ang_vel_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ang_vel_y = value

    @builtins.property
    def ang_vel_z(self):
        """Message field 'ang_vel_z'."""
        return self._ang_vel_z

    @ang_vel_z.setter
    def ang_vel_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ang_vel_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ang_vel_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ang_vel_z = value

    @builtins.property
    def acc_x(self):
        """Message field 'acc_x'."""
        return self._acc_x

    @acc_x.setter
    def acc_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'acc_x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'acc_x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._acc_x = value

    @builtins.property
    def acc_y(self):
        """Message field 'acc_y'."""
        return self._acc_y

    @acc_y.setter
    def acc_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'acc_y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'acc_y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._acc_y = value

    @builtins.property
    def acc_z(self):
        """Message field 'acc_z'."""
        return self._acc_z

    @acc_z.setter
    def acc_z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'acc_z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'acc_z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._acc_z = value

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'status' field must be an unsigned integer in [0, 255]"
        self._status = value

    @builtins.property
    def sensor_status(self):
        """Message field 'sensor_status'."""
        return self._sensor_status

    @sensor_status.setter
    def sensor_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'sensor_status' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'sensor_status' field must be an unsigned integer in [0, 4294967295]"
        self._sensor_status = value

    @builtins.property
    def pos_x_std(self):
        """Message field 'pos_x_std'."""
        return self._pos_x_std

    @pos_x_std.setter
    def pos_x_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pos_x_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pos_x_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pos_x_std = value

    @builtins.property
    def pos_y_std(self):
        """Message field 'pos_y_std'."""
        return self._pos_y_std

    @pos_y_std.setter
    def pos_y_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pos_y_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pos_y_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pos_y_std = value

    @builtins.property
    def pos_z_std(self):
        """Message field 'pos_z_std'."""
        return self._pos_z_std

    @pos_z_std.setter
    def pos_z_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pos_z_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pos_z_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pos_z_std = value

    @builtins.property
    def vel_x_std(self):
        """Message field 'vel_x_std'."""
        return self._vel_x_std

    @vel_x_std.setter
    def vel_x_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vel_x_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'vel_x_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._vel_x_std = value

    @builtins.property
    def vel_y_std(self):
        """Message field 'vel_y_std'."""
        return self._vel_y_std

    @vel_y_std.setter
    def vel_y_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vel_y_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'vel_y_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._vel_y_std = value

    @builtins.property
    def vel_z_std(self):
        """Message field 'vel_z_std'."""
        return self._vel_z_std

    @vel_z_std.setter
    def vel_z_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vel_z_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'vel_z_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._vel_z_std = value

    @builtins.property
    def roll_std(self):
        """Message field 'roll_std'."""
        return self._roll_std

    @roll_std.setter
    def roll_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'roll_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'roll_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._roll_std = value

    @builtins.property
    def pitch_std(self):
        """Message field 'pitch_std'."""
        return self._pitch_std

    @pitch_std.setter
    def pitch_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pitch_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pitch_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pitch_std = value

    @builtins.property
    def yaw_std(self):
        """Message field 'yaw_std'."""
        return self._yaw_std

    @yaw_std.setter
    def yaw_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw_std = value

    @builtins.property
    def tow_ms(self):
        """Message field 'tow_ms'."""
        return self._tow_ms

    @tow_ms.setter
    def tow_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'tow_ms' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'tow_ms' field must be an unsigned integer in [0, 4294967295]"
        self._tow_ms = value
