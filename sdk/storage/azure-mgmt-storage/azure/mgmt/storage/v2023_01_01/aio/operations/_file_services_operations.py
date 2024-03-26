# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._file_services_operations import (
    build_get_service_properties_request,
    build_list_request,
    build_set_service_properties_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class FileServicesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.storage.v2023_01_01.aio.StorageManagementClient`'s
        :attr:`file_services` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace_async
    async def list(self, resource_group_name: str, account_name: str, **kwargs: Any) -> _models.FileServiceItems:
        """List all file services in storage accounts.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileServiceItems or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_01_01.models.FileServiceItems
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-01-01"))
        cls: ClsType[_models.FileServiceItems] = kwargs.pop("cls", None)

        request = build_list_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("FileServiceItems", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices"
    }

    @overload
    async def set_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: _models.FileServiceProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.FileServiceProperties:
        """Sets the properties of file services in storage accounts, including CORS (Cross-Origin Resource
        Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param parameters: The properties of file services in storage accounts, including CORS
         (Cross-Origin Resource Sharing) rules. Required.
        :type parameters: ~azure.mgmt.storage.v2023_01_01.models.FileServiceProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword file_services_name: The name of the file Service within the specified storage account.
         File Service Name must be "default". Default value is "default". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype file_services_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_01_01.models.FileServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def set_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.FileServiceProperties:
        """Sets the properties of file services in storage accounts, including CORS (Cross-Origin Resource
        Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param parameters: The properties of file services in storage accounts, including CORS
         (Cross-Origin Resource Sharing) rules. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword file_services_name: The name of the file Service within the specified storage account.
         File Service Name must be "default". Default value is "default". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype file_services_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_01_01.models.FileServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def set_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: Union[_models.FileServiceProperties, IO],
        **kwargs: Any
    ) -> _models.FileServiceProperties:
        """Sets the properties of file services in storage accounts, including CORS (Cross-Origin Resource
        Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param parameters: The properties of file services in storage accounts, including CORS
         (Cross-Origin Resource Sharing) rules. Is either a FileServiceProperties type or a IO type.
         Required.
        :type parameters: ~azure.mgmt.storage.v2023_01_01.models.FileServiceProperties or IO
        :keyword file_services_name: The name of the file Service within the specified storage account.
         File Service Name must be "default". Default value is "default". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype file_services_name: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_01_01.models.FileServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-01-01"))
        file_services_name: Literal["default"] = kwargs.pop("file_services_name", "default")
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FileServiceProperties] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "FileServiceProperties")

        request = build_set_service_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            file_services_name=file_services_name,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.set_service_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("FileServiceProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    set_service_properties.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/{FileServicesName}"
    }

    @distributed_trace_async
    async def get_service_properties(
        self, resource_group_name: str, account_name: str, **kwargs: Any
    ) -> _models.FileServiceProperties:
        """Gets the properties of file services in storage accounts, including CORS (Cross-Origin Resource
        Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :keyword file_services_name: The name of the file Service within the specified storage account.
         File Service Name must be "default". Default value is "default". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype file_services_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2023_01_01.models.FileServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2023-01-01"))
        file_services_name: Literal["default"] = kwargs.pop("file_services_name", "default")
        cls: ClsType[_models.FileServiceProperties] = kwargs.pop("cls", None)

        request = build_get_service_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            file_services_name=file_services_name,
            template_url=self.get_service_properties.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("FileServiceProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_service_properties.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/{FileServicesName}"
    }
