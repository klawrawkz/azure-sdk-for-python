# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterator, Callable, Dict, IO, Optional, TypeVar, cast

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ...operations._operations import (
    build_schema_get_by_id_request,
    build_schema_get_schema_version_request,
    build_schema_query_id_by_content_request,
    build_schema_register_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SchemaOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.schemaregistry._generated.aio.AzureSchemaRegistry`'s
        :attr:`schema` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def get_by_id(self, id: str, **kwargs: Any) -> AsyncIterator[bytes]:
        """Get a registered schema by its unique ID reference.

        Gets a registered schema by its unique ID.  Azure Schema Registry guarantees that ID is unique
        within a namespace. Operation response type is based on serialization of schema requested.

        :param id: References specific schema in registry namespace. Required.
        :type id: str
        :return: Async iterator of the response bytes
        :rtype: AsyncIterator[bytes]
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
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        request = build_schema_get_by_id_request(
            id=id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(AsyncIterator[bytes], deserialized), response_headers)  # type: ignore

        return cast(AsyncIterator[bytes], deserialized)  # type: ignore

    async def get_schema_version(
        self, group_name: str, schema_name: str, schema_version: int, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        """Get specific schema versions.

        Gets one specific version of one schema.

        :param group_name: Schema group under which schema is registered.  Group's serialization type
         should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_version: Version number of specific schema. Required.
        :type schema_version: int
        :return: Async iterator of the response bytes
        :rtype: AsyncIterator[bytes]
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
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        request = build_schema_get_schema_version_request(
            group_name=group_name,
            schema_name=schema_name,
            schema_version=schema_version,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if response.status_code == 200:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Content-Type"] = self._deserialize("str", response.headers.get("Content-Type"))
            response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
            response_headers["Schema-Id-Location"] = self._deserialize(
                "str", response.headers.get("Schema-Id-Location")
            )
            response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
            response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
            response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

            deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, cast(AsyncIterator[bytes], deserialized), response_headers)  # type: ignore

        return cast(AsyncIterator[bytes], deserialized)  # type: ignore

    async def query_id_by_content(  # pylint: disable=inconsistent-return-statements
        self, group_name: str, schema_name: str, schema_content: IO, **kwargs: Any
    ) -> None:
        """Get ID for existing schema.

        Gets the ID referencing an existing schema within the specified schema group, as matched by
        schema content comparison.

        :param group_name: Schema group under which schema is registered.  Group's serialization type
         should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_content: String representation (UTF-8) of the registered schema. Required.
        :type schema_content: IO
        :return: None
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json; serialization=Avro")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = schema_content

        request = build_schema_query_id_by_content_request(
            group_name=group_name,
            schema_name=schema_name,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
        response_headers["Schema-Id-Location"] = self._deserialize("str", response.headers.get("Schema-Id-Location"))
        response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
        response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
        response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    async def register(  # pylint: disable=inconsistent-return-statements
        self, group_name: str, schema_name: str, schema_content: IO, **kwargs: Any
    ) -> None:
        """Register new schema.

        Register new schema. If schema of specified name does not exist in specified group, schema is
        created at version 1. If schema of specified name exists already in specified group, schema is
        created at latest version + 1.

        :param group_name: Schema group under which schema should be registered.  Group's serialization
         type should match the serialization type specified in the request. Required.
        :type group_name: str
        :param schema_name: Name of schema. Required.
        :type schema_name: str
        :param schema_content: String representation (UTF-8) of the schema being registered. Required.
        :type schema_content: IO
        :return: None
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json; serialization=Avro")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = schema_content

        request = build_schema_register_request(
            group_name=group_name,
            schema_name=schema_name,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
        response_headers["Schema-Id"] = self._deserialize("str", response.headers.get("Schema-Id"))
        response_headers["Schema-Id-Location"] = self._deserialize("str", response.headers.get("Schema-Id-Location"))
        response_headers["Schema-Group-Name"] = self._deserialize("str", response.headers.get("Schema-Group-Name"))
        response_headers["Schema-Name"] = self._deserialize("str", response.headers.get("Schema-Name"))
        response_headers["Schema-Version"] = self._deserialize("int", response.headers.get("Schema-Version"))

        if cls:
            return cls(pipeline_response, None, response_headers)
