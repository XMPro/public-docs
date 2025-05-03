# Part 5 – Rules of Engagement: Establishing Governance for Multi-Agent Generative Systems

[**Blog**](https://xmpro.com/category/blog/)**,** [**CEO'S Blog**](https://xmpro.com/category/blog/pieter-blog/)

## Part 5 – Rules of Engagement: Establishing Governance for Multi-Agent Generative Systems

Posted on [September 4, 2024](https://xmpro.com/part-5-rules-of-engagement-establishing-governance-for-multi-agent-generative-systems/) by [Wouter Beneke](https://xmpro.com/author/wbeneke/)![](https://xmpro.com/wp-content/uploads/2024/09/1725418991045.jpeg)

## Part 5 – Rules of Engagement: Establishing Governance for Multi-Agent Generative Systems

In parts [1 to 4](https://xmpro.com/part-4-pioneering-progress-real-world-applications-of-multi-agent-generative-systems/) of the series, we explored the potential of **Multi-Agent Generative Systems MAGS** to transform industrial processes. We examined how these systems can enhance _decision-making, improve efficiency, and adapt to complex operational environments_. As we move forward with implementing MAGS for industrial settings, it’s essential to address a fundamental aspect of their deployment: the rules that govern their behavior.

In this fifth article in the series, Dr. [Zoran Milosevic](https://www.linkedin.com/in/zorandmilosevic/) and I will focus on the concept of “**Rules of Engagemen**t” for MAGS. These rules serve as the foundation for the responsible and effective use of AI agents in industrial environments. _They ensure that our technological advancements align with organizational goals, legal requirements, and ethical standards._

![](https://xmpro.com/wp-content/uploads/2024/09/1725419058151-e1725842673545.png)

_Figure 1 – Position of Rules of Engagement_

The need for clear rules becomes apparent when we consider the _**autonomous nature**_ of MAGS. _**These systems can make decisions and take actions with minimal human intervention.**_ _While this autonomy offers significant benefits, it also presents risks if not properly managed._ Establishing robust rules of engagement helps mitigate these risks and builds trust in the technology.

Our discussion will cover various types of rules, including _regulatory, organizational, professional, legal, and ethical_ guidelines. We’ll explore how these rules apply to different entities within a MAGS ecosystem, including _**human operators, organizations, and AI agents**_&#x74;hemselves.

We’ll also examine practical approaches to implementing these rules. This includes _standards-based enterprise modeling_ and other structuring methods that can define _intentions, trust relationships, and interactions between agents and humans_. We will explain how these **Rules of Engagement**are areimplemented in XMPro MAGS.

Let’s begin by examining the fundamental concepts of rules and their importance in complex systems like MAGS.

### Engagement Rules: Why <a href="#ember969" id="ember969"></a>

Complex systems consist of diverse actors, each with their _own goals, as reflected in their intentions and behavioral preferences_. These actors can engage in interactions and collaborations within existing structures, such as organizations, where they accept obligations or commitments associated with their defined roles. They can also form _new partnerships with other actors based on mutual agreements_.

While internal rules guide the behavior of actors as independent entities and their involvement in collaborations, they must also adhere to external regulations. Both internal and external rules contribute to maintaining _system stability, predictability, and trust in an uncertain environment._

Our [earlier articles](https://www.linkedin.com/pulse/part-4-pioneering-progress-real-world-applications-van-schalkwyk-hgtvc/)demonstrate how AI agents are becoming an important element of complex systems, addressing the resource scarcity, data complexity and unlocking of new economic values.

_AI agents, engaged by humans or organizations, are a type of actor whose behavior can simulate or mimic that of humans_. However, _**ultimate accountability lies with the parties that have legal responsibilities**_, such as human creators or organizational owners. While AI agents may delegate tasks to other agents, the ultimate responsibility remains with the human or organization. _The importance of rules in this context is to clearly define responsibility and accountability across both human and AI agent entities._

We use the term **Rules of Engagement** to encompass the various types of rules needed to govern the behavior of actors in complex systems. These rules can be used to define _**obligations, permissions, and prohibitions**_ for actors involved in collaborative activities. They can originate from internal governance arrangements or from external rules.

The latter include &#x72;_&#x65;gulatory compliance, legal requirements, ethical considerations, professional conduct, engineering and security, safety and risk management, resource management, environmental responsibility_, and more.

### Engagement Rules: What <a href="#ember976" id="ember976"></a>

When considering computable approaches for supporting engagement rule expressions, the above considerations suggest a need to express:

* **Organizational context** that defines rules, whether the context captures a regulatory domain that specifies controlling rules over members of the domain (both individual actors and organisational structures), or a collaboration structure whose objective drives the rules of collaboration.
* **Legal entities** that have their own independent life and identity, regardless of their participation in any collaboration
* **Collaboration structures** that can define templates for interactions; these allow for multiple instantiations, such as different parties filling roles in such collaboration structures in different times.
* **Organizational or legal policies** that cover constraints over behavior of both the actors (parties and AI agents) and collaboration structures, providing guardrails over their autonomous behavior.
* **Range** of organisational or legal policy types, including simpler rules associated with obligations, permissions and prohibitions, but also their derivation, needed for more complex  expressions of accountability and responsibility (see Figure).
* **Dynamics of the** obligations, permissions and prohibitions as a result of **authorisation or delegation** of services or responsibilities across actor&#x73;**, while ensuring clear traceability of responsibility across the actors**
* **Agentic behavior** to define possible actions of actors over time, reflecting their objectives while also responding to the actions of others.
* **System policies** that can support the variability of system design over time and thus facilitate system evolutions, including the change of organisational or regulative policies.

### Engagement rules: How <a href="#ember979" id="ember979"></a>

When building complex systems, the engagement rules should be articulated in a computer interpretable style, to ensur&#x65;_&#x63;onsistency, interoperability and evolvabilit&#x79;_&#x6F;f the systems, as the operating environment rules change, including the availability of new technologies.

Such **computable expressions** in turn requires **formal models**to ensure that the computable language can be interpreted using suitable tools, including those that check consistency and traceability from business requirements to implementation, in support of conformance and compliance checking.

One practical approach to implementing such rules is based on formal models embedded in the concepts specifically developed to design and implement large or complex systems, namely the _**ISO/ITU-T/IEC open distributed processing systems (ODP) standard**_ \[1]. One component of the standard, the _ODP Enterprise Language_ provides \[2] much of the semantics needed _semantic foundatio&#x6E;_&#x66;or describing rules of engagement.

![](https://xmpro.com/wp-content/uploads/2024/09/1725414080581-1536x795.jpeg)

_(\* adapted from an upcoming conference publicatiob by_ [_Zoran Milosevic_](https://www.linkedin.com/in/zorandmilosevic/) _)_

For example, the ODP concept of **party**, can be used to model actors thar have broad set of responsibilities derived from some social or legal framework, and these can be natural persons or organisations.

Parties may engage automated **agents**], such as AI agents discussed previously, to perform actions on their behalf, and this involves **delegation** of their responsibility to address resource issues, either to do with capability specialisation or scalability reasons.   The aim here is to be able to trace the way that the **rights**and responsibilities of the parties are linked to the individual system actions and their consequences, which is key to ensuring building responsible digital twin systems.

Further, the ODP concept of **community** is useful to define the collaboration structures introduced earlier, which serve as templates for interactions of actors participating in collaborations. A community is essentially a **contract** specifying how actors can participate in different community **roles** to fulfil their objectives, and that of the community’s objective. The contract is expressed in terms of **obligations**, **permissions** or **prohibitions**policies that apply to the actors fulfilling these roles.

These policies, often referred as **deontic policies**, are intended to capture the rules of the community contract, including those that propagate to the community, from the outer regulatory environment. _Note that the term “Deontic” has roots in philosophy and logic,_&#x73;pecifically in the study of obligation, permission, and prohibition and in recent AI developments they are employed to design systems that adhere to rules and regulations, such as access control mechanisms, legal frameworks, and ethical guidelines for AI \[3].

The ODP-EL standard provides a practical implementation path for handling these deontic and accountability concepts, through encapsulating them within objects that can be handed over across the actors in the system, referred to as **deontic tokens** \[2]. Here, the holders of these tokens, are constrained  by the nature of policies encapsulated within them. _**This is similar mechanism as used in many recent security policy approaches such as OAuth 2.0 access tokens, although the constraints here are broader and apply to any holder’s actions rather than to narrower, data access actions, in access control policies.**_

Further, deontic tokens can be associated with some important actions performed by actors, when they result in changes of obligations, permissions or prohibitions associated with the actors.

These actions are referred to as **speech acts**, introduced following the linguistic concepts of speech act, and they can be used to _express how certain actions such as requests, orders or promises, change the state of world, from the perspective of obligations or permissions of actors involved_. They are powerful way of expressing chain of responsibility across parties and their AI agents.

This foundational model for expressing engagement rules as constraints on expected behaviour of agents, also serves as a basis for the inclusion of related modelling concepts/formalism and techniques needed for analysing and reasoning about system properties related to AI agent technologies.

One such technique, referred to as _**Promise Theory**_ \[4], is suitable for describing &#x69;_&#x6E;tention of AI agents and how these can be related to their objectives, future actions, and decisions, and thus the deontic formalism mentioned above_. Such decisions can be influenced by agents own objectives and commitments, while allowing for potential choices associated with expected behaviour and trust in other agents with which they can interact and collaborate.

### How do we implement the Rules of Engagement in XMPro MAGS <a href="#ember995" id="ember995"></a>

[XMPro’s Multi-Agent Generative System MAGS](https://github.com/XMPro/Multi-Agent) uses a structured approach to implement **Rules of Engagement** for AI agents.. This framework ensures AI agents operate within defined boundaries and follow organizational policies. &#x49;_&#x74; also helps agents make decisions that align with ethical standards and business objectives, which is crucial in complex industrial settings._

Here is an example from the oil and gas industry. A major refinery uses XMPro MAGS to manage its operations, from production planning to maintenance scheduling and safety monitoring. The system includes various AI agents responsible for different aspects of the refinery’s operations, each needing to work in harmony with others while adhering to strict industry regulations.

![](https://xmpro.com/wp-content/uploads/2024/09/1725426913067.png)

_Figure 3 – Agent Profile and Agent Instance_

Agent Profile System Prompts serve as the foundation for establishing overarching rules in XMPro MAGS. These prompts include

**Organizational rules:**&#x54;hese are high-level directives that reflect the company’s values and policies. For example:

```
"Prioritize safety in all operations" 
"Comply with environmental regulations at all times" 
"Optimize resource utilization to minimize waste" 
"Maintain product quality standards across all production lines" 
```

**Deontic rules:**&#x54;hese specify what agents must, may, or must not do in various situations. Examples include

```
"Agents must report any safety anomalies immediately" 
"Production agents may adjust output levels within specified ranges" 
"Maintenance agents must not schedule repairs during peak production hours unless critical" 
```

To implement these rules flexibly and dynamically, XMPro MAGS uses a system of _**Deontic Tokens**_. These tokens are based on concepts from the ISO/ITU-T/IEC open distributed processing systems (ODP) standard, ensuring a standardized approach to rule implementation. Each token represents a specific rule, including its type, the subject it applies to, and the conditions for its application.

The XMPro MAGS Agent Memory Cycle integrates these tokens at every stage of an agent’s decision-making process:

1. **Observation:**&#x54;okens guide what information agents can access and how they interpret it. For instance, a safety monitoring agent might be authorized to access real-time sensor data from all parts of the refinery.
2. **Reflection:**&#x41;gents consider applicable tokens when evaluating past actions and forming new insights. This allows them to learn from experience while staying within defined boundaries.
3. **Planning:**&#x54;oken-based rules influence the creation and prioritization of action plans. A production planning agent might adjust its scheduling strategy based on recent performance data and current operational constraints.
4. **Execution:**&#x42;efore any action, agents verify compliance with relevant tokens. This ensures that even in dynamic situations, all actions align with organizational rules and regulations.

This approach ensures that **Rules of Engagement** actively shape agent behavior in real-time. It allows the refinery to maintain safe, efficient, and compliant operations while adapting to changing conditions. _For example, system administrators can quickly update the relevant tokens through the Agent Profile if a new environmental regulation is introduced._&#x41;ll affected agents will immediately adjust their behavior to comply with the new rule, without reprograming each agent individually.

By implementing Rules of Engagement through Agent Profile System Prompts and Deontic Tokens, XMPro MAGS balances consistent agent behavior with operational flexibility. This method offers several benefits:

* Ensures AI systems remain aligned with business goals and regulatory requirements
* Provides a clear audit trail of decision-making, crucial in highly regulated industries
* Allows for quick adaptation to changing rules or conditions
* Maintains consistent behavior across different agents and processes
* Enables fine-grained control over agent permissions and restrictions
* Facilitates easier updates to system-wide policies without extensive recoding

The system also supports _hierarchical rule structures_, allowing for both broad, organization-wide rules and specific, task-level rules. This hierarchical approach ensures that agents can handle complex, nuanced situations while still adhering to overarching principles.

In the refinery example, this might look as follows:

* Top-level rules about safety and environmental compliance
* Department-level rules about production targets and quality standards
* Task-specific rules for individual processes or equipment

_This layered approach to Rules of Engagement helps organizations implement AI systems that are both powerful and controllable, suitable for complex industrial environments like oil and gas refineries. It provides the flexibility needed to optimize operations while maintaining the strict control necessary in high-risk, highly regulated industries._

### How to get started with RoE and MAGS <a href="#ember1019" id="ember1019"></a>

As we’ve explored in this article, implementing **Rules of Engagement** is essential for the successful deployment of Multi-Agent Generative Systems MAGS in industrial environments. _**These rules, when properly designed and executed, help organizations balance AI autonomy with necessary controls.**_ XMPro’s approach, using the Deontic Token System, offers a practical way to manage AI agent behavior while maintaining operational flexibility. This method allows companies to adapt quickly to changing regulations and business needs without compromising on safety or compliance.

_For senior managers and technical leaders considering MAGS for their operations, understanding these concepts is crucial._ The potential benefits of MAGS are significant, but so are the challenges of implementation. Every organization will have unique requirements for their Rules of Engagement, based on their industry, risk profile, and strategic goals.

If you’re interested in exploring how Rules of Engagement and Deontic systems could work for your company, we encourage you to take action. Dr. [Zoran Milosevic](https://www.linkedin.com/in/zorandmilosevic/) and [Pieter van Schalkwyk](https://www.linkedin.com/in/pietervs/) are available for in-depth discussions about applying these concepts to your specific situation. Their experience can help you navigate the complexities of AI governance in industrial settings. _**To arrange a consultation, please reach out through our website or LinkedIn profiles.**_ We look forward to helping you shape the future of your operations with responsible AI implementation.

***

**References**

\[1] Linington, P.F., Milosevic, Z., Tanaka, A., Vallecillo, A.: Building Enterprise Sys- tems with ODP: An Introduction to Open Distributed Processing, 1st Edition. Chap- man\&Hall/CRC Innovations in Software Engineering and Software Development (2011)

\[2] ISO/IEC IS 15414, Information Technology – Open Distributed Processing – Enterprise Language 3rd edn, 2015. Also published as ITU-T Recommendation X.911.

\[3] Z. Milosevic, Ethics in Digital Health: a deontic accountability framework, Proceeding of EDOC2019 conference, [https://ieeexplore.ieee.org/abstract/document/8945023](https://ieeexplore.ieee.org/abstract/document/8945023)

\[4] Burgess, M., & Bergstra, J. A. (2014). Promise theory: Principles and applications. Springer.

&#x20;

**Previous articles**

[Part 1: From Railroads to AI: The Evolution of Game-Changing Utilities](https://xmpro.com/part-1-from-railroads-to-ai-the-evolution-of-game-changing-utilities/)

[Part2: The Future of Work: Harnessing Generative Agents in Manufacturing](https://xmpro.com/part2-the-future-of-work-harnessing-generative-agents-in-manufacturing/)

[Part 3 – AI at the Core: LLMs and Data Pipelines for Industrial Multi-Agent Generative Systems](https://xmpro.com/part-3-ai-at-the-core-llms-and-data-pipelines-for-industrial-multi-agent-generative-systems/)

[Part 4 – Pioneering Progress | Real-World Applications of Multi-Agent Generative Systems](https://xmpro.com/part-4-pioneering-progress-real-world-applications-of-multi-agent-generative-systems/)

