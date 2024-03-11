# Examples

The following examples can be found on this page:

* [ADX Table](examples.md#adx-table)
* [ADX Query with Parameters](examples.md#adx-query-with-parameters)

## ADX Table

This example Application demonstrates how to read telemetry data from a table in an Azure Data Explorer instance using this Connector.&#x20;

You can download the files [here](examples.md#step-4-use-the-connection) to try it out for yourself - adjusting the steps to use your **own** Azure credentials.&#x20;

{% hint style="info" %}
Refer to [configuration](broken-reference) to understand all configuration options of this Connector.
{% endhint %}

### Step 1: Add the Connection

From the Properties blade of the widget to which the Azure Data Explorer Connector will be linked, a data grid in our example, select the Data Source tab.&#x20;

Click the plus icon next to Data Source, then the plus icon next to Connection, and select the Azure Data Explorer Connector.

![Table Example Step 1: Add the Connection](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Table - Step 1.gif>)

### Step 2: Configure Server

Enter the authentication details: the Cluster Url, Tenant Id, Client Id, and Secret Key. In this case, tick to use variables.

![Table Example Step 2: Configure Server](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Table - Step 2.gif>)

### Step 3: Configure Database

Select the database, table, primary key, and columns to return. In this case:

* Database: TestDatabase
* Table: TruckTelemetry table
* Primary key: PumpId
* Columns: ReadingNo, PumpId, PumpInletPressure, and Timestamp&#x20;

If there is a need to select data from multiple tables, tick the **Specify ADX Query** option and provide the query in the **ADX Query** field.&#x20;

<figure><img src="../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Table - Step 3.gif" alt=""><figcaption><p>Table Example Step 3: Configure Database</p></figcaption></figure>

### Step 4: Use the Connection

Enter a name for the Connection, and click Save. In this case, set the name to Azure Data Explorer Connector.

Select the Connection that was just created, select the entity to read, and enter the Data Source name. Save the Data Source.

Note that the primary key is auto-populated once the entity is selected.&#x20;

![Table Example Step 4: Use the Connection](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Table - Step 4.gif>)

### Step 5: Use the Data Source

Select the Data Source we just added, and save the Application.

![Table Example Step 5: Use the Data Source](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Table - Step 5.gif>)

### Step 6: Results

Click the Launch button and view the results. Observe that telemetry data is returned from Azure Data Explorer.

![Table Example Step 6: Results](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Table - Step 6.gif>)

### Files

<table><thead><tr><th width="137.33333333333331">File</th><th width="450" data-type="files">Link</th><th>Security Key</th></tr></thead><tbody><tr><td>Application</td><td><a href="../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Table.xapp">Azure Data Explorer Connector Example - Table.xapp</a></td><td>C0mp|ex123</td></tr></tbody></table>

{% hint style="info" %}
See the [Import, Export, and Clone - XMPro](https://documentation.xmpro.com/how-tos/import-export-and-clone#importing) article for steps to import an Application.
{% endhint %}

## ADX Query with Parameters

This example Application demonstrates how to read telemetry data from an Azure Data Explorer instance using an ADX Query with Query Parameters.&#x20;

You can download the files [here](examples.md#files-1) to try it out for yourself - adjusting the steps to use your **own** Azure credentials.&#x20;

{% hint style="info" %}
Refer to [configuration ](broken-reference)to understand all configuration options of this Connector.
{% endhint %}

### Step 1: Add the Connection

From the Properties blade of the widget to which the Azure Data Explorer Connector will be linked, a chart in our example, select the Data Source tab.&#x20;

Click the plus icon next to Data Source and then the plus icon next to Connection.

<figure><img src="../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 1.png" alt=""><figcaption><p>Query Example Step 1a: Add the Connection</p></figcaption></figure>

Select the Azure Data Explorer Connector and enter a name for the connection. In this case, set the name to "ADX Connection".

<figure><img src="../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 1a.png" alt=""><figcaption><p>Query Example Step 1b: Select Connector and Name the Connection</p></figcaption></figure>

### Step 2: Configure Server

Enter the authentication details: the Cluster Url, Tenant ID, Client ID, and Secret Key. In this case, tick to use variables.

![Query Example Step 2: Configure Server](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 2.png>)

### Step 3: Configure Database

Select the Database, ADX Query, Primary Key, and Columns to Return. In this case:

* Database: TestDatabase
* ADX Query: `StormEvents` \
  `| where StartTime > queryparam("StartDate","DateTime","2007-01-01")` \
  `| where State in (queryparam("StateList","Dynamic","'ALABAMA','INDIANA'"))`\
  `| take queryparam("NumRecords","Int","100")`
* Primary key: StartTime
* Columns: StartTime and DamageProperty&#x20;

Click Save.

![Query Example Step 3: Configure Database](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 3.png>)

### Step 4: Use the Connection

Use the Connection that was just created to complete entering the new Data Source. Save the Data Source.

In this case, enter the Data Source name as "Name", the select the "ADX Connection", the entity to read as "ADX Query".&#x20;

**Note:** the primary key is auto-populated once the entity is selected.&#x20;

![Query Example Step 4: Use the Connection](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 4.png>)

### Step 5: Use the Data Source

Select the Data Source we just added.&#x20;

Click the pencil icon next to Parameters to bind the query parameter values from the query entered in [step 3](examples.md#step-3-configure-database-1).

![Query Example Step 5a: Use the Data Source](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 5.png>)

Click the pencil icon next to Filter to enter criteria: 'DamageProperty' is less than 50000.

Apply the filter and save the Application.

**Note:** When query parameter values are not provided, the default values provided in the query are used.

<figure><img src="../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 5a.png" alt=""><figcaption><p>Query Example Step 5b: Add a Filter</p></figcaption></figure>

### Step 6: Configure Chart Data

Next, we'll add Data Series to the chart. Expand the Axes accordion, and set the X Axis' data type to Date Time.&#x20;

![Query Example Step 6a: Configure Chart's X-Axis Type](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 6.png>)

In the Data accordion, click the plus icon next to Series. The series settings blade will open on the right. Set the name, color, X Axis Data, and Y Axis Data. In this case:

* Name: Property Damage
* Colour: Red

<figure><img src="../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 6a.png" alt=""><figcaption><p>Query Example Step 6b: Configure Chart's Series</p></figcaption></figure>

* X Axis Data: Start Time
* Y Axis Data: Damage Property

Click Apply and Close, and save the Application. Click the Launch button and view the chart.&#x20;

<figure><img src="../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 6b.png" alt=""><figcaption><p>Query Example Step 6c: Configure Chart's Series Continued</p></figcaption></figure>

### Step 7: Results

Observe that the chart is populated with data from Azure Data Explorer.

![Query Example Step 7: Results](<../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query with Parameters - Step 7.png>)

### Files

<table><thead><tr><th width="133">File</th><th width="467.7642469348242" data-type="files">Link</th><th>Security Key</th></tr></thead><tbody><tr><td>Application</td><td><a href="../../../../../.gitbook/assets/Azure Data Explorer Connector Example - Query">Azure Data Explorer Connector Example - Query</a></td><td>C0mp|ex123</td></tr></tbody></table>

{% hint style="info" %}
See the [Import, Export, and Clone - XMPro](https://documentation.xmpro.com/how-tos/import-export-and-clone#importing) article for steps to import an Application.
{% endhint %}
