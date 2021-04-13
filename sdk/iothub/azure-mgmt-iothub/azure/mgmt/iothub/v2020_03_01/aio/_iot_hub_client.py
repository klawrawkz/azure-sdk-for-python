# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import IotHubClientConfiguration
from .operations import Operations
from .operations import IotHubResourceOperations
from .operations import ResourceProviderCommonOperations
from .operations import CertificatesOperations
from .operations import IotHubOperations
from .operations import PrivateLinkResourcesOperations
from .operations import PrivateEndpointConnectionsOperations
from .. import models


class IotHubClient(object):
    """Use this API to manage the IoT hubs in your Azure subscription.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.iothub.aio.operations.Operations
    :ivar iot_hub_resource: IotHubResourceOperations operations
    :vartype iot_hub_resource: azure.mgmt.iothub.aio.operations.IotHubResourceOperations
    :ivar resource_provider_common: ResourceProviderCommonOperations operations
    :vartype resource_provider_common: azure.mgmt.iothub.aio.operations.ResourceProviderCommonOperations
    :ivar certificates: CertificatesOperations operations
    :vartype certificates: azure.mgmt.iothub.aio.operations.CertificatesOperations
    :ivar iot_hub: IotHubOperations operations
    :vartype iot_hub: azure.mgmt.iothub.aio.operations.IotHubOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.iothub.aio.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.iothub.aio.operations.PrivateEndpointConnectionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = IotHubClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.iot_hub_resource = IotHubResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_provider_common = ResourceProviderCommonOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.certificates = CertificatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.iot_hub = IotHubOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "IotHubClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
