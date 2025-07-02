---
description: v4.4.19
---

# Docker

## Introduction

This guide covers the XMPro Stream Host Docker image available from version 4.4.19 onwards. The latest Stream Host images have been redesigned for improved security and usability.

{% hint style="info" %}
Note: For Stream Host images prior to v4.4.19, please refer to Docker v4.4.2 - v4.4.18 documentation.
{% endhint %}

## Prerequisites

### **Software Requirements**

A container runtime such as [Docker Desktop](https://www.docker.com/products/docker-desktop/).

### Hardware Requirements

| Component   | Small           | Medium         | Large           |
| ----------- | --------------- | -------------- | --------------- |
| Stream Host | 1 CPU, 4 GB RAM | 2 CPU, 8GB RAM | 4 CPU, 16GB RAM |

{% hint style="info" %}
Important: Actual resource requirements depend on your specific data streams. Monitor performance and adjust resources accordingly.
{% endhint %}

### Configuration

Essential Environment Variables

<table><thead><tr><th width="305">Key</th><th width="112" align="center">Required</th><th>Description</th><th data-hidden>Name</th></tr></thead><tbody><tr><td>xm__xmpro__Gateway__Id</td><td align="center">Optional</td><td><p>Unique GUID identifier for this Stream Host instance.</p><p><em>Default: A new GUID</em></p></td><td></td></tr><tr><td>xm__xmpro__Gateway__Name</td><td align="center">Optional</td><td><p>Display name in Data Stream Designer.</p><p><em>Default: "[Image-Version]-[Gateway Id]", e.g.</em> "alpine3.21-python3.12-3bd462d4-4f1f-4cda-b6c5-d02f986beb6f"</p></td><td></td></tr><tr><td>xm__xmpro__Gateway__CollectionId</td><td align="center">Required</td><td>ID of your Collection<br>(available in Data Stream Designer)</td><td></td></tr><tr><td>xm__xmpro__Gateway__Secret</td><td align="center">Required</td><td><p>Secret key of your Collection</p><p>(available in Data Stream Designer)</p></td><td><em>Server Url</em></td></tr><tr><td>xm__xmpro__Gateway__ServerUrl</td><td align="center">Required</td><td>The server URL for where Data Stream Designer is hosted. E.g. <em>"https://dsserver/datastreamdesigner/".</em> <br><br>Please note that this URL needs to end in a forward slash.</td><td><em>Collection ID</em></td></tr><tr><td>xm__xmpro__Gateway__Rank</td><td align="center">Optional</td><td>An integer, by default is "0".<br>See <a href="../../../concepts/collection.md#stream-host-rank">Stream Host Rank</a> for further details.</td><td></td></tr></tbody></table>

These settings can be found in Data Stream Designer:

![Fig 1: Collection details in Data Stream Designer](<../../../.gitbook/assets/image (1489) (1).png>)

## Docker Repository

Below is the XMPro Docker Stream Host repository.

```
xmpro.azurecr.io/stream-host
```

## Image Variants

### Version Tagging

All images are tagged with their version number. For example:

```
xmpro.azurecr.io/stream-host:4.4.19
```

The `latest`  tag points to the most recent release:

```
xmpro.azurecr.io/stream-host:latest
```

{% hint style="warning" %}
Warning: Using the `latest` tag caches the image locally. For guaranteed latest version, specify the exact version number or re-pull the image.
{% endhint %}

### **Available Variants**

A Stream Host running a Data Stream must provide the capabilities to run each Agents in the Data Stream. Choose your image depending on the capabilities that are required.

<table><thead><tr><th width="511">Image Name</th><th>Description</th></tr></thead><tbody><tr><td><code>xmpro.azurecr.io/stream-host:4.4.19-bookworm-slim</code></td><td>Debian (Default)</td></tr><tr><td><code>xmpro.azurecr.io/stream-host:4.4.19-bookworm-slim-python3.12</code></td><td>Debian with Python</td></tr><tr><td><code>xmpro.azurecr.io/stream-host:4.4.19-alpine3.21</code></td><td>Alpine</td></tr></tbody></table>

### Choosing the Right Image

* Alpine-based images offer a smaller footprint, ideal for environments where size matters
* Debian-based images (Bookworm Slim) provide more comprehensive tools and libraries for general use
* Python-enabled images come with Python pre-installed for running Python-based Agents and Connectors

## Python Package Installation

For Python-enabled images, you can install packages using:

Either a **`requirements.txt`** file,

```docker
pandas==2.1.4
numpy==1.26.3
```

Or the **`SH_PIP_MODULES`** environment variable:

<pre><code><strong>SH_PIP_MODULES = pandas==2.1.4 numpy==1.26.3
</strong></code></pre>

#### **Requirements.txt Location**

Specify the location of your `requirements.txt` file using the `PIP_REQUIREMENTS_PATH` environment variable:

```
 # Powershell and Bash Terminal
 -v "<path_to_your_solution>:/opt/"
 -e PIP_REQUIREMENTS_PATH="/opt"

 # Docker compose
 - PIP_REQUIREMENTS_PATH=/opt
volumes:
 - "<path_to_your_solution>:/opt/"
```

{% hint style="warning" %}
**Note:** If not specified, the system will look for `requirements.txt` in the default path `/app`.
{% endhint %}

### **Installing System Dependencies**

To install additional system packages (APK/APT), you can install it using environment variables:

```
ADDITIONAL_INSTALLS=git
```

## Deployment

### Docker

Replace `<values>` with your actual configuration settings.

#### PowerShell

```powershell
docker run `
  --name stream-host `
  --restart on-failure `
  -e "XM__XMPRO__GATEWAY__COLLECTIONID=<Collection ID>" `
  -e "XM__XMPRO__GATEWAY__SECRET=<Collection Secret>" `
  -e "XM__XMPRO__GATEWAY__SERVERURL=<Server URL>" `
  xmpro.azurecr.io/stream-host:latest
```

#### With optional environment variables:

<pre class="language-powershell"><code class="lang-powershell">docker run `
<strong>--name stream-host `
</strong>--restart on-failure `
--pull always `
-e "XM__XMPRO__GATEWAY__COLLECTIONID=&#x3C;Collection ID>" `
-e "XM__XMPRO__GATEWAY__SECRET=&#x3C;Collection Secret>" `
-e "XM__XMPRO__GATEWAY__SERVERURL=&#x3C;Server URL>" `
-e "XM__XMPRO__GATEWAY__ID=&#x3C;Stream Host Id>" `
-e "XM__XMPRO__GATEWAY__NAME=&#x3C;Stream Host Name>" `
-e "XM__XMPRO__GATEWAY__RANK=&#x3C;Stream Host Rank>" `
-e "SH_PIP_MODULES=pandas scikit-learn numpy" `
-v "&#x3C;path_to_your_solution>:/opt/" `
-e "PIP_REQUIREMENTS_PATH=/opt" `
-e "ADDITIONAL_INSTALLS=git" `
xmpro.azurecr.io/stream-host:latest
</code></pre>

{% hint style="info" %}
Remove optional variables that are NOT needed.
{% endhint %}

#### Bash/Terminal

```bash
docker run \
--name stream-host \
--restart on-failure \
-e "XM__XMPRO__GATEWAY__COLLECTIONID=<Collection ID>" \
-e "XM__XMPRO__GATEWAY__SECRET=<Collection Secret>" \
-e "XM__XMPRO__GATEWAY__SERVERURL=<Server URL>" \
xmpro.azurecr.io/stream-host:latest
```

With optional environment variables

```bash
MSYS_NO_PATHCONV=1 docker run \
--name stream-host \
--restart on-failure \
--pull always \
-e "XM__XMPRO__GATEWAY__COLLECTIONID=<Collection ID>" \
-e "XM__XMPRO__GATEWAY__SECRET=<Collection Secret>" \
-e "XM__XMPRO__GATEWAY__SERVERURL=<Server URL>" \
-e "XM__XMPRO__GATEWAY__ID=<Stream Host Id>" \
-e "XM__XMPRO__GATEWAY__NAME=<Stream Host Name>" \
-e "XM__XMPRO__GATEWAY__RANK=<Stream Host Rank>" \
-e "SH_PIP_MODULES=pandas scikit-learn numpy" \
-v "<path_to_your_solution>:/opt/" \
-e "PIP_REQUIREMENTS_PATH=/opt" \
-e "ADDITIONAL_INSTALLS=git" \
xmpro.azurecr.io/stream-host:latest
```

{% hint style="info" %}
Remove optional variables that are NOT needed.&#x20;
{% endhint %}

### Docker Compose

Create a `compose.yaml` file in your working directory:

```yaml
services:
  stream-host:
    image: xmpro.azurecr.io/stream-host:latest
    pull_policy: always
    container_name: 'stream-host'
    environment:
      - XM__XMPRO__GATEWAY__COLLECTIONID=<Collection ID>
      - XM__XMPRO__GATEWAY__SECRET=<Collection Secret>
      - XM__XMPRO__GATEWAY__SERVERURL=<Server URL>
    restart: on-failure
```

With optional environment variables

```yaml
services:
  stream-host:
    image: xmpro.azurecr.io/stream-host:latest
    pull_policy: always
    container_name: 'stream-host'
    environment:
      - XM__XMPRO__GATEWAY__COLLECTIONID=<Collection ID>
      - XM__XMPRO__GATEWAY__SECRET=<Collection Secret>
      - XM__XMPRO__GATEWAY__SERVERURL=<Server URL>
      # Optional: Uncomment if needed
      # - XM__XMPRO__GATEWAY__ID=<Stream Host Id>
      # - XM__XMPRO__GATEWAY__NAME=<Stream Host Name>
      # - XM__XMPRO__GATEWAY__RANK=<Stream Host Rank>
      # - SH_PIP_MODULES=pandas scikit-learn numpy
      # - PIP_REQUIREMENTS_PATH=/opt
      # - ADDITIONAL_INSTALLS=git
    # volumes:  
    # - "<path_to_your_solution>:/opt/"  
    restart: on-failure
```

Replace `<values>` with your actual configuration settings.

#### **Managing Your Docker Compose Container**

Start the Stream Host:

```
docker-compose up -d stream-host
```

Stop the Stream Host:

```
docker-compose down
```

{% hint style="info" %}
For more information on Docker Compose, see the [Docker Compose Overview](https://docs.docker.com/compose/).
{% endhint %}

## Next Step:&#x20;

Your Stream Host installation is now complete. To install default Agents & Connectors, visit:

{% content-ref url="broken-reference" %}
[Broken link](broken-reference)
{% endcontent-ref %}
