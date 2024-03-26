# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, TYPE_CHECKING, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.apimanagement import ApiManagementClient

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-apimanagement
# USAGE
    python api_management_create_graph_ql_api_resolver_policy.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ApiManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.graph_ql_api_resolver_policy.create_or_update(
        resource_group_name="rg1",
        service_name="apimService1",
        api_id="5600b57e7e8880006a040001",
        resolver_id="5600b57e7e8880006a080001",
        policy_id="policy",
        parameters={
            "properties": {
                "format": "xml",
                "value": '<http-data-source><http-request><set-method>GET</set-method><set-backend-service base-url="https://some.service.com" /><set-url>/api/users</set-url></http-request></http-data-source>',
            }
        },
    )
    print(response)


# x-ms-original-file: specification/apimanagement/resource-manager/Microsoft.ApiManagement/stable/2022-08-01/examples/ApiManagementCreateGraphQLApiResolverPolicy.json
if __name__ == "__main__":
    main()
