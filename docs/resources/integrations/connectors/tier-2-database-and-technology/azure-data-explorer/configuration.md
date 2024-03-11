---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Configuration

This section explains each of the properties in the configuration blade.

![](<../../../../../.gitbook/assets/Azure Data Explorer Connector - Config 1.png>)

![](<../../../../../.gitbook/assets/Azure Data Explorer Connector - Config 2.png>)

<figure><img src="../../../../../.gitbook/assets/Azure Data Explorer Connector - Config 3.jpg" alt=""><figcaption></figcaption></figure>

### General Properties

#### Name

The name that will appear in the Data Source list.

### Server Properties

#### Use Connection Variables?

Tick to use [variables](https://app.gitbook.com/@xmpro/s/xmpro-solution/variable) for the [Cluster Url](configuration.md#cluster-url), [Tenant ID](configuration.md#tenant-id), [Client ID](configuration.md#client-id), and [Secret Key](configuration.md#secret-key) settings; or enter them manually.

#### Cluster Url

The Host Name used to create, start, edit, list, terminate, and delete clusters - in the format _https://{clusterName}.{location}.kusto.windows.net)_. \
\
You can find the URL on the Azure Portal blade for the Data Explorer Cluster under the "URI" property.

#### Tenant ID

The Id of the tenant to which the [Client](configuration.md#client-id) belongs.

#### Client ID

The Id of the Azure App Registration used to connect to the Azure Data Explorer instance.

#### Secret Key

The Secret of the Azure App Registration used to connect to the Azure Data Explorer instance.

### Database Properties

Once the [Server Properties](configuration.md#server-properties) are entered, the Connector attempts to open a connection with the database server. If successful, the [Database](configuration.md#database) dropdown is populated with a list of available databases.

#### Database

The name of the database to connect to.\
Once selected, the [Table](configuration.md#table) property is populated with the list of available tables and materialized views in the database.

#### Table

The name of the table or materialized view to connect to (applies when [Specify ADX Query](configuration.md#specify-adx-query) is not ticked).\
Once selected, the [Primary Key Column](configuration.md#primary-key-column) and [Columns To Return](configuration.md#columns-to-return) properties are populated with a list of the table's columns.

#### Specify ADX Query?

Tick to query using a KQL statement, or select a table (default).

#### Use Query Parameters?

Tick to use query parameters in the [ADX Query](configuration.md#adx-query) (applies when [Specify ADX Query](configuration.md#specify-adx-query) is ticked)\
\
_Below is an example of the query parameter format:_ `queryparam("StartTime","DateTime","2022-01-01")` \
\
Where _StartTime_ is the name, _DateTime_ is the data type (possible values are DateTime, Int, Long, Double, Boolean, String, Dynamic) and last attribute is the value of the parameter that is used to execute the query during configuration and also at runtime if parameter value is not supplied from app page. All 3 attributes should be enclosed in double quotes and the attribute value shouldn't contain a double quote. \
\
_Below is an example ADX Query using query parameters:_ \
`StormEvents` \
`| where StartTime > queryparam("StartDate","DateTime","2007-01-01")` \
`| where State in (queryparam("StateList","Dynamic","'ALABAMA','INDIANA'"))` \
`| take queryparam("NumRecords","Int","1000")`

#### ADX Query

Query Azure Data Explorer (ADX) through a KQL statement (applies when [Specify ADX Query](configuration.md#specify-adx-query) is ticked).&#x20;

{% hint style="info" %}
This is useful when querying data by joining multiple tables or applying aggregation to a variable column selection.\
\
Refer to [Identifier Quoting](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/schema-entities/entity-names#identifier-quoting) when your query includes identifiers that are the same as keywords or contain special characters.
{% endhint %}

#### Primary Key Column

The column used to uniquely identify each row.

#### Columns To Return

The columns which the Connector should return. If no columns are specified, all are returned.\
It is mandatory when **Use Timeseries Aggregation** is ticked.

#### Ignore TimeZone Info from DateTime values?

By default, DateTime values are assumed to be in UTC. \
Tick to ignore timezone and the apps will not convert the values to the local timezone.

{% hint style="info" %}
If aggregation is required AND optional column selection, the aggregation should be implemented within the ADX query.
{% endhint %}

{% hint style="info" %}
**Special Characters in Identifier Names**

These special characters are supported: (\_) Underscore, (-) Dash, (.) Period and ( ) Space.\
\
The following special characters in ADX Query are not supported and will result in errors:

* (\*) Asterisk (_Request is invalid and cannot be executed._)
* (\\) Backslash and (\\\\) Double Backslash (_Parse error. No Values will be displayed._)
* (.) Period (_No Values will be displayed._)

Refer to Azure Data Explorer's [Identifier Naming Rules](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/schema-entities/entity-names#identifier-naming-rules) for more information when creating your entity.
{% endhint %}

### Timeseries Settings Properties

#### Is Timeseries Data?

Tick if the [Table](configuration.md#table) or [ADX Query](configuration.md#adx-query) contains timeseries data.

#### Timestamp Column

The column that contains timestamp value and uniquely identifies each row.

#### Use Timeseries Aggregation?

Tick if aggregation is applied to the timeseries data.

### Aggregation Parameters Properties

This applies when [Is Timeseries Data](configuration.md#is-timeseries-data) and [Use Timeseries Aggregation](configuration.md#use-timeseries-aggregation) are ticked**.** Ensure at least one of the return columns is of numeric data type. Aggregation is applied to numeric columns, grouped by the remaining return columns.

#### Maximum Record Count

Specify the maximum number of records to be returned after applying dynamic aggregation.\
\
If the total number of records from the  [Table](configuration.md#table) or [ADX Query](configuration.md#adx-query) is below this number, the aggregation will not be applied and all rows will be returned.&#x20;

#### Aggregation Type

The aggregation options are Average, Minimum, Maximum, and Any.

### Live Notifications Properties

This applies when [Is Timeseries Data](configuration.md#is-timeseries-data) is ticked.

#### Enable Polling?

Tick to specify if connector should enable live updates.&#x20;

#### Polling Interval (seconds)

Specify how often connector should look for new records.
