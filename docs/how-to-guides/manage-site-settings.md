# Manage Site Settings

These settings are used to configure each XMPro Product. To open the settings page, click on the _gears_ icon in the grey bar at the top of the screen.

{% hint style="info" %}
Please note that the settings that you will see on this page depend on the role and access rights that have been assigned to you.
{% endhint %}

![Fig 1: Access the Site Settings](<../.gitbook/assets/image (1118).png>)

## App Designer Settings

### Security

#### Enable Audit Trail

Enabling this setting would cause logs to be created whenever changes are made to [Recommendations](../concepts/recommendation/), [Connectors](../concepts/connector.md), and components of [Applications](../concepts/application/). The logs will contain details about who made the change and when it was applied.

### Integration

#### Integration Key

This key is used to verify Agents that integrate with the App Designer. The Integration Key will need to be copied into the Agent's configuration settings.

### Reports

_Added v4.3.7_

Standard reports give the administrator a view into where and how XMPro Objects such as Connectors have been used. The information is presented in a grid that can be sorted, filtered, reorganized, and grouped - as well as exported as an XLSX file.

<figure><img src="../.gitbook/assets/Manage Site Settings - AD Reports.png" alt=""><figcaption><p>Fig 2: Example App Designer Report</p></figcaption></figure>

#### Connector Usage Report

This report shows all loaded Connectors, their versions, and how many times a version is used in an Application, if any.

This master list shows the administrator which Connectors are installed and their utilization. This assists in identifying new Connectors or versions not yet added.&#x20;

#### Connector Usage Details Report

This report shows the Applications in which a Connector version has been used. Additional information includes the Application's owner and category.

This detailed report assists in gauging the impact of upgrading one or more Connector versions.

## Data Stream Designer Settings

### Security

#### Encryption Key

The encryption key is used to encrypt and decrypt sensitive data configured in the user settings of an [Agent](../concepts/agent/) when they are stored or retrieved from the database, for example, passwords.

#### Enable Audit Trail

Enabling this setting would cause logs to be created whenever changes are made to [Agents](../concepts/agent/), [Collections](../concepts/collection.md), and components of [Data Streams](../concepts/data-stream/). The records will contain details about who made the change and when it was applied.

### UI

#### Enable InputMap Highlights

Enables the Canvas arrow highlight which is shown if the arrow's configuration doesn't have mappings. This is useful for demos where the complete configuration has intentionally not been provided.

#### Enable Stream Metrics

Enables the logging and display of stream metrics in Data Streams. Refresh the page for the setting to be applied to the Data Stream Canvas.

### Behavior

#### Default Polling Interval (seconds)

_Added v4.3.7_

The default value that is used for the polling interval when a Polling Agent is added to a [Streaming](../concepts/data-stream/#data-stream-type) type Data Stream.&#x20;

If there is no value provided for this setting, the polling interval defaults to 3600 seconds (1 hour).

{% hint style="info" %}
The default is applied when the Agent is added to the canvas. A change to this site setting will only take effect for Agents added afterward.&#x20;
{% endhint %}

#### Live View Usage

_Added v4.3.6_

Over time, if users did not close the [Live View](../concepts/data-stream/running-data-streams.md#viewing-live-data), these open connections placed an additional load on the Data Stream Designer (DS) as the Stream Hosts continued to send live data back to DS. This reduced overall performance and reliability, and increased infrastructure costs.

We recommend that users always close the Live View of a published Data Stream before navigating away. When in doubt, an administrator can force a reset to close all open Live View connections.

The Live View Usage includes the following:

* The number of Stream Objects (Agents) with Live View enabled and the number of Data Streams affected.
*   A button to reset the Live View usage.&#x20;

    <figure><img src="../.gitbook/assets/Manage Site Settings - DS Live View Usage.PNG" alt=""><figcaption><p>Fig 3: Live View Usage and Reset Button</p></figcaption></figure>

Resetting the Live View will close any connections that may have been left open if a user closes the Data Stream canvas without first closing the Live View.&#x20;

It will also stop any open Live View blades from receiving data. To start receiving data again, re-open the Live View and reselect the Stream Objects.&#x20;

Refer to the [Live View Usage Report](manage-site-settings.md#live-view-usage-report) for a list of Stream Objects and Data Streams that are preselected for Live View.&#x20;

{% hint style="info" %}
A Stream Object with Live View enabled is an indicator that a user has viewed the data - it is not confirmation whether the user closed the connection.
{% endhint %}

{% hint style="success" %}
The Live View issue is addressed in the v4.3.7 release:

1. Open connections are closed regardless of how the Live View is closed (e.g. navigating away or closing the tab).&#x20;
2. All connections are closed when the Data Stream Designer app service is restarted.&#x20;

If you've upgraded to v4.3.7, use the Reset Live View button once to ensure all connections are closed.&#x20;
{% endhint %}

### Reports

_Added v4.3.7_

Standard reports give the administrator a view into where and how XMPro Objects such as Connectors have been used. The information is presented in a grid that can be sorted, filtered, reorganized, and grouped - as well as exported as an XLSX file.

<figure><img src="../.gitbook/assets/Manage Site Settings - DS Reports.png" alt=""><figcaption><p>Fig 4: Example Data Stream Designer Report</p></figcaption></figure>

#### Live View Usage Report

This report shows all Agents that have Live View enabled. Additional information includes the Data Stream name, Data Stream version, Data Stream owner, the Collection name, the Stream Object name, and whether the Data Stream is published.

This report along with the [Reset option](manage-site-settings.md#live-view-usage) was useful prior to v4.3.7, to determine where connections may have been left open.&#x20;

#### Agent Usage Report

This report shows all loaded Agents, their versions, their categories, and how many times a version is used in a Data Stream, if any.

This master list shows the administrator which Agents are installed and their utilization. This assists in identifying new Agents or versions not yet added.&#x20;

#### Agent Usage Details Report

This report shows Data Streams in which an Agent version has been used. Additional information includes the Data Stream version, its owner, the Collection, and the Stream Object name.

This detailed report assists in gauging the impact of upgrading one or more Agent versions.

#### Agent Polling Interval Report

This report shows the polling intervals configured on all Agents that have the Polling Interval option. Additional information includes the Agent Name, Agent Category, Data Stream name, Data Stream version, Data Stream owner, the Collection name, the Stream Object name, and whether the Data Stream is published.

This master list empowers the administrator to locate those set too short (1s) that may be causing performance issues. 10 seconds may be appropriate during initial testing, but ill-advised in a QA or Production environment.

## Subscriptions Manager Settings

### **Support**

#### **Email**

The email to which notifications will be sent if a user signs up to XMPro or makes a request, for instance, a request for a Subscription to a Product, or a request for a License.

#### Disable Email Notifications

Disables emails sent to the email address above for any reason. If email notifications are disabled then the Global Administrator will need to log in to Subscription Manager to check whether there are any pending requests.

### Security

#### Encryption Key

The encryption key is used to encrypt and decrypt sensitive data configured in the user settings of an [Agent](../concepts/agent/) when they are stored or retrieved from the database, for example, passwords.

#### Hide Users Outside Business Role Branch

When enabled, users can see the information of users in their business role and any of its parent business roles up to the root. They cannot see any child or sibling business roles and their users.

For example, a user cannot tag/search users outside of their business role tree path in a comment on a recommendation alert.

This defaults to true on new installations. Toggle it off to make all user information visible to all users in the company.&#x20;

{% hint style="warning" %}
The exception for this setting is a user with an Administrator role for the Subscription Manager product. They can assign access to XMPro objects to any user or business role in the company.&#x20;
{% endhint %}
