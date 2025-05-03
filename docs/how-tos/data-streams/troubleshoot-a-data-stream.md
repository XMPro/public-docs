# Troubleshoot a Data Stream

When creating and configuring a Data Stream, there is a chance it may not be working as expected, and you may have to find out more information as to why it is not behaving the way it should. There are a few options available on how to troubleshoot a Data Stream. Troubleshooting is required if you want to make sure the flow of data is accurate.

{% hint style="info" %}
It is recommended that you read the article listed below to improve your understanding of Data Streams.

* [Data Stream](../../concepts/data-stream/)
* [How to Manage Data Streams](manage-data-streams.md)
{% endhint %}

## Troubleshoot using Live View

To troubleshoot using the Live View, follow the steps below:

1. Click on _Publish_.

![](<../../.gitbook/assets/TS\_1 (1).png>)

&#x20;   2\. Click on _Live View_.\
&#x20;   3\. Select the Agent/s to view the Live Data for.\
&#x20;   4\. Click _Save_.

![](<../../.gitbook/assets/TS\_2 (1).png>)

{% hint style="info" %}
If data is not being displayed when it should be, or if the values are not being displayed as expected, something may be going wrong with the Agent.
{% endhint %}

![](<../../.gitbook/assets/Manage DS\_HowToOpen2.png>)

![](../../.gitbook/assets/TS\_4.png)

## Troubleshooting using Error Endpoints

To Troubleshoot using the Error Endpoints, follow the steps below:

1. Drag an _Event Printer_ agent onto the canvas. They can be found under ‘Action Agents.’
2. Add an arrow from the error endpoint connected to the Event Printer.
3. Click on _Publish_.

![](<../../.gitbook/assets/TS\_5 (1).png>)

&#x20;   4\. Click on _Live View_.\
&#x20;   5\. Select the _Event Printer_.\
&#x20;   6\. Click _Save_.

![](../../.gitbook/assets/TS\_6.png)

## Troubleshooting when there is no data visible

In some cases, the Event Printer does not show any data when trying to troubleshoot the Data Stream. If this is the case, the Collections Stream Host may be able to give some information. &#x20;

1. Open the _Collections_ page from the left-hand menu.
2. Click on the _Collection_.
3. Click on _Stream Hosts_.
4. Select the Stream Host.
5. View the logs from the Stream Host.

{% hint style="info" %}
Any errors that are generated from an Agent which are printed from the error endpoint are also printed in the Stream Host logs.&#x20;
{% endhint %}

![](<../../.gitbook/assets/image (1005).png>)

## Troubleshooting when there are no Stream Hosts

If the Stream Host is not running at all, you can view the logs from the install directory of the Stream Host on your computer. the install folder is named _XMPro Stream Host_ and is usually found in the _Program Files_ in the _C Drive_.

![](<../../.gitbook/assets/image (1333).png>)

![](../../.gitbook/assets/Troubleshoot\_9.png)

![](../../.gitbook/assets/Troubleshoot\_10.png)

![](../../.gitbook/assets/Troubleshoot\_11.png)
