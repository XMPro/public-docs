---
description: v4.4.1
---

# Location Capture

The Location Capture Block allows users to capture their current device location. This is useful when composing Applications such as a mobile inspection app and the user may be required to include the asset location when logging an issue. &#x20;

<figure><img src="../../.gitbook/assets/Location-capture-main.png" alt=""><figcaption><p>Fig 1: Location Capture Block</p></figcaption></figure>

## Location Capture Properties

### Appearance

#### Common Properties

The _visibility_ property is common to most Blocks;

[See the Common Properties article for more details on common appearance properties.](../common-properties.md#appearance)

#### Capture Button Text

The text displayed on the capture button.

### Behavior

#### Common Properties

The _disabled_ property is common to most Blocks;

[See the Common Properties article for more details on common behavior properties.](../common-properties.md#behavior)

### Value

#### Latitude Value

The Latitudinal value that is taken from the control such as when the capture button is clicked.

#### Longitude Value

The Longitudinal value that is taken from the control such as when the capture button is clicked.

### Validation

#### Common Properties

The _Validation Group and Required_ properties are common to most Blocks;

[See the Common Properties article for more details on common validation properties](../common-properties.md#validation).

#### Required Message

The text of the error message that is displayed to the user if no location data has been captured.

<figure><img src="../../.gitbook/assets/location-capture-required.png" alt=""><figcaption><p>Fig 2: Required Message</p></figcaption></figure>

#### Capture Failed Message

The text of the error message that is displayed to the user if the location capture fails for any reason. The reason for the failure is appended to it, e.g. "User denied the request for Geolocation".

<figure><img src="../../.gitbook/assets/Location-capture-failed.png" alt=""><figcaption><p>Fig 3: Capture Failed Message</p></figcaption></figure>
