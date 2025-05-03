# Menu

A Menu is a list of options, commands, or pages presented to the user that they can select. This can be used for navigation purposes, such as separating the app or page into sections that the user can be directed to.

![](<../../.gitbook/assets/image (395).png>)

## Adding Menu Items

Once a Menu Block has been added to the screen, menu items can be added by using the Items property under _Behavior_ in _Block Properties_. A separate area will open that will allow you to add items to your Menu. Here you can specify the text that will display on the link, and the page the app will navigate to when the user clicks on the link.&#x20;

![](<../../.gitbook/assets/image (1471).png>)

To edit an item, click the item on the grid, and edit mode will be enabled.&#x20;

Menu items can be reordered and moved inside to create a submenu by clicking the left icon and dragging it into position.

![](<../../.gitbook/assets/menu submenu.gif>)

## Menu Properties

### Appearance

#### Common Properties&#x20;

The menu has properties that are common to most Blocks: _visibility_ and _tooltips_,

[See the Common Properties article for more details on common appearance properties.](../common-properties.md#appearance)

Options that are specific to the Menu include _collapse when space is limited_, _orientation_, and _submenu direction_.

#### Collapse When Space is Limited

If the width of the menu is longer than the screen, it will collapse. Applies only if the [orientation ](menu.md#orientation)is "horizontal".

![](<../../.gitbook/assets/menu collapse.gif>)

#### Orientation

![](<../../.gitbook/assets/image (450).png>)

![](<../../.gitbook/assets/image (845).png>)

### Behavior

#### Common Properties

The _disabled_ property is common to most Blocks;

[See the Common Properties article for more details on common behavior properties.](../common-properties.md#behavior)

#### Items

The Items section is used to configure the menu items. If Menu is left unconfigured, by default it will display all the pages of the app.

#### Hide Submenu on Mouse Leave

_Hide submenu on mouse leave_ is when we have a submenu and if this option is enabled it will collapse the menu, otherwise, a click is required to close the menu.

![](<../../.gitbook/assets/menu hide on mouse leave.gif>)
