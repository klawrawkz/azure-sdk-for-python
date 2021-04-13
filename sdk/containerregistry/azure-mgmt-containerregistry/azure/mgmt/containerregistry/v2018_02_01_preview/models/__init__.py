# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Actor
    from ._models_py3 import BaseImageDependency
    from ._models_py3 import Build
    from ._models_py3 import BuildArgument
    from ._models_py3 import BuildArgumentList
    from ._models_py3 import BuildFilter
    from ._models_py3 import BuildGetLogResult
    from ._models_py3 import BuildListResult
    from ._models_py3 import BuildStep
    from ._models_py3 import BuildStepList
    from ._models_py3 import BuildStepProperties
    from ._models_py3 import BuildStepPropertiesUpdateParameters
    from ._models_py3 import BuildStepUpdateParameters
    from ._models_py3 import BuildTask
    from ._models_py3 import BuildTaskBuildRequest
    from ._models_py3 import BuildTaskFilter
    from ._models_py3 import BuildTaskListResult
    from ._models_py3 import BuildTaskUpdateParameters
    from ._models_py3 import BuildUpdateParameters
    from ._models_py3 import CallbackConfig
    from ._models_py3 import DockerBuildStep
    from ._models_py3 import DockerBuildStepUpdateParameters
    from ._models_py3 import Event
    from ._models_py3 import EventContent
    from ._models_py3 import EventInfo
    from ._models_py3 import EventListResult
    from ._models_py3 import EventRequestMessage
    from ._models_py3 import EventResponseMessage
    from ._models_py3 import GitCommitTrigger
    from ._models_py3 import IPRule
    from ._models_py3 import ImageDescriptor
    from ._models_py3 import ImageUpdateTrigger
    from ._models_py3 import ImportImageParameters
    from ._models_py3 import ImportSource
    from ._models_py3 import ImportSourceCredentials
    from ._models_py3 import NetworkRuleSet
    from ._models_py3 import OperationDefinition
    from ._models_py3 import OperationDisplayDefinition
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationMetricSpecificationDefinition
    from ._models_py3 import OperationServiceSpecificationDefinition
    from ._models_py3 import PlatformProperties
    from ._models_py3 import ProxyResource
    from ._models_py3 import QuarantinePolicy
    from ._models_py3 import QueueBuildRequest
    from ._models_py3 import QuickBuildRequest
    from ._models_py3 import RegenerateCredentialParameters
    from ._models_py3 import Registry
    from ._models_py3 import RegistryListCredentialsResult
    from ._models_py3 import RegistryListResult
    from ._models_py3 import RegistryNameCheckRequest
    from ._models_py3 import RegistryNameStatus
    from ._models_py3 import RegistryPassword
    from ._models_py3 import RegistryPolicies
    from ._models_py3 import RegistryUpdateParameters
    from ._models_py3 import RegistryUsage
    from ._models_py3 import RegistryUsageListResult
    from ._models_py3 import Replication
    from ._models_py3 import ReplicationListResult
    from ._models_py3 import ReplicationUpdateParameters
    from ._models_py3 import Request
    from ._models_py3 import Resource
    from ._models_py3 import ResourceAutoGenerated
    from ._models_py3 import Sku
    from ._models_py3 import Source
    from ._models_py3 import SourceControlAuthInfo
    from ._models_py3 import SourceRepositoryProperties
    from ._models_py3 import SourceRepositoryUpdateParameters
    from ._models_py3 import SourceUploadDefinition
    from ._models_py3 import Status
    from ._models_py3 import StorageAccountProperties
    from ._models_py3 import Target
    from ._models_py3 import TrustPolicy
    from ._models_py3 import VirtualNetworkRule
    from ._models_py3 import Webhook
    from ._models_py3 import WebhookCreateParameters
    from ._models_py3 import WebhookListResult
    from ._models_py3 import WebhookUpdateParameters
