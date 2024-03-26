# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_test_base_account_request(
    resource_group_name: str, test_base_account_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-04-01-preview")
    )  # type: Literal["2022-04-01-preview"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "testBaseAccountName": _SERIALIZER.url("test_base_account_name", test_base_account_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_request(
    resource_group_name: str, test_base_account_name: str, customer_event_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-04-01-preview")
    )  # type: Literal["2022-04-01-preview"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents/{customerEventName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "testBaseAccountName": _SERIALIZER.url("test_base_account_name", test_base_account_name, "str"),
        "customerEventName": _SERIALIZER.url("customer_event_name", customer_event_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str, test_base_account_name: str, customer_event_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-04-01-preview")
    )  # type: Literal["2022-04-01-preview"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents/{customerEventName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "testBaseAccountName": _SERIALIZER.url("test_base_account_name", test_base_account_name, "str"),
        "customerEventName": _SERIALIZER.url("customer_event_name", customer_event_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, test_base_account_name: str, customer_event_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop(
        "api_version", _params.pop("api-version", "2022-04-01-preview")
    )  # type: Literal["2022-04-01-preview"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents/{customerEventName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "testBaseAccountName": _SERIALIZER.url("test_base_account_name", test_base_account_name, "str"),
        "customerEventName": _SERIALIZER.url("customer_event_name", customer_event_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class CustomerEventsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.testbase.TestBase`'s
        :attr:`customer_events` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_test_base_account(
        self, resource_group_name: str, test_base_account_name: str, **kwargs: Any
    ) -> Iterable["_models.CustomerEventResource"]:
        """Lists all notification events subscribed under a Test Base Account.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CustomerEventResource or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.testbase.models.CustomerEventResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-04-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CustomerEventListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_test_base_account_request(
                    resource_group_name=resource_group_name,
                    test_base_account_name=test_base_account_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_test_base_account.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

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
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("CustomerEventListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_test_base_account.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents"}  # type: ignore

    def _create_initial(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        customer_event_name: str,
        parameters: Union[_models.CustomerEventResource, IO],
        **kwargs: Any
    ) -> _models.CustomerEventResource:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-04-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CustomerEventResource]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "CustomerEventResource")

        request = build_create_request(
            resource_group_name=resource_group_name,
            test_base_account_name=test_base_account_name,
            customer_event_name=customer_event_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("CustomerEventResource", pipeline_response)

        if response.status_code == 201:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )

            deserialized = self._deserialize("CustomerEventResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _create_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents/{customerEventName}"}  # type: ignore

    @overload
    def begin_create(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        customer_event_name: str,
        parameters: _models.CustomerEventResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.CustomerEventResource]:
        """Create or replace a Test Base Customer Event.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :param customer_event_name: The resource name of the Test Base Customer event. Required.
        :type customer_event_name: str
        :param parameters: Parameters supplied to create a Test Base CustomerEvent. Required.
        :type parameters: ~azure.mgmt.testbase.models.CustomerEventResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either CustomerEventResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.testbase.models.CustomerEventResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_create(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        customer_event_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.CustomerEventResource]:
        """Create or replace a Test Base Customer Event.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :param customer_event_name: The resource name of the Test Base Customer event. Required.
        :type customer_event_name: str
        :param parameters: Parameters supplied to create a Test Base CustomerEvent. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either CustomerEventResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.testbase.models.CustomerEventResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_create(
        self,
        resource_group_name: str,
        test_base_account_name: str,
        customer_event_name: str,
        parameters: Union[_models.CustomerEventResource, IO],
        **kwargs: Any
    ) -> LROPoller[_models.CustomerEventResource]:
        """Create or replace a Test Base Customer Event.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :param customer_event_name: The resource name of the Test Base Customer event. Required.
        :type customer_event_name: str
        :param parameters: Parameters supplied to create a Test Base CustomerEvent. Is either a model
         type or a IO type. Required.
        :type parameters: ~azure.mgmt.testbase.models.CustomerEventResource or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either CustomerEventResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.testbase.models.CustomerEventResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-04-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CustomerEventResource]
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_initial(  # type: ignore
                resource_group_name=resource_group_name,
                test_base_account_name=test_base_account_name,
                customer_event_name=customer_event_name,
                parameters=parameters,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("CustomerEventResource", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(
                PollingMethod, ARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs)
            )  # type: PollingMethod
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents/{customerEventName}"}  # type: ignore

    def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, test_base_account_name: str, customer_event_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-04-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            test_base_account_name=test_base_account_name,
            customer_event_name=customer_event_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    _delete_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents/{customerEventName}"}  # type: ignore

    @distributed_trace
    def begin_delete(
        self, resource_group_name: str, test_base_account_name: str, customer_event_name: str, **kwargs: Any
    ) -> LROPoller[None]:
        """Deletes a Test Base Customer Event.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :param customer_event_name: The resource name of the Test Base Customer event. Required.
        :type customer_event_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-04-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                test_base_account_name=test_base_account_name,
                customer_event_name=customer_event_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = cast(
                PollingMethod, ARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs)
            )  # type: PollingMethod
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents/{customerEventName}"}  # type: ignore

    @distributed_trace
    def get(
        self, resource_group_name: str, test_base_account_name: str, customer_event_name: str, **kwargs: Any
    ) -> _models.CustomerEventResource:
        """Gets a Test Base CustomerEvent.

        :param resource_group_name: The name of the resource group that contains the resource.
         Required.
        :type resource_group_name: str
        :param test_base_account_name: The resource name of the Test Base Account. Required.
        :type test_base_account_name: str
        :param customer_event_name: The resource name of the Test Base Customer event. Required.
        :type customer_event_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CustomerEventResource or the result of cls(response)
        :rtype: ~azure.mgmt.testbase.models.CustomerEventResource
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-04-01-preview"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CustomerEventResource]

        request = build_get_request(
            resource_group_name=resource_group_name,
            test_base_account_name=test_base_account_name,
            customer_event_name=customer_event_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CustomerEventResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TestBase/testBaseAccounts/{testBaseAccountName}/customerEvents/{customerEventName}"}  # type: ignore
