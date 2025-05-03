# End-To-End Use Case

> [!NOTE]
> This Use Case assumes the XMPro platform is installed and configured, or you are using the [Free Trial](free-trial.md) that has everything set up for you.

This step-by-step tutorial is meant to be an introduction to using the XMPro platform. Completing it will give you a solid foundation to understand the more advanced concepts and detailed how-to guides. This tutorial will explain how to create and design a Data Stream, configure Stream Objects to ingest, analyze, transform, and perform actions on data. You will also learn how to set up a Recommendation to generate alerts based on rule logic, create and design an App, create Data Sources and Connections, and configure a simple Data Grid and Chart.

> [!WARNING]
> Please note that the XMPro platform requires third-party cookies to be enabled on your browser.

## Use Case

Let's assume there is a power plant that uses a heat exchanger to keep the turbine cool and at the optimum temperature. The heat exchanger circulates water between the cooling tower and the heat exchanger to dissipate heat. To keep a proper circulation of liquid, there are three pumps \[A, B, C] installed. Each Pump has a sensor that provides live data for Flow Rate (L/m) and Temperature (°C) using MQTT.

Unless the Pump is under maintenance the Flow Rate should be above 15000 L/m and Water temperature should be below 130°C.

Engineers should be alerted if the average flow rate falls below 250 L/s. If the average temperature starts to rise above 130°C then a critical level alert should be raised.

Engineers should be provided a view to check the history of pump telemetry, maintenance records, and reservoir level to enable them to take necessary action.

## 1. Design Data Streams with Real-Time Data Sources

[Content for this section would be added during the actual migration]

## 2. Create Event Rules & Recommendations

[Content for this section would be added during the actual migration]

## 3. Create Event Boards & Apps

[Content for this section would be added during the actual migration]
