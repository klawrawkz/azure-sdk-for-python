# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservicessiterecovery import SiteRecoveryManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-recoveryservicessiterecovery
# USAGE
    python recovery_points_get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SiteRecoveryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="c183865e-6077-46f2-a3b1-deb0f4f4650a",
        resource_group_name="resourceGroupPS1",
        resource_name="vault1",
    )

    response = client.recovery_points.get(
        fabric_name="cloud1",
        protection_container_name="cloud_6d224fc6-f326-5d35-96de-fbf51efb3179",
        replicated_protected_item_name="f8491e4f-817a-40dd-a90c-af773978c75b",
        recovery_point_name="b22134ea-620c-474b-9fa5-3c1cb47708e3",
    )
    print(response)


# x-ms-original-file: specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/stable/2023-08-01/examples/RecoveryPoints_Get.json
if __name__ == "__main__":
    main()
