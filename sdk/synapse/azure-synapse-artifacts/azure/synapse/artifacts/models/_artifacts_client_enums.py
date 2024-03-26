# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionOnExistingTargetTable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Action on existing target table. If not specified, 'FailOnNonEmptyTable' action is used."""

    FAIL_ON_NON_EMPTY_TABLE = "FailOnNonEmptyTable"
    """Same existing tables on target database will be Failed."""
    DROP_AND_RECREATE_TABLE = "DropAndRecreateTable"
    """Same existing tables on target database will be dropped and recreated."""
    MERGE_WITH_EXISTING_DATA = "MergeWithExistingData"
    """Same existing tables on target database will be Merged together."""


class ActivityOnInactiveMarkAs(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status result of the activity when the state is set to Inactive. This is an optional property
    and if not provided when the activity is inactive, the status will be Succeeded by default.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SKIPPED = "Skipped"


class ActivityState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Activity state. This is an optional property and if not provided, the state will be Active by
    default.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"


class AmazonRdsForOraclePartitionOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AmazonRdsForOraclePartitionOption."""

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    DYNAMIC_RANGE = "DynamicRange"


class AvroCompressionCodec(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AvroCompressionCodec."""

    NONE = "none"
    DEFLATE = "deflate"
    SNAPPY = "snappy"
    XZ = "xz"
    BZIP2 = "bzip2"


class AzureFunctionActivityMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The list of HTTP methods supported by a AzureFunctionActivity."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    TRACE = "TRACE"


class AzureSearchIndexWriteBehaviorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specify the write behavior when upserting documents into Azure Search Index."""

    MERGE = "Merge"
    UPLOAD = "Upload"


class AzureStorageAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type used for authentication. Type: string."""

    ANONYMOUS = "Anonymous"
    ACCOUNT_KEY = "AccountKey"
    SAS_URI = "SasUri"
    SERVICE_PRINCIPAL = "ServicePrincipal"
    MSI = "Msi"


class BigDataPoolReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Big data pool reference type."""

    BIG_DATA_POOL_REFERENCE = "BigDataPoolReference"


class BlobEventType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BlobEventType."""

    MICROSOFT_STORAGE_BLOB_CREATED = "Microsoft.Storage.BlobCreated"
    MICROSOFT_STORAGE_BLOB_DELETED = "Microsoft.Storage.BlobDeleted"


class CassandraSourceReadConsistencyLevels(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The consistency level specifies how many Cassandra servers must respond to a read request
    before returning data to the client application. Cassandra checks the specified number of
    Cassandra servers for data to satisfy the read request. Must be one of
    cassandraSourceReadConsistencyLevels. The default value is 'ONE'. It is case-insensitive.
    """

    ALL = "ALL"
    EACH_QUORUM = "EACH_QUORUM"
    QUORUM = "QUORUM"
    LOCAL_QUORUM = "LOCAL_QUORUM"
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    LOCAL_ONE = "LOCAL_ONE"
    SERIAL = "SERIAL"
    LOCAL_SERIAL = "LOCAL_SERIAL"


class CellOutputType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Execution, display, or stream outputs."""

    EXECUTE_RESULT = "execute_result"
    DISPLAY_DATA = "display_data"
    STREAM = "stream"
    ERROR = "error"


class CompressionCodec(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """All available compressionCodec values."""

    NONE = "none"
    LZO = "lzo"
    BZIP2 = "bzip2"
    GZIP = "gzip"
    DEFLATE = "deflate"
    ZIP_DEFLATE = "zipDeflate"
    SNAPPY = "snappy"
    LZ4 = "lz4"
    TAR = "tar"
    TAR_G_ZIP = "tarGZip"


class ConfigurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the spark config."""

    DEFAULT = "Default"
    CUSTOMIZED = "Customized"
    ARTIFACT = "Artifact"


class CopyBehaviorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """All available types of copy behavior."""

    PRESERVE_HIERARCHY = "PreserveHierarchy"
    FLATTEN_HIERARCHY = "FlattenHierarchy"
    MERGE_FILES = "MergeFiles"


class CreateMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the mode of sql pool creation.

    Default: regular sql pool creation.

    PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql
    pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and
    restorePointInTime must be specified.

    Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as
    the recoverableDatabaseId to restore.

    Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId
    should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate
    must be specified.
    """

    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RECOVERY = "Recovery"
    RESTORE = "Restore"


class CredentialReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Credential reference type."""

    CREDENTIAL_REFERENCE = "CredentialReference"


class DataFlowComputeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Compute type of the cluster which will execute data flow job."""

    GENERAL = "General"
    MEMORY_OPTIMIZED = "MemoryOptimized"
    COMPUTE_OPTIMIZED = "ComputeOptimized"


class DataFlowDebugCommandType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The command type."""

    EXECUTE_PREVIEW_QUERY = "executePreviewQuery"
    EXECUTE_STATISTICS_QUERY = "executeStatisticsQuery"
    EXECUTE_EXPRESSION_QUERY = "executeExpressionQuery"


class DataFlowReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Data flow reference type."""

    DATA_FLOW_REFERENCE = "DataFlowReference"


class DatasetCompressionLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DatasetCompressionLevel."""

    OPTIMAL = "Optimal"
    FASTEST = "Fastest"


class DatasetReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Dataset reference type."""

    DATASET_REFERENCE = "DatasetReference"


class DayOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DayOfWeek."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class Db2AuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AuthenticationType to be used for connection. It is mutually exclusive with connectionString
    property.
    """

    BASIC = "Basic"


class DependencyCondition(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DependencyCondition."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    COMPLETED = "Completed"


class DynamicsAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """All available dynamicsAuthenticationType values."""

    OFFICE365 = "Office365"
    IFD = "Ifd"
    AAD_SERVICE_PRINCIPAL = "AADServicePrincipal"


class DynamicsDeploymentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """All available dynamicsDeploymentType values."""

    ONLINE = "Online"
    ON_PREMISES_WITH_IFD = "OnPremisesWithIfd"


class DynamicsServicePrincipalCredentialType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The service principal credential type to use in Server-To-Server authentication.
    'ServicePrincipalKey' for key/secret, 'ServicePrincipalCert' for certificate. Type: string (or
    Expression with resultType string).
    """

    SERVICE_PRINCIPAL_KEY = "ServicePrincipalKey"
    SERVICE_PRINCIPAL_CERT = "ServicePrincipalCert"


class DynamicsSinkWriteBehavior(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines values for DynamicsSinkWriteBehavior."""

    UPSERT = "Upsert"


class Enum13(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum13."""

    APPENDBLOCK = "appendblock"


class EventSubscriptionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Event Subscription Status."""

    ENABLED = "Enabled"
    PROVISIONING = "Provisioning"
    DEPROVISIONING = "Deprovisioning"
    DISABLED = "Disabled"
    UNKNOWN = "Unknown"


class ExpressionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Expression type."""

    EXPRESSION = "Expression"


class FtpAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to be used to connect to the FTP server."""

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"


class GoogleAdWordsAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The OAuth 2.0 authentication mechanism used for authentication. ServiceAuthentication can only
    be used on self-hosted IR.
    """

    SERVICE_AUTHENTICATION = "ServiceAuthentication"
    USER_AUTHENTICATION = "UserAuthentication"


class GoogleBigQueryAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The OAuth 2.0 authentication mechanism used for authentication. ServiceAuthentication can only
    be used on self-hosted IR.
    """

    SERVICE_AUTHENTICATION = "ServiceAuthentication"
    USER_AUTHENTICATION = "UserAuthentication"


class HBaseAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication mechanism to use to connect to the HBase server."""

    ANONYMOUS = "Anonymous"
    BASIC = "Basic"


class HdiNodeTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """All available HdiNodeTypes values."""

    HEADNODE = "Headnode"
    WORKERNODE = "Workernode"
    ZOOKEEPER = "Zookeeper"


class HDInsightActivityDebugInfoOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The HDInsightActivityDebugInfoOption settings to use."""

    NONE = "None"
    ALWAYS = "Always"
    FAILURE = "Failure"


class HiveAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication method used to access the Hive server."""

    ANONYMOUS = "Anonymous"
    USERNAME = "Username"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"


class HiveServerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Hive server."""

    HIVE_SERVER1 = "HiveServer1"
    HIVE_SERVER2 = "HiveServer2"
    HIVE_THRIFT_SERVER = "HiveThriftServer"


class HiveThriftTransportProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The transport protocol to use in the Thrift layer."""

    BINARY = "Binary"
    SASL = "SASL"
    HTTP = "HTTP "


class HttpAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to be used to connect to the HTTP server."""

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    DIGEST = "Digest"
    WINDOWS = "Windows"
    CLIENT_CERTIFICATE = "ClientCertificate"


class ImpalaAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to use."""

    ANONYMOUS = "Anonymous"
    SASL_USERNAME = "SASLUsername"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"


class IntegrationRuntimeEdition(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The edition for the SSIS Integration Runtime."""

    STANDARD = "Standard"
    ENTERPRISE = "Enterprise"


class IntegrationRuntimeEntityReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of this referenced entity."""

    INTEGRATION_RUNTIME_REFERENCE = "IntegrationRuntimeReference"
    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"


class IntegrationRuntimeLicenseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """License type for bringing your own license scenario."""

    BASE_PRICE = "BasePrice"
    LICENSE_INCLUDED = "LicenseIncluded"


class IntegrationRuntimeReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of integration runtime."""

    INTEGRATION_RUNTIME_REFERENCE = "IntegrationRuntimeReference"


class IntegrationRuntimeSsisCatalogPricingTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The pricing tier for the catalog database. The valid values could be found in
    https://azure.microsoft.com/en-us/pricing/details/sql-database/.
    """

    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PREMIUM_RS = "PremiumRS"


class IntegrationRuntimeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of integration runtime."""

    INITIAL = "Initial"
    STOPPED = "Stopped"
    STARTED = "Started"
    STARTING = "Starting"
    STOPPING = "Stopping"
    NEED_REGISTRATION = "NeedRegistration"
    ONLINE = "Online"
    LIMITED = "Limited"
    OFFLINE = "Offline"
    ACCESS_DENIED = "AccessDenied"


class IntegrationRuntimeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of integration runtime."""

    MANAGED = "Managed"
    SELF_HOSTED = "SelfHosted"


class JsonFormatFilePattern(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """JSON format file pattern. A property of JsonFormat."""

    SET_OF_OBJECTS = "setOfObjects"
    ARRAY_OF_OBJECTS = "arrayOfObjects"


class JsonWriteFilePattern(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """All available filePatterns."""

    SET_OF_OBJECTS = "setOfObjects"
    ARRAY_OF_OBJECTS = "arrayOfObjects"


class LivyStates(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The batch state."""

    NOT_STARTED = "not_started"
    STARTING = "starting"
    IDLE = "idle"
    BUSY = "busy"
    SHUTTING_DOWN = "shutting_down"
    ERROR = "error"
    DEAD = "dead"
    KILLED = "killed"
    SUCCESS = "success"
    RUNNING = "running"
    RECOVERING = "recovering"


class ManagedVirtualNetworkReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Managed Virtual Network reference type."""

    MANAGED_VIRTUAL_NETWORK_REFERENCE = "ManagedVirtualNetworkReference"


class MongoDbAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to be used to connect to the MongoDB database."""

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"


class NetezzaPartitionOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The partition mechanism that will be used for Netezza read in parallel."""

    NONE = "None"
    DATA_SLICE = "DataSlice"
    DYNAMIC_RANGE = "DynamicRange"


class NodeSize(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The level of compute power that each node in the Big Data pool has."""

    NONE = "None"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    X_LARGE = "XLarge"
    XX_LARGE = "XXLarge"
    XXX_LARGE = "XXXLarge"


class NodeSizeFamily(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of nodes that the Big Data pool provides."""

    NONE = "None"
    MEMORY_OPTIMIZED = "MemoryOptimized"


class NotebookParameterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Notebook parameter type."""

    STRING = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"


class NotebookReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Synapse notebook reference type."""

    NOTEBOOK_REFERENCE = "NotebookReference"


class ODataAadServicePrincipalCredentialType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specify the credential type (key or cert) is used for service principal."""

    SERVICE_PRINCIPAL_KEY = "ServicePrincipalKey"
    SERVICE_PRINCIPAL_CERT = "ServicePrincipalCert"


class ODataAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of authentication used to connect to the OData service."""

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    WINDOWS = "Windows"
    AAD_SERVICE_PRINCIPAL = "AadServicePrincipal"
    MANAGED_SERVICE_IDENTITY = "ManagedServiceIdentity"


class OraclePartitionOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The partition mechanism that will be used for Oracle read in parallel."""

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    DYNAMIC_RANGE = "DynamicRange"


class OrcCompressionCodec(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OrcCompressionCodec."""

    NONE = "none"
    ZLIB = "zlib"
    SNAPPY = "snappy"
    LZO = "lzo"


class ParameterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Parameter type."""

    OBJECT = "Object"
    STRING = "String"
    INT = "Int"
    FLOAT = "Float"
    BOOL = "Bool"
    ARRAY = "Array"
    SECURE_STRING = "SecureString"


class ParquetCompressionCodecEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ParquetCompressionCodecEnum."""

    NONE = "none"
    GZIP = "gzip"
    SNAPPY = "snappy"
    LZO = "lzo"


class PhoenixAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication mechanism used to connect to the Phoenix server."""

    ANONYMOUS = "Anonymous"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"


class PipelineReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Pipeline reference type."""

    PIPELINE_REFERENCE = "PipelineReference"


class PluginCurrentState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PluginCurrentState."""

    PREPARATION = "Preparation"
    RESOURCE_ACQUISITION = "ResourceAcquisition"
    QUEUED = "Queued"
    SUBMISSION = "Submission"
    MONITORING = "Monitoring"
    CLEANUP = "Cleanup"
    ENDED = "Ended"


class PolybaseSettingsRejectType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the RejectValue property is specified as a literal value or a percentage."""

    VALUE = "value"
    PERCENTAGE = "percentage"


class PrestoAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication mechanism used to connect to the Presto server."""

    ANONYMOUS = "Anonymous"
    LDAP = "LDAP"


class RecurrenceFrequency(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enumerates possible frequency option for the schedule trigger."""

    NOT_SPECIFIED = "NotSpecified"
    MINUTE = "Minute"
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"


class RequestStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enumerates possible request statuses."""

    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of managed identity for the workspace."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"


class ResourceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enumerates possible Status of the resource."""

    CREATING = "Creating"
    CREATED = "Created"
    FAILED = "Failed"


class RestServiceAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of authentication used to connect to the REST service."""

    ANONYMOUS = "Anonymous"
    BASIC = "Basic"
    AAD_SERVICE_PRINCIPAL = "AadServicePrincipal"
    MANAGED_SERVICE_IDENTITY = "ManagedServiceIdentity"
    O_AUTH2_CLIENT_CREDENTIAL = "OAuth2ClientCredential"


class RunQueryFilterOperand(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Parameter name to be used for filter. The allowed operands to query pipeline runs are
    PipelineName, RunStart, RunEnd and Status; to query activity runs are ActivityName,
    ActivityRunStart, ActivityRunEnd, ActivityType and Status, and to query trigger runs are
    TriggerName, TriggerRunTimestamp and Status.
    """

    PIPELINE_NAME = "PipelineName"
    STATUS = "Status"
    RUN_START = "RunStart"
    RUN_END = "RunEnd"
    ACTIVITY_NAME = "ActivityName"
    ACTIVITY_RUN_START = "ActivityRunStart"
    ACTIVITY_RUN_END = "ActivityRunEnd"
    ACTIVITY_TYPE = "ActivityType"
    TRIGGER_NAME = "TriggerName"
    TRIGGER_RUN_TIMESTAMP = "TriggerRunTimestamp"
    RUN_GROUP_ID = "RunGroupId"
    LATEST_ONLY = "LatestOnly"


class RunQueryFilterOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operator to be used for filter."""

    EQUALS = "Equals"
    NOT_EQUALS = "NotEquals"
    IN = "In"
    NOT_IN = "NotIn"
    IN_ENUM = "In"


class RunQueryOrder(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sorting order of the parameter."""

    ASC = "ASC"
    DESC = "DESC"


class RunQueryOrderByField(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Parameter name to be used for order by. The allowed parameters to order by for pipeline runs
    are PipelineName, RunStart, RunEnd and Status; for activity runs are ActivityName,
    ActivityRunStart, ActivityRunEnd and Status; for trigger runs are TriggerName,
    TriggerRunTimestamp and Status.
    """

    RUN_START = "RunStart"
    RUN_END = "RunEnd"
    PIPELINE_NAME = "PipelineName"
    STATUS = "Status"
    ACTIVITY_NAME = "ActivityName"
    ACTIVITY_RUN_START = "ActivityRunStart"
    ACTIVITY_RUN_END = "ActivityRunEnd"
    TRIGGER_NAME = "TriggerName"
    TRIGGER_RUN_TIMESTAMP = "TriggerRunTimestamp"


class SalesforceSinkWriteBehavior(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The write behavior for the operation. Default is Insert."""

    INSERT = "Insert"
    UPSERT = "Upsert"


class SalesforceSourceReadBehavior(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Salesforce read behavior for the operation."""

    QUERY = "Query"
    QUERY_ALL = "QueryAll"


class SapCloudForCustomerSinkWriteBehavior(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The write behavior for the operation. Default is 'Insert'."""

    INSERT = "Insert"
    UPDATE = "Update"


class SapHanaAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to be used to connect to the SAP HANA server."""

    BASIC = "Basic"
    WINDOWS = "Windows"


class SapHanaPartitionOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The partition mechanism that will be used for SAP HANA read in parallel."""

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    SAP_HANA_DYNAMIC_RANGE = "SapHanaDynamicRange"


class SapTablePartitionOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The partition mechanism that will be used for SAP table read in parallel."""

    NONE = "None"
    PARTITION_ON_INT = "PartitionOnInt"
    PARTITION_ON_CALENDAR_YEAR = "PartitionOnCalendarYear"
    PARTITION_ON_CALENDAR_MONTH = "PartitionOnCalendarMonth"
    PARTITION_ON_CALENDAR_DATE = "PartitionOnCalendarDate"
    PARTITION_ON_TIME = "PartitionOnTime"


class SchedulerCurrentState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SchedulerCurrentState."""

    QUEUED = "Queued"
    SCHEDULED = "Scheduled"
    ENDED = "Ended"


class ScriptActivityLogDestination(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The destination of logs. Type: string."""

    ACTIVITY_OUTPUT = "ActivityOutput"
    EXTERNAL_STORE = "ExternalStore"


class ScriptActivityParameterDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The direction of the parameter."""

    INPUT = "Input"
    OUTPUT = "Output"
    INPUT_OUTPUT = "InputOutput"


class ScriptActivityParameterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the parameter."""

    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    DATE_TIME_OFFSET = "DateTimeOffset"
    DECIMAL = "Decimal"
    DOUBLE = "Double"
    GUID = "Guid"
    INT16 = "Int16"
    INT32 = "Int32"
    INT64 = "Int64"
    SINGLE = "Single"
    STRING = "String"
    TIMESPAN = "Timespan"


class ScriptType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the query. Type: string."""

    QUERY = "Query"
    NON_QUERY = "NonQuery"


class ServiceNowAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to use."""

    BASIC = "Basic"
    O_AUTH2 = "OAuth2"


class SftpAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to be used to connect to the FTP server."""

    BASIC = "Basic"
    SSH_PUBLIC_KEY = "SshPublicKey"


class SparkAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication method used to access the Spark server."""

    ANONYMOUS = "Anonymous"
    USERNAME = "Username"
    USERNAME_AND_PASSWORD = "UsernameAndPassword"
    WINDOWS_AZURE_HD_INSIGHT_SERVICE = "WindowsAzureHDInsightService"


class SparkBatchJobResultType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Spark batch job result."""

    UNCERTAIN = "Uncertain"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"


class SparkConfigurationReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Spark configuration reference type."""

    SPARK_CONFIGURATION_REFERENCE = "SparkConfigurationReference"


class SparkErrorSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SparkErrorSource."""

    SYSTEM = "System"
    USER = "User"
    UNKNOWN = "Unknown"
    DEPENDENCY = "Dependency"


class SparkJobReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Synapse spark job reference type."""

    SPARK_JOB_DEFINITION_REFERENCE = "SparkJobDefinitionReference"


class SparkJobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The job type."""

    SPARK_BATCH = "SparkBatch"
    SPARK_SESSION = "SparkSession"


class SparkServerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Spark server."""

    SHARK_SERVER = "SharkServer"
    SHARK_SERVER2 = "SharkServer2"
    SPARK_THRIFT_SERVER = "SparkThriftServer"


class SparkThriftTransportProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The transport protocol to use in the Thrift layer."""

    BINARY = "Binary"
    SASL = "SASL"
    HTTP = "HTTP "


class SqlAlwaysEncryptedAkvAuthType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sql always encrypted AKV authentication type. Type: string."""

    SERVICE_PRINCIPAL = "ServicePrincipal"
    MANAGED_IDENTITY = "ManagedIdentity"
    USER_ASSIGNED_MANAGED_IDENTITY = "UserAssignedManagedIdentity"


class SqlConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the connection."""

    SQL_ON_DEMAND = "SqlOnDemand"
    SQL_POOL = "SqlPool"


class SqlPartitionOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The partition mechanism that will be used for Sql read in parallel."""

    NONE = "None"
    PHYSICAL_PARTITIONS_OF_TABLE = "PhysicalPartitionsOfTable"
    DYNAMIC_RANGE = "DynamicRange"


class SqlPoolReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL pool reference type."""

    SQL_POOL_REFERENCE = "SqlPoolReference"


class SqlScriptType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the SQL script."""

    SQL_QUERY = "SqlQuery"


class SsisLogLocationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of SSIS log location."""

    FILE = "File"


class SsisPackageLocationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of SSIS package location."""

    SSISDB = "SSISDB"
    FILE = "File"
    INLINE_PACKAGE = "InlinePackage"
    PACKAGE_STORE = "PackageStore"


class StoredProcedureParameterType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Stored procedure parameter type."""

    STRING = "String"
    INT = "Int"
    INT64 = "Int64"
    DECIMAL = "Decimal"
    GUID = "Guid"
    BOOLEAN = "Boolean"
    DATE = "Date"


class SybaseAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AuthenticationType to be used for connection."""

    BASIC = "Basic"
    WINDOWS = "Windows"


class TeamDeskAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to use."""

    BASIC = "Basic"
    TOKEN = "Token"


class TeradataAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AuthenticationType to be used for connection."""

    BASIC = "Basic"
    WINDOWS = "Windows"


class TeradataPartitionOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The partition mechanism that will be used for teradata read in parallel."""

    NONE = "None"
    HASH = "Hash"
    DYNAMIC_RANGE = "DynamicRange"


class TriggerReferenceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Trigger reference type."""

    TRIGGER_REFERENCE = "TriggerReference"


class TriggerRunStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Trigger run status."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    INPROGRESS = "Inprogress"


class TriggerRuntimeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enumerates possible state of Triggers."""

    STARTED = "Started"
    STOPPED = "Stopped"
    DISABLED = "Disabled"


class TumblingWindowFrequency(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enumerates possible frequency option for the tumbling window trigger."""

    MINUTE = "Minute"
    HOUR = "Hour"
    MONTH = "Month"


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Linked service reference type."""

    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"


class VariableType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Variable type."""

    STRING = "String"
    BOOL = "Bool"
    BOOLEAN = "Boolean"
    ARRAY = "Array"


class WebActivityMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The list of HTTP methods supported by a WebActivity."""

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class WebAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of authentication used to connect to the web table source."""

    BASIC = "Basic"
    ANONYMOUS = "Anonymous"
    CLIENT_CERTIFICATE = "ClientCertificate"


class WebHookActivityMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The list of HTTP methods supported by a WebHook activity."""

    POST = "POST"


class ZendeskAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication type to use."""

    BASIC = "Basic"
    TOKEN = "Token"
