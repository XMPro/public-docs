# Configuration

Find answers to some of the most frequently asked configuration questions.

## App Designer

### How do I rotate text in App Designer?

In the video below, we demonstrate how to rotate text -90 degrees around the z-axis using block styling's transform option.

#### Further Reading

* [Block Styling - Extra](../../concepts/application/block-styling.md#extra)

{% embed url="https://www.youtube.com/watch?v=3eQHzy5nAy0" %}

### How do I export Grid Data from my App to Microsoft Excel?

In the video below, we demonstrate how to toggle on your Data Grid's export button so that at runtime the grid contents can be exported to Excel.

#### Further Reading

* [Data Grid Properties - Allow Export To Excel](../../blocks/basic/data-grid.md#allow-export-to-excel)

{% embed url="https://www.youtube.com/watch?v=KrUothBHQVg" %}

## Data Stream Designer

### Can I use an older version of an Agent in a Data Stream?

_"I'm copying the same pattern used in another Data Stream and I want to use the same version of a specific Agent (v2.7) when a newer version is available (v2.8)."_

No, using an older version of an Agent when a newer version is available is not possible. The latest Agent should incorporate all of the functionalities of the previous version as well as any further modifications made.

However, you could clone the original Data Stream and choose not to upgrade the Agent to the latest version. &#x20;

#### Further Reading

* [Cloning](../../how-to-guides/import-export-and-clone.md#cloning)
* [Upgrade a Stream Object Version](../../how-to-guides/data-streams/upgrade-a-stream-object-version.md#upgrading-agents)

### How do I view errors on my Stream Host?

In the video below, we demonstrate how to view the log for a particular Stream Host in a Collection. The log contains errors encountered when publishing or running a Data Stream.

#### Further Reading

* [Stream Host Logs](../../how-to-guides/stream-host.md)
* [How to check Data Stream Logs](../../how-to-guides/data-streams/check-data-stream-logs.md)

{% embed url="https://youtu.be/_HYBmBCug2I?si=y1l5pccS44Ap5VHk" %}

### How are the Stream Load Metrics calculated?

_“I'm trying to reconcile the Stream Load metric in Data Stream designer with what I'm expecting based on the listeners. Is the metric calculated on the stream outputs or the inputs?_

_I have 3 listeners, each running at a 1 second interval, so I expect a 180/min metric. Is the \~360/min metric because there are double the number of outputs (action agents) per listener?”_

<figure><img src="../../.gitbook/assets/FAQ Run Recommendation.png" alt=""><figcaption></figcaption></figure>

Stream load is different from ingestion rate. The Stream load represents the total number of events published by all Stream Objects on the canvas. In this case, 60 x the total number of agents on the screen (assuming your Listeners bring back 1 record on every poll).

You would notice the actual number is much less because although you want it to run every second, the calls to dependencies like SQL etc do not return its data as quickly and hence the actual rate is less.

Generally, the number of events published per Agent decreases as you work through your data stream, because the intention is to work towards a smaller payload focused on the event in which you’re interested.

### Can I use more than one Run Recommendation Agent in a Data Stream?

We advise you to only have one recommendation agent on a data stream.

A recommendation rule is configured against a single Data Stream, not a given Stream Object in a Stream. It will find the first Run Recommendation in the selected Data Stream and let you define your Recommendation Rule against the output payload of that Agent.  If the payload differs at runtime, you may get weird results when triggering a recommendation alert.

If the data cannot be merged (using a join or union transformation) and used in the different recommendations, then consider creating 3 different data streams.  Remember you can have one **data stream** feed data to as many **recommendations** as you want to, BUT you should only have one _run recommendation agent_ on a data stream canvas.

<figure><img src="../../.gitbook/assets/FAQ Run Recommendation.png" alt=""><figcaption></figcaption></figure>

### My Data Stream Connector can do everything. Why use the other Connectors?

Although a wide variety of data can be surfaced from a Data Stream into your Application using the Data Stream Connector, there is a downside. The Data Stream is constantly pushing data, which can lead to out-of-resource errors - which appear as XMPro product errors. If your data requirement is ad-hoc, consider the other Connectors.

#### Further Reading

* [List of App Designer Connectors](../../concepts/application/data-integration.md#app-designer-connector)
* [Connector](../../concepts/connector.md)

### I've added a new recommendation - why can't I see the triggered alerts in the recommendation grid view?

You, as the owner of the recommendation, will not see the recommendation alerts unless you give yourself _Run Access_ to your own recommendations.&#x20;

#### Further Reading

* [How to manage run access](../../concepts/manage-access.md#manage-run-access)

### How do I drill down with data from a chart? <a href="#toc118190992" id="toc118190992"></a>

You can achieve this by combining navigating between pages and passing data to the Page by configuring the Pass Page Parameters. The data passed can be static, an expression, or dynamic. Please refer to the how-to article below for step-by-step instructions.

#### Further Reading

* [Navigation and parameters](../../concepts/application/navigation-and-parameters.md)
* [How to pass dynamic data to the page](../../how-to-guides/apps/pass-parameters-between-pages.md#passing-dynamic-data-to-the-page)

### How do I set up Stream Host Variables/provide unique Asset configuration?

Although each Stream Host in a given Collection downloads the same definition of a Data Stream, the [Variables](../../how-to-guides/manage-variables.md) defined in Data Stream Designer can be overridden by the individual Stream Host to provide the unique configuration per Asset e.g. OPC IP Address. Please refer to the how-to articles below for step-by-step instructions.

#### Further Reading

* [How to override Stream Host variables](../../how-to-guides/stream-host.md#how-to-override-variables)
* [How to manage variables](../../how-to-guides/manage-variables.md)
