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


class AllocationState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Allocation state of the compute. Possible values are: steady - Indicates that the compute is
    not resizing. There are no changes to the number of compute nodes in the compute in progress. A
    compute enters this state when it is created and when no operations are being performed on the
    compute to change the number of compute nodes. resizing - Indicates that the compute is
    resizing; that is, compute nodes are being added to or removed from the compute.
    """

    STEADY = "Steady"
    RESIZING = "Resizing"

class ApplicationSharingPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Policy for sharing applications on this compute instance among users of parent workspace. If
    Personal, only the creator can access applications on this compute instance. When Shared, any
    workspace user can access applications on this instance depending on his/her assigned role.
    """

    PERSONAL = "Personal"
    SHARED = "Shared"

class BillingCurrency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Three lettered code specifying the currency of the VM price. Example: USD
    """

    USD = "USD"

class ComputeInstanceState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Current state of a ComputeInstance.
    """

    CREATING = "Creating"
    CREATE_FAILED = "CreateFailed"
    DELETING = "Deleting"
    RUNNING = "Running"
    RESTARTING = "Restarting"
    JOB_RUNNING = "JobRunning"
    SETTING_UP = "SettingUp"
    SETUP_FAILED = "SetupFailed"
    STARTING = "Starting"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    USER_SETTING_UP = "UserSettingUp"
    USER_SETUP_FAILED = "UserSetupFailed"
    UNKNOWN = "Unknown"
    UNUSABLE = "Unusable"

class ComputeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of compute
    """

    AKS = "AKS"
    AML_COMPUTE = "AmlCompute"
    COMPUTE_INSTANCE = "ComputeInstance"
    DATA_FACTORY = "DataFactory"
    VIRTUAL_MACHINE = "VirtualMachine"
    HD_INSIGHT = "HDInsight"
    DATABRICKS = "Databricks"
    DATA_LAKE_ANALYTICS = "DataLakeAnalytics"

class EncryptionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether or not the encryption is enabled for the workspace.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class NodeState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of the compute node. Values are idle, running, preparing, unusable, leaving and
    preempted.
    """

    IDLE = "idle"
    RUNNING = "running"
    PREPARING = "preparing"
    UNUSABLE = "unusable"
    LEAVING = "leaving"
    PREEMPTED = "preempted"

class OperationName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of the last operation.
    """

    CREATE = "Create"
    START = "Start"
    STOP = "Stop"
    RESTART = "Restart"
    REIMAGE = "Reimage"
    DELETE = "Delete"

class OperationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Operation status.
    """

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    CREATE_FAILED = "CreateFailed"
    START_FAILED = "StartFailed"
    STOP_FAILED = "StopFailed"
    RESTART_FAILED = "RestartFailed"
    REIMAGE_FAILED = "ReimageFailed"
    DELETE_FAILED = "DeleteFailed"

class PrivateEndpointConnectionProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"
    TIMEOUT = "Timeout"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current deployment state of workspace resource. The provisioningState is to indicate states
    for resource provisioning.
    """

    UNKNOWN = "Unknown"
    UPDATING = "Updating"
    CREATING = "Creating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class QuotaUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """An enum describing the unit of quota measurement.
    """

    COUNT = "Count"

class ReasonCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason for the restriction.
    """

    NOT_SPECIFIED = "NotSpecified"
    NOT_AVAILABLE_FOR_REGION = "NotAvailableForRegion"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"

class RemoteLoginPortPublicAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh
    port is closed on all nodes of the cluster. Enabled - Indicates that the public ssh port is
    open on all nodes of the cluster. NotSpecified - Indicates that the public ssh port is closed
    on all nodes of the cluster if VNet is defined, else is open all public nodes. It can be
    default only during cluster creation time, after creation it will be either enabled or
    disabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    NOT_SPECIFIED = "NotSpecified"

class ResourceIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The identity type.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    NONE = "None"

class SshPublicAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh
    port is closed on this instance. Enabled - Indicates that the public ssh port is open and
    accessible according to the VNet/subnet policy if applicable.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class SslConfigurationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enable or disable ssl for scoring
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of update workspace quota.
    """

    UNDEFINED = "Undefined"
    SUCCESS = "Success"
    FAILURE = "Failure"
    INVALID_QUOTA_BELOW_CLUSTER_MINIMUM = "InvalidQuotaBelowClusterMinimum"
    INVALID_QUOTA_EXCEEDS_SUBSCRIPTION_LIMIT = "InvalidQuotaExceedsSubscriptionLimit"
    INVALID_VM_FAMILY_NAME = "InvalidVMFamilyName"
    OPERATION_NOT_SUPPORTED_FOR_SKU = "OperationNotSupportedForSku"
    OPERATION_NOT_ENABLED_FOR_REGION = "OperationNotEnabledForRegion"

class UnderlyingResourceAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DELETE = "Delete"
    DETACH = "Detach"

class UnitOfMeasure(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of time measurement for the specified VM price. Example: OneHour
    """

    ONE_HOUR = "OneHour"

class UsageUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """An enum describing the unit of usage measurement.
    """

    COUNT = "Count"

class VMPriceOSType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Operating system type used by the VM.
    """

    LINUX = "Linux"
    WINDOWS = "Windows"

class VmPriority(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Virtual Machine priority
    """

    DEDICATED = "Dedicated"
    LOW_PRIORITY = "LowPriority"

class VMTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the VM.
    """

    STANDARD = "Standard"
    LOW_PRIORITY = "LowPriority"
    SPOT = "Spot"
