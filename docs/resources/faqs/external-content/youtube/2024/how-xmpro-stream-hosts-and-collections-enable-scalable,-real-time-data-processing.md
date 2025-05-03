# How XMPro Stream Hosts and Collections Enable Scalable, Real-Time Data Processing

{% embed url="https://www.youtube.com/watch?v=cIEN6vtFcoI" %}

Welcome to our latest technical deep dive on XMPro stream hosts and collections! 🎥

In this video, we'll explore how these powerful tools enable scalable, real-time data processing, crucial for managing complex data orchestration tasks. Whether you're overseeing a few assets or thousands, stream hosts and collections provide the flexibility, efficiency, and scalability needed to transform your data operations.

🔍 What's Covered:

Introduction to Stream Hosts and Collections:

Overview of their role in enabling scalable real-time data processing. Importance of these components in intelligent business operations solutions. Data Stream Designer:

Mapping out real-time data flows. Integration, transformation, orchestration, and sanitation of data. Over 100 integrations, 75+ analytics agents, and 60+ action agents. Role of Stream Hosts:

Executing data stream logic. Deployment options for centralized and localized operations. Communication with various entities including assets and applications. Scalability with Collections:

Grouping of stream hosts for running the same use cases. Deployment of a single data stream to multiple stream hosts. Use of collection variables for specific configuration settings. Practical Examples:

Centralized and decentralized data management topologies. Various deployment setups for optimized data processing. Considerations for distributed streams and latency management. Conclusion and FAQs:

Summarizing the capabilities and deployment options. Addressing frequently asked questions. Why It Matters:

XMPro stream hosts and collections are the hidden yet essential elements ensuring robust and scalable intelligent operation solutions. By understanding how to leverage these tools, you can significantly enhance your data processing capabilities, driving efficiency and productivity in your operations.

📞 Contact Us: If you have any questions or need further assistance, please reach out to the XMPro team. Our solution engineers are here to help you maximize the potential of XMPro in your operations.

Don't forget to like, share, and subscribe for more insightful content on intelligent business operations and data solutions! 👍🔔

\#XMPro #DataProcessing #RealTimeData #Scalability #StreamHosts #Collections #DataStreamDesigner #IntelligentOperations #TechDeepDive #digitaltransformation #DigitalTwins #generativeai #genai #artificialintelligence #IntelligentOperations #assetmanagement #AssetPerformanceManagement #conditionmonitoring #processoptimization #predictivemaintenance

<details>

<summary>Transcript</summary>

hi and Welcome to our technical deep

dive on XM Pro stream hosts and

collections in this video we'll explore

how these powerful tools enable scalable

real-time data processing whether you're

managing a few assets or thousands

stream hosts and collections provide the

flexibility efficiency and scalability

needed to handle complex data

orchestration tasks let's get started

and see how XM Pro can transform your

DOA

operations when building intelligent

business operations Solutions it's easy

to focus solely on the user interface

however this overlooks The crucial

components that power and drive the

solution behind the scenes data streams

stream hosts and collections are the

hidden yet essential elements of XM Pro

ensuring your intelligent operation

Solutions are robust and

scalable the data stream designer is a

canvas where we map out real-time data

flows for specific use cases it allows

users to integrate transform orchestrate

and sanitize data within a single

cohesive data workflow with over 100

Integrations 75 plus analytics agents

and 60 plus action agents it empowers

you to derive meaningful insights

predict future Trends and automate

responses

seamlessly underpinning our data streams

are stream hosts which are responsible

for executing the logic of the data

streams configured in the data stream

designer when you configure a data

stream and hit publish a stream host

takes over to run it the number and

location of stream host depend on your

us case for centralized operations you

might use a single stream host for

localized operations stream hosts can be

deploy as close to assets as required

ensuring real-time data processing right

where it's needed stream hosts run the

data streams designed in the data string

designer executing the logic and

processes you have configured they

enable the agent library to communicate

with various entities including assets

line of business applications and other

systems let's jump into an example to

consider this scalability of string

hosts imagine you're monitoring the

temperature of an asset the data stream

collects temperature data filters for

values above a certain threshold and

then creates a work order in for example

sap at the bottom we have one asset with

compute capability next to it and we

have a Stream post deployed on it this

Computing capability could be a Windows

server or a Linux based system there are

multiple options available to us here

currently this stream host is running

for only one asset but what happens when

we have multiple

assets this is where collections come in

a collection is a container that enables

a grouping of stream posts running the

same use cases a collection allows us to

deploy one data stream to multiple

stream posts running the same use case

automatically by doing this a single

data stream can be published to one

collection and the stream posts by self

subscribing to the collection download

and then run the data stream logic

next let's touch on collection variables

collection variables are common to all

stream hosts that subscribe to a

collection each stream host defines a

value for these variables

locally this setup enables the same data

stream to be deployed to different

stream posts but the connection details

it requires can be unique per Stream

post for example if you have a data

stream that requires specific

configuration settings such as IP

addresses port numbers or authentication

credentials collection variables allow

each Stream post to use its own local

values for these

settings this means that while the logic

of the data stream remains consistent

across all stream posts the specific

interactions and connections can be

tailored to the unique requirements of

each Stream

post now that we have discussed the

various aspects of stream hosts and

collections let's conclude with a few

examples of how this is deployed in

practice in this example you have

multiple assets communicating with a

single stream host which then drives the

actions various assets can send data to

a central OBC server which can be

intercepted and managed by a single

Stream post this setup works well for

centralized data management and action

execution alternatively you can create a

different topology where each plant has

its own stream host these individual

stream hosts can send data to a central

cloud-based stream host which further

processes and integrates the

information this decentralized approach

allows for low localized data processing

and better management of specific plant

operations you can also have a

configuration where each stream host

runs different data streams such as LPC

mqt or others and sends the processed

data to a Central

Area this setup ensures that each data

stream is managed efficiently according

to its specific protocol and

requirements finally there's an option

to run one Stream post per asset

assuming you have sufficient compute

capability next to each asset asset when

it comes to scalability these different

topologies whether running stream posts

next to assets using a historian or

leveraging cloud-based servers allow you

to optimize data processing according to

your operational needs you can even have

distributed streams or parts of a data

Stream Run on different stream hosts

though this requires careful

consideration of latency and other

factors now let's conclude by addressing

some frequently asked questions if you

have any more questions please reach out

to the accent pro team

and one of our solution Engineers would

be happy to assist you

</details>
