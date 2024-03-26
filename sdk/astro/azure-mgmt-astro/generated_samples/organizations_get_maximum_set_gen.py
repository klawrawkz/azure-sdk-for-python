# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.astro import AstroMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-astro
# USAGE
    python organizations_get_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AstroMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="43454B17-172A-40FE-80FA-549EA23D12B3",
    )

    response = client.organizations.get(
        resource_group_name="rgastronomer",
        organization_name="S PS",
    )
    print(response)


# x-ms-original-file: specification/liftrastronomer/resource-manager/Astronomer.Astro/stable/2023-08-01/examples/Organizations_Get_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
