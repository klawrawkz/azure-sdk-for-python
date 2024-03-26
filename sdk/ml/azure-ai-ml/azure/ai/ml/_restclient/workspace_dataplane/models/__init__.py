# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ComputeRuntimeDto
    from ._models_py3 import CosmosDbSettings
    from ._models_py3 import EncryptionProperty
    from ._models_py3 import FeatureStoreSettings
    from ._models_py3 import IdentityForCmk
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import ManagedServiceIdentity
    from ._models_py3 import NotebookPreparationError
    from ._models_py3 import NotebookResourceInfo
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import Resource
    from ._models_py3 import ServiceManagedResourcesSettings
    from ._models_py3 import SharedPrivateLinkResource
    from ._models_py3 import Sku
    from ._models_py3 import SystemData
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceHubConfig
    from ._models_py3 import WorkspacePrivateEndpointResource
except (SyntaxError, ImportError):
    from ._models import ComputeRuntimeDto  # type: ignore
    from ._models import CosmosDbSettings  # type: ignore
    from ._models import EncryptionProperty  # type: ignore
    from ._models import FeatureStoreSettings  # type: ignore
    from ._models import IdentityForCmk  # type: ignore
    from ._models import KeyVaultProperties  # type: ignore
    from ._models import ManagedServiceIdentity  # type: ignore
    from ._models import NotebookPreparationError  # type: ignore
    from ._models import NotebookResourceInfo  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ServiceManagedResourcesSettings  # type: ignore
    from ._models import SharedPrivateLinkResource  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import UserAssignedIdentity  # type: ignore
    from ._models import Workspace  # type: ignore
    from ._models import WorkspaceHubConfig  # type: ignore
    from ._models import WorkspacePrivateEndpointResource  # type: ignore

from ._azure_machine_learning_workspaces_enums import (
    CreatedByType,
    EncryptionStatus,
    EndpointServiceConnectionStatus,
    ManagedServiceIdentityType,
    ProvisioningState,
    PublicNetworkAccessType,
    SkuTier,
)

__all__ = [
    'ComputeRuntimeDto',
    'CosmosDbSettings',
    'EncryptionProperty',
    'FeatureStoreSettings',
    'IdentityForCmk',
    'KeyVaultProperties',
    'ManagedServiceIdentity',
    'NotebookPreparationError',
    'NotebookResourceInfo',
    'PrivateEndpointConnection',
    'PrivateLinkServiceConnectionState',
    'Resource',
    'ServiceManagedResourcesSettings',
    'SharedPrivateLinkResource',
    'Sku',
    'SystemData',
    'UserAssignedIdentity',
    'Workspace',
    'WorkspaceHubConfig',
    'WorkspacePrivateEndpointResource',
    'CreatedByType',
    'EncryptionStatus',
    'EndpointServiceConnectionStatus',
    'ManagedServiceIdentityType',
    'ProvisioningState',
    'PublicNetworkAccessType',
    'SkuTier',
]
