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

# Docker

## Prerequisites

**Downloads**

Follow the instructions in the [Install Stream Host](./) guide to download the connection profile and get the following values ready as environment variables:
* Server URL
* Server ID
* Collection ID
* Collection Secret
* Stream Host/Device Name
* XMCryptography Key

**Hardware and Software**

XMPro Stream Host requires certain hardware and software specifications in order to install and run.

Refer to the [**hardware** requirements](../../install.md#hardware-requirements) and the [**software** requirements](../../install.md#software-requirements) in the **1. Preparation** guide.

#### **Docker Run Commands**&#x20;

Install required dependencies using the following commands:

```bash
docker run  --env-file=envfile --name stream-host xmpro.azurecr.io/stream-host:latest

```

```bash

#envfile contents
xm__xmpro__Gateway__ServerUrl=<Server URL>
xm__xmpro__Gateway__Id=<Server ID>
xm__xmpro__Gateway__CollectionId=<Collection ID>
xm__xmpro__Gateway__Secret=<Collection Secret>
xm__xmpro__Gateway__Name=<Device Name>
xm__xmpro__XMCryptography__TripleDES__Key=<XMCryptography Key>
xm__xmpro__Gateway__featureFlags__enableLegacyCore=false
```

#### **Docker Compose Example**&#x20;

```yml
  stream-host:
    image: xmpro.azurecr.io/stream-host:latest
    container_name: 'stream-host'
    environment:
      - xm:xmpro:Gateway:ServerUrl=<Server URL>
      - xm:xmpro:Gateway:Id=<Server ID>
      - xm:xmpro:Gateway:CollectionId=<Collection ID>
      - xm:xmpro:Gateway:Secret=<Collection Secret>
      - xm:xmpro:Gateway:Name=<Device Name>
      - xm:xmpro:XMCryptography:TripleDES:Key=<XMCryptography Key>
      - xm:xmpro:Gateway:featureFlags:enableLegacyCore=false
    restart: on-failure
```
```bash
docker-compose up -d stream-host 

```


## Uninstall/Stop Docker

```bash
docker rm -f stream-host

```

```bash
docker-compose down

```

## Next Step: Agents & Connectors

The stream host installation is complete. Please click below to install the default Agents & Connectors:

{% content-ref url="../install-connectors.md" %}
[install-connectors.md](../install-connectors.md)
{% endcontent-ref %}
