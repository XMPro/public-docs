# XMPro Auto Scale - Understanding Distributed Caching for Cloud-Native Applications

{% embed url="https://www.youtube.com/watch?v=hpusWm3GEko" %}

In today's video, we delve into the mechanics and advantages of Distributed Caching in cloud-native applications, specifically focusing on its crucial role when scaling out server instances. This discussion is designed for engineers, architects, and experts who require in-depth understanding rather than surface-level insights.

Key Takeaways: Fundamentals of Data Caching: A brief overview of how data caching improves application performance by storing data in quick-access memory rather than relying on time-consuming database queries.

Architecture: We explore how the typical architecture for AWS mirrors that of other cloud platforms like Azure, particularly in the role of load balancers such as AWS Elastic Beanstalk and Azure App Service.

Cache Consistency: Understand why maintaining cache data consistency across various server instances is vital, especially in a scaled-out architecture.

Practical Use Cases: We discuss real-world scenarios like streaming data from multiple hosts and the influence of caching on application designers.

Scaling: Learn about two primary dimensions—vertical scaling (scale up) for performance improvement and horizontal scaling (scale out) for added resiliency and meeting high-demand situations.

Resiliency and Redundancy: We illustrate how having multiple server instances can protect against performance degradation, thus ensuring a more robust application environment.

Cost-Effectiveness: Discover how to use auto-scaling strategies to optimize infrastructure costs without sacrificing performance.

Early benchmarking data indicates noticeable performance improvements when using Distributed Caching, even on a single-instance setup. This video aims to provide you with the comprehensive knowledge needed to make informed decisions on implementing Distributed Caching in your cloud-native applications.

Whether you're looking to improve performance, add resiliency, or manage costs, understanding the nuances of Distributed Caching can provide the edge your applications need.

Please subscribe for more in-depth technical content tailored to professionals. Feel free to ask questions in the comments section; we're here to facilitate a dialogue among experts.

Tags: #DistributedCaching #CloudNative #AWS #Azure #PerformanceOptimization #Resiliency #CostManagement #Engineering #Scalability

<details>

<summary>Transcript</summary>

data catering is a technique to improve

the performance and responsiveness of

applications where frequently Access

Data stored in memory

a fast and easily accessible location

rather than a time-consuming operation

like accessing a database

distributed casing is when it is stored

in an external service accessible by one

or more servers

it is mandatory when you scale out and

run more than one instance of our

product

I'm showing the typical architecture for

AWS but it is the same concept on other

platforms and you can view their typical

architecture on our product

your Cloud native implementation handles

adding Resources by basically cloning

the web service

they're out of the box load balancer

such as AWS elastic Beanstalk or Azure

app service determines which web service

the user's browser connects to as soon

as you scale out

between different browsers and stream

hosts talk to any of the web server

instances the cache data must give the

same result

in the example of an app page that is

initially loaded

everyone will see the same published app

page because it's saved in the database

when someone edits that app page in

order for every other user to see those

changes near real time

those changes must be stored somewhere

in memory that all the servers server

instances access

with distributed caching we move that

in-memory data out of the individual web

servers and into readers

the end result is that the web server

instances all access the same memory

allowing the clients connected to the

different servers to see those changes

in near real time too

there's a lot of functionality in our

product that uses cache data

for example streaming data from a stream

host or multiple stream hosts connecting

to application designer where the stream

hosts our clients as well

the main reason for scaling is

performance

for example if the CPU was high for data

streams and you had many streams running

you could scale up by increasing the app

service plan in Azure but there is a

limit to how high you can go

this is when you would scale up to get

more CPU

so one reason is for performance to

scale up and out

the second reason is resiliency

for example if you had data stream

designer on Azure app service plan 2 and

it had an issue with a performance was

deprecated for some reason users would

be locked out

however if you had two instances at a

lower service plan and one of those had

an issue that caused performance to be

degraded the users would be able to

continue to use the product on the

second instance

so resiliency is another Factor

\[Music]

the third benefit is cost

technically you can Auto scale out an

inner gain automatically or on a

schedule to better manage your

infrastructure costs in Peak periods

early benchmarking results indicate that

using distributed caching has

performance improvements even when you

are running only one instance of the

product and so is something you may want

to consider switching to for larger

production ready implementations

such as those with a large number of

data streams

</details>
