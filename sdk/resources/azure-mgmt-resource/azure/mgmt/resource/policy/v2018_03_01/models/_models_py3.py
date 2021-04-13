# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._policy_client_enums import *


class ErrorResponse(msrest.serialization.Model):
    """Error response indicates Azure Resource Manager is not able to process the incoming request. The reason is provided in the error message.

    :param http_status: Http status code.
    :type http_status: str
    :param error_code: Error code.
    :type error_code: str
    :param error_message: Error message indicating why the operation failed.
    :type error_message: str
    """

    _attribute_map = {
        'http_status': {'key': 'httpStatus', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        http_status: Optional[str] = None,
        error_code: Optional[str] = None,
        error_message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.http_status = http_status
        self.error_code = error_code
        self.error_message = error_message


class PolicyAssignment(msrest.serialization.Model):
    """The policy assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy assignment.
    :vartype id: str
    :ivar type: The type of the policy assignment.
    :vartype type: str
    :ivar name: The name of the policy assignment.
    :vartype name: str
    :param sku: The policy sku. This property is optional, obsolete, and will be ignored.
    :type sku: ~azure.mgmt.resource.policy.v2018_03_01.models.PolicySku
    :param display_name: The display name of the policy assignment.
    :type display_name: str
    :param policy_definition_id: The ID of the policy definition or policy set definition being
     assigned.
    :type policy_definition_id: str
    :param scope: The scope for the policy assignment.
    :type scope: str
    :param not_scopes: The policy's excluded scopes.
    :type not_scopes: list[str]
    :param parameters: Required if a parameter is used in policy rule.
    :type parameters: object
    :param description: This message will be part of response in case of policy violation.
    :type description: str
    :param metadata: The policy assignment metadata.
    :type metadata: object
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'PolicySku'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'not_scopes': {'key': 'properties.notScopes', 'type': '[str]'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        sku: Optional["PolicySku"] = None,
        display_name: Optional[str] = None,
        policy_definition_id: Optional[str] = None,
        scope: Optional[str] = None,
        not_scopes: Optional[List[str]] = None,
        parameters: Optional[object] = None,
        description: Optional[str] = None,
        metadata: Optional[object] = None,
        **kwargs
    ):
        super(PolicyAssignment, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.sku = sku
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
        self.scope = scope
        self.not_scopes = not_scopes
        self.parameters = parameters
        self.description = description
        self.metadata = metadata


class PolicyAssignmentListResult(msrest.serialization.Model):
    """List of policy assignments.

    :param value: An array of policy assignments.
    :type value: list[~azure.mgmt.resource.policy.v2018_03_01.models.PolicyAssignment]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PolicyAssignment"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PolicyAssignmentListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PolicyDefinition(msrest.serialization.Model):
    """The policy definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy definition.
    :vartype id: str
    :ivar name: The name of the policy definition.
    :vartype name: str
    :ivar type: The type of the resource (Microsoft.Authorization/policyDefinitions).
    :vartype type: str
    :param policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
     and Custom. Possible values include: "NotSpecified", "BuiltIn", "Custom".
    :type policy_type: str or ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyType
    :param mode: The policy definition mode. Possible values are NotSpecified, Indexed, and All.
     Possible values include: "NotSpecified", "Indexed", "All".
    :type mode: str or ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyMode
    :param display_name: The display name of the policy definition.
    :type display_name: str
    :param description: The policy definition description.
    :type description: str
    :param policy_rule: The policy rule.
    :type policy_rule: object
    :param metadata: The policy definition metadata.
    :type metadata: object
    :param parameters: Required if a parameter is used in policy rule.
    :type parameters: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'policy_rule': {'key': 'properties.policyRule', 'type': 'object'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        policy_type: Optional[Union[str, "PolicyType"]] = None,
        mode: Optional[Union[str, "PolicyMode"]] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        policy_rule: Optional[object] = None,
        metadata: Optional[object] = None,
        parameters: Optional[object] = None,
        **kwargs
    ):
        super(PolicyDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.policy_type = policy_type
        self.mode = mode
        self.display_name = display_name
        self.description = description
        self.policy_rule = policy_rule
        self.metadata = metadata
        self.parameters = parameters


class PolicyDefinitionListResult(msrest.serialization.Model):
    """List of policy definitions.

    :param value: An array of policy definitions.
    :type value: list[~azure.mgmt.resource.policy.v2018_03_01.models.PolicyDefinition]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PolicyDefinition"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PolicyDefinitionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PolicyDefinitionReference(msrest.serialization.Model):
    """The policy definition reference.

    :param policy_definition_id: The ID of the policy definition or policy set definition.
    :type policy_definition_id: str
    :param parameters: Required if a parameter is used in policy rule.
    :type parameters: object
    """

    _attribute_map = {
        'policy_definition_id': {'key': 'policyDefinitionId', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        policy_definition_id: Optional[str] = None,
        parameters: Optional[object] = None,
        **kwargs
    ):
        super(PolicyDefinitionReference, self).__init__(**kwargs)
        self.policy_definition_id = policy_definition_id
        self.parameters = parameters


class PolicySetDefinition(msrest.serialization.Model):
    """The policy set definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy set definition.
    :vartype id: str
    :ivar name: The name of the policy set definition.
    :vartype name: str
    :ivar type: The type of the resource (Microsoft.Authorization/policySetDefinitions).
    :vartype type: str
    :param policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
     and Custom. Possible values include: "NotSpecified", "BuiltIn", "Custom".
    :type policy_type: str or ~azure.mgmt.resource.policy.v2018_03_01.models.PolicyType
    :param display_name: The display name of the policy set definition.
    :type display_name: str
    :param description: The policy set definition description.
    :type description: str
    :param metadata: The policy set definition metadata.
    :type metadata: object
    :param parameters: The policy set definition parameters that can be used in policy definition
     references.
    :type parameters: object
    :param policy_definitions: An array of policy definition references.
    :type policy_definitions:
     list[~azure.mgmt.resource.policy.v2018_03_01.models.PolicyDefinitionReference]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'policy_definitions': {'key': 'properties.policyDefinitions', 'type': '[PolicyDefinitionReference]'},
    }

    def __init__(
        self,
        *,
        policy_type: Optional[Union[str, "PolicyType"]] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[object] = None,
        parameters: Optional[object] = None,
        policy_definitions: Optional[List["PolicyDefinitionReference"]] = None,
        **kwargs
    ):
        super(PolicySetDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.policy_type = policy_type
        self.display_name = display_name
        self.description = description
        self.metadata = metadata
        self.parameters = parameters
        self.policy_definitions = policy_definitions


class PolicySetDefinitionListResult(msrest.serialization.Model):
    """List of policy set definitions.

    :param value: An array of policy set definitions.
    :type value: list[~azure.mgmt.resource.policy.v2018_03_01.models.PolicySetDefinition]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicySetDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PolicySetDefinition"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PolicySetDefinitionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PolicySku(msrest.serialization.Model):
    """The policy sku. This property is optional, obsolete, and will be ignored.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the policy sku. Possible values are A0 and A1.
    :type name: str
    :param tier: The policy sku tier. Possible values are Free and Standard.
    :type tier: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        tier: Optional[str] = None,
        **kwargs
    ):
        super(PolicySku, self).__init__(**kwargs)
        self.name = name
        self.tier = tier
