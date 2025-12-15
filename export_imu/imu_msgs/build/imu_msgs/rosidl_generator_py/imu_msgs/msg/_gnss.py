# generated from rosidl_generator_py/resource/_idl.py.em
# with input from imu_msgs:msg/Gnss.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Gnss(type):
    """Metaclass of message 'Gnss'."""

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
                'imu_msgs.msg.Gnss')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__gnss
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__gnss
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__gnss
            cls._TYPE_SUPPORT = module.type_support_msg__msg__gnss
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__gnss

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


class Gnss(metaclass=Metaclass_Gnss):
    """Message class 'Gnss'."""

    __slots__ = [
        '_header',
        '_longitude',
        '_lon_sigma',
        '_latitude',
        '_lat_sigma',
        '_altitude',
        '_alt_sigma',
        '_gps_fix',
        '_rtk_age',
        '_flags_pos',
        '_flags_vel',
        '_flags_attitude',
        '_flags_time',
        '_hor_vel',
        '_track_angle',
        '_ver_vel',
        '_latency_vel',
        '_base_length',
        '_yaw',
        '_yaw_sigma',
        '_pitch',
        '_pitch_sigma',
        '_utc_time',
        '_ts_pos',
        '_ts_vel',
        '_ts_heading',
        '_state',
        '_num_master',
        '_gdop',
        '_pdop',
        '_hdop',
        '_htdop',
        '_tdop',
        '_num_reserve',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'longitude': 'double',
        'lon_sigma': 'float',
        'latitude': 'double',
        'lat_sigma': 'float',
        'altitude': 'double',
        'alt_sigma': 'float',
        'gps_fix': 'uint16',
        'rtk_age': 'uint16',
        'flags_pos': 'uint8',
        'flags_vel': 'uint8',
        'flags_attitude': 'uint8',
        'flags_time': 'uint8',
        'hor_vel': 'float',
        'track_angle': 'float',
        'ver_vel': 'float',
        'latency_vel': 'float',
        'base_length': 'float',
        'yaw': 'float',
        'yaw_sigma': 'float',
        'pitch': 'float',
        'pitch_sigma': 'float',
        'utc_time': 'string',
        'ts_pos': 'uint32',
        'ts_vel': 'uint32',
        'ts_heading': 'uint32',
        'state': 'uint8',
        'num_master': 'uint8',
        'gdop': 'float',
        'pdop': 'float',
        'hdop': 'float',
        'htdop': 'float',
        'tdop': 'float',
        'num_reserve': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.longitude = kwargs.get('longitude', float())
        self.lon_sigma = kwargs.get('lon_sigma', float())
        self.latitude = kwargs.get('latitude', float())
        self.lat_sigma = kwargs.get('lat_sigma', float())
        self.altitude = kwargs.get('altitude', float())
        self.alt_sigma = kwargs.get('alt_sigma', float())
        self.gps_fix = kwargs.get('gps_fix', int())
        self.rtk_age = kwargs.get('rtk_age', int())
        self.flags_pos = kwargs.get('flags_pos', int())
        self.flags_vel = kwargs.get('flags_vel', int())
        self.flags_attitude = kwargs.get('flags_attitude', int())
        self.flags_time = kwargs.get('flags_time', int())
        self.hor_vel = kwargs.get('hor_vel', float())
        self.track_angle = kwargs.get('track_angle', float())
        self.ver_vel = kwargs.get('ver_vel', float())
        self.latency_vel = kwargs.get('latency_vel', float())
        self.base_length = kwargs.get('base_length', float())
        self.yaw = kwargs.get('yaw', float())
        self.yaw_sigma = kwargs.get('yaw_sigma', float())
        self.pitch = kwargs.get('pitch', float())
        self.pitch_sigma = kwargs.get('pitch_sigma', float())
        self.utc_time = kwargs.get('utc_time', str())
        self.ts_pos = kwargs.get('ts_pos', int())
        self.ts_vel = kwargs.get('ts_vel', int())
        self.ts_heading = kwargs.get('ts_heading', int())
        self.state = kwargs.get('state', int())
        self.num_master = kwargs.get('num_master', int())
        self.gdop = kwargs.get('gdop', float())
        self.pdop = kwargs.get('pdop', float())
        self.hdop = kwargs.get('hdop', float())
        self.htdop = kwargs.get('htdop', float())
        self.tdop = kwargs.get('tdop', float())
        self.num_reserve = kwargs.get('num_reserve', int())

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
        if self.longitude != other.longitude:
            return False
        if self.lon_sigma != other.lon_sigma:
            return False
        if self.latitude != other.latitude:
            return False
        if self.lat_sigma != other.lat_sigma:
            return False
        if self.altitude != other.altitude:
            return False
        if self.alt_sigma != other.alt_sigma:
            return False
        if self.gps_fix != other.gps_fix:
            return False
        if self.rtk_age != other.rtk_age:
            return False
        if self.flags_pos != other.flags_pos:
            return False
        if self.flags_vel != other.flags_vel:
            return False
        if self.flags_attitude != other.flags_attitude:
            return False
        if self.flags_time != other.flags_time:
            return False
        if self.hor_vel != other.hor_vel:
            return False
        if self.track_angle != other.track_angle:
            return False
        if self.ver_vel != other.ver_vel:
            return False
        if self.latency_vel != other.latency_vel:
            return False
        if self.base_length != other.base_length:
            return False
        if self.yaw != other.yaw:
            return False
        if self.yaw_sigma != other.yaw_sigma:
            return False
        if self.pitch != other.pitch:
            return False
        if self.pitch_sigma != other.pitch_sigma:
            return False
        if self.utc_time != other.utc_time:
            return False
        if self.ts_pos != other.ts_pos:
            return False
        if self.ts_vel != other.ts_vel:
            return False
        if self.ts_heading != other.ts_heading:
            return False
        if self.state != other.state:
            return False
        if self.num_master != other.num_master:
            return False
        if self.gdop != other.gdop:
            return False
        if self.pdop != other.pdop:
            return False
        if self.hdop != other.hdop:
            return False
        if self.htdop != other.htdop:
            return False
        if self.tdop != other.tdop:
            return False
        if self.num_reserve != other.num_reserve:
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
    def lon_sigma(self):
        """Message field 'lon_sigma'."""
        return self._lon_sigma

    @lon_sigma.setter
    def lon_sigma(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lon_sigma' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'lon_sigma' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._lon_sigma = value

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
    def lat_sigma(self):
        """Message field 'lat_sigma'."""
        return self._lat_sigma

    @lat_sigma.setter
    def lat_sigma(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lat_sigma' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'lat_sigma' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._lat_sigma = value

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
    def alt_sigma(self):
        """Message field 'alt_sigma'."""
        return self._alt_sigma

    @alt_sigma.setter
    def alt_sigma(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'alt_sigma' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'alt_sigma' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._alt_sigma = value

    @builtins.property
    def gps_fix(self):
        """Message field 'gps_fix'."""
        return self._gps_fix

    @gps_fix.setter
    def gps_fix(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'gps_fix' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'gps_fix' field must be an unsigned integer in [0, 65535]"
        self._gps_fix = value

    @builtins.property
    def rtk_age(self):
        """Message field 'rtk_age'."""
        return self._rtk_age

    @rtk_age.setter
    def rtk_age(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'rtk_age' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'rtk_age' field must be an unsigned integer in [0, 65535]"
        self._rtk_age = value

    @builtins.property
    def flags_pos(self):
        """Message field 'flags_pos'."""
        return self._flags_pos

    @flags_pos.setter
    def flags_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'flags_pos' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'flags_pos' field must be an unsigned integer in [0, 255]"
        self._flags_pos = value

    @builtins.property
    def flags_vel(self):
        """Message field 'flags_vel'."""
        return self._flags_vel

    @flags_vel.setter
    def flags_vel(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'flags_vel' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'flags_vel' field must be an unsigned integer in [0, 255]"
        self._flags_vel = value

    @builtins.property
    def flags_attitude(self):
        """Message field 'flags_attitude'."""
        return self._flags_attitude

    @flags_attitude.setter
    def flags_attitude(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'flags_attitude' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'flags_attitude' field must be an unsigned integer in [0, 255]"
        self._flags_attitude = value

    @builtins.property
    def flags_time(self):
        """Message field 'flags_time'."""
        return self._flags_time

    @flags_time.setter
    def flags_time(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'flags_time' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'flags_time' field must be an unsigned integer in [0, 255]"
        self._flags_time = value

    @builtins.property
    def hor_vel(self):
        """Message field 'hor_vel'."""
        return self._hor_vel

    @hor_vel.setter
    def hor_vel(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'hor_vel' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'hor_vel' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._hor_vel = value

    @builtins.property
    def track_angle(self):
        """Message field 'track_angle'."""
        return self._track_angle

    @track_angle.setter
    def track_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'track_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'track_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._track_angle = value

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
    def latency_vel(self):
        """Message field 'latency_vel'."""
        return self._latency_vel

    @latency_vel.setter
    def latency_vel(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'latency_vel' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'latency_vel' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._latency_vel = value

    @builtins.property
    def base_length(self):
        """Message field 'base_length'."""
        return self._base_length

    @base_length.setter
    def base_length(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'base_length' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'base_length' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._base_length = value

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
    def yaw_sigma(self):
        """Message field 'yaw_sigma'."""
        return self._yaw_sigma

    @yaw_sigma.setter
    def yaw_sigma(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw_sigma' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'yaw_sigma' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._yaw_sigma = value

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
    def pitch_sigma(self):
        """Message field 'pitch_sigma'."""
        return self._pitch_sigma

    @pitch_sigma.setter
    def pitch_sigma(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pitch_sigma' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pitch_sigma' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pitch_sigma = value

    @builtins.property
    def utc_time(self):
        """Message field 'utc_time'."""
        return self._utc_time

    @utc_time.setter
    def utc_time(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'utc_time' field must be of type 'str'"
        self._utc_time = value

    @builtins.property
    def ts_pos(self):
        """Message field 'ts_pos'."""
        return self._ts_pos

    @ts_pos.setter
    def ts_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'ts_pos' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'ts_pos' field must be an unsigned integer in [0, 4294967295]"
        self._ts_pos = value

    @builtins.property
    def ts_vel(self):
        """Message field 'ts_vel'."""
        return self._ts_vel

    @ts_vel.setter
    def ts_vel(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'ts_vel' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'ts_vel' field must be an unsigned integer in [0, 4294967295]"
        self._ts_vel = value

    @builtins.property
    def ts_heading(self):
        """Message field 'ts_heading'."""
        return self._ts_heading

    @ts_heading.setter
    def ts_heading(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'ts_heading' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'ts_heading' field must be an unsigned integer in [0, 4294967295]"
        self._ts_heading = value

    @builtins.property
    def state(self):
        """Message field 'state'."""
        return self._state

    @state.setter
    def state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'state' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'state' field must be an unsigned integer in [0, 255]"
        self._state = value

    @builtins.property
    def num_master(self):
        """Message field 'num_master'."""
        return self._num_master

    @num_master.setter
    def num_master(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'num_master' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'num_master' field must be an unsigned integer in [0, 255]"
        self._num_master = value

    @builtins.property
    def gdop(self):
        """Message field 'gdop'."""
        return self._gdop

    @gdop.setter
    def gdop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gdop' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'gdop' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._gdop = value

    @builtins.property
    def pdop(self):
        """Message field 'pdop'."""
        return self._pdop

    @pdop.setter
    def pdop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pdop' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'pdop' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._pdop = value

    @builtins.property
    def hdop(self):
        """Message field 'hdop'."""
        return self._hdop

    @hdop.setter
    def hdop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'hdop' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'hdop' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._hdop = value

    @builtins.property
    def htdop(self):
        """Message field 'htdop'."""
        return self._htdop

    @htdop.setter
    def htdop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'htdop' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'htdop' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._htdop = value

    @builtins.property
    def tdop(self):
        """Message field 'tdop'."""
        return self._tdop

    @tdop.setter
    def tdop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tdop' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'tdop' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._tdop = value

    @builtins.property
    def num_reserve(self):
        """Message field 'num_reserve'."""
        return self._num_reserve

    @num_reserve.setter
    def num_reserve(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'num_reserve' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'num_reserve' field must be an unsigned integer in [0, 255]"
        self._num_reserve = value
