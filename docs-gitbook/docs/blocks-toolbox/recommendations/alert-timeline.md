---
description: v4.4.7
---

# Alert Timeline

A list of the activities that have occurred on an Alert.&#x20;

If this list includes a hyperlink for an escalated alert, configuration properties allow the designer to determine the behavior of that hyperlink. Perhaps the design is for all alerts to be shown using the same Page, or use a formula to show archived alerts on a different Page in the same or a different App (use the URL option to accomplish this).

<figure><img src="../../.gitbook/assets/alert-timeline (1).png" alt=""><figcaption><p>Fig 1: Alert Timeline</p></figcaption></figure>

## Alert Timeline Properties

### Appearance

#### Common Properties

The _visibility_ property is common to most Blocks;

[See the Common Properties article for more details on common appearance properties.](../common-properties.md#appearance)

#### Title

Optional text that shows at the top of the block and defaults to "Alert Timeline".&#x20;

### Behavior

#### Alert ID

Supply an Alert Identifier and its timeline is displayed when the Page is opened.

#### **Navigate To**

This configures the page or website that the webpage will navigate to when the user clicks on a linked alert's hyperlink:

* Page takes you to the specified page of the current App, optionally in a new tab/window
* URL takes you to the specified URL (any website), optionally in a new tab/window

**Page**

The page to which the user is redirected, which is applicable when [Navigate To](https://documentation.xmpro.com/blocks-toolbox/common-properties#navigate-to) is set to 'Page'.

<figure><img src="https://documentation.xmpro.com/~gitbook/image?url=https%3A%2F%2F2732679253-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FmqQbULZD1ybtHYhUoujY%252Fuploads%252FZX21EYNRPwSIljyNw7ay%252Fimage.png%3Falt%3Dmedia%26token%3D1f96a727-6035-421f-b7d2-100de15681c5&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=e97382694d00bf405ae663dcf5914732750d5ef8ba0959985539f2c2d0ce8ee6" alt=""><figcaption><p>Fig 2: Navigate To and Page properties</p></figcaption></figure>

See the [Navigate Between Pages article ](https://documentation.xmpro.com/how-tos/apps/navigate-between-pages)for more information about navigating between pages.

**URL**

The URL to which the user is redirected, which is applicable when [Navigate To](https://documentation.xmpro.com/blocks-toolbox/common-properties#navigate-to) is set to 'URL'.

<figure><img src="../../.gitbook/assets/navigate-to-url-timeline.png" alt=""><figcaption><p>Fig 3: Naviage To, URL, Open in New Tab/Window, and Alert Paramater Name properties</p></figcaption></figure>

#### Open in New Tab/Window

Tick to open in a new tab/window, instead of redirecting the current tab.

#### Alert Parameter Name

Supply the parameter name of the Page/URL that will be used to navigate to the escalated alert. It is used to append the escalated Alert Identifier.
