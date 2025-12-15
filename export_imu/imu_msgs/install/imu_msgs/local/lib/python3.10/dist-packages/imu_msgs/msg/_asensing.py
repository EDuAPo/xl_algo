# generated from rosidl_generator_py/resource/_idl.py.em
# with input from imu_msgs:msg/ASENSING.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ASENSING(type):
    """Metaclass of message 'ASENSING'."""

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
                'imu_msgs.msg.ASENSING')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__asensing
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__asensing
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__asensing
            cls._TYPE_SUPPORT = module.type_support_msg__msg__asensing
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__asensing

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ASENSING(metaclass=Metaclass_ASENSING):
    """Message class 'ASENSING'."""

    __slots__ = [
        '_latitude',
        '_longitude',
        '_altitude',
        '_north_velocity',
        '_east_velocity',
        '_ground_velocity',
        '_roll',
        '_pitch',
        '_azimuth',
        '_x_angular_velocity',
        '_y_angular_velocity',
        '_z_angular_velocity',
        '_x_acc',
        '_y_acc',
        '_z_acc',
        '_latitude_std',
        '_longitude_std',
        '_altitude_std',
        '_north_velocity_std',
        '_east_velocity_std',
        '_ground_velocity_std',
        '_roll_std',
        '_pitch_std',
        '_azimuth_std',
        '_ins_status',
        '_position_type',
        '_sec_of_week',
        '_gps_week_number',
        '_temperature',
        '_wheel_speed_status',
        '_heading_type',
        '_numsv',
        '_is_available',
        '_utm_x',
        '_utm_y',
    ]

    _fields_and_field_types = {
        'latitude': 'double',
        'longitude': 'double',
        'altitude': 'double',
        'north_velocity': 'double',
        'east_velocity': 'double',
        'ground_velocity': 'double',
        'roll': 'double',
        'pitch': 'double',
        'azimuth': 'double',
        'x_angular_velocity': 'double',
        'y_angular_velocity': 'double',
        'z_angular_velocity': 'double',
        'x_acc': 'double',
        'y_acc': 'double',
        'z_acc': 'double',
        'latitude_std': 'float',
        'longitude_std': 'float',
        'altitude_std': 'float',
        'north_velocity_std': 'float',
        'east_velocity_std': 'float',
        'ground_velocity_std': 'float',
        'roll_std': 'float',
        'pitch_std': 'float',
        'azimuth_std': 'float',
        'ins_status': 'uint32',
        'position_type': 'uint32',
        'sec_of_week': 'double',
        'gps_week_number': 'double',
        'temperature': 'float',
        'wheel_speed_status': 'uint32',
        'heading_type': 'uint32',
        'numsv': 'uint32',
        'is_available': 'boolean',
        'utm_x': 'double',
        'utm_y': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
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
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.latitude = kwargs.get('latitude', float())
        self.longitude = kwargs.get('longitude', float())
        self.altitude = kwargs.get('altitude', float())
        self.north_velocity = kwargs.get('north_velocity', float())
        self.east_velocity = kwargs.get('east_velocity', float())
        self.ground_velocity = kwargs.get('ground_velocity', float())
        self.roll = kwargs.get('roll', float())
        self.pitch = kwargs.get('pitch', float())
        self.azimuth = kwargs.get('azimuth', float())
        self.x_angular_velocity = kwargs.get('x_angular_velocity', float())
        self.y_angular_velocity = kwargs.get('y_angular_velocity', float())
        self.z_angular_velocity = kwargs.get('z_angular_velocity', float())
        self.x_acc = kwargs.get('x_acc', float())
        self.y_acc = kwargs.get('y_acc', float())
        self.z_acc = kwargs.get('z_acc', float())
        self.latitude_std = kwargs.get('latitude_std', float())
        self.longitude_std = kwargs.get('longitude_std', float())
        self.altitude_std = kwargs.get('altitude_std', float())
        self.north_velocity_std = kwargs.get('north_velocity_std', float())
        self.east_velocity_std = kwargs.get('east_velocity_std', float())
        self.ground_velocity_std = kwargs.get('ground_velocity_std', float())
        self.roll_std = kwargs.get('roll_std', float())
        self.pitch_std = kwargs.get('pitch_std', float())
        self.azimuth_std = kwargs.get('azimuth_std', float())
        self.ins_status = kwargs.get('ins_status', int())
        self.position_type = kwargs.get('position_type', int())
        self.sec_of_week = kwargs.get('sec_of_week', float())
        self.gps_week_number = kwargs.get('gps_week_number', float())
        self.temperature = kwargs.get('temperature', float())
        self.wheel_speed_status = kwargs.get('wheel_speed_status', int())
        self.heading_type = kwargs.get('heading_type', int())
        self.numsv = kwargs.get('numsv', int())
        self.is_available = kwargs.get('is_available', bool())
        self.utm_x = kwargs.get('utm_x', float())
        self.utm_y = kwargs.get('utm_y', float())

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
        if self.latitude != other.latitude:
            return False
        if self.longitude != other.longitude:
            return False
        if self.altitude != other.altitude:
            return False
        if self.north_velocity != other.north_velocity:
            return False
        if self.east_velocity != other.east_velocity:
            return False
        if self.ground_velocity != other.ground_velocity:
            return False
        if self.roll != other.roll:
            return False
        if self.pitch != other.pitch:
            return False
        if self.azimuth != other.azimuth:
            return False
        if self.x_angular_velocity != other.x_angular_velocity:
            return False
        if self.y_angular_velocity != other.y_angular_velocity:
            return False
        if self.z_angular_velocity != other.z_angular_velocity:
            return False
        if self.x_acc != other.x_acc:
            return False
        if self.y_acc != other.y_acc:
            return False
        if self.z_acc != other.z_acc:
            return False
        if self.latitude_std != other.latitude_std:
            return False
        if self.longitude_std != other.longitude_std:
            return False
        if self.altitude_std != other.altitude_std:
            return False
        if self.north_velocity_std != other.north_velocity_std:
            return False
        if self.east_velocity_std != other.east_velocity_std:
            return False
        if self.ground_velocity_std != other.ground_velocity_std:
            return False
        if self.roll_std != other.roll_std:
            return False
        if self.pitch_std != other.pitch_std:
            return False
        if self.azimuth_std != other.azimuth_std:
            return False
        if self.ins_status != other.ins_status:
            return False
        if self.position_type != other.position_type:
            return False
        if self.sec_of_week != other.sec_of_week:
            return False
        if self.gps_week_number != other.gps_week_number:
            return False
        if self.temperature != other.temperature:
            return False
        if self.wheel_speed_status != other.wheel_speed_status:
            return False
        if self.heading_type != other.heading_type:
            return False
        if self.numsv != other.numsv:
            return False
        if self.is_available != other.is_available:
            return False
        if self.utm_x != other.utm_x:
            return False
        if self.utm_y != other.utm_y:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def latitude(self):
        """Message field 'latitude'."""
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'latitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'latitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._latitude = value

    @builtins.property
    def longitude(self):
        """Message field 'longitude'."""
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'longitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'longitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._longitude = value

    @builtins.property
    def altitude(self):
        """Message field 'altitude'."""
        return self._altitude

    @altitude.setter
    def altitude(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'altitude' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'altitude' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._altitude = value

    @builtins.property
    def north_velocity(self):
        """Message field 'north_velocity'."""
        return self._north_velocity

    @north_velocity.setter
    def north_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'north_velocity' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'north_velocity' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._north_velocity = value

    @builtins.property
    def east_velocity(self):
        """Message field 'east_velocity'."""
        return self._east_velocity

    @east_velocity.setter
    def east_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'east_velocity' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'east_velocity' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._east_velocity = value

    @builtins.property
    def ground_velocity(self):
        """Message field 'ground_velocity'."""
        return self._ground_velocity

    @ground_velocity.setter
    def ground_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ground_velocity' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ground_velocity' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ground_velocity = value

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
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'roll' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
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
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'pitch' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._pitch = value

    @builtins.property
    def azimuth(self):
        """Message field 'azimuth'."""
        return self._azimuth

    @azimuth.setter
    def azimuth(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'azimuth' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'azimuth' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._azimuth = value

    @builtins.property
    def x_angular_velocity(self):
        """Message field 'x_angular_velocity'."""
        return self._x_angular_velocity

    @x_angular_velocity.setter
    def x_angular_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_angular_velocity' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_angular_velocity' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_angular_velocity = value

    @builtins.property
    def y_angular_velocity(self):
        """Message field 'y_angular_velocity'."""
        return self._y_angular_velocity

    @y_angular_velocity.setter
    def y_angular_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_angular_velocity' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_angular_velocity' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_angular_velocity = value

    @builtins.property
    def z_angular_velocity(self):
        """Message field 'z_angular_velocity'."""
        return self._z_angular_velocity

    @z_angular_velocity.setter
    def z_angular_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'z_angular_velocity' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'z_angular_velocity' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._z_angular_velocity = value

    @builtins.property
    def x_acc(self):
        """Message field 'x_acc'."""
        return self._x_acc

    @x_acc.setter
    def x_acc(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_acc' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_acc' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_acc = value

    @builtins.property
    def y_acc(self):
        """Message field 'y_acc'."""
        return self._y_acc

    @y_acc.setter
    def y_acc(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_acc' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_acc' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_acc = value

    @builtins.property
    def z_acc(self):
        """Message field 'z_acc'."""
        return self._z_acc

    @z_acc.setter
    def z_acc(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'z_acc' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'z_acc' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._z_acc = value

    @builtins.property
    def latitude_std(self):
        """Message field 'latitude_std'."""
        return self._latitude_std

    @latitude_std.setter
    def latitude_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'latitude_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'latitude_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._latitude_std = value

    @builtins.property
    def longitude_std(self):
        """Message field 'longitude_std'."""
        return self._longitude_std

    @longitude_std.setter
    def longitude_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'longitude_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'longitude_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._longitude_std = value

    @builtins.property
    def altitude_std(self):
        """Message field 'altitude_std'."""
        return self._altitude_std

    @altitude_std.setter
    def altitude_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'altitude_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'altitude_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._altitude_std = value

    @builtins.property
    def north_velocity_std(self):
        """Message field 'north_velocity_std'."""
        return self._north_velocity_std

    @north_velocity_std.setter
    def north_velocity_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'north_velocity_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'north_velocity_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._north_velocity_std = value

    @builtins.property
    def east_velocity_std(self):
        """Message field 'east_velocity_std'."""
        return self._east_velocity_std

    @east_velocity_std.setter
    def east_velocity_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'east_velocity_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'east_velocity_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._east_velocity_std = value

    @builtins.property
    def ground_velocity_std(self):
        """Message field 'ground_velocity_std'."""
        return self._ground_velocity_std

    @ground_velocity_std.setter
    def ground_velocity_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ground_velocity_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'ground_velocity_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._ground_velocity_std = value

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
    def azimuth_std(self):
        """Message field 'azimuth_std'."""
        return self._azimuth_std

    @azimuth_std.setter
    def azimuth_std(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'azimuth_std' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'azimuth_std' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._azimuth_std = value

    @builtins.property
    def ins_status(self):
        """Message field 'ins_status'."""
        return self._ins_status

    @ins_status.setter
    def ins_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'ins_status' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'ins_status' field must be an unsigned integer in [0, 4294967295]"
        self._ins_status = value

    @builtins.property
    def position_type(self):
        """Message field 'position_type'."""
        return self._position_type

    @position_type.setter
    def position_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'position_type' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'position_type' field must be an unsigned integer in [0, 4294967295]"
        self._position_type = value

    @builtins.property
    def sec_of_week(self):
        """Message field 'sec_of_week'."""
        return self._sec_of_week

    @sec_of_week.setter
    def sec_of_week(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'sec_of_week' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sec_of_week' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sec_of_week = value

    @builtins.property
    def gps_week_number(self):
        """Message field 'gps_week_number'."""
        return self._gps_week_number

    @gps_week_number.setter
    def gps_week_number(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gps_week_number' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'gps_week_number' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._gps_week_number = value

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
    def wheel_speed_status(self):
        """Message field 'wheel_speed_status'."""
        return self._wheel_speed_status

    @wheel_speed_status.setter
    def wheel_speed_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'wheel_speed_status' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'wheel_speed_status' field must be an unsigned integer in [0, 4294967295]"
        self._wheel_speed_status = value

    @builtins.property
    def heading_type(self):
        """Message field 'heading_type'."""
        return self._heading_type

    @heading_type.setter
    def heading_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'heading_type' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'heading_type' field must be an unsigned integer in [0, 4294967295]"
        self._heading_type = value

    @builtins.property
    def numsv(self):
        """Message field 'numsv'."""
        return self._numsv

    @numsv.setter
    def numsv(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'numsv' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'numsv' field must be an unsigned integer in [0, 4294967295]"
        self._numsv = value

    @builtins.property
    def is_available(self):
        """Message field 'is_available'."""
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_available' field must be of type 'bool'"
        self._is_available = value

    @builtins.property
    def utm_x(self):
        """Message field 'utm_x'."""
        return self._utm_x

    @utm_x.setter
    def utm_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'utm_x' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'utm_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._utm_x = value

    @builtins.property
    def utm_y(self):
        """Message field 'utm_y'."""
        return self._utm_y

    @utm_y.setter
    def utm_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'utm_y' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'utm_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._utm_y = value
