# Pass Parameters Between Pages

You can use Parameters if you want to send particular values to another Page. For example, if you have a list of machines, and a user selects one, the Application may open a new Page that displays information for that particular machine. In that case, you may want to pass the ID of the machine the user clicked on to the Page that is being opened.

{% hint style="info" %}
It is recommended that you read the article listed below to improve your understanding of Navigating between Pages.

* [Navigation and Parameters](../../concepts/application/navigation-and-parameters.md)
* [How to Navigate Between Pages](navigate-between-pages.md)
{% endhint %}

## Adding a Parameter to the Page

A Parameter needs to be added to the Page that is receiving the data. In this example, there are two Pages that exist in the Application: the main Landing Page and the secondary Page. The second page is the Page where the Parameter is added.&#x20;

### Step One: Add a Parameter (receiving Page)

1. Click on _Applications_ from the left-hand menu.
2. Click on the _edit_ button of the Application from the list.

![](<../../.gitbook/assets/image (531).png>)

3\. Click on the page where you want to data to be sent to.\
4\. Click on _Page Data_.\
5\. Click on the _plus_ to add a Parameter.

![](../../.gitbook/assets/params_2.png)

6\. Add the name and type of the new Parameter.\
7\. Click on _Create_.\
8\. Click on _Save_.

![](<../../.gitbook/assets/image (499).png>)

### Step Two: Display the Parameter (receiving Page)

Now that a Parameter has been added, create a textbox or a way to display the value when it is passed to the Page during runtime.

1. Add a textbox to the Page so you will be able to display the value when it is passed from the main page to this page.

![](../../.gitbook/assets/params_4.png)

2\. Click on _Block Properties_.\
3\. Click on the ‘_A_’ button to toggle between static and dynamic text.\
4\. Select the Parameter from the dropdown.\
5\. Click on _Save_.

![](../../.gitbook/assets/params_5.png)

### Step Three: Populate the Parameter (sending Page)

The data has to be sent from the main page to the secondary page. To pass data from the main Landing Page using the Parameter you just created, follow the steps below:

1. Go to the page you will be sending data from.
2. Select the button/link that navigates to the second page.
3. Click on _Block Properties_.
4. Click on the _Edit_ button under Pass Page Parameters.
5. Configure if the data being passed is dynamic or static.
6. Add/Select a value that you would like to pass to the parameter on the second page.
7. Click on _Apply_.

![](../../.gitbook/assets/params_6.png)

![](../../.gitbook/assets/params_7.png)

## Passing Dynamic Data to the Page

When navigating between pages, you can also pass dynamic data - such as the Chart value - to the next page using page parameters. First, configure the [Chart](../../blocks-toolbox/visualizations/chart.md) block then follow the steps below:

1. Click on Block Properties.
2. Under _'_&#x41;ppearance' set Show Drilldown to True.

<figure><img src="../../.gitbook/assets/ChartDrilldown_1.PNG" alt=""><figcaption></figcaption></figure>

3\. Under ‘Action’, click on the Navigate To Dropdown and select Page.

4\. Select the page you want to navigate to.

5\. Click Pass Page Parameters.

6\. Pass Page Parameter blade will open.

<figure><img src="../../.gitbook/assets/ChartDrilldown_3.png" alt=""><figcaption></figcaption></figure>

7\. Type in the name of the parameter and select the type.

8\. Click Add.

<figure><img src="../../.gitbook/assets/ChartDrilldown_4.PNG" alt=""><figcaption></figcaption></figure>

9\. Change the field type to Dynamic Value.

10\. Select the Chart value you want to pass on the next page.

11\. Click _Apply_.

<figure><img src="../../.gitbook/assets/ChartDrilldown_5.png" alt=""><figcaption></figcaption></figure>

## View values passed to other pages at runtime

Once the Parameter has been configured, launch the application to see how the data will be passed between Pages at runtime.

1. Click on _Launch_.

![](../../.gitbook/assets/params_8.png)

2\. Click on the link that goes to the second page.\
3\. The data sent from the first page should reach the second page.

![](../../.gitbook/assets/params_9.png)

![](../../.gitbook/assets/params_10.png)

## Edit a Parameter

To edit a Parameter, follow the steps below:

1. Click on _Page Data_.
2. Click on the _pencil/edit_ button for the Parameter.

![](<../../.gitbook/assets/params_11 (1).png>)

3\. Make changes to the Parameter.\
4\. Click on _Save_.

![](../../.gitbook/assets/params_12.png)

## Delete a Parameter

To delete a Parameter, follow the steps below:

1. Click on _Page Data_.
2. Click on the _pencil/edit_ button for the Parameter.

![](../../.gitbook/assets/params_13.png)

3\. Click on _Delete._

![](../../.gitbook/assets/params_14.png)

4\. Confirm that you would like to delete the Parameter.

![](../../.gitbook/assets/params_15.png)
