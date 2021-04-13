# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class DayOfWeek(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Day of the week when a cache can be patched.
    """

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    EVERYDAY = "Everyday"
    WEEKEND = "Weekend"

class DefaultName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Redis instance provisioning status.
    """

    CREATING = "Creating"
    DELETING = "Deleting"
    DISABLED = "Disabled"
    FAILED = "Failed"
    LINKING = "Linking"
    PROVISIONING = "Provisioning"
    RECOVERING_SCALE_FAILURE = "RecoveringScaleFailure"
    SCALING = "Scaling"
    SUCCEEDED = "Succeeded"
    UNLINKING = "Unlinking"
    UNPROVISIONING = "Unprovisioning"
    UPDATING = "Updating"

class RebootType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Which Redis node(s) to reboot. Depending on this value data loss is possible.
    """

    PRIMARY_NODE = "PrimaryNode"
    SECONDARY_NODE = "SecondaryNode"
    ALL_NODES = "AllNodes"

class RedisKeyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Redis access key to regenerate.
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class ReplicationRole(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Role of the linked server.
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class SkuFamily(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The SKU family to use. Valid values: (C, P). (C = Basic/Standard, P = Premium).
    """

    C = "C"
    P = "P"

class SkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Redis cache to deploy. Valid values: (Basic, Standard, Premium)
    """

    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class TlsVersion(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, '1.0',
    '1.1', '1.2')
    """

    ONE0 = "1.0"
    ONE1 = "1.1"
    ONE2 = "1.2"
