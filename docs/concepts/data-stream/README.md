# Data Stream

A Data Stream is a visual display of data flow, letting you integrate and connect various systems or data sources to view your information. This includes real-time data from machines, websites, or other streaming sources, as well as contextual data like an item's make or model.

The Data Stream Designer lets you see all connected data in one place and manipulate it in different ways, such as aggregating, filtering, displaying, or saving to another database. You can monitor data to spot critical events like machine failures, without needing coding skills.

{% embed url="https://www.youtube.com/watch?v=gcsBKSqA0FU" %}
Video Presentation Discussing Data Stream Designer
{% endembed %}

Data Stream's flow is represented by agents connected by arrows, enabling data processing at each agent based on its function, allowing you to view and perform actions on data from multiple sources in one place.

{% hint style="info" %}
We recommend reading this documentation in conjunction with the article below to enhance your understanding of data streams.

* [Agent](../agent/)
{% endhint %}

## Finding Data Streams

Use the search bar to find specific Data Streams, and select from the dropdown menu to search either throughout Data Stream Designer or only for Data Streams.

![Fig 1. Ways to Find Data Streams](<../../.gitbook/assets/DS - Search Data Streams.png>)

## Data Stream Type

The Type selected in the Properties affects your choice of how often and when polling-based Agents run.

**Streaming (Default)**: This allows you to specify a Polling Interval in seconds on polling-based Agents in the Stream Object configuration. Polling starts immediately and continues indefinitely.

**Recurring**: This allows you to specify granular options to schedule polling-based Agents in the Stream Object configuration. Options allow you to control the start time, repetition interval, and end time or number of repetitions. There is also the option to repeat indefinitely.

## Buffer Size

An advanced option in Data Stream enables compensation for large event sizes, high event numbers, or increased stream complexity by allocating more memory. The default buffer size is 128kb.

## The Canvas

Data streams are crafted in an interactive canvas, allowing you to drag agents from the toolbox to the drawing area. In the same environment, configure agent settings, manage versions, define business cases, and more.&#x20;

Stream Objects on the canvas can be duplicated or deleted, and for easy identification and access, they're marked with a unique color and abbreviation.

<figure><img src="../../.gitbook/assets/ds.newvisualindicator.concepts.data-stream.canvas.1 (1).png" alt=""><figcaption><p>Fig 2. The Canvas</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/ds.newvisualindicator.concepts.data-stream.canvas.2.png" alt=""><figcaption><p>Fig 3. Data Stream Interface</p></figcaption></figure>

## The Toolbox

The toolbox is a component in the Data Stream Designer that allows you to choose an Agent from a library of Agents that have been uploaded to the system and drag the agent from the toolbox to the Canvas when building a stream. All agents in the toolbox will always be the latest version and will all be available for all users, regardless of their role, unless a user does not have permission to view any of the Agents.&#x20;

Agents are grouped by category in the toolbox. To expand a category, click on the arrow next to the category name. Please note that if no agents in a particular category are uploaded, the entire category will be hidden. Thus, if you are missing some of the categories in the toolbox, it is likely that there aren’t any Agents uploaded belonging to that category.

<figure><img src="../../.gitbook/assets/ds.newvisualindicator.concepts.data-stream.canvas.3 (1).png" alt=""><figcaption><p>Fig 4. Data Stream Toolbox Interface</p></figcaption></figure>

## Building a stream

{% hint style="info" %}
See the [Manage Data Streams article](../../how-to-guides/data-streams/manage-data-streams.md) for detailed instructions and an example of how to build your first stream.
{% endhint %}

## Actions on the Data Stream

| **Action**                                                                                              | **Description**                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Save                                                                                                    | Saves any changes made to the Data Stream up to this point.                                                                                                                                                               |
| Discard                                                                                                 | Discards any changes made to the Data Stream up to this point.                                                                                                                                                            |
| Properties                                                                                              | Opens the properties for the Data Stream. Also allows you to Delete the Data Stream.                                                                                                                                      |
| [Business Case](../../how-to-guides/data-streams/use-business-case-and-notes.md#adding-a-business-case) | Opens the Business Case for the Data Stream.                                                                                                                                                                              |
| [Notes](../../how-to-guides/data-streams/use-business-case-and-notes.md#adding-notes)                   | Opens the Notes, which allows you to add notes about the Application for collaboration and future-proofing.                                                                                                               |
| [Versions](../version.md)                                                                               | Versioning for the Recommendation.                                                                                                                                                                                        |
| [Timeline](timeline.md)                                                                                 | Opens the Timeline, which shows a timeline of the history of the Data Stream.                                                                                                                                             |
| [Manage Access](../manage-access.md)                                                                    | Allows you to manage which users are allowed to view or modify this Data Stream.                                                                                                                                          |
| [Integrity Check](verifying-stream-integrity.md)                                                        | Verifies if the agents in your stream are configured correctly.                                                                                                                                                           |
| Logs                                                                                                    | Allows you to check for log messages for the [Stream Host](../../how-to-guides/stream-host.md) being used to run the Data Stream.                                                                                         |
| Error Flow                                                                                              | Toggles between being able to view and configure the default error Agent for the Stream, which collects all the errors from all agents with an [Error endpoint](../../how-to-guides/data-streams/use-error-endpoints.md). |
| [Publish/Unpublish](../../how-to-guides/publish/)                                                       | Publishes or unpublishes the Recommendation, which makes it start listening for data from the Data Stream.                                                                                                                |
| Configure (Agent)                                                                                       | Opens the configuration page for the selected Stream Object.                                                                                                                                                              |
| Upgrade (Agent)                                                                                         | Upgrades the selected Stream Object to the latest Agent Version. Only available if the selected Stream Object's Agent is not the latest version.                                                                          |
| Delete (Agent)                                                                                          | Deletes the selected Stream Object from the canvas and Data Stream.                                                                                                                                                       |
| Help (Agent)                                                                                            | Opens the help page for the selected Stream Object's Agent.                                                                                                                                                               |
| Delete                                                                                                  | Deletes the Data Stream.                                                                                                                                                                                                  |
| [Export](../../how-to-guides/import-export-and-clone.md)                                                | Export the Data Stream as an encrypted file.                                                                                                                                                                              |
| [Clone](../../how-to-guides/import-export-and-clone.md#cloning)                                         | Clones the Data Stream as a new Data Stream.                                                                                                                                                                              |

## Further Reading

* [How to Create and Manage Data Streams](../../how-to-guides/data-streams/manage-data-streams.md)
* [How to Manage Recurrent Data Streams](../../how-to-guides/data-streams/manage-recurrent-data-streams.md)
* [How to Troubleshoot a Data Stream](../../how-to-guides/data-streams/troubleshoot-a-data-stream.md)
