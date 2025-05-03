---
description: v4.4.8
---

# Alert Action

Configure a button to perform one of the following [actions](../../concepts/recommendation/recommendation-alert.md#actions) on an open Recommendation Alert:&#x20;

* Mark As Resolved
* Mark As False Positive
* Save
* Share
* Assign

The button text - and in some cases the icon - are defaulted when the [action](alert-action.md#action) property is selected, but the designer can override these properties.

The action button will be disabled at run-time should the alert be archived.&#x20;

<figure><img src="../../.gitbook/assets/alert-action-mark-as-resolved.png" alt=""><figcaption><p>Fig 1: Alert Action</p></figcaption></figure>

## Alert Action Properties

### Appearance

#### Common Properties

Properties that are common to most Blocks include _visible, styling mode_, _tooltip_, and _icon;_

[See the Common Properties article for more details on common appearance properties.](../common-properties.md#appearance)

#### Type

The type of the button can be changed depending on its purpose. Options include danger, normal, success, and default.

![](<../../.gitbook/assets/image (843).png>)

#### Text

The text that shows on top of the Button.

### Behavior

#### Common Properties

Properties that are common to most Blocks include _disabled;_

[See the Common Properties article for more details on common behavior properties.](../common-properties.md#behavior)

#### Alert ID

Supply an Alert Identifier on which the selected action will be performed.

#### **Action**

The action to be performed on the alert.

<table><thead><tr><th width="154">Action</th><th>Description</th></tr></thead><tbody><tr><td>Mark as Resolved</td><td>Someone reviewed the issue, took mitigation steps, and considered the matter resolved.</td></tr><tr><td>Mark as False Positive</td><td>Someone reviewed the issue, determined that the asset doesn't have an issue or it was triggered while in Maintenance/Service mode, and considered the matter closed.</td></tr><tr><td>Save</td><td>Saves the changes made on the Recommendation Alert.</td></tr><tr><td>Share</td><td>Ability to share the Recommendation Alert to users that have run access to the Recommendation. Selected users will receive an email with the note and a link to the Recommendation Alert.</td></tr><tr><td>Assign</td><td><p>Ability to Assign (or Reassign) responsibility for the Recommendation Alert to a user that has run access to the Recommendation. The default selection is the logged-in user.</p><p>When this action is performed, the action is recorded on the <a href="https://documentation.xmpro.com/concepts/recommendation/recommendation-alert#timeline">Timeline </a>and in the <a href="https://documentation.xmpro.com/concepts/recommendation/recommendation-alert#discussion-1">Discussion</a> - thus notifying the assignee.</p></td></tr></tbody></table>

#### Enable Focus

This determines if the user can navigate to the Button by using the keyboard. This includes using the tab button to switch between text boxes on a form, and then clicking the tab button at the end to highlight and select the Button. Buttons will also be focused on when you click on them. If a Button is clicked, and no action occurs, the Button will also remain in focus.

![](<../../.gitbook/assets/enable focus true.gif>)

### Action

Configure actions to be triggered when the user clicks the button.

[For detailed instructions see the Common Properties article for more details](../common-properties.md#action)
