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


class IdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of managed service identity.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"

class KeyName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """key name to generate (Key1|Key2)
    """

    KEY1 = "Key1"
    KEY2 = "Key2"

class KeySource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates the possible value of keySource for Encryption
    """

    MICROSOFT_COGNITIVE_SERVICES = "Microsoft.CognitiveServices"
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"

class NetworkRuleAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The default action when no rule from ipRules and from virtualNetworkRules match. This is only
    used after the bypass property has been evaluated.
    """

    ALLOW = "Allow"
    DENY = "Deny"

class PrivateEndpointServiceConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the status of the cognitive services account at the time the operation was called.
    """

    CREATING = "Creating"
    RESOLVING_DNS = "ResolvingDNS"
    MOVING = "Moving"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class PublicNetworkAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether or not public endpoint access is allowed for this account. Value is optional but if
    passed in, must be 'Enabled' or 'Disabled'
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class QuotaUsageStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Cognitive Services account quota usage status.
    """

    INCLUDED = "Included"
    BLOCKED = "Blocked"
    IN_OVERAGE = "InOverage"
    UNKNOWN = "Unknown"

class ResourceSkuRestrictionsReasonCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason for restriction.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"

class ResourceSkuRestrictionsType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of restrictions.
    """

    LOCATION = "Location"
    ZONE = "Zone"

class SkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the sku tier. This is based on the SKU name.
    """

    FREE = "Free"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    ENTERPRISE = "Enterprise"

class UnitType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of the metric.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
    MILLISECONDS = "Milliseconds"
