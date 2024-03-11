# Manage Connections

The parameters defined in a Connection allow the App to connect to a source of data like a SQL Database and expose the entities as Data Sources within the Page. Connection parameters can include credentials such as a username, password, path, URL, or location identifier that you can use to make a remote connection to the Data Source.&#x20;

For example, Connection parameters to connect to an SQL Database would include the Server Name, Authentication type, Username, and password.

{% hint style="info" %}
It is recommended that you read the article listed below to improve your understanding of Data Integration.

* [Data Integration](../../concepts/application/data-integration.md)
* [How to Manage Pages](manage-pages.md)
{% endhint %}

## Adding a Connection to the Application

Connections can be added directly to an Application by adding it to the App Data. To add a Connection to an Application, follow the steps below:

1. Open the _Applications_ page from the left-hand menu.
2. Click on the _edit_ button to edit an application from the list.

![](<../../.gitbook/assets/image (936).png>)

![](../../.gitbook/assets/conn\_1.png)

&#x20;   3\. Click on _App Data._\
&#x20;   4\. Click on _add._\
&#x20;   5\. Select a connector, for example, the SQL connector.\
&#x20;   6\. Enter the details of the Connection, including it's name.\
&#x20;   7\. Click on _Save_.

![](<../../.gitbook/assets/conn\_2 (1).png>)

The new Connection should appear in the list of connectors, and can now be used in the application to add Data Sources. The Connection can be used for all pages within the application it was added to.

![](../../.gitbook/assets/conn\_3.png)

## Deleting a Connection

### Single Connection

To delete a single Connection, follow the steps below:

1. Open the _Applications_ page from the left-hand menu.
2. Click on the _edit_ button to edit an application.

![](../../.gitbook/assets/conn\_4.png)

&#x20;   3\. Click on _App Data._\
&#x20;   4\. Select the Connection.\
&#x20;   5\. Click on _Delete._\
&#x20;   6_._ Confirm that you want to delete the Connection.

![](../../.gitbook/assets/conn\_5.png)

### Multiple Connections

To delete multiple Connections, follow the steps below:

1. Open the _Applications_ page from the left-hand menu.
2. Click on the _edit_ button to edit an application.

![](../../.gitbook/assets/conn\_6.png)

&#x20;   3\. Click on _App Data._\
&#x20;   4\. Click on _Select_.\
&#x20;   5\. Select multiple Connections to be deleted.\
&#x20;   6\. Click on _Delete_.

![](<../../.gitbook/assets/conn\_7 (1).png>)

&#x20;   7\. Confirm that you want to delete the Connection.

![](../../.gitbook/assets/conn\_8.png)

{% hint style="info" %}
You can cancel the multi-select by clicking on the select button again.
{% endhint %}

## Data Stream Connections

Navigate to the Data Stream Connector to access a comprehensive inventory of the Data Stream Connections for the Application. The connections are categorized based on the respective pages where they are utilized.&#x20;

You can use this list to verify the current version of the Data Stream in use and make any necessary updates if required.

<figure><img src="../../.gitbook/assets/image (917).png" alt=""><figcaption></figcaption></figure>

## Further Reading

* [How to Manage Data Sources](manage-data-sources.md)
