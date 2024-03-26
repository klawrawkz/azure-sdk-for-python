# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ActiveBaseSecurityAdminRule
from ._models_py3 import ActiveBaseSecurityUserRule
from ._models_py3 import ActiveConfigurationParameter
from ._models_py3 import ActiveConnectivityConfiguration
from ._models_py3 import ActiveConnectivityConfigurationsListResult
from ._models_py3 import ActiveDefaultSecurityAdminRule
from ._models_py3 import ActiveDefaultSecurityUserRule
from ._models_py3 import ActiveSecurityAdminRule
from ._models_py3 import ActiveSecurityAdminRulesListResult
from ._models_py3 import ActiveSecurityUserRule
from ._models_py3 import ActiveSecurityUserRulesListResult
from ._models_py3 import AddressPrefixItem
from ._models_py3 import AdminRule
from ._models_py3 import AdminRuleListResult
from ._models_py3 import BaseAdminRule
from ._models_py3 import BaseUserRule
from ._models_py3 import CloudErrorBody
from ._models_py3 import ConfigurationGroup
from ._models_py3 import ConnectivityConfiguration
from ._models_py3 import ConnectivityConfigurationListResult
from ._models_py3 import ConnectivityGroupItem
from ._models_py3 import DefaultAdminRule
from ._models_py3 import DefaultUserRule
from ._models_py3 import EffectiveBaseSecurityAdminRule
from ._models_py3 import EffectiveConnectivityConfiguration
from ._models_py3 import EffectiveDefaultSecurityAdminRule
from ._models_py3 import EffectiveSecurityAdminRule
from ._models_py3 import EffectiveVirtualNetwork
from ._models_py3 import EffectiveVirtualNetworksListResult
from ._models_py3 import EffectiveVirtualNetworksParameter
from ._models_py3 import GroupMembersItem
from ._models_py3 import Hub
from ._models_py3 import NetworkGroup
from ._models_py3 import NetworkGroupListResult
from ._models_py3 import NetworkManager
from ._models_py3 import NetworkManagerCommit
from ._models_py3 import NetworkManagerDeploymentStatus
from ._models_py3 import NetworkManagerDeploymentStatusListResult
from ._models_py3 import NetworkManagerDeploymentStatusParameter
from ._models_py3 import NetworkManagerEffectiveConnectivityConfigurationListResult
from ._models_py3 import NetworkManagerEffectiveSecurityAdminRulesListResult
from ._models_py3 import NetworkManagerListResult
from ._models_py3 import NetworkManagerPropertiesNetworkManagerScopes
from ._models_py3 import NetworkManagerSecurityGroupItem
from ._models_py3 import NetworkSecurityPerimeter
from ._models_py3 import NetworkSecurityPerimeterListResult
from ._models_py3 import NspAccessRule
from ._models_py3 import NspAccessRuleListResult
from ._models_py3 import NspAssociation
from ._models_py3 import NspAssociationsListResult
from ._models_py3 import NspLink
from ._models_py3 import NspLinkListResult
from ._models_py3 import NspLinkReference
from ._models_py3 import NspLinkReferenceListResult
from ._models_py3 import NspProfile
from ._models_py3 import NspProfileListResult
from ._models_py3 import PerimeterAssociableResource
from ._models_py3 import PerimeterAssociableResourcesListResult
from ._models_py3 import PerimeterBasedAccessRule
from ._models_py3 import ProxyResource
from ._models_py3 import QueryRequestOptions
from ._models_py3 import Resource
from ._models_py3 import RuleCollection
from ._models_py3 import RuleCollectionListResult
from ._models_py3 import SecurityConfiguration
from ._models_py3 import SecurityConfigurationListResult
from ._models_py3 import SubResource
from ._models_py3 import SubscriptionId
from ._models_py3 import SystemData
from ._models_py3 import TagsObject
from ._models_py3 import UpdateTagsRequest
from ._models_py3 import UserRule
from ._models_py3 import UserRuleListResult

