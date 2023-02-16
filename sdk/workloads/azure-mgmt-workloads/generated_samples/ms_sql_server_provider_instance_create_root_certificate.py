# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.workloads import WorkloadsClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-workloads
# USAGE
    python ms_sql_server_provider_instance_create_root_certificate.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = WorkloadsClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.provider_instances.begin_create(
        resource_group_name="myResourceGroup",
        monitor_name="mySapMonitor",
        provider_instance_name="myProviderInstance",
        provider_instance_parameter={
            "properties": {
                "providerSettings": {
                    "dbPassword": "****",
                    "dbPasswordUri": "",
                    "dbPort": "5912",
                    "dbUsername": "user",
                    "hostname": "hostname",
                    "providerType": "MsSqlServer",
                    "sapSid": "sid",
                    "sslPreference": "RootCertificate",
                }
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/workloads/resource-manager/Microsoft.Workloads/preview/2022-11-01-preview/examples/workloadmonitor/MsSqlServerProviderInstance_Create_Root_Certificate.json
if __name__ == "__main__":
    main()
