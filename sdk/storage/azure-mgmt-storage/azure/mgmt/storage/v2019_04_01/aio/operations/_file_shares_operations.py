# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._file_shares_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class FileSharesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.storage.v2019_04_01.aio.StorageManagementClient`'s
        :attr:`file_shares` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        account_name: str,
        skip_token: Optional[str] = None,
        maxpagesize: Optional[str] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.FileShareItem"]:
        """Lists all shares.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param skip_token: Optional. Continuation token for the list operation. Default value is None.
        :type skip_token: str
        :param maxpagesize: Optional. Specified maximum number of shares that can be included in the
         list. Default value is None.
        :type maxpagesize: str
        :param filter: Optional. When specified, only share names starting with the filter will be
         listed. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FileShareItem or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.storage.v2019_04_01.models.FileShareItem]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-04-01"))
        cls: ClsType[_models.FileShareItems] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
                    skip_token=skip_token,
                    maxpagesize=maxpagesize,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FileShareItems", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares"
    }

    @overload
    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        file_share: _models.FileShare,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.FileShare:
        """Creates a new share under the specified account as described by request body. The share
        resource includes metadata and properties for that share. It does not include a list of the
        files contained by the share.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number. Required.
        :type share_name: str
        :param file_share: Properties of the file share to create. Required.
        :type file_share: ~azure.mgmt.storage.v2019_04_01.models.FileShare
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_04_01.models.FileShare
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        file_share: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.FileShare:
        """Creates a new share under the specified account as described by request body. The share
        resource includes metadata and properties for that share. It does not include a list of the
        files contained by the share.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number. Required.
        :type share_name: str
        :param file_share: Properties of the file share to create. Required.
        :type file_share: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_04_01.models.FileShare
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        file_share: Union[_models.FileShare, IO],
        **kwargs: Any
    ) -> _models.FileShare:
        """Creates a new share under the specified account as described by request body. The share
        resource includes metadata and properties for that share. It does not include a list of the
        files contained by the share.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number. Required.
        :type share_name: str
        :param file_share: Properties of the file share to create. Is either a FileShare type or a IO
         type. Required.
        :type file_share: ~azure.mgmt.storage.v2019_04_01.models.FileShare or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_04_01.models.FileShare
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-04-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FileShare] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(file_share, (IOBase, bytes)):
            _content = file_share
        else:
            _json = self._serialize.body(file_share, "FileShare")

        request = build_create_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
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

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("FileShare", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("FileShare", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}"
    }

    @overload
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        file_share: _models.FileShare,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.FileShare:
        """Updates share properties as specified in request body. Properties not mentioned in the request
        will not be changed. Update fails if the specified share does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number. Required.
        :type share_name: str
        :param file_share: Properties to update for the file share. Required.
        :type file_share: ~azure.mgmt.storage.v2019_04_01.models.FileShare
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_04_01.models.FileShare
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        file_share: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.FileShare:
        """Updates share properties as specified in request body. Properties not mentioned in the request
        will not be changed. Update fails if the specified share does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number. Required.
        :type share_name: str
        :param file_share: Properties to update for the file share. Required.
        :type file_share: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_04_01.models.FileShare
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        share_name: str,
        file_share: Union[_models.FileShare, IO],
        **kwargs: Any
    ) -> _models.FileShare:
        """Updates share properties as specified in request body. Properties not mentioned in the request
        will not be changed. Update fails if the specified share does not already exist.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number. Required.
        :type share_name: str
        :param file_share: Properties to update for the file share. Is either a FileShare type or a IO
         type. Required.
        :type file_share: ~azure.mgmt.storage.v2019_04_01.models.FileShare or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_04_01.models.FileShare
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-04-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.FileShare] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(file_share, (IOBase, bytes)):
            _content = file_share
        else:
            _json = self._serialize.body(file_share, "FileShare")

        request = build_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
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

        deserialized = self._deserialize("FileShare", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}"
    }

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, account_name: str, share_name: str, **kwargs: Any
    ) -> _models.FileShare:
        """Gets properties of a specified share.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number. Required.
        :type share_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileShare or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2019_04_01.models.FileShare
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-04-01"))
        cls: ClsType[_models.FileShare] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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

        deserialized = self._deserialize("FileShare", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}"
    }

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, account_name: str, share_name: str, **kwargs: Any
    ) -> None:
        """Deletes specified share under its account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive. Required.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only. Required.
        :type account_name: str
        :param share_name: The name of the file share within the specified storage account. File share
         names must be between 3 and 63 characters in length and use numbers, lower-case letters and
         dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter
         or number. Required.
        :type share_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2019-04-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}"
    }
