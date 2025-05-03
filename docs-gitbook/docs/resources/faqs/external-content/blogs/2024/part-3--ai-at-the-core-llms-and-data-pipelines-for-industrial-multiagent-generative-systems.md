# Part 3 – AI at the Core: LLMs and Data Pipelines for Industrial Multi-Agent Generative Systems

[**Articles**](https://xmpro.com/category/blog/articles-blog/)**,** [**Blog**](https://xmpro.com/category/blog/)**,** [**CEO'S Blog**](https://xmpro.com/category/blog/pieter-blog/)

## Part 3 – AI at the Core: LLMs and Data Pipelines for Industrial Multi-Agent Generative Systems

Posted on [July 24, 2024](https://xmpro.com/part-3-ai-at-the-core-llms-and-data-pipelines-for-industrial-multi-agent-generative-systems/) by [Pieter van Schalkwyk](https://xmpro.com/author/pietervs/)![](https://xmpro.com/wp-content/uploads/2024/07/1721190831981-1024x585.png)

## **Part 3 – AI at the Core: LLMs and Data Pipelines for Industrial Multi-Agent Generative Systems**

## **Part 3 – AI at the Core: LLMs and Data Pipelines for Industrial Multi-Agent Generative Systems**

![](https://xmpro.com/wp-content/uploads/2022/03/Pieter-2019-Square-Web-150x150.jpeg)

#### **Pieter Van Schalkwyk**

**CEO at XMPRO**, Author – Building Industrial Digital Twins, DTC Ambassador, Co-chair for AI Joint Work Group at Digital Twin Consortium

July 14, 2024 – Originallly posted on [Linkedin](https://www.linkedin.com/pulse/part-3-ai-core-llms-data-pipelines-industrial-pieter-van-schalkwyk-1rdnc)

In [Part 1](https://xmpro.com/part-1-from-railroads-to-ai-the-evolution-of-game-changing-utilities/), “**From Railroads to AI: The Evolution of Game-Changing Utilities,”** I shared my thoughts on why GenAI will become a “utility” like electricity and why we have an opportunity to create “appliances” that will change the way we work and improve the quality of life for everyone.

In [Part 2](https://xmpro.com/part2-the-future-of-work-harnessing-generative-agents-in-manufacturing/), “**The Future of Work: Harnessing Generative Agents in Manufacturing**,” I explained that skills shortages and gaps, productivity challenges, and the complexity of doing business at the speed of thought is forcing us to look at alternate, novel ways to do work and have a  “Technology Enabling Focus” as [Michael Carroll](https://www.linkedin.com/in/michael-carroll-0106367/) so accurately commented.

> _Utilizing technology to foster focus instead of allowing it to become a distraction or creating additive sickness. This means avoiding constant alerts from dashboards and warnings from analytics that divert attention away from meaningful work – Mike Carroll_

As I was writing Part 3 on the architecture of Multi Agent Generative Systems (MAGS) with examples from applications with XMPro, I realized that I first have to explain **“What”** the reason is for using agents in the first place, that it is not just writing procedural code with some LLM capabilities baked in. So this became Part 3, with [Part 4](https://xmpro.com/part-4-pioneering-progress-real-world-applications-of-multi-agent-generative-systems/) following to show the architecture and **“How”** to build an XMPro MAGS agent team with some examples. I also decided to add Part 5, which will discuss governance, ethical use, trustworthiness, and some thoughts on managing change in organizations planning to use MAGS with the help of [Zoran Milosevic](https://www.linkedin.com/in/zorandmilosevic/)

Through parts 3 and 4, I explain XMPro MAGS using an Industrial Predictive Maintenance Agent Team and will explore the anatomy of this Reliability and Root Cause Agent as an example.

&#x20;

![](https://xmpro.com/wp-content/uploads/2024/07/1721191917497-1536x806.jpeg)

_**Figure 1 – XMPro MAGS Reliability and Root Cause Agent in a Data Pipeline**_

The following key topics will guide the discussion **“Chain of Thought”** in this paper:

* **Understanding Industrial Processes**: What distinguishes industrial processes from others, and how do the agents within these systems operate differently?
* **Employing LLM-based Agents**: How can Large Language Models (LLMs) be utilized within industrial processes?
* **Data Pipelines in Industrial Systems**: Why are data pipelines crucial for assembling industrial MAGS?

In part 4 “**Pioneering Progress: Real-World Applications of Multi-Agent Generative Systems**” I will continue and expand on:

* **Anatomy of MAGS**: What are the structural and functional components of MAGS?
* **Examples of XMPro MAGS Applications**: What are some real-world applications of XMPro MAGS in industrial contexts?

***

In my career, I’ve worked with both industrial and non-industrial operational business processes. Here is why I think industrial processes are different and why their agent teams are different.

### Understanding the Uniqueness of Industrial Processes <a href="#ember1496" id="ember1496"></a>

Operational processes in industrial settings markedly differ from typical business workflows found in non-industrial environments. The operational impact of industrial processes often results in safety issues or significant loss, and decisions are made on real-time operations intelligence through SCADA, IoT, Digital Twins, and other operational technology applications.

Traditional business processes are mostly **deterministic**, designed to follow a predetermined workflow that ensures consistency and efficiency. Such processes execute tasks based on “If-then-else” logic, where every step is predefined and structured to enable consistent performance, even by the least skilled personnel. This model is great for Robotic Process Automation (RPA), where tasks are clearly defined, and outcomes are predictable.

In the image below, I asked Claude to create a Mermaid diagram of the agent process that typical GenAI Agent frameworks like CrewAI, Autogen, and LangChain follow:

![](https://xmpro.com/wp-content/uploads/2024/07/1721191965711.png)

_**Figure 2 – Typical Task-based LLM Agent**_

These GenAI Agent frameworks are tailored to support defined workflow tasks by generating content, curating, and reviewing within these deterministic processes. These frameworks enhance efficiency by automating routine content generation and curation processes governed by set rules and procedures. _Creating the Mermaid diagram is an example of a typical deterministic content generation task that I can assign to one of these agents to improve my efficiency._

#### “The Decision is the Task” for Many Industrial Processes <a href="#ember1502" id="ember1502"></a>

In contrast, operational business processes in industrial applications rely on dynamic and complex data inputs. They generally use real-time operational and sensor data that frequently changes, requiring integrating this data with recent contextual information. This information is synthesized and presented to Subject Matter Experts (SMEs) such as Operations Managers, Reliability Engineers, or Quality Supervisors.

These subject matter experts use detailed data, combined with their skills and available documentation, to make informed decisions. It is most often presented in a dashboard to provide the information and context. Their decision-making further involves causal analysis to determine why (_Knowing What Causes What, and When – more on this in the future_) before taking any action.

We describe these as **Emergent Processes**, where the next best steps emerge based on the SME’s ability to observe, reflect, plan, and determine actionable options, making these processes fundamentally adaptive and responsive to the changing environment.

MAGS is an example of a GenAI Agent framework that _**mimics these SME actions**_. It supports emergent, non-deterministic processes that must handle far more complex and dynamic decision-making than its deterministic counterparts.

MAGS’ primary focus is to use advanced reasoning processes to recommend actions, and in fully automated industrial environments, potentially execute these actions directly. In such scenarios, the SME assumes a critical oversight role as the _**‘Human On The Loop’**_, ensuring that the automated actions align with strategic objectives and operational safety standards.

This shift emphasizes the framework’s ability to operate independently while still under expert governance, enhancing efficiency without compromising control or quality.

### What is MAGS? <a href="#ember1509" id="ember1509"></a>

Multi Agent Generative Systems (MAGS) are systems that _consist of multiple agents, each with a defined role, working together to deconstruct and solve complex problems. These systems mimic the hierarchical structure of enterprises and mirror real-world team dynamics._ They can also scale intelligently by adding more agents to handle increased workloads.

Each agent in the system _handles modular decision-making step&#x73;_&#x74;hat contribute to the overall problem-solving process in a composable way. The agents can further collaborate and cooperate to achieve defined goals without human intervention.

Inspired by this _**foundational research**_ at Stanford, [_Generative Agents: Interactive Simulacra of Human Behavior_](https://arxiv.org/pdf/2304.03442), XMPro MAGS enables a collaborative environment where multiple agents share insights, learn from each other, and make more informed and contextually relevant decisions. XMPro MAGS has the ability to observe, reflect, memorize, learn, plan, and act using LLMs to simulate the same behavior human SMEs use to make operational decisions.

### From Coding to Commanding: Leveraging LLMs for Enhanced Decision-Making in Industrial Applications <a href="#ember1513" id="ember1513"></a>

A _**common application**_ for existing GenAI Agents, including platforms like CrewAI, Autogen, and LangChain, is _**optimizing the software development process.**_ These GenAI agents enhance efficiency by specializing in distinct roles within the project workflow.

Project Manager Agents break projects into manageable subtasks, Coding Agents handle the actual development of software, Testing Agents are responsible for quality assurance, and Documentation Agents create comprehensive user guides. This specialization streamlines the entire development process, from conception to completion, ensuring each phase meets high standards of quality and efficiency.

Here, large language models primarily automate tasks like coding and testing, focusing on individual steps without integrating them into broader decision-making processes.

Conversely, Multi-Agent Generative Systems (MAGS) use LLMs for _**complex decision-making**_ in industrial settings.

For example, an Expert OEE MAGS, which is explained in more detail later, actively improves manufacturing efficiency by deploying specialized AI agents focusing on availability, performance, quality monitoring, and predictive maintenance. These agents can reason and decide on actions based on their observations, reflections, memory, and planning, as shown in Figure 3. They dynamically optimize operations and adapt to evolving industrial challenges by continuously analyzing real-time data.

![](https://xmpro.com/wp-content/uploads/2024/07/1721192042079-1536x707.jpeg)_**Figure 3 – XMPro MAGS Agent Observe, Reflect, Plan, Act**_

In systems like the Expert OEE Optimizer, MAGS monitors equipment performance, analyzes data to uncover patterns, devises optimization strategies, and executes these plans, significantly impacting operational outcomes. The primary value of LLMs in MAGS lies not just in performing tasks, but in driving sophisticated reasoning processes that enhance decision-making and operational efficiency.

This contrast _**highlights significant differences in LLM utilization**_:

* **Task vs. Decision-Making Focus**: In typical non-industrial GenAI agent applications, LLMs enhance task execution. In industrial settings, they support a cycle of observation, reflection, planning, and action, directly influencing strategic, tactical, and operational decisions.
* **Integration and Impact**: Non-industrial LLM GenAI agent integration is often compartmentalized, focusing on specific tasks. Industrial LLMs work holistically, with agents interacting and adapting based on collective insights, boosting system intelligence and responsiveness.
* **Scope of Automation**: While non-industrial automation targets reducing manual labor in routine tasks (like me drawing the Mermaid diagram), industrial automation through MAGS aims to optimize entire processes, employing GenAI to create effective decision intelligence.

Another key distinction between traditional GenAI Agent frameworks for task-based processes and Multi-Agent Generative Systems (MAGS) lies in their development and deployment methodologies. Task-oriented agent frameworks typically _**employ a procedural, coded approach**_ that defines LLM content tasks and sequences.

In contrast, MAGS, particularly those developed with XMPro, favor a _**visual data pipeline approach.**_ This method enables an agile and flexible composition of work teams and agents, enabling more dynamic interaction and rapid adaptation to changing conditions in the operational environment.

### Why Data Pipelines are Superior to Traditional Procedural Approaches in MAGS <a href="#ember1525" id="ember1525"></a>

Traditional task-based Generative AI (GenAI) agents primarily employ procedural coding to execute predefined tasks in a sequence defined by a controller or “supervisor,” as shown in the Mermaid flow diagram in Figure 2. Some platforms assign the “CEO” role to the orchestration functions.  While effective for straightforward content generation and curation tasks, this approach struggles in dynamic and complex decision-making applications typical of industrial settings.

In contrast, data pipelines or data streams offer a transformative approach to building MAGS. Unlike procedural coding, data pipelines utilize a fluid, dynamic method that allows for continuous data integration. This integration ensures decisions are based on the most up-to-date and relevant information, which is critical in fast-paced industrial environments. The flexibility of data pipelines allows for modular changes with minimal disruption to the overall system, facilitating easier adaptation to evolving requirements and conditions.

![](https://xmpro.com/wp-content/uploads/2024/07/1721192083008-1536x666.jpeg)

The real power of using data pipelines in MAGS centers on their **ability to effectively employ LLMs for complex reasoning and decision-making.** Rather than just automating tasks, LLMs in these pipelines can observe data and patterns, reflect, learn, plan, act, and collaborate within a governance framework or _**“Rules of Engagement”**_.

This capability significantly **improves decision-making** by allowing the integration of diverse data sources and tools to contextualize decision data. It facilitates the incorporation of physics-based, statistical, and traditional AI models, anchoring MAGS in practical and empirical reality. This approach ensures that decisions are data-driven and realistically applicable, grounded in physics and reality, greatly enhancing the system’s reliability and effectiveness.

Furthermore, the **use of visual, drag-and-drop interfaces** in constructing data pipelines offers substantial advantages in terms of **usability and explainability.** These interfaces allow users to visually map out and modify data flows, _**making the system’s operations transparent and comprehensible even to those without deep technical expertise**_. This visual aspect not only simplifies the monitoring and debugging processes but also helps maintain organizational governance.

By implementing data pipelines, organizations can build MAGS that are not only more efficient and adaptive _**but also easier to manage and scale**_. The visual building tools and _**modular, composable design of data pipelines reduce development time and increase consistency across different applications. The ability to visually represent and explain the decision-making process further enhances the value of MAGS, providing clarity and insight into how decisions are derived, which is invaluable for continuous improvement and alignment with business objectives.**_

While traditional GenAI agents are constrained by the limitations of procedural coding, data pipelines provide a robust framework for developing advanced MAGS. This framework _supports dynamic data integration, sophisticated reasoning capabilities, and a visual, modular approach to system design, making it ideally suited to the complexities and demands of industrial applications._

In part 4, “[**Pioneering Progress: Real-World Applications of Multi-Agent Generative Systems**](https://xmpro.com/part-4-pioneering-progress-real-world-applications-of-multi-agent-generative-systems/),”  I continue and show the anatomy of an XMPro MAGS agent team that is built and deployed on this data pipeline and use two examples to demonstrate the capabilities of these agent applications.

![](https://xmpro.com/wp-content/uploads/2024/07/1721196628356-1536x802.jpeg)

**If this excites you and you want to be part of the next evolution in industrial applications, please reach out to me or** [Gavin Green](https://www.linkedin.com/in/greengavin/) **, VP Strategic Solutions.**

**We are opening limited pilot opportunities for innovative, agile leaders in the industry.**