except (SyntaxError, ImportError):
    from ._models import Actor  # type: ignore
    from ._models import BaseImageDependency  # type: ignore
    from ._models import Build  # type: ignore
    from ._models import BuildArgument  # type: ignore
    from ._models import BuildArgumentList  # type: ignore
    from ._models import BuildFilter  # type: ignore
    from ._models import BuildGetLogResult  # type: ignore
    from ._models import BuildListResult  # type: ignore
    from ._models import BuildStep  # type: ignore
    from ._models import BuildStepList  # type: ignore
    from ._models import BuildStepProperties  # type: ignore
    from ._models import BuildStepPropertiesUpdateParameters  # type: ignore
    from ._models import BuildStepUpdateParameters  # type: ignore
    from ._models import BuildTask  # type: ignore
    from ._models import BuildTaskBuildRequest  # type: ignore
    from ._models import BuildTaskFilter  # type: ignore
    from ._models import BuildTaskListResult  # type: ignore
    from ._models import BuildTaskUpdateParameters  # type: ignore
    from ._models import BuildUpdateParameters  # type: ignore
    from ._models import CallbackConfig  # type: ignore
    from ._models import DockerBuildStep  # type: ignore
    from ._models import DockerBuildStepUpdateParameters  # type: ignore
    from ._models import Event  # type: ignore
    from ._models import EventContent  # type: ignore
    from ._models import EventInfo  # type: ignore
    from ._models import EventListResult  # type: ignore
    from ._models import EventRequestMessage  # type: ignore
    from ._models import EventResponseMessage  # type: ignore
    from ._models import GitCommitTrigger  # type: ignore
    from ._models import IPRule  # type: ignore
    from ._models import ImageDescriptor  # type: ignore
    from ._models import ImageUpdateTrigger  # type: ignore
    from ._models import ImportImageParameters  # type: ignore
    from ._models import ImportSource  # type: ignore
    from ._models import ImportSourceCredentials  # type: ignore
    from ._models import NetworkRuleSet  # type: ignore
    from ._models import OperationDefinition  # type: ignore
    from ._models import OperationDisplayDefinition  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationMetricSpecificationDefinition  # type: ignore
    from ._models import OperationServiceSpecificationDefinition  # type: ignore
    from ._models import PlatformProperties  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import QuarantinePolicy  # type: ignore
    from ._models import QueueBuildRequest  # type: ignore
    from ._models import QuickBuildRequest  # type: ignore
    from ._models import RegenerateCredentialParameters  # type: ignore
    from ._models import Registry  # type: ignore
    from ._models import RegistryListCredentialsResult  # type: ignore
    from ._models import RegistryListResult  # type: ignore
    from ._models import RegistryNameCheckRequest  # type: ignore
    from ._models import RegistryNameStatus  # type: ignore
    from ._models import RegistryPassword  # type: ignore
    from ._models import RegistryPolicies  # type: ignore
    from ._models import RegistryUpdateParameters  # type: ignore
    from ._models import RegistryUsage  # type: ignore
    from ._models import RegistryUsageListResult  # type: ignore
    from ._models import Replication  # type: ignore
    from ._models import ReplicationListResult  # type: ignore
    from ._models import ReplicationUpdateParameters  # type: ignore
    from ._models import Request  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceAutoGenerated  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import Source  # type: ignore
    from ._models import SourceControlAuthInfo  # type: ignore
    from ._models import SourceRepositoryProperties  # type: ignore
    from ._models import SourceRepositoryUpdateParameters  # type: ignore
    from ._models import SourceUploadDefinition  # type: ignore
    from ._models import Status  # type: ignore
    from ._models import StorageAccountProperties  # type: ignore
    from ._models import Target  # type: ignore
    from ._models import TrustPolicy  # type: ignore
    from ._models import VirtualNetworkRule  # type: ignore
    from ._models import Webhook  # type: ignore
    from ._models import WebhookCreateParameters  # type: ignore
    from ._models import WebhookListResult  # type: ignore
    from ._models import WebhookUpdateParameters  # type: ignore

from ._container_registry_management_client_enums import (
    Action,
    BaseImageDependencyType,
    BaseImageTriggerType,
    BuildArgumentType,
    BuildStatus,
    BuildStepType,
    BuildTaskStatus,
    BuildType,
    DefaultAction,
    ImportMode,
    OsType,
    PasswordName,
    PolicyStatus,
    ProvisioningState,
    RegistryUsageUnit,
    SkuName,
    SkuTier,
    SourceControlType,
    TokenType,
    TrustPolicyType,
    WebhookAction,
    WebhookStatus,
)

__all__ = [
    'Actor',
    'BaseImageDependency',
    'Build',
    'BuildArgument',
    'BuildArgumentList',
    'BuildFilter',
    'BuildGetLogResult',
    'BuildListResult',
    'BuildStep',
    'BuildStepList',
    'BuildStepProperties',
    'BuildStepPropertiesUpdateParameters',
    'BuildStepUpdateParameters',
    'BuildTask',
    'BuildTaskBuildRequest',
    'BuildTaskFilter',
    'BuildTaskListResult',
    'BuildTaskUpdateParameters',
    'BuildUpdateParameters',
    'CallbackConfig',
    'DockerBuildStep',
    'DockerBuildStepUpdateParameters',
    'Event',
    'EventContent',
    'EventInfo',
    'EventListResult',
    'EventRequestMessage',
    'EventResponseMessage',
    'GitCommitTrigger',
    'IPRule',
    'ImageDescriptor',
    'ImageUpdateTrigger',
    'ImportImageParameters',
    'ImportSource',
    'ImportSourceCredentials',
    'NetworkRuleSet',
    'OperationDefinition',
    'OperationDisplayDefinition',
    'OperationListResult',
    'OperationMetricSpecificationDefinition',
    'OperationServiceSpecificationDefinition',
    'PlatformProperties',
    'ProxyResource',
    'QuarantinePolicy',
    'QueueBuildRequest',
    'QuickBuildRequest',
    'RegenerateCredentialParameters',
    'Registry',
    'RegistryListCredentialsResult',
    'RegistryListResult',
    'RegistryNameCheckRequest',
    'RegistryNameStatus',
    'RegistryPassword',
    'RegistryPolicies',
    'RegistryUpdateParameters',
    'RegistryUsage',
    'RegistryUsageListResult',
    'Replication',
    'ReplicationListResult',
    'ReplicationUpdateParameters',
    'Request',
    'Resource',
    'ResourceAutoGenerated',
    'Sku',
    'Source',
    'SourceControlAuthInfo',
    'SourceRepositoryProperties',
    'SourceRepositoryUpdateParameters',
    'SourceUploadDefinition',
    'Status',
    'StorageAccountProperties',
    'Target',
    'TrustPolicy',
    'VirtualNetworkRule',
    'Webhook',
    'WebhookCreateParameters',
    'WebhookListResult',
    'WebhookUpdateParameters',
    'Action',
    'BaseImageDependencyType',
    'BaseImageTriggerType',
    'BuildArgumentType',
    'BuildStatus',
    'BuildStepType',
    'BuildTaskStatus',
    'BuildType',
    'DefaultAction',
    'ImportMode',
    'OsType',
    'PasswordName',
    'PolicyStatus',
    'ProvisioningState',
    'RegistryUsageUnit',
    'SkuName',
    'SkuTier',
    'SourceControlType',
    'TokenType',
    'TrustPolicyType',
    'WebhookAction',
    'WebhookStatus',
]
