# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class DigitalTwinsSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the SKU."""

    F1 = "F1"


class EndpointProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state."""

    PROVISIONING = "Provisioning"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class EndpointType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Digital Twins endpoint."""

    EVENT_HUB = "EventHub"
    EVENT_GRID = "EventGrid"
    SERVICE_BUS = "ServiceBus"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state."""

    PROVISIONING = "Provisioning"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class Reason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Message providing the reason why the given name is invalid."""

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"
