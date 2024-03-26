# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse

from . import models as _models
from ._configuration import ArtifactsClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    BigDataPoolsOperations,
    DataFlowDebugSessionOperations,
    DataFlowOperations,
    DatasetOperations,
    IntegrationRuntimesOperations,
    KqlScriptOperations,
    KqlScriptsOperations,
    LibraryOperations,
    LinkConnectionOperations,
    LinkedServiceOperations,
    MetastoreOperations,
    NotebookOperationResultOperations,
    NotebookOperations,
    PipelineOperations,
    PipelineRunOperations,
    RunNotebookOperations,
    SparkConfigurationOperations,
    SparkJobDefinitionOperations,
    SqlPoolsOperations,
    SqlScriptOperations,
    TriggerOperations,
    TriggerRunOperations,
    WorkspaceGitRepoManagementOperations,
    WorkspaceOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class ArtifactsClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """ArtifactsClient.

    :ivar link_connection: LinkConnectionOperations operations
    :vartype link_connection: azure.synapse.artifacts.operations.LinkConnectionOperations
    :ivar run_notebook: RunNotebookOperations operations
    :vartype run_notebook: azure.synapse.artifacts.operations.RunNotebookOperations
    :ivar kql_scripts: KqlScriptsOperations operations
    :vartype kql_scripts: azure.synapse.artifacts.operations.KqlScriptsOperations
    :ivar kql_script: KqlScriptOperations operations
    :vartype kql_script: azure.synapse.artifacts.operations.KqlScriptOperations
    :ivar metastore: MetastoreOperations operations
    :vartype metastore: azure.synapse.artifacts.operations.MetastoreOperations
    :ivar spark_configuration: SparkConfigurationOperations operations
    :vartype spark_configuration: azure.synapse.artifacts.operations.SparkConfigurationOperations
    :ivar big_data_pools: BigDataPoolsOperations operations
    :vartype big_data_pools: azure.synapse.artifacts.operations.BigDataPoolsOperations
    :ivar data_flow: DataFlowOperations operations
    :vartype data_flow: azure.synapse.artifacts.operations.DataFlowOperations
    :ivar data_flow_debug_session: DataFlowDebugSessionOperations operations
    :vartype data_flow_debug_session:
     azure.synapse.artifacts.operations.DataFlowDebugSessionOperations
    :ivar dataset: DatasetOperations operations
    :vartype dataset: azure.synapse.artifacts.operations.DatasetOperations
    :ivar workspace_git_repo_management: WorkspaceGitRepoManagementOperations operations
    :vartype workspace_git_repo_management:
     azure.synapse.artifacts.operations.WorkspaceGitRepoManagementOperations
    :ivar integration_runtimes: IntegrationRuntimesOperations operations
    :vartype integration_runtimes: azure.synapse.artifacts.operations.IntegrationRuntimesOperations
    :ivar library: LibraryOperations operations
    :vartype library: azure.synapse.artifacts.operations.LibraryOperations
    :ivar linked_service: LinkedServiceOperations operations
    :vartype linked_service: azure.synapse.artifacts.operations.LinkedServiceOperations
    :ivar notebook: NotebookOperations operations
    :vartype notebook: azure.synapse.artifacts.operations.NotebookOperations
    :ivar notebook_operation_result: NotebookOperationResultOperations operations
    :vartype notebook_operation_result:
     azure.synapse.artifacts.operations.NotebookOperationResultOperations
    :ivar pipeline: PipelineOperations operations
    :vartype pipeline: azure.synapse.artifacts.operations.PipelineOperations
    :ivar pipeline_run: PipelineRunOperations operations
    :vartype pipeline_run: azure.synapse.artifacts.operations.PipelineRunOperations
    :ivar spark_job_definition: SparkJobDefinitionOperations operations
    :vartype spark_job_definition: azure.synapse.artifacts.operations.SparkJobDefinitionOperations
    :ivar sql_pools: SqlPoolsOperations operations
    :vartype sql_pools: azure.synapse.artifacts.operations.SqlPoolsOperations
    :ivar sql_script: SqlScriptOperations operations
    :vartype sql_script: azure.synapse.artifacts.operations.SqlScriptOperations
    :ivar trigger: TriggerOperations operations
    :vartype trigger: azure.synapse.artifacts.operations.TriggerOperations
    :ivar trigger_run: TriggerRunOperations operations
    :vartype trigger_run: azure.synapse.artifacts.operations.TriggerRunOperations
    :ivar workspace: WorkspaceOperations operations
    :vartype workspace: azure.synapse.artifacts.operations.WorkspaceOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param endpoint: The workspace development endpoint, for example
     ``https://myworkspace.dev.azuresynapse.net``. Required.
    :type endpoint: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(self, credential: "TokenCredential", endpoint: str, **kwargs: Any) -> None:
        _endpoint = "{endpoint}"
        self._config = ArtifactsClientConfiguration(credential=credential, endpoint=endpoint, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: PipelineClient = PipelineClient(base_url=_endpoint, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.link_connection = LinkConnectionOperations(self._client, self._config, self._serialize, self._deserialize)
        self.run_notebook = RunNotebookOperations(self._client, self._config, self._serialize, self._deserialize)
        self.kql_scripts = KqlScriptsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.kql_script = KqlScriptOperations(self._client, self._config, self._serialize, self._deserialize)
        self.metastore = MetastoreOperations(self._client, self._config, self._serialize, self._deserialize)
        self.spark_configuration = SparkConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.big_data_pools = BigDataPoolsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_flow = DataFlowOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_flow_debug_session = DataFlowDebugSessionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.dataset = DatasetOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspace_git_repo_management = WorkspaceGitRepoManagementOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.library = LibraryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.linked_service = LinkedServiceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.notebook = NotebookOperations(self._client, self._config, self._serialize, self._deserialize)
        self.notebook_operation_result = NotebookOperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.pipeline = PipelineOperations(self._client, self._config, self._serialize, self._deserialize)
        self.pipeline_run = PipelineRunOperations(self._client, self._config, self._serialize, self._deserialize)
        self.spark_job_definition = SparkJobDefinitionOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.sql_pools = SqlPoolsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sql_script = SqlScriptOperations(self._client, self._config, self._serialize, self._deserialize)
        self.trigger = TriggerOperations(self._client, self._config, self._serialize, self._deserialize)
        self.trigger_run = TriggerRunOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspace = WorkspaceOperations(self._client, self._config, self._serialize, self._deserialize)

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
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ArtifactsClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
