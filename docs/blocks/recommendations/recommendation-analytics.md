---
description: v4.3.2
---

# Recommendation Analytics

Recommendation Analytics is an area in which the number of Alerts for an Entity Identifier over a period of time can be compared - with an optional [alert ranking](../../concepts/recommendation/rule.md#alert-ranking) filter.&#x20;

The Entity Identifier of an Alert is defined in the [Run Recommendation Agent](https://xmpro.gitbook.io/run-recommendation/how-to-use/configuration#entity) of the Recommendation's Data Stream.&#x20;

The analytics section compares the currently viewed period of alerts with the previous period and displays the difference as a percentage. The statistics compared are:&#x20;

1. The number of Alerts generated
2. The number of Alerts that were auto escalated
3. The number of Alerts marked as false positive
4. The number of Alerts resolved.

Below the breakdown, there is a stacked bar chart of the number of Alerts for the Entity Identifier over time.

Below that is a horizontal bar of the number of Alerts for the Entity Identifier in the selected period, separated by Rule.

<figure><img src="../../.gitbook/assets/image (1874).png" alt=""><figcaption><p>Fig 1: The recommendation analytics for Entity ID 1 over the last 30 days and for all alert rankings.</p></figcaption></figure>

## Recommendation Analytics Properties

### Behavior

#### Entity ID

The _Entity ID_ field will filter and show analytics on all Recommendation Alerts that match the given Entity Identifier.&#x20;
