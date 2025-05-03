# From Many, One – The Nature of Complex Event Processing

[**Blog**](https://xmpro.com/category/blog/)

## From Many, One – The Nature of Complex Event Processing

Posted on [July 22, 2015](https://xmpro.com/the-nature-of-complex-event-processing/) by [Kirsten Schwarzer](https://xmpro.com/author/kschwarzer/)

Initially, systems management software was used to detect singular events within a given system, by detecting log entries or event triggers located within a device or system or application or database. The management system would then detect an event within that subsystem, create an alert, and leave it to humans to diagnose the ultimate problem.

This worked fine for simple systems, and simplistic management paradigms. But as systems rapidly evolved into complex, heterogeneous environments comprised of multiple subsystems, the ability to spot events in a near real-time capacity became nearly impossible. Complex systems can create complex events, where multiple subsystems each give a partial indication of an event, but the reality can’t be understood from any one indicator. In other words, in a complex system, some events can’t be ‘seen’ unless all of the smaller indicators are gathered and correlated to provide a complete, holistic picture of the situation.

#### Principal uses of Complex Event Processing

Complex Event Processing (CEP) tools, then are critical for understanding and managing events across complex, distributed systems, to uncover things that are happening in the environment, which might not be detected by any one singe system. As such, complex event processing is used in a number of ways, including:

**Security intrusion and attack detection** – Intrusion detection, almost by definition, relies on complex event processing to detect patterns of attack and intrusion across different systems. For example, a router may log traffic coming from a given IP range, a server may detect a login by an account with admin level rights, and a database might log a a download of data. All of these alone are not necessarily of note. But, taken altogether, they signal a potential compromise in process.

**Fraud prevention** – Certain fraud schemes, especially within financial systems, can be extremely difficult to detect. And just like the security event described above, any one event in a fraud detection event might not be noteworthy in and of itself, but becomes very interesting when correlated with other events to paint a complete picture.

**Scheduling and control automation** – Complex events are not just related to security, however, and detection and management of complex events can also lead to increases in productivity and bottom-line revenues. By detecting events as they are in progress, a CEP tool allows for the automated response to those events, to minimize response to certain events much more quickly than can be achieved via human interaction. CEP tools allow individual systems to modify their settings and controls in response to complex events, in order to either minimize damage caused by that event, maximize gains by capitalizing on the event, or both.

**Business process automation** – Once complex events are understood and modeled, business processes can be developed to manage and capitalize on those events to benefit the organization. CEP tools allow process owners to not only model and capture events, but design and implement those business processes.

#### Common Criteria of Complex Event Processing Tools

Complex event processing systems can be used across a variety of complex systems, in a variety of ways. And as noted above, CEP tools can be used not only to detect and mitigate problems, but also to

**Modeling of complex events and their criteria** – One of the key aspects of capturing and managing complex events lies in the ability to model those events, and understand how they manifest themselves within the underlying sub-systems of the environment. This allows the management systems to understand what it’s ‘looking’ at, and identify complex events on a more timely basis.

**Hierarchical classification of events** – Closely tied to the point above is the ability to arrange singular events into a hierarchical classification, which allows for both the prioritization of those events and the remediation and response. This hierarchical classification ties into things like event mapping, to aid in the modeling and classification of the complex events.

**Event-driven Architecture** – CEP tools commonly utilize an event-driven architecture, which captures and correlates individual messages and event indicators, classifies and prioritizes them, and proceeds with automated responses, if those responses have been defined.

#### XMPro and Complex Event Processing

Complex event processing is one of the primary functions of the XMPro toolset, and both the Business Activity Monitor and Intelligent Operations Monitor modules are built on CEP principles. XMPro is designed to model and automate both events and the operational and business processes to respond to and capitalize on those events as they occur. XMPro utilizes an event-driven architecture comprised of activity triggers, which are processed into an activity queue and ultimately lead to the invocation of activity agents that allow businesses to respond to events quickly and effectively.

