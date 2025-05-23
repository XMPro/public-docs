---
description: v4.3.1
---

# Configure Auto Scale (Optional)

{% embed url="https://youtu.be/hpusWm3GEko" %}

## Overview

Data caching is a technique used to improve the performance and responsiveness of applications. It works by storing frequently accessed data in a fast and easily accessible location.&#x20;

When an application needs the data it can be retrieved quickly without having to go through time-consuming operations like accessing a database.

_Distributed caching_ takes the concept of caching further by caching data in an external service accessible by one or more servers. This approach offers several benefits, including increased capacity to handle larger amounts of data, synchronized data across servers, and better scalability. By distributing the cache, the overall performance of the application can be enhanced, ensuring faster response times and improved efficiency.

### In-memory caching: Single Server

The default behavior for all XMPro installations is that this location is on the host server memory, i.e. a single server.&#x20;

### Distributed caching: Multiple Servers&#x20;

Auto Scale, XMPro's implementation of distributed caching, offers a superior caching approach that is highly recommended, particularly for larger production-ready implementations. XMPro utilizes “Redis” (Remote Dictionary Server), which is a popular open-source data structure store for XMPro’s distributed caching needs.

## Configure Auto Scale

The upgrade path to utilize Auto Scale is as follows:

1. Upgrade XMPro to V4.3.1+.
2. Provision Redis.\
   Refer to [Redis documentation](https://redis.io/docs/getting-started/) for a guide on how to provision Redis.

Although Auto Scale has a bigger impact on App Designer performance, it is for all XMPro products that use SignalR, i.e. Data Stream Designer and Subscription Manager too.

### Application Designer

1. Enable the `AutoScale` setting in Application Designer.
   1. Open the Application Designer _appsettings.json_ file.
   2. In the `autoscale` object, set `enabled` to _true_ and enter the `connectionstring` value.
   3. Save the file and restart the Application Designer service.

```json
 {
  "xmpro": {    
    "autoScale": {
      "enabled": true,
      "connectionString": "<redis connection string>"
    }
  }
}
```

2. Upgrade [Data Streams Connector](https://xmpro.gitbook.io/data-streams-connector/) to V2.0+.\
   Refer to [Manage Connectors](../../how-tos/connectors/manage-connectors.md#adding-a-connector) for a guide on adding a Connector and view the versions in use.
3. Upgrade Apps to use Data Streams Connector V2.0+.\
   Refer to [Data Integration ](../../concepts/application/data-integration.md#connection)for a guide on how to upgrade an App's connection.

{% hint style="warning" %}
Upgrading the Connector will clear the cache from the existing connector, and all data for the consuming App will be lost.

You do not have to upgrade all Apps to the new Connector version - their cached data and caching process will continue to work as before.
{% endhint %}

### Data Stream Designer

Repeat step 1 for Data Stream Designer.

### Subscription Manager

Repeat step 1 for Subscription Manager but in the _web.config_ file.

{% hint style="info" %}
It might be encrypted, which will require you to decrypt it first. For instructions, please refer to the [How to encrypt and decrypt a web.config file](https://docs.xmpro.com/knowledge-base-2/how-to-encrypt-and-decrypt-a-web-config-file/) Knowledge Base article.
{% endhint %}
