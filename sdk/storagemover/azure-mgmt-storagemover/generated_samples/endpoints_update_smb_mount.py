# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.storagemover import StorageMoverMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storagemover
# USAGE
    python endpoints_update_smb_mount.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageMoverMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="60bcfc77-6589-4da2-b7fd-f9ec9322cf95",
    )

    response = client.endpoints.update(
        resource_group_name="examples-rg",
        storage_mover_name="examples-storageMoverName",
        endpoint_name="examples-endpointName",
        endpoint={
            "properties": {
                "credentials": {
                    "passwordUri": "https://examples-azureKeyVault.vault.azure.net/secrets/examples-updated-password",
                    "type": "AzureKeyVaultSmb",
                    "usernameUri": "https://examples-azureKeyVault.vault.azure.net/secrets/examples-updated-username",
                },
                "description": "Updated Endpoint Description",
                "endpointType": "SmbMount",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/storagemover/resource-manager/Microsoft.StorageMover/stable/2023-10-01/examples/Endpoints_Update_SmbMount.json
if __name__ == "__main__":
    main()
