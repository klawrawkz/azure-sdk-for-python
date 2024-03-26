# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._deny_assignments_operations import DenyAssignmentsOperations
from ._provider_operations_metadata_operations import ProviderOperationsMetadataOperations
from ._role_assignments_operations import RoleAssignmentsOperations
from ._permissions_operations import PermissionsOperations
from ._role_definitions_operations import RoleDefinitionsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DenyAssignmentsOperations",
    "ProviderOperationsMetadataOperations",
    "RoleAssignmentsOperations",
    "PermissionsOperations",
    "RoleDefinitionsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
