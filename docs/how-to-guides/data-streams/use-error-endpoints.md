# Use Error Endpoints

When data flows from one Agent to another, a particular Agent may fail to process a certain data point during runtime. When this happens, the data point that failed and the reason why it failed will be passed through the error endpoint instead of going forward to the output endpoint. Each Agent displays its own errors, and therefore this can be a useful tool for debugging particular Agents.

{% hint style="info" %}
It is recommended that you read the article listed below to improve your understanding of Agents.

* [Agent](../../concepts/agent/)
* [How to Manage Data Streams](manage-data-streams.md)
{% endhint %}

## How to Use Error Endpoints

To use an error endpoint, follow the steps below:

1. Click on the red endpoint and drag the arrow to where you want to error data to flow. In this example, the error endpoints are going to be printed using an _Event Printer_ Agent.

&#x20;   2\. Click on _Save_.\
&#x20;   3\. To view the error data, click on _Publish_.

![](../../.gitbook/assets/ER\_1.png)

![](../../.gitbook/assets/ER\_2.png)

&#x20;   4\. Click on _Live View._\
&#x20;   5_._ Click on the Event Printer to display errors that occur during runtime.\
&#x20;   6\. Click on Save.

![](../../.gitbook/assets/ER\_3.png)

The data printed for the Error Endpoint includes the AgentID of the Agent that had the error, as well as the timestamp of when the error occurred. The message of the error is also printed. The exact data from the data points are also printed.

Instead of using the Event Printer to print errors, Error Endpoints can also connect to actions that trigger at the time of the error. For example, the following will send an email to a configured email address if an error occurs.&#x20;

![](../../.gitbook/assets/ER\_4.png)

## Handling multiple errors from Error Endpoints

A Union can be used to handle multiple errors at a time. To use the union Agent to do this, follow the steps below:

1. Under the _Transformation A_gents, drag and drop a _Union_ Agent onto the Data Stream.

![](../../.gitbook/assets/ER\_5.png)

&#x20;   2\. Connect the error endpoints of multiple Agents to the union.\
&#x20;   3\. Add another Agent to deal with all the errors at the same time.

![](../../.gitbook/assets/ER\_6.png)
