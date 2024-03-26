# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from ._configuration import ServiceFabricManagedClustersManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    ApplicationTypeVersionsOperations,
    ApplicationTypesOperations,
    ApplicationsOperations,
    ManagedApplyMaintenanceWindowOperations,
    ManagedAzResiliencyStatusOperations,
    ManagedClusterVersionOperations,
    ManagedClustersOperations,
    ManagedMaintenanceWindowStatusOperations,
    ManagedUnsupportedVMSizesOperations,
    NodeTypeSkusOperations,
    NodeTypesOperations,
    OperationResultsOperations,
    OperationStatusOperations,
    Operations,
    ServicesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class ServiceFabricManagedClustersManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Service Fabric Managed Clusters Management Client.

    :ivar application_types: ApplicationTypesOperations operations
    :vartype application_types:
     azure.mgmt.servicefabricmanagedclusters.operations.ApplicationTypesOperations
    :ivar application_type_versions: ApplicationTypeVersionsOperations operations
    :vartype application_type_versions:
     azure.mgmt.servicefabricmanagedclusters.operations.ApplicationTypeVersionsOperations
    :ivar applications: ApplicationsOperations operations
    :vartype applications:
     azure.mgmt.servicefabricmanagedclusters.operations.ApplicationsOperations
    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.servicefabricmanagedclusters.operations.ServicesOperations
    :ivar managed_clusters: ManagedClustersOperations operations
    :vartype managed_clusters:
     azure.mgmt.servicefabricmanagedclusters.operations.ManagedClustersOperations
    :ivar managed_az_resiliency_status: ManagedAzResiliencyStatusOperations operations
    :vartype managed_az_resiliency_status:
     azure.mgmt.servicefabricmanagedclusters.operations.ManagedAzResiliencyStatusOperations
    :ivar managed_maintenance_window_status: ManagedMaintenanceWindowStatusOperations operations
    :vartype managed_maintenance_window_status:
     azure.mgmt.servicefabricmanagedclusters.operations.ManagedMaintenanceWindowStatusOperations
    :ivar managed_apply_maintenance_window: ManagedApplyMaintenanceWindowOperations operations
    :vartype managed_apply_maintenance_window:
     azure.mgmt.servicefabricmanagedclusters.operations.ManagedApplyMaintenanceWindowOperations
    :ivar managed_cluster_version: ManagedClusterVersionOperations operations
    :vartype managed_cluster_version:
     azure.mgmt.servicefabricmanagedclusters.operations.ManagedClusterVersionOperations
    :ivar managed_unsupported_vm_sizes: ManagedUnsupportedVMSizesOperations operations
    :vartype managed_unsupported_vm_sizes:
     azure.mgmt.servicefabricmanagedclusters.operations.ManagedUnsupportedVMSizesOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status:
     azure.mgmt.servicefabricmanagedclusters.operations.OperationStatusOperations
    :ivar operation_results: OperationResultsOperations operations
    :vartype operation_results:
     azure.mgmt.servicefabricmanagedclusters.operations.OperationResultsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.servicefabricmanagedclusters.operations.Operations
    :ivar node_types: NodeTypesOperations operations
    :vartype node_types: azure.mgmt.servicefabricmanagedclusters.operations.NodeTypesOperations
    :ivar node_type_skus: NodeTypeSkusOperations operations
    :vartype node_type_skus:
     azure.mgmt.servicefabricmanagedclusters.operations.NodeTypeSkusOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The customer subscription identifier. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-12-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ServiceFabricManagedClustersManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.application_types = ApplicationTypesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.application_type_versions = ApplicationTypeVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.applications = ApplicationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.services = ServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.managed_clusters = ManagedClustersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_az_resiliency_status = ManagedAzResiliencyStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_maintenance_window_status = ManagedMaintenanceWindowStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_apply_maintenance_window = ManagedApplyMaintenanceWindowOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_cluster_version = ManagedClusterVersionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_unsupported_vm_sizes = ManagedUnsupportedVMSizesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operation_results = OperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.node_types = NodeTypesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.node_type_skus = NodeTypeSkusOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ServiceFabricManagedClustersManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
