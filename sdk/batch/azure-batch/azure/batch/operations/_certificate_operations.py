# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class CertificateOperations(object):
    """CertificateOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for the request. Constant value: "2023-11-01.18.0".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2023-11-01.18.0"

        self.config = config

    def add(
            self, certificate, certificate_add_options=None, custom_headers=None, raw=False, **operation_config):
        """Adds a Certificate to the specified Account.

        Warning: This operation is deprecated and will be removed after
        February, 2024. Please use the [Azure KeyVault
        Extension](https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide)
        instead.

        :param certificate: The Certificate to be added.
        :type certificate: ~azure.batch.models.CertificateAddParameter
        :param certificate_add_options: Additional parameters for the
         operation
        :type certificate_add_options:
         ~azure.batch.models.CertificateAddOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`BatchErrorException<azure.batch.models.BatchErrorException>`
        """
        timeout = None
        if certificate_add_options is not None:
            timeout = certificate_add_options.timeout
        client_request_id = None
        if certificate_add_options is not None:
            client_request_id = certificate_add_options.client_request_id
        return_client_request_id = None
        if certificate_add_options is not None:
            return_client_request_id = certificate_add_options.return_client_request_id
        ocp_date = None
        if certificate_add_options is not None:
            ocp_date = certificate_add_options.ocp_date

        # Construct URL
        url = self.add.metadata['url']
        path_format_arguments = {
            'batchUrl': self._serialize.url("self.config.batch_url", self.config.batch_url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; odata=minimalmetadata; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct body
        body_content = self._serialize.body(certificate, 'CertificateAddParameter')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.BatchErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
                'DataServiceId': 'str',
            })
            return client_raw_response
    add.metadata = {'url': '/certificates'}

    def list(
            self, certificate_list_options=None, custom_headers=None, raw=False, **operation_config):
        """Lists all of the Certificates that have been added to the specified
        Account.

        Warning: This operation is deprecated and will be removed after
        February, 2024. Please use the [Azure KeyVault
        Extension](https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide)
        instead.

        :param certificate_list_options: Additional parameters for the
         operation
        :type certificate_list_options:
         ~azure.batch.models.CertificateListOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Certificate
        :rtype:
         ~azure.batch.models.CertificatePaged[~azure.batch.models.Certificate]
        :raises:
         :class:`BatchErrorException<azure.batch.models.BatchErrorException>`
        """
        filter = None
        if certificate_list_options is not None:
            filter = certificate_list_options.filter
        select = None
        if certificate_list_options is not None:
            select = certificate_list_options.select
        max_results = None
        if certificate_list_options is not None:
            max_results = certificate_list_options.max_results
        timeout = None
        if certificate_list_options is not None:
            timeout = certificate_list_options.timeout
        client_request_id = None
        if certificate_list_options is not None:
            client_request_id = certificate_list_options.client_request_id
        return_client_request_id = None
        if certificate_list_options is not None:
            return_client_request_id = certificate_list_options.return_client_request_id
        ocp_date = None
        if certificate_list_options is not None:
            ocp_date = certificate_list_options.ocp_date

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'batchUrl': self._serialize.url("self.config.batch_url", self.config.batch_url, 'str', skip_quote=True)
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')
                if max_results is not None:
                    query_parameters['maxresults'] = self._serialize.query("max_results", max_results, 'int', maximum=1000, minimum=1)
                if timeout is not None:
                    query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if return_client_request_id is not None:
                header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
            if ocp_date is not None:
                header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.BatchErrorException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.CertificatePaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/certificates'}

    def cancel_deletion(
            self, thumbprint_algorithm, thumbprint, certificate_cancel_deletion_options=None, custom_headers=None, raw=False, **operation_config):
        """Cancels a failed deletion of a Certificate from the specified Account.

        If you try to delete a Certificate that is being used by a Pool or
        Compute Node, the status of the Certificate changes to deleteFailed. If
        you decide that you want to continue using the Certificate, you can use
        this operation to set the status of the Certificate back to active. If
        you intend to delete the Certificate, you do not need to run this
        operation after the deletion failed. You must make sure that the
        Certificate is not being used by any resources, and then you can try
        again to delete the Certificate.
        Warning: This operation is deprecated and will be removed after
        February, 2024. Please use the [Azure KeyVault
        Extension](https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide)
        instead.

        :param thumbprint_algorithm: The algorithm used to derive the
         thumbprint parameter. This must be sha1.
        :type thumbprint_algorithm: str
        :param thumbprint: The thumbprint of the Certificate being deleted.
        :type thumbprint: str
        :param certificate_cancel_deletion_options: Additional parameters for
         the operation
        :type certificate_cancel_deletion_options:
         ~azure.batch.models.CertificateCancelDeletionOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`BatchErrorException<azure.batch.models.BatchErrorException>`
        """
        timeout = None
        if certificate_cancel_deletion_options is not None:
            timeout = certificate_cancel_deletion_options.timeout
        client_request_id = None
        if certificate_cancel_deletion_options is not None:
            client_request_id = certificate_cancel_deletion_options.client_request_id
        return_client_request_id = None
        if certificate_cancel_deletion_options is not None:
            return_client_request_id = certificate_cancel_deletion_options.return_client_request_id
        ocp_date = None
        if certificate_cancel_deletion_options is not None:
            ocp_date = certificate_cancel_deletion_options.ocp_date

        # Construct URL
        url = self.cancel_deletion.metadata['url']
        path_format_arguments = {
            'batchUrl': self._serialize.url("self.config.batch_url", self.config.batch_url, 'str', skip_quote=True),
            'thumbprintAlgorithm': self._serialize.url("thumbprint_algorithm", thumbprint_algorithm, 'str'),
            'thumbprint': self._serialize.url("thumbprint", thumbprint, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.BatchErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
                'DataServiceId': 'str',
            })
            return client_raw_response
    cancel_deletion.metadata = {'url': '/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})/canceldelete'}

    def delete(
            self, thumbprint_algorithm, thumbprint, certificate_delete_options=None, custom_headers=None, raw=False, **operation_config):
        """Deletes a Certificate from the specified Account.

        You cannot delete a Certificate if a resource (Pool or Compute Node) is
        using it. Before you can delete a Certificate, you must therefore make
        sure that the Certificate is not associated with any existing Pools,
        the Certificate is not installed on any Nodes (even if you remove a
        Certificate from a Pool, it is not removed from existing Compute Nodes
        in that Pool until they restart), and no running Tasks depend on the
        Certificate. If you try to delete a Certificate that is in use, the
        deletion fails. The Certificate status changes to deleteFailed. You can
        use Cancel Delete Certificate to set the status back to active if you
        decide that you want to continue using the Certificate.
        Warning: This operation is deprecated and will be removed after
        February, 2024. Please use the [Azure KeyVault
        Extension](https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide)
        instead.

        :param thumbprint_algorithm: The algorithm used to derive the
         thumbprint parameter. This must be sha1.
        :type thumbprint_algorithm: str
        :param thumbprint: The thumbprint of the Certificate to be deleted.
        :type thumbprint: str
        :param certificate_delete_options: Additional parameters for the
         operation
        :type certificate_delete_options:
         ~azure.batch.models.CertificateDeleteOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`BatchErrorException<azure.batch.models.BatchErrorException>`
        """
        timeout = None
        if certificate_delete_options is not None:
            timeout = certificate_delete_options.timeout
        client_request_id = None
        if certificate_delete_options is not None:
            client_request_id = certificate_delete_options.client_request_id
        return_client_request_id = None
        if certificate_delete_options is not None:
            return_client_request_id = certificate_delete_options.return_client_request_id
        ocp_date = None
        if certificate_delete_options is not None:
            ocp_date = certificate_delete_options.ocp_date

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'batchUrl': self._serialize.url("self.config.batch_url", self.config.batch_url, 'str', skip_quote=True),
            'thumbprintAlgorithm': self._serialize.url("thumbprint_algorithm", thumbprint_algorithm, 'str'),
            'thumbprint': self._serialize.url("thumbprint", thumbprint, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.BatchErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
            })
            return client_raw_response
    delete.metadata = {'url': '/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})'}

    def get(
            self, thumbprint_algorithm, thumbprint, certificate_get_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets information about the specified Certificate.

        Warning: This operation is deprecated and will be removed after
        February, 2024. Please use the [Azure KeyVault
        Extension](https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide)
        instead.

        :param thumbprint_algorithm: The algorithm used to derive the
         thumbprint parameter. This must be sha1.
        :type thumbprint_algorithm: str
        :param thumbprint: The thumbprint of the Certificate to get.
        :type thumbprint: str
        :param certificate_get_options: Additional parameters for the
         operation
        :type certificate_get_options:
         ~azure.batch.models.CertificateGetOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Certificate or ClientRawResponse if raw=true
        :rtype: ~azure.batch.models.Certificate or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`BatchErrorException<azure.batch.models.BatchErrorException>`
        """
        select = None
        if certificate_get_options is not None:
            select = certificate_get_options.select
        timeout = None
        if certificate_get_options is not None:
            timeout = certificate_get_options.timeout
        client_request_id = None
        if certificate_get_options is not None:
            client_request_id = certificate_get_options.client_request_id
        return_client_request_id = None
        if certificate_get_options is not None:
            return_client_request_id = certificate_get_options.return_client_request_id
        ocp_date = None
        if certificate_get_options is not None:
            ocp_date = certificate_get_options.ocp_date

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'batchUrl': self._serialize.url("self.config.batch_url", self.config.batch_url, 'str', skip_quote=True),
            'thumbprintAlgorithm': self._serialize.url("thumbprint_algorithm", thumbprint_algorithm, 'str'),
            'thumbprint': self._serialize.url("thumbprint", thumbprint, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.BatchErrorException(self._deserialize, response)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Certificate', response)
            header_dict = {
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})'}
