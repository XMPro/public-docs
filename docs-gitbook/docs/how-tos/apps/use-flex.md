# Use Flex

Flex styles are a way of changing the layout of the page so it is responsive. When using Flex, the layout and position of the Blocks will respond to fit the screen, which is important in ensuring that users have a good user experience regardless of the screen size they are viewing your Application on.

{% hint style="info" %}
It is recommended that you read the article listed below to improve your understanding of Devices and the Style Manager.

* [Device](../../concepts/application/devices.md)
* [Style Manager](../../concepts/application/block-styling.md)
* [How to Use Style Manager and Devices](use-block-styling-and-devices.md)
{% endhint %}

## Enabling Flex Styles

To enable Flex styles, follow the steps below:

1. Select the parent Block of the Blocks you want to configure the position for.
2. Click on _Block Styling_.
3. Choose _Flex_ for the display or _enable_ the flex container.

![](../../.gitbook/assets/Flex\_1.png)

## Flex Container

### Direction

The direction determines which direction the content will go. It can either be:

1. Row - Left to right
2. Reverse row - right to left
3. Column – Top to Bottom
4. Reverse column – Bottom to Top

![](../../.gitbook/assets/Flex\_2.png)

![](../../.gitbook/assets/Flex\_3.png)

![](../../.gitbook/assets/Flex\_4.png)

![](../../.gitbook/assets/Flex\_5.png)

### Justify

Justify determines the way the contents are laid out. It can either be:

1. Start
2. End
3. Space Between (puts spaces between the Blocks)
4. Space Around (puts an equal amount of space around each Block)
5. Center

![](../../.gitbook/assets/Flex\_6.png)

![](../../.gitbook/assets/Flex\_7.png)

![](../../.gitbook/assets/Flex\_8.png)

![](../../.gitbook/assets/Flex\_9.png)

![](../../.gitbook/assets/Flex\_10.png)

### Align-Items

Determines the vertical alignment of the Blocks. It can either be:

1. Start&#x20;
2. End
3. Stretch
4. Center

![](../../.gitbook/assets/Flex\_11.png)

![](../../.gitbook/assets/Flex\_12.png)

![](../../.gitbook/assets/Flex\_13.png)

![](../../.gitbook/assets/Flex\_14.png)

## Blocks inside the Flex Container

### Grow

Grow will grow the item to fit the container.

![](../../.gitbook/assets/Flex\_15.png)

If multiple Blocks have a grow value greater than 0, they will take up a ratio of the available space.

![](../../.gitbook/assets/Flex\_16.png)

### Shrink

Shrink determines whether an item is allowed to shrink if the screen is too small or if other Blocks take up too much space. Shrink will not work if the Block has a minimum width or height.

![](../../.gitbook/assets/Flex\_17.png)

### Basis

This determines the default size of the object along its direction axis.   &#x20;

![](../../.gitbook/assets/Flex\_18.png)

### Order

The order will change the order of the Blocks. Blocks with no order will be displayed first, followed by the ordered Blocks going in ascending order.

![](../../.gitbook/assets/Flex\_19.png)

### Align-Item

Aligns the individual Blocks. They can either be:

1. Start
2. End
3. Stretch
4. Center

![](../../.gitbook/assets/Flex\_20.png)

![](../../.gitbook/assets/Flex\_21.png)

![](../../.gitbook/assets/Flex\_22.png)

![](../../.gitbook/assets/Flex\_23.png)

## Further Reading

* [How to Design Pages for Mobile](design-pages-for-mobile.md)
