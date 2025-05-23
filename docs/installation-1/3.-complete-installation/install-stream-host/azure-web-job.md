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
    visible: false
---

# Azure Web Job

## Prerequisites

The first Azure Web Job is created as part of the Azure ARM Template and has already met the [**hardware** requirements](../../install.md#hardware-requirements) and [**software** requirements](../../install.md#software-requirements).

If you require more Stream Hosts, follow these steps to add additional Azure Web Job Stream hosts.

## Setting up a Web Job

XMPro Stream Host can be hosted as a Web Job in Azure. Following are the steps required to set up a web job:

&#x20; 1\. Install a Stream Host locally as a Console Application

{% hint style="danger" %}
**Warning:** Read the instructions in the [Install Stream Host on Windows x64 article](windows-x64.md).
{% endhint %}

&#x20; 2\. Copy the installed files and add them to this [zip](https://firebasestorage.googleapis.com/v0/b/gitbook-legacy-files/o/assets%2F-MZAQh4Gn3jXbTJU2Mb4%2F-MdQnhG4EDOuuKUgRaen%2F-Md\_\_5-am8y9M1w3Ms85%2FSH%20WebJob.zip?alt=media\&token=31a4ebd0-111a-4081-af43-dbfef057e559)

{% hint style="info" %}
Installed files can usually be found at _C:\Program Files\XMPro Stream Host\\\*_
{% endhint %}

&#x20; 3\. Azure may restrict file uploads to 50Mb. If so, remove these from the zip to cut down the size:

* Cache folder
* Logs folder
* \*.jar files
* \*.pdb

&#x20; 4\. Create a Web Job as per the instructions on the [Microsoft Documentation site](https://docs.microsoft.com/en-us/azure/app-service/webjobs-create#CreateContinuous).

&#x20; 5\. Choose the following settings:

| **Name**    | **Value**                    |
| ----------- | ---------------------------- |
| File Upload | Select the zip created above |
| Type        | Continuous                   |
| Scale       | Single Instance              |

{% hint style="info" %}
It is recommended to use a separate App service for Web Jobs to keep Data Stream Designer and Stream Hosts separate.
{% endhint %}

## Next Step: Agents & Connectors

The stream host installation is complete. Please click below to install the default Agents & Connectors:

{% content-ref url="../install-connectors.md" %}
[install-connectors.md](../install-connectors.md)
{% endcontent-ref %}
