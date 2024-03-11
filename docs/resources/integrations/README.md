# Integrations

## Agents

An [_Agent_](../../concepts/agent/) is a reusable object which forms the building block of a Data Stream. When a number of Agents are connected together, a Data Stream is formed.&#x20;

Each Agent is designed to perform a specific function in the stream. For example, they can be used to retrieve data from a database in real-time, display data, filter, sort the data, or save the data somewhere else, depending on the function of that individual Agent.

Looking for an Agent that is not on the list? Send us a [request](mailto:support@xmpro.com) or check out the [Framework](../../how-to-guides/agents/building-agents.md#overview) to create a new Agent yourself.

The following tables group the available Agents by tier:

### Tier 1 - Social & Communication

| <img src="../../.gitbook/assets/Email.png" alt="" data-size="line"> [Email](https://xmpro.gitbook.io/email/)    | Listener, Action Agent |
| --------------------------------------------------------------------------------------------------------------- | ---------------------- |
| <img src="../../.gitbook/assets/Twilio.png" alt="" data-size="line"> [Twilio](https://xmpro.gitbook.io/twilio/) | Action Agent           |

### Tier 2 - Database & Technology

| <img src="../../.gitbook/assets/icon (1).png" alt="" data-size="line"> [Azure Data Explorer](https://xmpro.gitbook.io/azure-data-explorer/)              | Listener, Context Provider, Action Agent  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| <img src="../../.gitbook/assets/Azure Data Factory Icon.png" alt="" data-size="line"> [Azure Data Factory](https://xmpro.gitbook.io/azure-data-factory/) | Action Agent                              |
| <img src="../../.gitbook/assets/azure data lake.svg" alt="" data-size="line"> [Azure Data Lake](https://xmpro.gitbook.io/azure-data-lake/)               | Action Agent                              |
| ![](../../.gitbook/assets/AzureDigitalTwin.png) [Azure Digital Twin](https://xmpro.gitbook.io/azure-digital-twin/)                                       | Listener, Context Provider, Action Agent  |
| <img src="../../.gitbook/assets/Azure Event Hub.png" alt="" data-size="line"> [Azure Event Hub](https://xmpro.gitbook.io/azure-event-hub/)               | Listener, Action Agent                    |
| <img src="../../.gitbook/assets/azure-iot-hub.png" alt="" data-size="line"> [Azure IoT Hub](https://xmpro.gitbook.io/azure-iot-hub/)                     | Listener                                  |
| <img src="../../.gitbook/assets/timeseries.png" alt="" data-size="line"> [Azure Time Series](https://xmpro.gitbook.io/azure-time-series/) _(Deprecated)_ | Listener                                  |
| <img src="../../.gitbook/assets/cognite.png" alt="" data-size="line"> [Cognite](https://xmpro.gitbook.io/cognite/)                                       | Listener, Context Provider                |
| <img src="../../.gitbook/assets/Excel File Reader.png" alt="" data-size="line"> [Excel File Reader](https://xmpro.gitbook.io/excel-file-reader/)         | Action Agent                              |
| <img src="../../.gitbook/assets/ifm.png" alt="" data-size="line"> [ifm](https://xmpro.gitbook.io/ifm/)                                                   | Listener                                  |
| <img src="../../.gitbook/assets/influx db.png" alt="" data-size="line"> [InfluxDB](https://xmpro.gitbook.io/influxdb/)                                   | Listener, Context Provider, Action Agent  |
|  <img src="../../.gitbook/assets/Litmus.png" alt="" data-size="line">   [Litmus Edge OPC UA](https://xmpro.gitbook.io/litmus-edge-opc-ua/)               | Listener, Action Agent                    |
|  <img src="../../.gitbook/assets/mongodb-icon.png" alt="" data-size="line">   [MongoDB](https://xmpro.gitbook.io/mongodb/)                               | Listener, Context Provider, Action Agent  |
| <img src="../../.gitbook/assets/MOVUS.png" alt="" data-size="line"> [MOVUS](https://xmpro.gitbook.io/movus/)                                             | Listener, Context Provider, Action Agent  |
| <img src="../../.gitbook/assets/mysql.png" alt="" data-size="line"> [MySQL](https://xmpro.gitbook.io/mysql/)                                             | Listener, Context Provider, Action Agent  |
| <img src="../../.gitbook/assets/OData.png" alt="" data-size="line"> [OData](https://xmpro.gitbook.io/odata/)                                             | Context Provider, Action Agent            |
| <img src="../../.gitbook/assets/ODBC Icon.png" alt="" data-size="line"> [ODBC](https://xmpro.gitbook.io/odbc/)                                           | Listener, Context Provider                |
| <img src="../../.gitbook/assets/opc (2).png" alt="" data-size="line">[OPC DA](https://xmpro.gitbook.io/opc-da/)                                          | Listener, Action Agent                    |
| ![](../../.gitbook/assets/opc.png) [OPC UA](https://xmpro.gitbook.io/opc-ua/)                                                                            | Listener, Action Agent                    |
| <img src="../../.gitbook/assets/Oracle.png" alt="" data-size="line"> [Oracle](https://xmpro.gitbook.io/oracle/)                                          | Action Agent                              |
| <img src="../../.gitbook/assets/Snowflake logo.png" alt="" data-size="line"> [Snowflake](https://xmpro.gitbook.io/snowflake/)                            | Listener, Context Provider, Action Agent  |

### Tier 3 - ERP & Advanced App

| <img src="../../.gitbook/assets/Erbessed.png" alt="" data-size="line"> [Erbessed](https://xmpro.gitbook.io/erbessd/)                                               | Listener, Context Provider               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| <img src="../../.gitbook/assets/iPOS.png" alt="" data-size="line"> [iPOS](https://xmpro.gitbook.io/ipos/)                                                          | Action Agent                             |
| <img src="../../.gitbook/assets/FinOps.PNG" alt="" data-size="line"> [FinOps](https://xmpro.gitbook.io/finops/)                                                    | Context Provider, Action Agent           |
| <img src="../../.gitbook/assets/Nanoprecise.png" alt="" data-size="line"> [Nanoprecise](https://xmpro.gitbook.io/nanoprecise/)                                     | Listener, Context Provider, Action Agent |
| <img src="../../.gitbook/assets/OSIsoft.png" alt="" data-size="line"> [OSIsoft PI](https://xmpro.gitbook.io/osisoft-pi/)                                           | Listener, Context Provider, Action Agent |
| <img src="../../.gitbook/assets/Tango.png" alt="" data-size="line"> [Tango](https://xmpro.gitbook.io/tango/)                                                       | Listener, Context Provider               |
| <img src="../../.gitbook/assets/deviceWISE_favicon_144x144.png" alt="" data-size="line"> [Telit deviceWise](https://xmpro.gitbook.io/telit-devicewise/)            | Listener, Context Provider, Action Agent |
| <img src="../../.gitbook/assets/image.png" alt="" data-size="line"> [Telit MQTT](https://xmpro.gitbook.io/telit-mqtt)                                              | Listener, Action Agent                   |
| <img src="../../.gitbook/assets/image (1).png" alt="" data-size="line"> [Telit OPC UA](https://xmpro.gitbook.io/telit-opc-ua/)                                     | Listener, Action Agent                   |
| <img src="../../.gitbook/assets/Salesforce.png" alt="" data-size="line"> [Salesforce](https://xmpro.gitbook.io/salesforce/)                                        | Listener, Context Provider, Action Agent |
| <img src="../../.gitbook/assets/sap.png" alt="" data-size="line"> [SAP](https://xmpro.gitbook.io/sap/)                                                             | Context Provider, Action Agent           |
| <img src="../../.gitbook/assets/sap (1).png" alt="" data-size="line"> [SAP HANA](https://xmpro.gitbook.io/sap-hana/)                                               | Context Provider, Action Agent           |
| <img src="../../.gitbook/assets/Streaming data platform.png" alt="" data-size="line"> [Streaming Data Platform](https://xmpro.gitbook.io/streaming-data-platform/) | Listener, Context Provider               |

### Tier 4 - AI, Data Science & Custom

| <img src="../../.gitbook/assets/openai-logo.png" alt="" data-size="line"> [Azure OpenAI](https://xmpro.gitbook.io/azure-openai/)    | AI & Machine Learning |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| <img src="../../.gitbook/assets/Amber.png" alt="" data-size="line"> [Boon Amber](https://xmpro.gitbook.io/boon-amber/)              | AI & Machine Learning |
| <img src="../../.gitbook/assets/FFT.png" alt="" data-size="line"> [FFT](https://xmpro.gitbook.io/fft/)                              | Function              |
| <img src="../../.gitbook/assets/SignalFilter.jpg" alt="" data-size="line"> [Signal Filter](https://xmpro.gitbook.io/signal-filter/) | Function              |
| <img src="../../.gitbook/assets/webscraper icon.png" alt="" data-size="line"> [WebScraper](https://xmpro.gitbook.io/webscraper/)    | Context Provider      |

### Tier 5 - Free & Open Source

{% hint style="info" %}
Download the tier 5 files [here](https://xmappstore.blob.core.windows.net/tier5/Tier%205%20-%20Agents.zip).&#x20;

Use these individual files if you are not on v4.1.13 or higher:&#x20;

* [Action Agents](https://xmappstore.blob.core.windows.net/tier5/Tier%205%20-%20Action%20Agents.zip)
* [AI & ML](https://xmappstore.blob.core.windows.net/tier5/Tier%205%20-%20AI\_ML.zip)
* [Context Providers](https://xmappstore.blob.core.windows.net/tier5/Tier%205%20-%20Context%20Providers.zip)
* [Functions](https://xmappstore.blob.core.windows.net/tier5/Tier%205%20-%20Functions.zip)
* [Listeners](https://xmappstore.blob.core.windows.net/tier5/Tier%205%20-%20Listeners.zip)

\
Links for the larger AI & ML Agents\* are on their individual documentation pages.
{% endhint %}

| <img src="../../.gitbook/assets/anomaly-detection.png" alt="" data-size="line"> [Anomaly Detection](https://xmpro.gitbook.io/anomaly-detection/)               | AI & Machine Learning\*                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| <img src="../../.gitbook/assets/Azure ML.png" alt="" data-size="line"> [Azure ML](https://xmpro.gitbook.io/azure-ml/)                                          | AI & Machine Learning                    |
| <img src="../../.gitbook/assets/AzureSQL.png" alt="" data-size="line"> [Azure SQL](https://xmpro.gitbook.io/azure-sql/)                                        | Listener, Context Provider, Action Agent |
| <img src="../../.gitbook/assets/Binary Classification.png" alt="" data-size="line"> [Binary Classification](https://xmpro.gitbook.io/binary-classification/)   | AI & Machine Learning\*                  |
| ![](../../.gitbook/assets/CFU.png) [Convert Flow Units](https://xmpro.gitbook.io/convert-flow-units/)                                                          | Function                                 |
| <img src="../../.gitbook/assets/icon.png" alt="" data-size="line"> [CRC16](https://xmpro.gitbook.io/crc16/)                                                    | Function                                 |
| <img src="../../.gitbook/assets/CSV.png" alt="" data-size="line"> [CSV](https://xmpro.gitbook.io/csv/)                                                         | Listener, Context Provider, Action Agent |
| <img src="../../.gitbook/assets/Fixed Width.png" alt="" data-size="line"> [Fixed Width File Reader](https://xmpro.gitbook.io/fixed-width-file-reader/)         | Action Agent                             |
| <img src="../../.gitbook/assets/Forecasting.png" alt="" data-size="line"> [Forecasting](https://xmpro.gitbook.io/forecasting-agent/)                           | AI & Machine Learning\*                  |
| <img src="../../.gitbook/assets/GoalSeek.png" alt="" data-size="line"> [Goal Seek](https://xmpro.gitbook.io/goal-seek/)                                        | Function                                 |
| <img src="../../.gitbook/assets/JSON File Context Provider.png" alt="" data-size="line"> [JSON](https://xmpro.gitbook.io/json/)                                | Context Provider, Transformation         |
| <img src="../../.gitbook/assets/KMeans Clustering.png" alt="" data-size="line"> [Kmeans Clustering](https://xmpro.gitbook.io/kmeans-clustering/)               | AI & Machine Learning\*                  |
| <img src="../../.gitbook/assets/linear interpolation.png" alt="" data-size="line">[Linear Interpolation](https://xmpro.gitbook.io/linear-interpolation/)       | Function                                 |
| <img src="../../.gitbook/assets/Min Max.png" alt="" data-size="line"> [Min Max](https://xmpro.gitbook.io/min-max/)                                             | Function                                 |
| <img src="../../.gitbook/assets/MLflow icon.png" alt="" data-size="line"> [MLflow](https://xmpro.gitbook.io/mlflow/)                                           | AI & Machine Learning                    |
| <img src="../../.gitbook/assets/MQTT.png" alt="" data-size="line"> [MQTT](https://xmpro.gitbook.io/mqtt-listener/)                                             | Listener, Action Agent                   |
| <img src="../../.gitbook/assets/issue-labeler.png" alt="" data-size="line"> [Multi Class Classification](https://xmpro.gitbook.io/multi-class-classification/) | AI & Machine Learning\*                  |
| <img src="../../.gitbook/assets/pdf converter.png" alt="" data-size="line"> [PDF Converter](https://xmpro.gitbook.io/pdf-converter/)                           | Action Agent                             |
| <img src="../../.gitbook/assets/python2.png" alt="" data-size="line"> [Python](https://xmpro.gitbook.io/python/)                                               | AI & Machine Learning                    |
| <img src="../../.gitbook/assets/Regression.png" alt="" data-size="line"> [Regression](https://xmpro.gitbook.io/regression/)                                    | AI & Machine Learning\*                  |
| <img src="../../.gitbook/assets/rest.png" alt="" data-size="line"> [REST API](https://xmpro.gitbook.io/rest-api/)                                              | Context Provider, Action Agent           |
| <img src="../../.gitbook/assets/Rounding.png" alt="" data-size="line"> [Rounding](https://xmpro.gitbook.io/rounding/)                                          | Function                                 |
| <img src="../../.gitbook/assets/R.png" alt="" data-size="line">  [RScript](https://xmpro.gitbook.io/rscript/)                                                  | AI & Machine Learning                    |
| <img src="../../.gitbook/assets/SQL Server.png" alt="" data-size="line"> [SQL Server](https://xmpro.gitbook.io/sql-server/)                                    | Listener, Context Provider, Action Agent |
| <img src="../../.gitbook/assets/XML Reader.png" alt="" data-size="line"> [XML File Reader](https://xmpro.gitbook.io/xml-file-reader/)                          | Action Agent                             |

### Tier 6 - XMPro Internal

{% hint style="info" %}
Download the tier 6 files [here](https://xmappstore.blob.core.windows.net/tier6/Tier%206%20-%20Agents.zip).

Use these individual files if you are not on v4.1.13 or higher:&#x20;

* [Action Agents](https://xmappstore.blob.core.windows.net/tier6/Tier%206%20-%20Action%20Agents.zip)
* [Functions](https://xmappstore.blob.core.windows.net/tier6/Tier%206%20-%20Functions.zip)
* [Listeners](https://xmappstore.blob.core.windows.net/tier6/Tier%206%20-%20Listeners.zip)
* [Recommendations](https://xmappstore.blob.core.windows.net/tier6/Tier%206%20-%20Recommendations.zip)
* [Transformations](https://xmappstore.blob.core.windows.net/tier6/Tier%206%20-%20Transformations.zip)
{% endhint %}

<table data-header-hidden><thead><tr><th width="150">Agent</th><th>Type</th></tr></thead><tbody><tr><td><img src="../../.gitbook/assets/Aggregate.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/aggregate/">Aggregate</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/alter-attribute-64.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/alter-attributes/">Alter Attributes</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/AUC.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/area-under-the-curve/">Area Under the Curve</a></td><td>Function</td></tr><tr><td><img src="../../.gitbook/assets/Batch Identifier.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/batch-identifier/">Batch Identifier</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Broadcast.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/broadcast/">Broadcast</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Calculated Field.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/calculated-field/">Calculated Field</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/ActionRequestIcon.png" alt=""> <a href="https://xmpro.gitbook.io/action-request-agents/">Close Action Request</a></td><td>Recommendation</td></tr><tr><td><img src="../../.gitbook/assets/concat.png" alt=""><a href="https://xmpro.gitbook.io/concatenate-row-values/">Concatenate Row Values</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Data Conversion.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/data-conversion">Data Conversion</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Edge Analysis.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/edge-analysis/">Edge Analysis</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Event Printer.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/event-printer/">Event Printer</a></td><td>Action Agent</td></tr><tr><td><img src="../../.gitbook/assets/Event Simulator.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/event-simulator/">Event Simulator</a></td><td>Listener</td></tr><tr><td><img src="../../.gitbook/assets/File Monitor.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/file/">File Listener</a></td><td>Listener</td></tr><tr><td><img src="../../.gitbook/assets/Filter.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/filter/">Filter</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/GeoFence.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/geofence/">Geofence</a></td><td>Function</td></tr><tr><td><img src="../../.gitbook/assets/Group and Merge.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/group-and-merge/">Group &#x26; Merge</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Join.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/join/">Join</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Missing Values Detector.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/missing-values-detector/">Missing Value Detector</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Missing Values Substitutor.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/missing-value-substitutor/">Missing Value Substitutor</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/NormalizeFieldsIcon.png" alt=""> <a href="https://xmpro.gitbook.io/normalize-fields/">Normalize Fields</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Pass Through.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/pass-through/">Pass Through</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/pivot.png" alt=""> <a href="https://xmpro.gitbook.io/pivot-table/">Pivot Table</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/RandomNumberIcon.png" alt=""> <a href="https://xmpro.gitbook.io/random-numbers/">Random Number</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/ActionRequestIcon.png" alt=""> <a href="https://xmpro.gitbook.io/action-request-agents/">Read Action Request</a></td><td>Recommendation</td></tr><tr><td><img src="../../.gitbook/assets/Read Recommendation.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/read-recommendation/">Read Recommendation </a></td><td>Recommendation</td></tr><tr><td><img src="../../.gitbook/assets/Resolve Recommendation.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/resolve-recommendation/">Resolve Recommendation</a></td><td>Recommendation</td></tr><tr><td><img src="../../.gitbook/assets/Row Count.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/row-count/">Row Count</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Row Padding.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/row-padding/">Row Padding</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Run Recommendation.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/run-recommendation">Run Recommendation</a></td><td>Recommendation</td></tr><tr><td><img src="../../.gitbook/assets/Sort.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/sort/">Sort</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Threshold Monitor.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/threshold-monitor/">Threshold Monitor</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/pivot.png" alt=""><a href="https://xmpro.gitbook.io/transpose/">Transpose</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Trim.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/trim/">Trim</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/Union.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/union/">Union</a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/UnzipIcon.png" alt=""> <a href="https://xmpro.gitbook.io/unzip/">Unzip</a></td><td>Action Agent</td></tr><tr><td><img src="../../.gitbook/assets/Update Recommendation.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/update-recommendation/">Update Recommendation</a></td><td>Recommendation</td></tr><tr><td><img src="../../.gitbook/assets/Window.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/window/">Window </a></td><td>Transformation</td></tr><tr><td><img src="../../.gitbook/assets/XMPro App.png" alt="" data-size="line"> <a href="https://xmpro.gitbook.io/xmpro-app/">XMPro App</a></td><td>Action Agent</td></tr></tbody></table>

## Connectors

A [_Connector_](../../concepts/connector.md) is a pre-built integration plug-in for the XMPro App Designer that allows you to connect to third-party data sources without having to code.

Whereas the Agents in a published Data Stream continuously poll for data, the Connectors in a published App retrieve data on an ad-hoc basis.

{% hint style="info" %}
Download the tier 5 & 6 files [here](https://xmappstore.blob.core.windows.net/tier5/Tier%205%20%26%206%20-%20Connectors.zip).
{% endhint %}

The following tables group the available Connectors by tier:

### Tier 2 - Database & Technology

| <img src="../../.gitbook/assets/icon (1).png" alt="" data-size="line"> [Azure Data Explorer Connector](connectors/tier-2-database-and-technology/azure-data-explorer/) |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../../.gitbook/assets/AzureDigitalTwin.png) [Azure Digital Twin Connector](https://xmpro.gitbook.io/azure-digital-twin-connector/)                                 |
| <img src="../../.gitbook/assets/Snowflake logo.png" alt="" data-size="line"> [Snowflake Connector](https://xmpro.gitbook.io/snowflake-connector/)                      |

### Tier 3 - ERP & Advanced App

| <img src="../../.gitbook/assets/Erbessd Logo.png" alt="" data-size="line"> [Erbessd Connector](https://xmpro.gitbook.io/erbessd-connector/)                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="../../.gitbook/assets/Nanoprecise.png" alt="" data-size="line"> [Nanoprecise Connector](https://xmpro.gitbook.io/nanoprecise-connector/)              |
| <img src="../../.gitbook/assets/OSISoft.png" alt="" data-size="line"> [OSIsoft PI Connector](https://xmpro.gitbook.io/osisoft-pi-connector/)                    |
| <img src="../../.gitbook/assets/OSISoft.png" alt="" data-size="line"> [OSIsoftPI Histogram Connector](https://xmpro.gitbook.io/osisoft-pi-histogram-connector/) |

### Tier 5 - Free & Open Source

| <img src="../../.gitbook/assets/AzureSQL.png" alt="" data-size="line">[Azure SQL Connector](https://xmpro.gitbook.io/azure-sql-connector/)               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="../../.gitbook/assets/JSON.png" alt="" data-size="line">[JSON Connector](https://xmpro.gitbook.io/json-connector/)                             |
| <img src="../../.gitbook/assets/SQL Server.png" alt="" data-size="line"> [SQL Server Connector](https://xmpro.gitbook.io/sql-server-connector/)          |
| <img src="../../.gitbook/assets/SQL Server.png" alt="" data-size="line"> [TSC SQL Server Connector](https://xmpro.gitbook.io/tsc-sql-server-connector/)  |

### Tier 6 - XMPro Internal Connectors

| <img src="../../.gitbook/assets/DS Icon.png" alt="" data-size="line"> [Data Streams Connector](https://xmpro.gitbook.io/data-streams-connector/) |
| ------------------------------------------------------------------------------------------------------------------------------------------------ |

## Visualization Blocks

An App Designer [_visualization block_](../../blocks/visualizations/) allows a no-code way to integrate with third-party systems and create rich user experiences. Listed below are some of the integration blocks found in the App Designer toolbox:&#x20;

<table data-header-hidden><thead><tr><th width="383">Name</th></tr></thead><tbody><tr><td><img src="../../.gitbook/assets/Autodesk-Forge-icon (1).png" alt=""> <a href="../../blocks/visualizations/autodesk-forge.md">Autodesk Forge</a></td></tr><tr><td><img src="../../.gitbook/assets/d3widget-icon.png" alt=""> <a href="../../blocks/visualizations/d3-visualization.md">D3 Visualization</a></td></tr><tr><td><img src="../../.gitbook/assets/esri-arcgis-icon.png" alt=""> <a href="../../blocks/visualizations/esri-map.md">Esri Map</a></td></tr><tr><td><img src="../../.gitbook/assets/pivot-grid-icon.png" alt=""> <a href="../../blocks/visualizations/pivot-grid.md">Pivot Grid</a></td></tr><tr><td><img src="../../.gitbook/assets/powerbi-icon.png" alt=""> <a href="../../blocks/visualizations/power-bi.md">Power BI</a></td></tr><tr><td><img src="../../.gitbook/assets/trendchart-icon.png" alt=""> <a href="../../blocks/visualizations/time-series-chart.md">Time Series Chart</a></td></tr><tr><td><img src="../../.gitbook/assets/unity-icon.png" alt=""> <a href="../../blocks/visualizations/unity-1.md">Unity</a></td></tr></tbody></table>
