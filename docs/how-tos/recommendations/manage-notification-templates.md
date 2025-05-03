# Manage Notification Templates

When a [Recommendation Alert](../../concepts/recommendation/recommendation-alert.md) is triggered by a critical event, the user can receive a notification via text message or email. The notification contains a message that notifies the user of the Recommendation Alert. You can choose to create a custom message template for when a notification is triggered, or use a default template provided. &#x20;

{% hint style="info" %}
It is recommended that you read the articles listed below to improve your understanding of Recommendations:

* [Notification](../../concepts/recommendation/notification.md)
* [Manage Notifications](manage-notifications.md)
{% endhint %}

## Add a Recommendation Notification Template&#x20;

To change what message template is used when users are notified to a Recommendation Alert, follow the steps below:

1. Click on Manage Recommendations.

![](../../.gitbook/assets/template1.png)

&#x20; 2\. Click on a Recommendation.\
&#x20; 3\. Select a Rule.\
&#x20; 4\. Scroll down and select a Notification.

![](../../.gitbook/assets/template2.png)

&#x20; 5\. Select a Notification channel (Email or SMS).\
&#x20; 6\. Click on Edit Templates.\
&#x20; 7\. Choose from the list of notification templates.\
&#x20; 8\. Choose between Default or Custom.\
&#x20; 9\. Press Save.

![](../../.gitbook/assets/notifications1.png)

## Add Custom HTML Templates for Email

By default, each notification template is set to 'default'. You can add a custom email template instead that includes different styling. The HTML file can also include placeholders for certain data that you would like to show on the notification.

Here is an example of an HTML Template file:

{% file src="../../.gitbook/assets/Recommendation Notification Template.zip" %}

To upload a custom email template, follow the steps below:

&#x20; 1\. Click on Edit Templates on any selected notification.\
&#x20; 2\. Choose from the list of notification templates for Email.\
&#x20; 3\. Choose Custom.

![](../../.gitbook/assets/notifications2.png)

&#x20; 4\. Upload an HTML template file. \
&#x20; 5\. If you have any custom placeholders, select the values that will be in those fields.\
&#x20; 6\. Press Save.

{% hint style="info" %}
Add capitalized placeholders for data within the HTML file between curly bracket symbols. For example, \{{ALERTID\}}.
{% endhint %}

![](../../.gitbook/assets/ReworkNotifTemplates1.png)

{% hint style="info" %}
This list of predefined placeholders can be used in the template without mapping:

* ALERTID
* HREF
* TITLE
* DESCRIPTION
* NOTE
* PENDINGTIME
* RULENAME
* RECNAME (Recommendation Name)
{% endhint %}

Click the link to see a preview of the email.

![](../../.gitbook/assets/ReworkNotifTemplates2.png)

## Custom Templates for SMS

By default, each notification template is set to 'default'. To use a custom SMS template instead, follow the steps below:

&#x20; 1\. Click on Edit Templates on any selected notification.\
&#x20; 2\. Choose from the list of notification templates for SMS.\
&#x20; 3\. Choose Custom.\
&#x20; 4\. Enter a custom notification message.\
&#x20; 5\. Press Save.

{% hint style="info" %}
Use the '@' symbol to choose tags from your Data Stream.
{% endhint %}

![](../../.gitbook/assets/notifications5.png)

![](../../.gitbook/assets/notifications6.png)

## Examples

### Default Template Example

If ‘Default’ is selected, a default notification message will be sent to your email address or mobile. This is an example of an email notification using a Default Template:

![](../../.gitbook/assets/template5.png)

### Custom Template Example

This is an example of an email notification using a Custom Template:

![](../../.gitbook/assets/template6.png)
