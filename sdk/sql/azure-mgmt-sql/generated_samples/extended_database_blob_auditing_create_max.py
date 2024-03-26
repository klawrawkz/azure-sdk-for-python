# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-sql
# USAGE
    python extended_database_blob_auditing_create_max.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SqlManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-1111-2222-3333-444444444444",
    )

    response = client.extended_database_blob_auditing_policies.create_or_update(
        resource_group_name="blobauditingtest-4799",
        server_name="blobauditingtest-6440",
        database_name="testdb",
        parameters={
            "properties": {
                "auditActionsAndGroups": [
                    "DATABASE_LOGOUT_GROUP",
                    "DATABASE_ROLE_MEMBER_CHANGE_GROUP",
                    "UPDATE on database::TestDatabaseName by public",
                ],
                "isAzureMonitorTargetEnabled": True,
                "isStorageSecondaryKeyInUse": False,
                "predicateExpression": "statement = 'select 1'",
                "queueDelayMs": 4000,
                "retentionDays": 6,
                "state": "Enabled",
                "storageAccountAccessKey": "sdlfkjabc+sdlfkjsdlkfsjdfLDKFTERLKFDFKLjsdfksjdflsdkfD2342309432849328476458/3RSD==",
                "storageAccountSubscriptionId": "00000000-1234-0000-5678-000000000000",
                "storageEndpoint": "https://mystorage.blob.core.windows.net",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2021-11-01-preview/examples/ExtendedDatabaseBlobAuditingCreateMax.json
if __name__ == "__main__":
    main()
