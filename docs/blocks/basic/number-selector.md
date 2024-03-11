# Number Selector

In scenarios where the user should select a number, the Number Selector is an input field that gives the user the option to do so. When the user enters a value, the field automatically makes sure the value entered is a number.

{% hint style="info" %}
Number Selector automatically converts the entered value into a scientific notation if it is greater than 21 digits for an integer value and greater than 6 digits for a decimal value.
{% endhint %}

## Number Selector Properties

### Appearance

#### Common Properties

The Number Selector has the option to change its _visibility, styling mode, set a placeholder, show tooltips,_ and _show clear button._&#x20;

[See the Common Properties article for more details on common appearance properties.](../common-properties.md#appearance)

An option that is specific to Number Selector is Show Spin Buttons.

#### Style

![](<../../.gitbook/assets/image (1035).png>)

#### Show Clear Button

The clear button will appear on the right side. Clicking the button will remove the value from the control.

![](<../../.gitbook/assets/image (1671).png>)

#### Show Spin Buttons

The up and down buttons will be shown on the right side of the control which the user can use to increase or decrease the current value.

![](<../../.gitbook/assets/image (1479).png>)

### Behavior

#### Common Properties

The Number Selector has the option to set the option for _read-only_ and _disabled_.&#x20;

[See the Common Properties article for more details on common behavior properties.](../common-properties.md#behavior)

Options that are specific to Number Selector are min, max, format.

#### Min and Max

Affects the minimum and maximum values that Number Selector can accept.&#x20;

![](<../../.gitbook/assets/number selector min and max.gif>)

#### Format

This will format the value to the format that was specified. In the example below, it will show it as a currency. &#x20;

![](<../../.gitbook/assets/image (714).png>)

#### Read Only and Disabled

This affects whether or not the Number Selector value can be changed and if it can only be read and not manipulated.

![](<../../.gitbook/assets/image (895).png>)

### Value

The Number Selector accepts numbers only. The value can be static, dynamic, or an expression.

[See the Common Properties article for more details on common value properties.](../common-properties.md#behavior-1)

![](<../../.gitbook/assets/image (1302).png>)

### Validation

#### Common Properties

Properties that are common to most Blocks include: _validation Group, required, pattern,_ and _message;_

[See the Common Properties article for more details on common validation properties.](../common-properties.md#validation)

### Action

#### Common Properties

Properties that are common to most Blocks include: _Navigate To and Show Confirmation Dialog;_

[See the Common Properties article for more details on common action properties.](../common-properties.md#action)