from ._network_management_client_enums import AccessRuleDirection
from ._network_management_client_enums import AddressPrefixType
from ._network_management_client_enums import AdminRuleKind
from ._network_management_client_enums import AssociationAccessMode
from ._network_management_client_enums import ConfigurationType
from ._network_management_client_enums import ConnectivityTopology
from ._network_management_client_enums import CreatedByType
from ._network_management_client_enums import DeleteExistingNSGs
from ._network_management_client_enums import DeleteExistingPeering
from ._network_management_client_enums import DeploymentStatus
from ._network_management_client_enums import EffectiveAdminRuleKind
from ._network_management_client_enums import EffectiveUserRuleKind
from ._network_management_client_enums import GroupConnectivity
from ._network_management_client_enums import IsGlobal
from ._network_management_client_enums import MembershipType
from ._network_management_client_enums import NspLinkProvisioningState
from ._network_management_client_enums import NspLinkStatus
from ._network_management_client_enums import NspProvisioningState
from ._network_management_client_enums import ProvisioningState
from ._network_management_client_enums import SecurityConfigurationRuleAccess
from ._network_management_client_enums import SecurityConfigurationRuleDirection
from ._network_management_client_enums import SecurityConfigurationRuleProtocol
from ._network_management_client_enums import SecurityType
from ._network_management_client_enums import UseHubGateway
from ._network_management_client_enums import UserRuleKind
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ActiveBaseSecurityAdminRule",
    "ActiveBaseSecurityUserRule",
    "ActiveConfigurationParameter",
    "ActiveConnectivityConfiguration",
    "ActiveConnectivityConfigurationsListResult",
    "ActiveDefaultSecurityAdminRule",
    "ActiveDefaultSecurityUserRule",
    "ActiveSecurityAdminRule",
    "ActiveSecurityAdminRulesListResult",
    "ActiveSecurityUserRule",
    "ActiveSecurityUserRulesListResult",
    "AddressPrefixItem",
    "AdminRule",
    "AdminRuleListResult",
    "BaseAdminRule",
    "BaseUserRule",
    "CloudErrorBody",
    "ConfigurationGroup",
    "ConnectivityConfiguration",
    "ConnectivityConfigurationListResult",
    "ConnectivityGroupItem",
    "DefaultAdminRule",
    "DefaultUserRule",
    "EffectiveBaseSecurityAdminRule",
    "EffectiveConnectivityConfiguration",
    "EffectiveDefaultSecurityAdminRule",
    "EffectiveSecurityAdminRule",
    "EffectiveVirtualNetwork",
    "EffectiveVirtualNetworksListResult",
    "EffectiveVirtualNetworksParameter",
    "GroupMembersItem",
    "Hub",
    "NetworkGroup",
    "NetworkGroupListResult",
    "NetworkManager",
    "NetworkManagerCommit",
    "NetworkManagerDeploymentStatus",
    "NetworkManagerDeploymentStatusListResult",
    "NetworkManagerDeploymentStatusParameter",
    "NetworkManagerEffectiveConnectivityConfigurationListResult",
    "NetworkManagerEffectiveSecurityAdminRulesListResult",
    "NetworkManagerListResult",
    "NetworkManagerPropertiesNetworkManagerScopes",
    "NetworkManagerSecurityGroupItem",
    "NetworkSecurityPerimeter",
    "NetworkSecurityPerimeterListResult",
    "NspAccessRule",
    "NspAccessRuleListResult",
    "NspAssociation",
    "NspAssociationsListResult",
    "NspLink",
    "NspLinkListResult",
    "NspLinkReference",
    "NspLinkReferenceListResult",
    "NspProfile",
    "NspProfileListResult",
    "PerimeterAssociableResource",
    "PerimeterAssociableResourcesListResult",
    "PerimeterBasedAccessRule",
    "ProxyResource",
    "QueryRequestOptions",
    "Resource",
    "RuleCollection",
    "RuleCollectionListResult",
    "SecurityConfiguration",
    "SecurityConfigurationListResult",
    "SubResource",
    "SubscriptionId",
    "SystemData",
    "TagsObject",
    "UpdateTagsRequest",
    "UserRule",
    "UserRuleListResult",
    "AccessRuleDirection",
    "AddressPrefixType",
    "AdminRuleKind",
    "AssociationAccessMode",
    "ConfigurationType",
    "ConnectivityTopology",
    "CreatedByType",
    "DeleteExistingNSGs",
    "DeleteExistingPeering",
    "DeploymentStatus",
    "EffectiveAdminRuleKind",
    "EffectiveUserRuleKind",
    "GroupConnectivity",
    "IsGlobal",
    "MembershipType",
    "NspLinkProvisioningState",
    "NspLinkStatus",
    "NspProvisioningState",
    "ProvisioningState",
    "SecurityConfigurationRuleAccess",
    "SecurityConfigurationRuleDirection",
    "SecurityConfigurationRuleProtocol",
    "SecurityType",
    "UseHubGateway",
    "UserRuleKind",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
