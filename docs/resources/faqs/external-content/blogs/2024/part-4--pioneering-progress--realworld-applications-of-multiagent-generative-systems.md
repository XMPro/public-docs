# Part 4 – Pioneering Progress | Real-World Applications of Multi-Agent Generative Systems

[**Articles**](https://xmpro.com/category/blog/articles-blog/)**,** [**Blog**](https://xmpro.com/category/blog/)**,** [**CEO'S Blog**](https://xmpro.com/category/blog/pieter-blog/)

## Part 4 – Pioneering Progress | Real-World Applications of Multi-Agent Generative Systems

Posted on [July 24, 2024](https://xmpro.com/part-4-pioneering-progress-real-world-applications-of-multi-agent-generative-systems/) by [Pieter van Schalkwyk](https://xmpro.com/author/pietervs/)![](https://xmpro.com/wp-content/uploads/2024/07/1721194626724-1024x585.png)

## **Part 4 – Pioneering Progress | Real-World Applications of Multi-Agent Generative Systems**

## **Part 4 – Pioneering Progress | Real-World Applications of Multi-Agent Generative Systems**

![](https://xmpro.com/wp-content/uploads/2022/03/Pieter-2019-Square-Web-150x150.jpeg)

#### **Pieter Van Schalkwyk**

**CEO at XMPRO**, Author – Building Industrial Digital Twins, DTC Ambassador, Co-chair for AI Joint Work Group at Digital Twin Consortium

July 18, 2024 – Originallly posted on [Linkedin](https://www.linkedin.com/pulse/part-4-pioneering-progress-real-world-applications-van-schalkwyk-hgtvc/)

Welcome to Part 4 of our series, where we explore the real-world applications of Multi-Agent Generative Systems (MAGS) in industrial settings. This installment, “_**Pioneering Progress | Real-World Applications of Multi-Agent Generative Systems**,_” shifts our focus from theory to the tangible implementation of these advanced systems. Before we dive deeper, let’s briefly revisit where we’ve been

* In **Part 1**, “_**From Railroads to AI The Evolution of Game-Changing Utilities**_,” I discussed how Generative AI (GenAI) is becoming as fundamental as electricity in our lives, creating opportunities for innovative applications across various sectors. [Read Part 1 Here](https://xmpro.com/part-1-from-railroads-to-ai-the-evolution-of-game-changing-utilities/)
* **Part 2**, “_**The Future of Work Harnessing Generative Agents in Manufacturing**_,” addressed the critical skills shortages and productivity challenges that are reshaping how work is conducted in manufacturing environments. [Read Part 2 Here](https://xmpro.com/part2-the-future-of-work-harnessing-generative-agents-in-manufacturing/)
* In **Part 3**, “_**AI at the Core LLMs and Data Pipelines for Industrial Multi-Agent Generative Systems,**_” I covered the architecture of MAGS, focusing on why and how these systems use agents to enhance industrial processes. [Read Part 3 Here](https://xmpro.com/part-3-ai-at-the-core-llms-and-data-pipelines-for-industrial-multi-agent-generative-systems/)

Now, let’s delve into how XMPro leverages its established infrastructure to deploy MAGS effectively, enhancing operational efficiency and adaptability in complex industrial environments.

### The Anatomy of an XMPro MAGS Agent <a href="#ember1693" id="ember1693"></a>

XMPro stands at the forefront of industrial MAGS development, leveraging our _**existing, robust data pipeline**_ infrastructure. This same foundation, which powers our _cutting-edge condition monitoring, predictive operations, and event intelligence solutions_, now serves as the bedrock for our MAGS implementation.

![](https://xmpro.com/wp-content/uploads/2024/07/1721197984701.png)

Figure 1 shows an Industrial Predictive Maintenance team structured around XMPro DataStreams. This setup features four distinct agents, each with specific roles and functions, which will be detailed in the subsequent sections of this article. This configuration operates without a central “supervising” agent, highlighting our system’s flexibility. Instead, each agent continuously shares and receives updates—observations, reflections, plans, and actions—enhancing collaborative decision-making.

The agents in this example work together to optimize the output of a windfarm while reducing costs and working within resources, time, and budget constraints. This single team can monitor hundreds of wind turbines on the wind farm simultaneously and optimize the overall performance of the system in real-time.

![](https://xmpro.com/wp-content/uploads/2024/07/1721208408157.png)

Figure 3 shows the “_**Anatomy**_” of the Reliability Agent in the wind farm, which is used in the two examples later in this article. It demonstrates the power and flexibility of XMPro’s DataStreams to compose these agents.

These agents not only communicate with each other but also actively engage with real-time data streams, integrating these inputs into their ongoing processes as per the standard data pipeline architecture discussed in Part 3.

![](https://xmpro.com/wp-content/uploads/2024/07/1721196628356-1536x802.jpeg)

The XMPro DataStream connector framework’s extensibility enables seamless, drag-and-drop integrations across IT, OT, and Engineering systems, providing unparalleled flexibility. Building on this proven architecture, we’ve developed innovative “Agent Brain” components that can be strategically placed within data streams, resulting in fully-featured MAGS agents.

Block 1 represents a standard pattern where industrial data is continually ingested from SCADA, IoT, historians, and other engineering sources. The data is contextualized from business systems, such as a Digital Twin in this example. The XMPro Data Stream can combine, wrangle, and transform this data to ensure the data quality with capabilities such as continuously tracking error rates, completeness ratios, and validity scores.

![](https://xmpro.com/wp-content/uploads/2024/07/1721197984562.png)

In this part of the Agent Data Stream, we can pass all this information to an analytical, statistical, or machine-learning model to provide further insights. In this example, the Reliability Agent runs the information from the DataStream through the [Reliability Python library](https://reliability.readthedocs.io/en/latest/index.html) for expert analysis of the data. This is “kinda like” giving it a PhD in Reliability Engineering. This step “grounds” the agent in physics and reality. The output of this step is what XMPro typically sends to a real-time dashboard with a recommendation for a human subject matter expert to decide on the next step.

We do this in Block 2 to enable “human on the loop” oversight and guidance, in case we want to monitor how the agent responds to the information from the analysis in Block 1.

![](https://xmpro.com/wp-content/uploads/2024/07/1721199421371-1.jpeg)

Blocks 1 and 2 represent a typical Predictive Maintenance data stream that monitors specific equipment, runs a predictive model over it, and present prescriptive recommendations to SMEs and other business users.

XMPro has customers that routinely process more than _**50 million**_ of these monitoring events **per day** across a range of _complex industrial assets_. It is a robust and proven part of the XMPro MAGS agent framework.

Block 3 is the XMPro MAGS extension of the data pipeline and represents the _**“Agent Brain”**_ that takes the output from the operational data and analytics _“function block”_ and adds to it input from other agents in the team, recent memory on the equipment, and the user or task prompt that is configured for this agent when it is set up. All of this is merged and passed to the XMPro MAGS agent that uses this as an _**observation, combines it with memories, and reflects on it before planning and coming up with a plan of action**_.

![](https://xmpro.com/wp-content/uploads/2024/07/1721197985305.png)

In this example, the XMPro MAGS agent runs on a local deployment of a Llama model to ensure privacy and security. _**XMPro is agnostic to the LLM service and can run both cloud and local models, as well as a hybrid of both.**_ Different agents can run on different models that best suit their objectives.

![](https://xmpro.com/wp-content/uploads/2024/07/1721199541763.jpeg)

The output of Block 3 determines the actions that the agent can take in Block 4. It could be a recommendation to a human user, but in this example, it updates the preventative maintenance schedules in the Maintenance Management Systems, and it creates a work ticket for a technician to inspect or repair the equipment based on the root causes of failures.

_**This visual, explainable approach makes it easier to understand the agent’s process and logic. It also makes troubleshooting and fine-tuning much easier, as the output from every step in the data stream can be monitored and evaluated.**_

#### Scalability and Governance <a href="#ember1722" id="ember1722"></a>

The use of a _data stream approach_ further enables scalability and governance that are required for industrial-grade MAGS solutions.

The _**“stream host”**_ architecture of XMPro DataStreams makes it possible to _**“instantiate”**_ an infinite number of agents based on an _**“Agent Profile.”**_ This profile is maintained separately and contains the _**“Rules of Engagement”**_ that include a _system prompt with skills, policies, and deontic rules such as obligations, permissions, authorizations, and delegation of authority._ These _**system prompts always override any user or task prompts**_ to ensure the responsible use of XMPro MAGS.

![](https://xmpro.com/wp-content/uploads/2024/07/1721197985025.png)

This _**“Separation of Concerns”**_ is designed to ensure that the XMPro MAGS agents are fit for the tasks assigned to them but behave according to company policies, rules, and regulatory requirements. This is a key area that I will address with [Zoran Milosevic](https://www.linkedin.com/in/zorandmilosevic/)‘s help in part 5.

Figure 9 shows how the XMPro MAGS Predictive Maintenance Team instantiates a team of four agent-based Agent Profiles and then starts observing, reflecting, planning actions, and recoding all this in an XMPro _**“BrainGraph”**_ memory.

The Reliability Engineering and Root Cause Analysis Agent’s _**planning and task output are used to create actions based on the plans using the XMPro DataStream Action connectors**_. Each action and result are further added to the memory to enable learning and continuous self-improvement.

![](https://xmpro.com/wp-content/uploads/2024/07/1721197986888.png)

The XMPro MAGS ‘BrainGraph” is an example of a Predictive Maintenance team collaboratively optimizing asset performance through planning and executing corrective and preventative maintenance tasks.

### XMPro MAGS Examples <a href="#ember1733" id="ember1733"></a>

I mentioned the Predictive Maintenance and OEE Expert Optimizer examples earlier, and here is a short summary of these solutions.

#### Industrial Predictive Maintenance MAGS Team <a href="#ember1735" id="ember1735"></a>

The Industrial Predictive Maintenance MAGS solution shown in Figure 10 utilizes a _**team of specialized AI agents**_ working collaboratively to enhance industrial maintenance operations. _**Each agent plays a pivotal role**_, ensuring that maintenance is not only reactive but also predictive and strategic, thus minimizing downtime and extending equipment lifespan.

![](https://xmpro.com/wp-content/uploads/2024/07/1721197984755.png)

Key agents and their roles within this system include

1. **Reliability Engineering and Root Cause Analysis Agent** This agent analyzes equipment performance and failures to improve reliability and conduct thorough root cause analyses. It monitors equipment data to detect patterns that may indicate potential failures, provides detailed root cause analysis reports, and recommends preventive measures to avoid future breakdowns. _This agent is based on the same “Agent Profile” as the “Predictive Maintenance Agent” in the OEE Expert Optimizer team._
2. **Maintenance Planning and Scheduling Agent** This agent is responsible for efficiently planning and scheduling maintenance activities. It creates predictive maintenance schedules using equipment performance data and historical maintenance records. It aims to optimize these schedules to reduce downtime and improve resource utilization, producing optimized maintenance plans and schedules.
3. **Maintenance Management Oversight Agent** This agent ensures that maintenance tasks are executed effectively and in compliance with established standards. It oversees maintenance activities, validates their completion and effectiveness, and enforces maintenance protocols, ultimately ensuring all maintenance activities meet required standards. It doesn’t act as a supervisor that delegate tasks but rather as the process quality assurance.
4. **Reporting and Feedback Agent** Focused on transparency and continuous improvement, this agent collects and analyzes data from maintenance activities and equipment performance. It generates real-time Key Performance Indicator (KPI) reports and provides feedback mechanisms to foster ongoing improvements in maintenance operations.

The MAGS workflow of these agents is highly integrated and systematic

* **Data Collection** Continuous gathering of equipment performance data, historical maintenance records, and operator input.
* **Reliability Analysis** The Reliability Engineering Agent continuously monitors and analyzes equipment to identify and address potential failures.
* **Maintenance Planning** The Maintenance Planning Agent develops and refines maintenance schedules based on the analysis.
* **Maintenance Execution** Maintenance tasks are carried out as scheduled, and records are duly updated.
* **Management Oversight** The Maintenance Management Oversight Agent reviews and validates the maintenance tasks for compliance and efficacy.
* **Reporting and Feedback** The Reporting and Feedback Agent provides essential KPIs and actionable insights to ensure continuous optimization of maintenance processes.

By employing this structured approach, the Industrial Predictive Maintenance MAGS solution ensures that maintenance operations are proactive, efficient, and aligned with the organization’s strategic goals, significantly enhancing operational reliability and cost efficiency.

#### XMPro OEE Optimization Expert team <a href="#ember1744" id="ember1744"></a>

The Expert OEE Optimizer Multi-Agent Generative System uses an array of specialized AI agents, each tasked with optimizing different facets of manufacturing operations to enhance Overall Equipment Effectiveness (OEE). These agents collaborate in real time, ensuring a highly responsive and adaptive manufacturing environment.

![](https://xmpro.com/wp-content/uploads/2024/07/1721208780086.png)

**Key Agents and Their Roles**

1. **Availability Monitoring Agent** This agent manages equipment uptime and downtime data along with maintenance schedules to maximize machine availability. It provides real-time alerts and actionable recommendations to mitigate downtime risks effectively.
2. **Performance Monitoring Agent** Responsible for analyzing production speed, cycle times, and operational data, this agent identifies bottlenecks that reduce performance. It offers real-time solutions to enhance production speed and efficiency, thereby optimizing throughput.
3. **Quality Monitoring Agent** By assessing quality inspection data, defect rates, and rework records, this agent ensures products meet quality standards. It proactively identifies quality issues, offering solutions to improve product quality and reduce defect rates.
4. **Predictive Maintenance Agent** Utilizing equipment sensor data and maintenance logs, this agent predicts potential equipment failures and schedules preventive maintenance. Its goal is to minimize unplanned downtime and optimize ongoing maintenance efforts. _This agent is based on the same “Agent Profile” as the “Reliability and Root Cause Analysis Agent” in the Industrial Predictive Maintenance team._
5. **Anomaly Detection and Root Cause Analysis Agent** This agent processes historical and real-time operational data to detect anomalies and perform root cause analysis, ensuring swift resolution of performance issues.
6. **Simulation and Scenario Analysis Agent** Using synthetic data to represent various operating conditions, this agent simulates potential scenarios to forecast their impact on OEE. The insights generated aid in proactive decision-making and operational optimization.

![](https://xmpro.com/wp-content/uploads/2024/07/1721197986940.png)

The MAGS workflow of these agents is highly integrated and systematic

1. **Data Ingestion** The system continuously collects data from sensors, maintenance logs, production records, and quality inspections, ensuring a comprehensive data pool for analysis.
2. **Agent Processing** Each agent processes the ingested data independently, generating specific outputs such as maintenance alerts, quality reports, and performance metrics.
3. **Collaboration** Agents share their outputs to collaboratively refine and enhance operational strategies, leveraging combined insights for a holistic improvement approach.
4. **Solution Presentation** The integrated outputs are synthesized into optimized solutions that are presented to human operators and decision-makers, ensuring the implementation of the most effective strategies.
5. **Feedback Loop** The implemented solutions are monitored, and the feedback obtained is used to continuously train and improve the agents, enhancing their accuracy and effectiveness over time.

It is still early days in the development of these collaborative, automated MAGS solutions, but for the OEE Expert Optimizer team, Table 1 shows the types of objectives we are setting and measuring. While the objectives differ from factory to factory, they illustrate the potential benefits of a team that observes, plans, acts, learns, and continuously improves with scarce human resources “on” the loop rather than “in” the loop.

![](https://xmpro.com/wp-content/uploads/2024/07/1721215933601-1536x674.png)

By integrating these agents into a cohesive system, the Expert OEE Optimizer not only improves current manufacturing operations but also adapts dynamically to meet future challenges, ensuring sustainable operational excellence and resilience.

### Join us on the Journey <a href="#ember1757" id="ember1757"></a>

We at XMPro are excited about the opportunity that this capability brings. It enables you to augment current skills and address shortages with a framework that mimics the work of your best SMEs. It is not replacing jobs; it is automating suitable tasks so that you can free up scarce SMEs to focus on value-adding work and enable you to do more with less. In the process, you address the productivity challenge mentioned in Part 2.

As systems become more complex, you can use GenAI for what it is good at, processing large volumes of data consistently and helping you to make sense of it, deciding on what action to take next.

Fortunately, the journey doesn’t have to start with full multi-agent MAGS. Maybe you want to start with the Reliability Agent and grow into more functionality and capabilities as your confidence grows with the MAGS approach. XMPro MAGS is a flexible approach that allows you to start small and scale fast.

![](https://xmpro.com/wp-content/uploads/2024/07/1721198126467.jpeg)

**If this excites you and you want to be part of the next evolution in industrial applications, please reach out to me or** [Gavin Green](https://www.linkedin.com/in/greengavin/) **, VP Strategic Solutions.**

**We are opening limited pilot opportunities for innovative, agile leaders in the industry.**

_**Continue to**_ [_**Part 5 – Rules of Engagement: Establishing Governance for Multi-Agent Generative Systems**_](https://xmpro.com/part-5-rules-of-engagement-establishing-governance-for-multi-agent-generative-systems/)

