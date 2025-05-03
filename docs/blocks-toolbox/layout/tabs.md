# Tabs

Tabs are Blocks that allow you to separate and view related items together. Tabs can be added or removed to the tab Block if needed. They are useful for creating sections that the user can switch between or grouping related groups into one area of the page.

![](../../.gitbook/assets/y6PGlCOPxd.gif)

## Adding a Tab

To add a new Tab, select the whole tab Block or an individual Tab and click on the _plus_ symbol in the top-right hand Block toolbar.&#x20;

{% hint style="info" %}
[See the Canvas article for more details on these controls.](../../concepts/application/canvas.md#block-toolbar)&#x20;
{% endhint %}

![](../../.gitbook/assets/oVjtnJIDhd.gif)

## Deleting a Tab

To delete a Tab, select the whole Tab Block or an individual Tab and click on the _bin_ symbol in the top-right hand Block toolbar.&#x20;

{% hint style="info" %}
[See the Canvas article for more details on these controls.](../../concepts/application/canvas.md#block-toolbar)&#x20;
{% endhint %}

![](../../.gitbook/assets/E3xpP6Te1g.gif)

## Navigating Between Tabs

You can navigate between the Tabs within the canvas itself. Click on each Tab to open the contents within that particular Tab.

![](../../.gitbook/assets/WOuj0j6m7o.gif)

## Reordering Tabs

Tabs can be reordered by clicking and dragging them to change the order. When a Tab is highlighted, hold the move icon and drag the Tab to another location within the Block.

{% hint style="info" %}
[See the Canvas article for more details on these controls.](../../concepts/application/canvas.md#block-toolbar)&#x20;
{% endhint %}

![](../../.gitbook/assets/6bLoCkO6H8.gif)

## Tab Properties

### Appearance

#### Common Properties&#x20;

Tabs have properties that are common to most Blocks: _visibility_ and _tooltip_.

[See the Common Properties article for more details on common appearance properties.](../common-properties.md#appearance)

#### Selected Index

The selected index determines which tab is open by default. The index starts from 0, which means that an index of 0 refers to the first Tab, an index of 1 refers to the second Tab, and so on.

![](<../../.gitbook/assets/image (1736).png>)

![](<../../.gitbook/assets/image (435).png>)

### Behavior

#### Common Properties

The _disabled_ property is common to most Blocks;

[See the Common Properties article for more details on common behavior properties.](../common-properties.md#behavior)

#### Hide Tab Navigation

When enabled, a hidden icon appears to the left of the tab icon and name on the Canvas. The user will see the selected tab's content at runtime, but they cannot see the tabs or click on another tab.

The navigation between tabs is controlled by the [Selected Index](tabs.md#selected-index) property, e.g. by an expression.

<figure><img src="../../.gitbook/assets/Tab Hide Navigate.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
This is useful when a header or footer section is reused across multiple pages. For example, one page is used in three different drill-down scenarios. The top one-third differs based on the drill-down type and the bottom two-thirds is the same for all scenarios.

Rather than cloning the page and maintaining all three, place the top one-third in a Tab Block - and set the Selected Index to a parameter passed from the previous page to control which tab's content is shown.
{% endhint %}

### Data Source

#### Common Properties&#x20;

Tabs have properties that are common to most Blocks: filter, sort, show # of results, and skip # of results;

[See the Common Properties article for more details on common Data Source properties.](../common-properties.md#data-source)

## Tab Item Properties

### Appearance

#### Title and Icon

Each Tab has a heading that labels that particular tab section. An icon can also be added for visual purposes.
