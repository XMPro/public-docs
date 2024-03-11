# Azure Data Explorer

<img src="../../../../../.gitbook/assets/Azure Data Explorer Icon.png" alt="" data-size="line"> The Azure Data Explorer Connector allows you to connect to an Azure Data Explorer instance and retrieve data as requested by the Application.

The Azure Data Explorer platform is a fully managed, high-performance, big data analytics platform that makes it easy to analyze high volumes of data in near real-time.&#x20;

Please see their [store page](https://azure.microsoft.com/en-us/services/data-explorer/) and [documentation](https://docs.microsoft.com/en-us/azure/data-explorer/) for more information about the Azure Data Explorer platform.&#x20;

Read on for an [example](examples.md),[ ](broken-reference)its [configuration](configuration.md), and [release notes](release-notes.md).

### Live Updates

This Connector supports Live Updates, i.e. it can update the entity to display the most up-to-date information.&#x20;

This capability is available when the Connector is configured for time series data (See [Is Time Series](broken-reference)) and polling (See [Enable Polling](broken-reference)).

### Pre-requisites

The user must have credentials to an Azure subscription with permission to read Azure Data Explorer instances.

{% hint style="info" %}
Azure Data Explorer's Kusto limits the number of records returned to **500,000**, and the overall data size for those records to **64 MB**. Read more about limits on the result set size [here](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/concepts/query-limits#limit-on-result-set-size-result-truncation).
{% endhint %}

### Downloads

| Name                                | Link                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------- |
| Azure Data Explorer Connector v1.97 | [Request](mailto:support@xmpro.com?subject=AP-Connector-azure-data-explorer-connector-1.97) |

Please [contact](mailto:support@xmpro.com?subject=azure-data-explorer-connector-older-version) XMPro if you're looking for an older version of this Connector.&#x20;
