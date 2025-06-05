# Navigate Between Apps

It is possible to allow navigation between Apps by configuring the Action of a Block on the launching App to navigate to the destination App's URL and set it's landing page's Parameter. This allows you to separate your content into different applications that can still be easily navigated by the user.

**Important Considerations:**

* The parameter name in both Apps must match exactly
* The destination App must be published and accessible to users of the launching App.

{% hint style="info" %}
We're going to achieve this by combining concepts from the following articles:

* [How to Navigate Between Pages](navigate-between-pages.md)
* [How to Pass Parameters Between Pages](pass-parameters-between-pages.md)
{% endhint %}

## Configure the destination App

Add a Parameter and a textbox to display the value when it is passed to the Page during runtime.

See [How to Add a Parameter to the Page](pass-parameters-between-pages.md#adding-a-parameter-to-the-page) for detailed steps.

### Add a Parameter

1. Click _Applications_ from the left-hand menu.
2. Click the _edit_ button of the destination App from the list.
3. Click _Page Data_ on the landing page
4. Click the _plus_ to add a Parameter
5. Add the name and type of the new Parameter
6. Click _Create._
7. Click on _Save._

### Add a display (Optional)

1. Add a Textbox to the Page so you can display the parameter value when it is passed from the launching App.

* Click _Block Properties_
* Click the _'A'_ button to toggle from static to dynamic text.
* Select the Parameter from the dropdown.
* Click _Save._

## Configure the launching App

Add a Button to launch the second app and populate the page parameter you just created in the URL using a dynamic expression.

### Add a Button

1. Click _Applications_ from the left-hand menu.
2. Click the _edit_ button of the Application from the list.
3. Select a Page from the Application’s Edit menu.
4. Click on _Blocks_.
5. Under ‘_Actions_’, select an action such as a button.
6. Drag and drop it onto the Page of the application.
7. Select the button.
8. Click on _Block Properties._
9. Under ‘_Action_,’ click on the _Navigate To_ Dropdown and select _URL_.
10. Click the _'A'_ button to toggle the _URL_ from static to expression mode.
11. Click the dropdown to edit the expression value.
12. Enter the destination App's URL with parameters (e.g., "[https://your-xmpro-instance.com/render;appId=123?assetId=](https://your-xmpro-instance.com/app/your-app-id?parameterName=value)"+{Variable.AssetID})
13. Under ‘_Appearance,_’ give the button a name.
14. Click _Save_.

See [How to Copy the App Link](navigate-between-apps.md#copy-the-app-link) for details on how to copy the launch App's URL.

## Copy the App Link

You can copy the App link if you want to share it. This creates a link to the published app version - or to the latest version if there is no published version.

1. Click More.
2. Click Copy App Link.

<figure><img src="../../.gitbook/assets/image (1762).png" alt=""><figcaption></figcaption></figure>

## Further Reading

* [How to Pass Parameters between Pages](pass-parameters-between-pages.md)
