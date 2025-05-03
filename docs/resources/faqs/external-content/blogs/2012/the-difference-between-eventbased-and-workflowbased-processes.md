# The Difference Between Event-based And Workflow-based Processes

[**Blog**](https://xmpro.com/category/blog/)**,** [**CEO'S Blog**](https://xmpro.com/category/blog/pieter-blog/)

## The Difference Between Event-based And Workflow-based Processes

Posted on [May 14, 2012](https://xmpro.com/the-difference-between-event-based-and-workflow-based-processes/) by [Pieter van Schalkwyk](https://xmpro.com/author/pietervs/)

There is a long running misconception that business processes are workflow-based. It stems from Business Process Analysis (BPA) efforts to try and map the flow of a process, document it and then look at possible ways to improve on it.

The BPA and Business Process Reengineering (BPR) movements needed exact flows to firstly understand processes and secondly try and improve efficiency gains from these processes. Many of it stemmed from a “factory-styled” view where processes flow sequentially and sometimes even in parallel but always in a pre-determined route.

In these instances processes start with the flow in mind. The activities that happen along the flow path are secondary to the flow. Many workflow and BPM tools also work on this premise. It starts of by mapping the process flow in an exact flow model and even in a flow executable that can be plugged into a flow engine.

This **workflow-based approach** requires that all potential exceptions are included in the model (which can make for an incomprehensible diagram in complex real-world processes) and routing is often decided by hard-coded business rules and yes/no decisions. This approach works for a limited number of processes in modern organizations with the rise of what Peter Drucker called “Knowledge Workers”. A workflow-based approach is restrictive for most knowledge workers.

A key part of knowledge work is to make decisions when the business rules fail to understand the context of a process. Paul Harmon of BPTrends.com describes this decision-making process very well in a [recent article](http://www.bptrends.com/publicationfiles/advisor20120327.pdf). This diagram from the article describes the problem with decision-making in processes. (I suggest that you click on the image and read the article by Paul)

&#x20;

[![](https://xmpro.com/wp-content/uploads/2012/05/BPTrendsDecision.png)](http://www.bptrends.com/publicationfiles/advisor20120327.pdf)

When processes are viewed at a high level (as often happens in BPA) then all tasks seem to be based on some predetermined decision logic. But as you get to specific tasks and activities lower in process it appears that many require user decision-making that is based on contextual information and past experience.

A simple example is when a sales person decides to refer an account for a credit check prior to continuing an on-boarding process. This may be as a result of reading a newspaper report on the current prospect. There are many combinations and permutations of possible customer on-boarding activities that may/need to occur to take a customer from the CRM system to the Accounts Receivable system. A workflow-based approach in this instance is too restrictive.

An **Event-based approach** on the other hand looks at all the possible events that can occur for a specific process. These events or activities are placed in a single process “container” but the flow relationships are not pre-defined. Event-based processes are sequenced when the user need to access that specific event.

&#x20;

[![](https://xmpro.com/wp-content/uploads/2012/05/Unstructured_Process.png)](https://xmpro.com/xmpro-ibpms/xmdesigner/)

&#x20;

A sales person may have a number of options like “Credit Check”, “Technical Review”, “Legal Review” and many more. The context of a specific transaction will determine the route that will be chosen for that specific transaction. It can be completely different for the next transaction. This provides the flexibility to cater for the work that knowledge workers do. It also allows for new events to be “discovered” and added to the process container without jeopardizing the “workflow”.

An event-based approach starts with the activity or event in mind, its characteristics, human interface (if required), integration, documents and artifacts, and business rules (if applicable). The workflow characteristics are secondary to the activities or events that occur.

There are many benefits of an event-based approach above a workflow-based approach. Here are a few:

* &#x20;It allows business users to respond to business processes in the context of each specific transaction and respond appropriately to each;
* With the use of Business Intelligence or reporting it is possible to analyze the “real” flows in processes retrospectively. This is highly valuable information for process improvement initiatives;
* Additional events can be added without jeopardizing complex workflow routings;
* It is possible to create “hybrid” processes that may have workflow-like structure in some areas while it is case-style unstructured in other parts of the process. Most real-world complex processes resemble this behavior; and
* Event-based is not prescriptive and if it is combined with process goals it can be used to drive process outcomes similar to a business GPS that allows users to take different options and routes to suit the circumstances.

The best analogy on the difference between workflow-based and event-based is that you are not running on train tracks, you are driving with a GPS.

