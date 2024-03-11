# Packaging Connectors

## **Getting Started**

The XMPro Package Manager is a Windows 10 desktop application that enables you to package a new Connector or update details for an existing Connector. [See the Connector article for more information on Connectors.](../../concepts/connector.md)

This application takes you through the process of specifying all the properties your Connector requires, adding or changing the controls for each user setting, and uploading the DLL files of the [Connector code](building-connectors.md). It will provide you, upon completion, with a file that can be uploaded to Application Designer after which you can use the Connector in App Pages.

You can download the software from the Microsoft Windows 10 Store or clicking [here](https://www.microsoft.com/en-us/p/xmpro-package-manager/9n3f4wnslgzk?activetab=pivot:overviewtab).

![](<../../.gitbook/assets/image (1163).png>)

After installing the XMPro Package Manager, launch the application from the Microsoft Store or search for “XMPro Package Manager” in the Start menu and then click on “XMPro Package Manager”.

![](<../../.gitbook/assets/image (1409).png>)

## **New / Import**

On the first screen of the application, you can either create a new Connector package or import and update an existing one.

{% hint style="info" %}
&#x20;Use the arrows at the bottom of the page section to move forward or backward in the application.
{% endhint %}

![](<../../.gitbook/assets/image (1002).png>)

## **Details**

The Details form allows you to specify or edit the properties of a Connector. These properties are listed and explained below.

![](<../../.gitbook/assets/image (1443).png>)

### **Name**

The name of the Connector is what the Connector will be known as once it is uploaded to the Application Designer platform, for example, “_SQL Connector_”.

### **Description**

The description is a brief explanation of what the Connector does, for example, “_This Connector allows you to read/update a SQL Database table_“.

### **Version**

The [version](../../concepts/version.md) of the Connector. Any real number is acceptable, for example, "_1.02_".

{% hint style="danger" %}
If you make a change to an existing Connector, make sure you increment the version number as Application Designer will not allow you to upload two of the same Connectors with the same version.
{% endhint %}

### **Entry Point**

The entry point is the namespace and class name of the actual Connector’s DLL file.

For example, if a Connector with the class name “_Connector”_ is located in the _XMPro.AzureSQLConnectors_ namespace, the Entry Endpoint for it would be “_XMPro.AzureSQLConnectors.Connector”._

### **Icon File**

The icon used to represent your Connector. Click the _Browse_ button, navigate to where you’ve stored the file via the Explorer and select the new image file.

{% hint style="info" %}
It is recommended that you upload either a JPG or PNG file with a size of 64×64 pixels to accommodate for retina displays.
{% endhint %}

## **References**

The References form is where you upload the DLL file(s) that were generated when you built the project containing your Connector. You are only required to upload your Connector's DLL file; there is no need to upload the _XMPro.Integration.Framework.dll_ file as this DLL is automatically included.

To upload a file, click on the _Browse_ button next to the _DLL File(s)_ field and navigate to where the files are located and select them. When you’ve selected all the files needed, click on the _Add_ button to add them to the _Selected File(s)_ list. Please note that only files in the _Selected File(s)_ list will be included in the package. To remove a DLL from the list, click on the _Delete_ button next to the DLL name in the _Selected File(s)_ list.

{% hint style="info" %}
The XMPro Package Manager can package DLL(s) created in .NET.
{% endhint %}

![](<../../.gitbook/assets/image (1331).png>)

## **Settings**

Depending on what your Connector does, it might require that the user provide certain information, such as a server URL, username, or password. For each of these information fields (or _settings_), you need to specify which control should be used and what each control represents, for example, the SQL Connector will require the user to add a server URL. The user should provide this value using a text-box control. Thus, you need to create a control with a type of “TextBox” and a caption that reads “Server URL” in the XMPro Package Manager application.

The following controls are available to be used to capture user input:

| <ul><li>Button</li><li>CheckBox</li><li>CheckList</li><li>DropDown</li><li>EditList</li><li>FileUpload</li></ul> | <ul><li>Filter</li><li>Grid</li><li>Group</li><li>HTML Editor</li><li>NumberBox</li></ul><p></p> | <ul><li>ScriptBox</li><li>TextBox</li><li>Title</li><li>TokenBox</li><li>VariableBox</li></ul><p></p> |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |

Each control has several properties that have to be set and not all properties apply to all controls. For example, options apply to a drop-down control and not a text-box control.&#x20;

The table below contains a list of all the available properties, their description, and to which controls they are applicable.

<table><thead><tr><th width="214.33333333333331">Property Name</th><th width="190">Control Type</th><th>Description</th></tr></thead><tbody><tr><td>Allow Custom Text</td><td>Drop-Down</td><td>Allows the user to type custom text in the drop-down field if checked.</td></tr><tr><td>Allow Custom Tokens</td><td>Token Box</td><td>Allows the user to add custom tokens if checked.</td></tr><tr><td>Caption</td><td>All</td><td>Text that will be displayed with the group or setting. The caption is usually one or two words, describing the value that should be provided by the user, for example, “Server URL”.</td></tr><tr><td>Default Value</td><td>Title</td><td>The default value of the title.</td></tr><tr><td>Font Size</td><td>Script Box</td><td>Size of the font in the Script Box.</td></tr><tr><td>Help Text</td><td>All, excluding Groups</td><td>If you need to provide the user with any additional information about the purpose of the setting or helpful instructions, specify it in this field.</td></tr><tr><td>Key</td><td>All</td><td>Uniquely identifies the group or setting.</td></tr><tr><td>Keywords</td><td>Script Box</td><td>Define your variables or other custom keywords here, so that they will be available in the editor’s IntelliSense.</td></tr><tr><td>Options <br>(Drop Down)</td><td>Drop-Down</td><td>Use the Options-area to add values to the drop-down menu by specifying the Text and Value fields and then clicking Save. You may also choose an option to be used as the default option by checking the “Set as Default Value” box.</td></tr><tr><td>Options <br>(HTML Editor)</td><td>HTML Editor</td><td>Allows you to specify placeholders that can be mapped to input fields in the input received by the Agent.</td></tr><tr><td>Postback</td><td>All</td><td>If checked, will cause the form to do a postback to retrieve values from the server when the field loses focus (when the user clicks out of the field).</td></tr><tr><td>Required</td><td>All, excluding Groups</td><td>The control will be validated to make sure that a value has been specified if this box is checked.</td></tr><tr><td>ScriptBox Height</td><td>Script Box</td><td>Height of Script Box.</td></tr><tr><td>ScriptBox Mode</td><td>Script Box</td><td>Language in which script has to be written.</td></tr><tr><td>ScriptBox Theme</td><td>Script Box</td><td><p>The theme of the Script Box. Themes available include the following:</p><ul><li>Ambiance</li><li>Chaos</li><li>Chrome</li><li>Clouds</li><li>Clouds_midnight</li><li>Cobalt</li><li>Cromson_editor</li><li>Dawn</li><li>Dreamweaver</li></ul></td></tr><tr><td>ScriptBox Width</td><td>Script Box</td><td>Width of Script Box.</td></tr><tr><td>Secure</td><td>All</td><td>The value of the control will be treated as a secure value if this box is checked (encrypted and not displayed on the form in plain text). An example of a secure value is a SQL Server password.</td></tr><tr><td>Show Grid Lines</td><td>Grid</td><td>The grid lines of the grid will be shown if checked.</td></tr><tr><td>Show Header</td><td>Grid</td><td>The header of the grid will be displayed, if checked.</td></tr><tr><td>Sort Index</td><td>All</td><td>This is used to determine the group or setting’s position and works with increments of 10. Adjust this value to move the group or setting up or down on the form.</td></tr><tr><td>Unique Key</td><td>Grid</td><td>Mark a specific column as being unique, for example, an identity column.</td></tr><tr><td>Visible</td><td>All</td><td>This field sets the initial visibility of the group or setting.</td></tr></tbody></table>

![](<../../.gitbook/assets/image (69).png>)

### **Adding Settings**

Settings are grouped logically into one or more groups, such as authentication, criteria, and output.&#x20;

Create a group first, then add controls for settings to the group. To do this, follow the steps below:

1. Click on the plus-icon (top right, next to the Settings header). A form section will open, allowing you to specify a group for the settings.
2. Specify a unique value that can be used as the key for the group.
3. Add the caption you would like to use.
4. Click _Save._
5. Next, we are going to add a setting. Click on the plus-icon next to the group you’ve created.
6. Choose the type of control you would like to use.
7. Add a unique key for your control. Please note that this key needs to correspond to what you defined in your code.
8. Add a caption for your control.
9. If needed, add a default value.
10. If required, add help text.
11. Select the options that apply from the list of check-boxes.
12. Click _Save_.

![](<../../.gitbook/assets/image (306).png>)

![](<../../.gitbook/assets/image (1823).png>)

## **Output**

The second last step is to provide the location on the file system where you would like the package to be created. Click on the Browse button and navigate to the folder where you would like the package to be exported, and enter a file name. The file name defaults to the preferred format, _category\_name\_version_.xmp.

Tick the checkbox if you would like to export the file as JSON too. It will be saved to the same directory as the XMP file.

![](<../../.gitbook/assets/image (555).png>)

{% hint style="info" %}
If you imported an existing file, ensure you enter a different file name or the original will be overwritten.
{% endhint %}

## **Review: Details**

Lastly, you can navigate back through the steps to review the details that you’ve specified. If you are satisfied, complete the wizard by clicking the Save button below. Your package will be created as a file with a “.xmp” extension.

{% hint style="info" %}
If you imported an existing file, take care to either click 'Save As' to generate a new Agent, or click 'Save' to generate a new version of the original Agent.  Fu
{% endhint %}

![](<../../.gitbook/assets/image (1524).png>)

## **Further Reading**

* [How to upload your new Connector to Application Designer](manage-connectors.md)

{% hint style="info" %}
You need to have the correct permissions set against your user to be able to edit and upload Connectors. This is a role not typically given to all users.
{% endhint %}
