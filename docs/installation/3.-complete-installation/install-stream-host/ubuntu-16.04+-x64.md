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

# Ubuntu 20.04 x64

## Prerequisites

**Downloads**

Follow the instructions in the [Install Stream Host](./) guide to download the connection profile and installer.

**Hardware and Software**

XMPro Stream Host requires certain hardware and software specifications in order to install and run.

Refer to the [**hardware** requirements](../../install.md#hardware-requirements) and the [**software** requirements](../../install.md#software-requirements) in the **1. Preparation** guide.

#### **Software Install Commands**&#x20;

Install required dependencies using the following commands:

```bash
sudo apt-get update
sudo apt-get install -y wget liblttng-ust0 libkrb5-3 zlib1g uuid-runtime systemd 

# Install Dotnet Runtime
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install -y dotnet-runtime-6.0

# Install Libssl
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb
sudo dpkg -i libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb

# Downgrade Libcurl
sudo apt-get remove -y libcurl4
wget http://archive.ubuntu.com/ubuntu/pool/main/c/curl3/libcurl3_7.58.0-2ubuntu2_amd64.deb
sudo dpkg -i libcurl3_7.58.0-2ubuntu2_amd64.deb
sudo apt-mark hold libcurl3


```

## Install

When you are ready, you may install the Stream Host by using the following command:

_`sudo dpkg -i /home/adminuser/xmpro-stream-host.deb`_

During the installation process, you will be asked a few questions:

*   “_Enter a Friendly Name for this Stream Host_”

    This is the name that appears when you view the Stream Hosts online.
*   “_Enter Server Url to connect to_”

    This is the server where Data Stream Designer is hosted, for example: “_https://mysampleserver/datastreamdesigner/_“. Please note that this URL needs to end in a forward slash.
*   “_Enter Collection Id_”

    This is the ID of your Collection and can be copied from Data Stream Designer.
*   “_Enter collection secret Key_”

    This is the secret key of your Collection and can be copied from Data Stream Designer.
*   “_Enter encryption key_”

    This is the key that the Stream Host will use to encrypt or decrypt secure [user settings](https://docs.xmpro.com/docs/data-stream-designer/concepts/agents/#agent-components), for example, a SQL Server password.

These settings can be found in Data Stream Designer:

![](<../../../.gitbook/assets/image (1489).png>)

## Uninstall

To uninstall a Stream Host, use the following command:

_`sudo dpkg -r xmpro-stream-host`_

The Stream Host will then be removed. Some files, such as logs, may not be removed because they were created after the installation.

## Next Step: Agents & Connectors

The stream host installation is complete. Please click below to install the default Agents & Connectors:

{% content-ref url="../install-connectors.md" %}
[install-connectors.md](../install-connectors.md)
{% endcontent-ref %}
