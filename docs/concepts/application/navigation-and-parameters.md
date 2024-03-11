# Navigation and Parameters

It is possible to allow navigation between Pages of an App by configuring the Action of a Block, and pass data to the Page by configuring the Pass Page Parameters option. You can add Parameters to the Page you are navigating to, and configure what value should be passed to them when the button is clicked. You can choose Dynamic or Static values.

Parameters may be needed if you want to send particular values onto another page as the user clicks on it. For example, if you have a list of machines, and a user selects one, the application may open a new page that displays information for that particular machine. In that case, you may want to pass the ID of the machine the user clicked on to the page that is being opened.&#x20;

![](<../../.gitbook/assets/image (1433).png>)

![The page will be navigated to with 14 as the value of the Id Parameter ](<../../.gitbook/assets/image (647).png>)

You can add and edit Parameters for the current Page in the Page Data tab.

![](<../../.gitbook/assets/image (176).png>)

Parameters have a Type that restricts what type of data can be sent to the Parameter. The options for Type are Boolean, DateTime, Double, Int, Long, and String.

The following Blocks allow Action:

* [Box Hyperlink](../../blocks/actions/box-hyperlink.md)
* [Button](../../blocks/actions/button.md)
* [Chart](../../blocks/visualizations/chart.md)
* [Esri Map](../../blocks/visualizations/esri-map.md)
* [Data Grid](../../blocks/basic/data-grid.md)
* [Hyperlink](../../blocks/actions/hyperlink.md)
* [Indicator](../../blocks/basic/indicator.md)
* [List](../../blocks/basic/list.md)
* [Map](../../blocks/visualizations/map.md)
* [Templated List](../../blocks/layout/templated-list.md)
* [Toolbar](../../blocks/layout/toolbar.md)
* [Tree Grid](../../blocks/basic/tree-grid.md)
* [Tree List](../../blocks/basic/tree-list.md)

## Further Reading

* [How to Navigate between Pages](../../how-to-guides/apps/navigate-between-pages.md)
* [How to Pass Parameters Between Pages](../../how-to-guides/apps/pass-parameters-between-pages.md)
