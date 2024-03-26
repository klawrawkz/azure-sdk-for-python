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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class DynamicList(Model):
    """Defines an extension for a list entity.

    All required parameters must be populated in order to send to Azure.

    :param list_entity_name: Required. The name of the list entity to extend.
    :type list_entity_name: str
    :param request_lists: Required. The lists to append on the extended list
     entity.
    :type request_lists:
     list[~azure.cognitiveservices.language.luis.runtime.models.RequestList]
    """

    _validation = {
        'list_entity_name': {'required': True},
        'request_lists': {'required': True},
    }

    _attribute_map = {
        'list_entity_name': {'key': 'listEntityName', 'type': 'str'},
        'request_lists': {'key': 'requestLists', 'type': '[RequestList]'},
    }

    def __init__(self, **kwargs):
        super(DynamicList, self).__init__(**kwargs)
        self.list_entity_name = kwargs.get('list_entity_name', None)
        self.request_lists = kwargs.get('request_lists', None)


class Error(Model):
    """Represents the error that occurred.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error:
     ~azure.cognitiveservices.language.luis.runtime.models.ErrorBody
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorBody'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorException(HttpOperationError):
    """Server responded with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)


class ErrorBody(Model):
    """Represents the definition of the error that occurred.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code.
    :type code: str
    :param message: Required. The error message.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorBody, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class ExternalEntity(Model):
    """Defines a user predicted entity that extends an already existing one.

    All required parameters must be populated in order to send to Azure.

    :param entity_name: Required. The name of the entity to extend.
    :type entity_name: str
    :param start_index: Required. The start character index of the predicted
     entity.
    :type start_index: int
    :param entity_length: Required. The length of the predicted entity.
    :type entity_length: int
    :param resolution: A user supplied custom resolution to return as the
     entity's prediction.
    :type resolution: object
    :param score: A user supplied score to return as the entity's prediction
     score.
    :type score: float
    """

    _validation = {
        'entity_name': {'required': True},
        'start_index': {'required': True},
        'entity_length': {'required': True},
    }

    _attribute_map = {
        'entity_name': {'key': 'entityName', 'type': 'str'},
        'start_index': {'key': 'startIndex', 'type': 'int'},
        'entity_length': {'key': 'entityLength', 'type': 'int'},
        'resolution': {'key': 'resolution', 'type': 'object'},
        'score': {'key': 'score', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(ExternalEntity, self).__init__(**kwargs)
        self.entity_name = kwargs.get('entity_name', None)
        self.start_index = kwargs.get('start_index', None)
        self.entity_length = kwargs.get('entity_length', None)
        self.resolution = kwargs.get('resolution', None)
        self.score = kwargs.get('score', None)


class Intent(Model):
    """Represents an intent prediction.

    :param score: The score of the fired intent.
    :type score: float
    :param child_app: The prediction of the dispatched application.
    :type child_app:
     ~azure.cognitiveservices.language.luis.runtime.models.Prediction
    """

    _attribute_map = {
        'score': {'key': 'score', 'type': 'float'},
        'child_app': {'key': 'childApp', 'type': 'Prediction'},
    }

    def __init__(self, **kwargs):
        super(Intent, self).__init__(**kwargs)
        self.score = kwargs.get('score', None)
        self.child_app = kwargs.get('child_app', None)


class Prediction(Model):
    """Represents the prediction of a query.

    All required parameters must be populated in order to send to Azure.

    :param altered_query: The query after spell checking. Only set if spell
     check was enabled and a spelling mistake was found.
    :type altered_query: str
    :param top_intent: Required. The name of the top scoring intent.
    :type top_intent: str
    :param intents: Required. A dictionary representing the intents that
     fired.
    :type intents: dict[str,
     ~azure.cognitiveservices.language.luis.runtime.models.Intent]
    :param entities: Required. A dictionary representing the entities that
     fired.
    :type entities: dict[str, object]
    :param sentiment: The result of the sentiment analysis.
    :type sentiment:
     ~azure.cognitiveservices.language.luis.runtime.models.Sentiment
    """

    _validation = {
        'top_intent': {'required': True},
        'intents': {'required': True},
        'entities': {'required': True},
    }

    _attribute_map = {
        'altered_query': {'key': 'alteredQuery', 'type': 'str'},
        'top_intent': {'key': 'topIntent', 'type': 'str'},
        'intents': {'key': 'intents', 'type': '{Intent}'},
        'entities': {'key': 'entities', 'type': '{object}'},
        'sentiment': {'key': 'sentiment', 'type': 'Sentiment'},
    }

    def __init__(self, **kwargs):
        super(Prediction, self).__init__(**kwargs)
        self.altered_query = kwargs.get('altered_query', None)
        self.top_intent = kwargs.get('top_intent', None)
        self.intents = kwargs.get('intents', None)
        self.entities = kwargs.get('entities', None)
        self.sentiment = kwargs.get('sentiment', None)


class PredictionRequest(Model):
    """Represents the prediction request parameters.

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The query to predict.
    :type query: str
    :param options: The custom options defined for this request.
    :type options:
     ~azure.cognitiveservices.language.luis.runtime.models.PredictionRequestOptions
    :param external_entities: The externally predicted entities for this
     request.
    :type external_entities:
     list[~azure.cognitiveservices.language.luis.runtime.models.ExternalEntity]
    :param dynamic_lists: The dynamically created list entities for this
     request.
    :type dynamic_lists:
     list[~azure.cognitiveservices.language.luis.runtime.models.DynamicList]
    """

    _validation = {
        'query': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'options': {'key': 'options', 'type': 'PredictionRequestOptions'},
        'external_entities': {'key': 'externalEntities', 'type': '[ExternalEntity]'},
        'dynamic_lists': {'key': 'dynamicLists', 'type': '[DynamicList]'},
    }

    def __init__(self, **kwargs):
        super(PredictionRequest, self).__init__(**kwargs)
        self.query = kwargs.get('query', None)
        self.options = kwargs.get('options', None)
        self.external_entities = kwargs.get('external_entities', None)
        self.dynamic_lists = kwargs.get('dynamic_lists', None)


class PredictionRequestOptions(Model):
    """The custom options for the prediction request.

    :param datetime_reference: The reference DateTime used for predicting
     datetime entities.
    :type datetime_reference: datetime
    :param prefer_external_entities: Whether to make the external entities
     resolution override the predictions if an overlap occurs.
    :type prefer_external_entities: bool
    """

    _attribute_map = {
        'datetime_reference': {'key': 'datetimeReference', 'type': 'iso-8601'},
        'prefer_external_entities': {'key': 'preferExternalEntities', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PredictionRequestOptions, self).__init__(**kwargs)
        self.datetime_reference = kwargs.get('datetime_reference', None)
        self.prefer_external_entities = kwargs.get('prefer_external_entities', None)


class PredictionResponse(Model):
    """Represents the prediction response.

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The query used in the prediction.
    :type query: str
    :param prediction: Required. The prediction of the requested query.
    :type prediction:
     ~azure.cognitiveservices.language.luis.runtime.models.Prediction
    """

    _validation = {
        'query': {'required': True},
        'prediction': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'prediction': {'key': 'prediction', 'type': 'Prediction'},
    }

    def __init__(self, **kwargs):
        super(PredictionResponse, self).__init__(**kwargs)
        self.query = kwargs.get('query', None)
        self.prediction = kwargs.get('prediction', None)


class RequestList(Model):
    """Defines a sub-list to append to an existing list entity.

    All required parameters must be populated in order to send to Azure.

    :param name: The name of the sub-list.
    :type name: str
    :param canonical_form: Required. The canonical form of the sub-list.
    :type canonical_form: str
    :param synonyms: The synonyms of the canonical form.
    :type synonyms: list[str]
    """

    _validation = {
        'canonical_form': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'canonical_form': {'key': 'canonicalForm', 'type': 'str'},
        'synonyms': {'key': 'synonyms', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(RequestList, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.canonical_form = kwargs.get('canonical_form', None)
        self.synonyms = kwargs.get('synonyms', None)


class Sentiment(Model):
    """The result of the sentiment analysis.

    All required parameters must be populated in order to send to Azure.

    :param label: The label of the sentiment analysis result.
    :type label: str
    :param score: Required. The sentiment score of the query.
    :type score: float
    """

    _validation = {
        'score': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'score': {'key': 'score', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(Sentiment, self).__init__(**kwargs)
        self.label = kwargs.get('label', None)
        self.score = kwargs.get('score', None)
