---
description: v4.2.0
---

# Scoring

## What is Alert Ranking and Alert Scoring?

When setting up a Recommendation, authors are able to influence the order in which Alerts will be shown. Ranking and Scoring help the alert recipient prioritize recommendations according to their importance.&#x20;

## What is the difference between Alert Ranking and Alert Scoring?

[**Alert Ranking**](../../how-tos/recommendations/create-rules.md#create-rules) allows users to rank a recommendation as High/Medium/Low.&#x20;

**Alert Scoring** is an alternate fine-tuning of the alert ranking by specific factors such as recommendation, category, rule, and an optional value from the Data Stream.

By allowing the author to assign a calculated score to an Alert instead of a ranking, you can have even more detailed control over its importance level.&#x20;

This Score also helps the alert recipient to understand its relative importance.&#x20;

{% hint style="info" %}
Authors still have the option to use Alert Ranking instead of Alert Scoring if they prefer.
{% endhint %}

## How is the scoring calculated?

This feature allows recommendation authors to assign numerical values (1-10) to various aspects during configuration. These values are then multiplied, resulting in an alert score.

```
score = recommendation factor * category factor * rule factor * optional factor
```

The score is calculated at the time the alert is generated and is not recalculated should any of the factors be updated.

## Where are scoring values added?

The values used to score an Alert could be configured in these different areas:

* [**Recommendation**](../../how-tos/recommendations/manage-recommendations.md#create-a-recommendation) – assesses the significance of the recommendation itself

<figure><img src="../../.gitbook/assets/Fig 1. Recommendation Factor.PNG" alt=""><figcaption><p>Fig 1. Recommendation Factor</p></figcaption></figure>

* [**Recommendation Category**](../../how-tos/manage-categories.md#adding-a-new-category) – evaluates the importance of the recommendation's category

<figure><img src="../../.gitbook/assets/Fig 2. Category Factor.PNG" alt=""><figcaption><p>Fig 2. Category Factor</p></figcaption></figure>

* [**Recommendation Rule**](../../how-tos/recommendations/create-rules.md#create-rules) **-** when managing a rule within a recommendation

<figure><img src="../../.gitbook/assets/Fig 3. Rule Factor.PNG" alt=""><figcaption><p>Fig 3. Rule Factor</p></figcaption></figure>

* [**Recommendation Optional**](../../how-tos/recommendations/create-rules.md#create-rules) - an Optional Rule Factor value retrieved from the Data Stream.&#x20;

<figure><img src="../../.gitbook/assets/Fig 4. Optional Factor.PNG" alt=""><figcaption><p>Fig 4. Optional Factor</p></figcaption></figure>

## Viewing the recommendation scoring

When viewing the **Recommendation Alerts** list, The Recommendation Scoring is displayed on the Score Column, and the Alerts are arranged in a descending order based on their Scoring.

<figure><img src="../../.gitbook/assets/Fig 5. Recommendation Alerts List.PNG" alt=""><figcaption><p>Fig 5. Recommendation Alerts List</p></figcaption></figure>

You can also view the Scores using the **Score Factor Matrix**. To open the Score Factor Matrix:

1. Open Manage Recommendations
2. Click on _“More”_ ellipses
3. Click the "_Score Factor Matrix"_ button

<figure><img src="../../.gitbook/assets/Fig 6. Step 1 of 3 - Where to find Open Manage Recommendations.PNG" alt=""><figcaption><p>Fig 6. Step 1 of 3 - Where to find "Open Manage Recommendations"</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Fig 7. Step 2 of 3 - Where to find ... and Step 3 of 3 - Where to find Score Factor Matrix.PNG" alt=""><figcaption><p>Fig 7. Step 2 of 3 - Where to find "..." and Step 3 of 3 - Where to find "Score Factor Matrix"</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Fig 8. Score Factor Matrix.PNG" alt=""><figcaption><p>Fig 8. Score Factor Matrix</p></figcaption></figure>

{% hint style="info" %}
This table only shows an estimate as the Optional Factor of the Recommendation could not be determined until the Alert is generated.
{% endhint %}

## Viewing the Score Factor history on a timeline

The changes made on a Score Factor Recommendation can be viewed on a timeline in the following areas:

* **Category Timeline** – when observing score factor changes within this timeline.

<figure><img src="../../.gitbook/assets/Fig 9. Category Timeline.PNG" alt=""><figcaption><p>Fig 9. Category Timeline</p></figcaption></figure>

* **Recommendation & Rule Timeline** – when viewing score factor changes within this timeline.

<figure><img src="../../.gitbook/assets/Fig 10. Recommendation &#x26; Rule Timeline.PNG" alt=""><figcaption><p>Fig 10. Recommendation &#x26; Rule Timeline</p></figcaption></figure>
