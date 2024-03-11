---
description: v4.3.0
---

# Configure Logging (Optional)

{% embed url="https://youtu.be/N5f1_4F6g84" %}

## Overview

Application logging refers to recording and storing information about the events and activities that occur within a software application. It involves capturing relevant data, such as error messages, warnings, user interactions, and system events, and storing them in a log file or database.&#x20;

Application logging is essential for troubleshooting and debugging, as it helps identify and analyze issues that may arise during the application's execution. It also provides valuable insights into the application's performance, usage patterns, and security.

[Serilog](https://serilog.net/) is the diagnostic logging library used in the XMPro suite, and the following logging outputs are supported:

* [Logging to file](configure-logging-optional.md#logging-to-file)
* [Application Insights](configure-logging-optional.md#application-insights)
* [Application Insights plus Telemetry](configure-logging-optional.md#application-insights-plus-telemetry) _(Added v4.3.6)_
* [Datadog](configure-logging-optional.md#datadog)

{% hint style="info" %}
Subscription Manager currently only supports logging to file.
{% endhint %}

## Enable Logging

{% hint style="info" %}
Logging for Subscription Manager and Stream Hosts is always enabled and does not require configuration.&#x20;
{% endhint %}

Repeat these steps for any of the XMPro products (Application Designer, Data Stream Designer, and AI XMPro) - except Subscription Manager and Stream Hosts.&#x20;

1. Navigate to the IIS location where the XMPro product has been installed.
2. Open the _appsettings.json_ file.
3. Set `enableLogging` in the `featureFlags` object to _true_.
4. Save the file.
5. Restart the XMPro product service.

```json
"xmpro": {
  "appDesigner": {
    "featureFlags": {
      "enableLogging": true
    }
  }
}
```

## Logging to File

This utilizes the Serilog file sink. See [Serilog sinks file documentation ](https://github.com/serilog/serilog-sinks-file)for a complete set of configuration options.

Below are examples for each XMPro Product.

#### Subscription Manager

1. Open the _web.config_ file.
2. Add the Serilog keys to the `appSettings` element.
3. Save the file and restart the Subscription Manager service.

```json
<appSettings>
    <add key="serilog:using:File" value="Serilog.Sinks.File" />
    <add key="serilog:using:Expressions" value="Serilog.Expressions" />
    <add key="serilog:write-to:File.path" value="<path>" />
    <add key="serilog:write-to:File.rollingInterval" value="<rollingInterval> " />
    <add key="serilog:write-to:File.rollOnFileSizeLimit" value="true" />
    <add key="serilog:write-to:File.outputTemplate" value="{Timestamp} [{Level}] ({Name}) Company: {Company} UserId: {UserId} {NewLine}{Message}{NewLine}{Exception}"/>
</appSettings>
```

{% hint style="info" %}
It might be encrypted, which will require you to decrypt it first. For instructions, please refer to the [How to encrypt and decrypt a web.config file](https://docs.xmpro.com/knowledge-base-2/how-to-encrypt-and-decrypt-a-web-config-file/) Knowledge Base article.
{% endhint %}

#### Stream Hosts

_Changed in v4.4.0_

1. Close or stop the Stream Host.
2. Navigate to the file location where the Stream Host has been installed.
3. Open the _appsettings.json_ file.
4. Add the “File Logging" Serilog configuration.
5. Save the file and restart or reopen the Stream Host.

```json
{
  "FileLogging": {
    "MinimumLevel": {
      "Default": "Information",
      "Override": {
        "Microsoft": "Warning"
      }
    },
    "WriteTo": [
      {
        "Name": "File",
        "Args": {
          "path": "C:\\some\\path\\to\\logs\\log.txt",
          "rollingInterval": "Day",
          "outputTemplate": "{Timestamp:yyyy-MM-dd HH:mm:ss} [{Level:u3}] {SourceContext} Message: {Message:lj}{NewLine}{Properties}{NewLine}{Exception}{NewLine}"
        }
      }
    ]
  }
}
```

#### Other XMPro products

Repeat these steps for all the XMPro products except Subscription Manager: App Designer, Data Stream Designer, and AI XMPro.

1. Open the _appsettings.json_ file.
2. Add the “File” Serilog configuration inside the WriteTo array.
3. Save the file and restart the XMPro product service.

```json
{  
  "Serilog": {    
    "WriteTo": [
      {
        "Name": "File",
        "Args": {
          "path": "<path>",
          "rollingInterval": "<rollingInterval>",
          "outputTemplate": "{Timestamp:yyyy-MM-dd HH:mm:ss} [{Level:u3}] {SourceContext} Company: {Company} User Id: {UserId} Message: {Message:lj}{NewLine}{Exception}"
        }
      }  
    ]
  }
}
```

## Application Insights

This utilizes the Serilog application insights sink. See [Serilog sinks file for Application Insights](https://github.com/serilog-contrib/serilog-sinks-applicationinsights) for a complete set of configuration options.&#x20;

Below are the steps for an _**example**_ of how it can be used in App Designer, Data Stream Designer, Stream Hosts, and AI XMPro:

1. Open the _appsettings.json_ file.
2. Add the “ApplicationInsights” Serilog configuration inside the WriteTo array.
3. Save the file and restart the XMPro product service or Stream Host.

```json
{  
  "Serilog": {    
    "WriteTo": [      
      {
        "Name": "ApplicationInsights",
        "Args": {
          "connectionString": "<connection string>",
          "telemetryConverter": "Serilog.Sinks.ApplicationInsights.TelemetryConverters.TraceTelemetryConverter, Serilog.Sinks.ApplicationInsights"
        }
      }
    ]
  }
}
```

## Application Insights plus Telemetry

This utilizes the Serilog application insights sink to write events to Microsoft Azure Application Insights and collect valuable Telemetry data.&#x20;

Below are the steps for an _**example**_ of how it can be used in App Designer, Data Stream Designer, Stream Hosts, and AI XMPro:

1. Set `enableApplicationInsightsTelemetry` in the `featureFlags` object to _true -_ the same as you already did [here](configure-logging-optional.md#enable-logging) for `enableLogging`.
2. Open the _appsettings.json_ file.
3. Add the “ApplicationInsights” configuration.
4. Save the file and restart the XMPro product service or Stream Host.

```json
{  
  "ApplicationInsights": { 
    "ConnectionString" : "InstrumentationKey=<Instrumentation Key here>";
  }
}
```

## Datadog

This utilizes the Serilog datadog sink. See [Serilog Sinks File for Datadog](https://github.com/DataDog/serilog-sinks-datadog-logs) for a complete set of configuration options.&#x20;

Below are the steps for an _**example**_ of how it can be used in App Designer, Data Stream Designer, Stream Hosts, and AI:

1. Open the _appsettings.json_ file.
2. Determine the site parameter by checking [here](https://docs.datadoghq.com/getting\_started/site/#access-the-datadog-site).
3. Get the endpoint/URL and port number by checking [here](https://docs.datadoghq.com/logs/log\_collection/?tab=host#supported-endpoints).
4. Add the “DatadogLogs” Serilog configuration inside the WriteTo array.
5. Save the file and restart the XMPro product service or Stream Host.

```json
{  
  "Serilog": {    
    "WriteTo": [
      {
        "Name": "DatadogLogs",
        "Args": {
          "apiKey": "<api key>",
          "source": "<source>",
          "host": "<host>",
          "configuration": {
            "url": "<url>",
            "port": port
          }
        }
      }
    ]
  }
}
```
