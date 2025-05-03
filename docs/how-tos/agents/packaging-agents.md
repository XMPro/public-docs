# Packaging Agents

## **Getting Started**

The XMPro Package Manager is a Windows 11 desktop application that enables you to package a new Agent or update details for an existing Agent. [See the Agent article for more information on Agents](../../concepts/agent/).

This application takes you through the process of specifying all the properties your Agent requires, adding or changing the controls for each of the user settings, and uploading the DLL files of the [Agent code](building-agents.md). It will provide you, upon completion, with a file that can be uploaded to Data Stream Designer after which you can build Data Streams using the Agent.

You can download the software from the Microsoft Windows 10 Store or by clicking [here](https://www.microsoft.com/en-us/p/xmpro-package-manager/9n3f4wnslgzk?activetab=pivot:overviewtab).

![](<../../.gitbook/assets/image (1163).png>)

After installing the XMPro Package Manager, launch the application from the Microsoft Store or search for “XMPro Package Manager” in the Start menu and then click on “XMPro Package Manager”.

{% hint style="info" %}
You can run multiple instances of Package Manager at the same time. This side-by-side comparison is helpful when developing a new Agent that is similar to another; or comparing different versions of the same Agent.&#x20;
{% endhint %}

![](<../../.gitbook/assets/image (1409).png>)

## **New / Import**

On the first screen of the application, you can either create a new Agent package or import and update an existing one.

{% hint style="info" %}
Use the arrows at the bottom of the page section to move forward or backward in the application.\
\
When you import an existing package, you have the option to export the package as a JSON file. This is useful either to compare packages or for source control and version management.

You can also import the JSON file from an existing package, which is particularly useful if you need to modify translations added through the [Include Multilingual Support](packaging-agents.md#include-multilingual-support) feature.
{% endhint %}

![](<../../.gitbook/assets/image (1002).png>)

## **Details**

The Details form allows you to configure the properties of an Agent. These properties are listed and explained below.

![](<../../.gitbook/assets/Package Manager Details.PNG>)

### **Name**

The name of the Agent is what the Agent will be known as once it is uploaded to the Data Stream Designer platform, for example, “_Jupyter Notebook_”.

### Category

The [category ](../../concepts/agent/#categories)is selected based on the function the Agent performs, for example, "_AI & Machine Learning_".

### **Description**

The description is a brief explanation of what the Agent does, for example, “_This Action Agent allows you to create and load Jupyter Notebook files_“.

### **Version**

The [version](../../concepts/version.md) of the Agent.  Any real number is acceptable, for example, "_1.02_".

{% hint style="danger" %}
If you make a change to an existing Agent, make sure you increment the version number as Data Stream Designer will not allow you to upload two of the same Agents with the same version.
{% endhint %}

### **Virtual**

Agents can be classified as either [Virtual or Non-Virtual.](../../concepts/agent/virtual-vs-non-virtual-agents.md)

An Agent is Virtual if it is not specific to a certain environment and can be configured remotely. Non-Virtual Agents have to be in their respective environments to be able to function correctly, e.g. the SQL Server Agent, which has to connect to SQL Server via the intranet.

### **Entry Point**

The entry point is the namespace and class name of the actual Agent’s DLL file.

For example, if an Agent with the class name “_ActionAgent”_ is located in the _XMPro.JupyterNotebookAgents_ namespace, the Entry Endpoint for it would be “_XMPro.JupyterNotebookAgents.ActionAgent”._

### Isolated Loading

When loading Agents to use in a Stream Host, all the libraries are put in a separate _Load Context._ Tick _Isolated Loading_ to keep Agent files separate and reduce the risk of libraries clashing or conflicting together. In most cases, this option should be enabled.

### **Icon File**

The icon used to represent your Agent. Click the _Browse_ button, navigate to where you’ve stored the file via the Explorer and select the new image file.

{% hint style="info" %}
It is recommended that you upload either a JPG or PNG file with a size of 64×64 pixels to accommodate for retina displays.
{% endhint %}

### **Require Input Map**

Tick _Require Input Map_ to specify that your Agent will be receiving events in a defined structure. The arrow leading to your Agent will be configurable to allow the user to map the inputs of your Agent to incoming attributes.

{% hint style="info" %}
If left unticked, parent outputs will be published to this Agent as they are.
{% endhint %}

### **Add** O**n-Error Endpoint?**

Tick to add an additional Output Endpoint, called an Error Endpoint.&#x20;

An Error Endpoint will output error information when your stream is running and something goes wrong, making debugging easier. You can also define actions that will be executed after error data is sent to the next Agent in the stream by your Agent, for example when a certain record is not valid.

## Endpoints

The Endpoints form allows you to specify any Input or Output Endpoints.

### **Input Endpoints**

These Endpoints represent entry points to the Agent, which will allow the Agent to receive data or input from another Agent.&#x20;

To add an Input Endpoint, type it's name in the text field and click _Add_. The new Endpoint will appear in the list below the Add button. You may need to hover over the list and scroll down to see it. As per the image, an Input Endpoint named “Input” has been added.

{% hint style="danger" %}
The name of the Input Endpoints has to match what has been defined in the Agent’s code.
{% endhint %}

To remove an existing Endpoint, scroll down in the list until you see it, select the Endpoint and click on the _Remove_ button.

### **Output Endpoints**

Output Endpoints represent exit points from an Agent and allow you to connect your Agent to another Agent, making it possible to pass data from your Agent to another Agent.&#x20;

To add an Output Endpoint, type it's name in the text field, change the Endpoint Type to "Output", and click _Add_. The new Endpoint will appear in the list below the Add button. You may need to hover over the list underneath the text field and scroll down before being able to see it. In the image, an Output Endpoint named “_Output_” has been added.

{% hint style="danger" %}
The name of the Output Endpoints should match what has been defined in the Agent’s code.
{% endhint %}

To remove an existing Endpoint, scroll down in the list until you see it, select the Endpoint and click on the _Delete_ button.

![](<../../.gitbook/assets/image (1522).png>)

## **References**

The References form is where you upload the file(s) required for the Agent to execute. Only files in the _Selected File(s)_ list will be included in the package, and any DLLs must be created in .NET.&#x20;

To upload a file, click the _Browse_ button next to the _DLL File(s)_ field and navigate to where the files are located. Select all the files needed and click the _Add_ button to add them to the _Selected File(s)_ list.&#x20;

To remove a file from the list, click the _Delete_ button next to the file name in the _Selected File(s)_ list.

<table><thead><tr><th width="132">Type</th><th>Description</th></tr></thead><tbody><tr><td>Agent</td><td>The DLL file that was generated when you built the project containing your Agent source code.</td></tr><tr><td>Reference</td><td>Additional DLL file(s) referenced by the Agent File, such as Newtonsoft.Json. <br>You do not need to upload the <em>XMIoT.Framework.dll</em> file as this DLL is automatically included.</td></tr><tr><td>Resource</td><td>Additional DLL file(s) needed by the Reference File. </td></tr><tr><td>Zip</td><td>The Stream Host decompresses the file, while maintaining the folder structure,  so that Agents such as the <a href="https://xmpro.gitbook.io/meta/how-to-use/configuration#export-agent">Meta Agent</a> can run external source code and self package. </td></tr></tbody></table>

![](<../../.gitbook/assets/image (101).png>)

## **Settings**

Depending on what your Agent does, it might require that the user provide certain information, such as a server URL, username, or password. For each of these information fields (or _settings_), you need to specify which control should be used and what each control represents, for example, the Jupyter Notebook Agent will require the user to add a server URL. The user should provide this value using a text-box control. Thus, you need to create a control with a type of “TextBox” and a caption that reads “Server URL” in the XMPro Package Manager application.

The following controls are available to be used to capture user input:

| <ul><li>Button</li><li>CheckBox</li><li>CheckList</li><li>DropDown</li><li>EditList</li><li>FileUpload</li></ul> | <ul><li>Filter</li><li>Grid</li><li>Group</li><li>HTML Editor</li><li>NumberBox</li></ul><p></p> | <ul><li>ScriptBox</li><li>TextBox</li><li>Title</li><li>TokenBox</li><li>VariableBox</li></ul><p></p> |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |

Each control has several properties that have to be set and not all properties apply to all controls. For example, options apply to a drop-down control and not a text-box control.&#x20;

The table below contains a list of all the available properties, their description, and to which controls they are applicable.

<table><thead><tr><th width="194">Property Name</th><th width="163.33333333333331">Control Type</th><th>Description</th></tr></thead><tbody><tr><td>Allow Custom Text</td><td>Drop-Down</td><td>Allows the user to type custom text in the drop-down field if checked.</td></tr><tr><td>Allow Custom Tokens</td><td>Token Box</td><td>Allows the user to add custom tokens if checked.</td></tr><tr><td>Caption</td><td>All</td><td>Text that will be displayed with the group or setting. The caption is usually one or two words, describing the value that should be provided by the user, for example, “Server URL”.</td></tr><tr><td>Default Value</td><td>Title</td><td>The default value of the title.</td></tr><tr><td>Font Size</td><td>Script Box</td><td>Size of the font in the Script Box.</td></tr><tr><td>Group Type</td><td>Groups</td><td>Appears as either a sub heading (Default) or a hyperlink (SubPage) on the Agent's configuration page.  </td></tr><tr><td>Help Text</td><td>All, excluding Groups</td><td>If you need to provide the user with any additional information about the purpose of the setting or helpful instructions, specify it in this field.</td></tr><tr><td>Key</td><td>All</td><td>Uniquely identifies the group or setting.</td></tr><tr><td>Keywords</td><td>Script Box</td><td>Define your variables or other custom keywords here, so that they will be available in the editor’s IntelliSense.</td></tr><tr><td>Options <br>(Drop Down)</td><td>Drop-Down</td><td>Use the Options-area to add values to the drop-down menu by specifying the Text and Value fields and then clicking Save. You may also choose an option to be used as the default option by checking the “Set as Default Value” box.</td></tr><tr><td>Options <br>(HTML Editor)</td><td>HTML Editor</td><td>Allows you to specify placeholders that can be mapped to input fields in the input received by the Agent.</td></tr><tr><td>Postback</td><td>All</td><td>If checked, will cause the form to do a postback to retrieve values from the server when the field loses focus (when the user clicks out of the field).</td></tr><tr><td>Required</td><td>All, excluding Groups</td><td>The control will be validated to make sure that a value has been specified if this box is checked.</td></tr><tr><td>ScriptBox Height</td><td>Script Box</td><td>Height of Script Box.</td></tr><tr><td>ScriptBox Mode</td><td>Script Box</td><td>Language in which script has to be written.</td></tr><tr><td>ScriptBox Theme</td><td>Script Box</td><td><p>The theme of the Script Box. Themes available include the following:</p><ul><li>Ambiance</li><li>Chaos</li><li>Chrome</li><li>Clouds</li><li>Clouds_midnight</li><li>Cobalt</li><li>Cromson_editor</li><li>Dawn</li><li>Dreamweaver</li></ul></td></tr><tr><td>ScriptBox Width</td><td>Script Box</td><td>Width of Script Box.</td></tr><tr><td>Secure</td><td>All</td><td>The value of the control will be treated as a secure value if this box is checked (encrypted and not displayed on the form in plain text). An example of a secure value is a SQL Server password.</td></tr><tr><td>Show Grid Lines</td><td>Grid</td><td>The grid lines of the grid will be shown if checked.</td></tr><tr><td>Show Header</td><td>Grid</td><td>The header of the grid will be displayed, if checked.</td></tr><tr><td>Sort Index</td><td>All</td><td>This is used to determine the group or setting’s position and works with increments of 10. Adjust this value to move the group or setting up or down on the form.</td></tr><tr><td>Unique Key</td><td>Grid</td><td>Mark a specific column as being unique, for example, an identity column.</td></tr><tr><td>Visible</td><td>All</td><td>This field sets the initial visibility of the group or setting.</td></tr></tbody></table>

![](<../../.gitbook/assets/image (831).png>)

### **Adding Settings**

Settings are grouped logically into one or more groups, such as authentication, criteria, and output.&#x20;

Create a group first, then add controls for settings to the group. To do this, follow the steps below:

1. Click on the plus-icon (top right, next to the Settings header). A form section will open, allowing you to specify a group for the settings.
2. Specify a unique value that can be used as the key for the group.
3. Add the caption you would like to use.
4. Click _Save._
5. Next, we are going to add a setting. Click on the plus-icon next to the group you’ve created.
6. Choose the type of control you would like to use.
7. Add a unique key for your control. This key must correspond to what you defined in your code.
8. Add a caption for your control.
9. If needed, add a default value.
10. If required, add help text.
11. Select the options that apply from the list of check-boxes.
12. Click _Save_.

![](<../../.gitbook/assets/image (306).png>)

![](<../../.gitbook/assets/image (1823).png>)

## **Output**

### **Export as JSON file**

Tick the checkbox **Export as JSON file too?** if you would like to export the file as JSON too. It will later be saved to the same directory as the XMP file with the file name _category\_name\_version_.json.

### Include Multilingual Support

Tick the checkbox **Include Multilingual Support?** if you would like to add support for languages other than English. Uncheck languages you don't want to include.

This feature leverages generative AI to provide language translation. It is available only if the following requirements are met:

* You are connected to the internet.
* Open AI is configured (Click [here](packaging-agents.md#configure-openai-api) for instructions on how to do so).

{% hint style="info" %}
- Only the Agent Description, Properties and Static Helptext are translated. Internal messages and dynamic Helptext added when [building the Agent](building-agents.md) are not included.
- Multilingual support requires XMPro Data Stream Designer and Stream Host v4.4.16+.
- Override the automated translations by editing the JSON file and repackaging it with an incremented version number.
{% endhint %}

![](<../../.gitbook/assets/PM Output (1).png>)

### **Configure OpenAI**

1. Click _Configure OpenAI_.
2. A form will open for you to add or modify the OpenAI Endpoint and Api Key.
3. Click _Save._

<figure><img src="../../.gitbook/assets/PM Config OpenAI.png" alt=""><figcaption></figcaption></figure>

## **Review: Details**

Lastly, you can navigate back through the steps to review the details that you’ve specified. If you are satisfied, complete the wizard by clicking the Save button below before navigating to the folder where you would like the package to be exported. Your package will be created with the file name _category\_name\_version_.xmp.

{% hint style="info" %}
If you imported an existing file, take care to:

* either click 'Save as new Agent' to generate a new Agent, or click 'Save' to generate a new version of the original Agent.
* ensure you select a different location folder or increment the version to avoid overwriting the original.
{% endhint %}

![](<../../.gitbook/assets/PM Success Agent.png>)

## **Further Reading**

* [How to upload your new Agent to Data Stream Designer](manage-agents.md)

{% hint style="info" %}
You need to have the correct permissions set against your user to be able to edit and upload Agents. This is a role not typically given to all users.
{% endhint %}
