# Webinar - XMPro 4.3 Release Showcase
{% embed url="https://www.youtube.com/watch?v=02YTYa0ZerA" %}




<details>
<summary>Transcript</summary>
hello everyone and welcome to the XM Pro

4.3 release showcase

my name is Kim Marie Davenport product

manager here at XM Pro and I'm excited

to share with you the highlights of this

release in terms of what the features

are

they do and why you would benefit from

applying them in your ex in Pro

environment

if you have any questions please send

them through and we'll cover them at the

end

before we begin I'd like to point out

that today's content Builds on a couple

of prior webinars

haven't already watched them I'd highly

recommend that you do so

you can find them on our XM Pro channel

in YouTube

XM Pro CEO Peter Van scope explains the

concept of the intelligent digital twins

as well as going into detail on our

product strategy the intelligent digital

twins framework

also known as XM Pro i3c which stands

for integrated intelligent interactive

and composable

while that i3c framework is a longer

term view of where we're heading Daniel

King's product roadmap webinar describes

the items we're working on now and next

to get us there

every initiative that we work on falls

under one of the four pillars of the XM

Pro product

namely accelerate transformation Ai and

engineering

zero trust architecture and the cloud to

Edge continuum

together they support each of our three

themes

faster time to Value distributed

intelligence and security across

deployments

triangle layout illustrates how each of

these pillars support one another as

well as their varying impact on people

process and Technology

the 4.3 release contains new features

for both the cloud to Edge Continuum and

Ai and Engineering excellence

kicking off with the cloud to Edge

Continuum there are three features

included in

distributed casing through redis allows

us to run the distributed infrastructure

needed in Cloud to Edge computing

the other two features are complementary

health check endpoints is about

detecting an issue and roughly where

that issue lies and logging enables the

going in and doing analysis around

finding that problem

they are important groundwork on our

journey to be more agnostic more

performant and more scalable

allowing data to be accessed along that

continuum

now a health check endpoint is precisely

as it sounds a product service has a

health check API endpoint such as HTTP

forward slash help that Returns the help

of the service

when it is called the API endpoint

Handler performs various checks and

responds with the simple status of the

API and its dependencies

or unhealthy

when it is troubleshooting health checks

are the industry standard for the first

diagnostic step

they quickly indicate connectivity

health

either highlighting an issue such as

access to a database or allowing the

troubleshooter to rule out connectivity

and move on to their next check

we've implemented standard best practice

health check endpoints with two

different ways to consume this

information

in person or utilizing a diagnostic tool

as a baseline a person can monitor the

help UI which sits outside of our

product

it has to or you wouldn't be able to

access it if our products were not

healthy

however there is more to be gained by

configuring the raw Json API response to

be read by diagnostic tools such as

Azure with app insights

so that the endpoints are constantly

monitored on the infrastructure itself

you can build rules triggered if it goes

from healthy to unhealthy and when

triggered you can build actions such as

an email or a team's message or maybe

even to Auto scale

Health endpoints are crucial for

enabling self-healing functionalities in

your infrastructure

being able to automatically restart

unhealthy services on the edge

is extremely powerful in increasing

product uptime and performance

imagine if your application is running

on kubernetes and you can automatically

restart the service

or the Pod that it's running on and

hopefully get it back to a healthy state

the health checks are particularly

useful for customer installations on

their own infrastructure

there's always a risk that connectivity

might not have been opened on a service

that XM Pro needs and it's not

transparent that this is the case

time has been lost in previous

installations going through that

diagnosis process it requires certain

skill sets so it becomes time consuming

and costly to troubleshoot what may end

up being a trivial issue

with health checks now when you do the

initial installation you could for

example confirm application designer has

connectivity to subscription manager and

to its database

if it doesn't then we can tell straight

away that it can't connect and see the

relevant error message

the problem is narrowed down to

connectivity between two systems and

it's simple to proceed to The Next Step

which could be something like opening an

exception on the firewall

[Music]

there are also day-to-day operations

where the environment in which XM Pro is

installed unexpectedly changes

whether it's the Cloud Server provide

running updates

sorry whether it's the cloud provider

running updates or deprecating

underlying functionality

or the customer themselves making

changes

these endpoints are available so that XM

Pro connectivity can be actively

monitored

connectivity is inadvertently broken

someone can be proactively notified of

an issue and investigate further

the loss of connectivity assists in

knowing which area is working as

expected and which area to troubleshoot

berder

let me take you to our product

documentation for a quick look

this is the

sorry this is the health path of an

application designer Services URL and

the raw API response

note the overall status is healthy and

that there is an entry for each of the

related product Service apis as well as

the database

observe the duration for each individual

check their healthy status as well as

the optional descriptive tags

next we'll look at the same information

using the Baseline help UI

here we can see in the top part

the same information for application

designer but it is a lot easier on the

human eye

the overall status is healthy

and again there are entries for each

related product service API as well as

the database

observe again the duration for each

check their healthy status as well as

the optional descriptive tags

our documentation includes an example of

how to configure the Xin pro products as

well as how to add third-party systems

that have health endpoints

a reminder that how you choose to use

these in health checks is up to you

our product is decoupled from any

specific cloud provider so that XM Pro

remains platform independent

so now that you know roughly where the

problem is how do you solve it

previously we had log files being

written to the web server

you had to be an administrator log into

that service download the log files and

then view a large text file full of logs

this has issues of accessibility and

security

you can't open access to many people

because of the security constraint

and it's time consuming to get access to

those logs

then once you get them you just see a

wall of text

you don't get any of the benefits of AI

insights anomalies or trending Analytics

you can't see there's been a spike in

latency to a certain endpoint request

or multiple 500 error codes coming back

from another endpoint

your native service provider can't

consume the logs and pair them with

telemetry

information about the infrastructure

service that's running your application

like CPU and RAM

[Music]

so we've done three things in 4.3 we've

added more logging added more context to

that logging and then made those logs

available to services that are optimized

for monitoring and analyzing the data in

those logs

when we say we've added more product

application logging

what this means is that we've increased

the number of messages that are logged

to expose how the product is working

internally

this gives more insight for

troubleshooting Diagnostics and Optima

optimization purposes

where previously an endpoint may have

been receiving a lot of requests

hypothetically recommendations and

taking a long time to process them

this was not visible if the request was

not logged

now that the endpoints are locked it is

visible and allows designers to optimize

how applications and streams are

implemented to improve overall

performance

we've added more context where possible

to each log

so if there's a user ID Associated we

always put the user ID on it

if there's a company ID we always put

the company on it

when you look at the log you have more

context as to which area it relates to

this gives users finer grained

information when named

you can stay with the logs being written

to file on the service

or take advantage of the new feature

logging provider support

to send the output to third-party login

providers like Azure application

insights or datadog or centralized

monitoring analysis

they are specialists in this area and

provide fantastic features for searching

monitoring dashboarding and alerting

for example you could search the logs

for a specific user or recommendation

and we're doing this in an industry

standard way using best practices of a

standard platform independent login

provider logging Library

the benefit is that we can quickly and

easily add support for more providers if

you request one that we don't have

in summary application logging is

essential for troubleshooting and

debugging as it helps identify and

analyze issues that may arise during the

application's execution

it also provides valuable insights into

the application's performance usage

patterns and security

near the end of 2022 we heard feedback

from a customer that the distributed

casing was not working as expected on

AWS

despite scaling up and after resources

some f Pages were slow and some were

timing out

these performance issues were due to the

large volume of data in memory

with the 4.3 release the timeouts have

been fixed across all platforms by

refactoring our implementation of

distributed

we're still using redis or remote

dictionary server a popular open source

data structure store

but we're using it more effectively by

breaking the memory used into smaller

pieces

these are more easily managed by Raiders

to handle larger volumes of memory and

cash faster which is passed on to the

users who experience those faster

response times

data catering is a technique to improve

the performance and responsiveness of

applications

we're frequently accessed data stored in

memory

a fast and easily accessible location

rather than a time-consuming operation

like accessing a data

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

in year real time too

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

this is when you would scale out to get

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

[Music]

the third benefit is costs

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

once more

we have two complementary features from

a pillar included in 4.3 this time for

AI and Engineering intelligence

neither a data scientist nor a designer

wants to create a model in one

environment and manually load them into

Data stream designer each time they

change

it's in Pro notebook provides data

scientists with the ability to work

within the XM pro products Suite to

create models using scientific computing

and our mlflow agent enables effective

model governance to run the production

model version against live event data in

a data stream

we'll end off with the significant

performance improvements to the time

series chart block

enabling quicker data retrieval for

longer periods

exim Pro notebook is a new product

released for freemium in 4.3

existing customers and premium users can

contact us for access

and Licensing options

this is an embedded Jupiter notebook

providing a familiar interface for data

science scientific Computing and machine

learning

data scientists analysts and Engineers

will be able to access data to innovate

within the XM Pro Suite

we've added built-in chat GPT

functionality to help you in the process

for example you can ask it to create

code to represent data in a certain

visualization

[Music]

when you're done you can save the file

and execute it using our python agent as

embedded AI

or you can apply governance

leverage the mlflow library to commit

the model to your repository right from

within X in Pro notebook

for use in a data stream

this was just a small test of XM Pro

notebook

in last month's webinar Gavin Green

presented a Hands-On demonstration of AI

in intelligent digital twins which is a

fully extended version that explains

these features and more in detail it is

well worth watching

moving on to ml flow

as AI scales within the organization

corporate guard rails require AI to be

modeled within an ml Ops framework

you don't want to end up with models

stored in a variety of places and lose

track of which is the latest version or

where it is located

ml flow agent is the first in a series

that enables effective model governance

using a popular ml Ops toolset

let us know if you are using a different

Repository

[Music]

this empowers data scientists to promote

new model versions within mlflow without

going back to edit the data stream

let's see this in action

my thanks to Chris for recording this

demo

as soon as I find my mouse

in it we have an mlflow agent configured

to use version one of a model called

wine quality

once the data stream is published

observe that the first event confirms

model version 1 was used to make a

prediction

now we'll change over to ml flow

and promote version 2 to production

going back to the data stream without

reconfiguring or republishing observe

that model version 2 is seamlessly used

to make the next prediction

application designers time series chart

or TSC is one of our most popular data

visualizations

however we found that performance is not

satisfactory with large volumes of data

and as you know this is usually the case

with time series data

all relevant data is returned to the

client for processing so that it doesn't

need to be refreshed

unless certain parameters are changed

but large volumes of data are slow to

return and slow to process on the client

[Music]

we've made changes to the block itself

and released a specialized TSC connector

that only Returns the data points

displayed on that chart the block sends

the requested parameters to the

connector which retrieves the data from

the data source punches the numbers and

sends back only the data actually

displayed

for example rather than sending 60 000

records for 180 buckets we're only

returning 180 records

this results in a fast and scalable user

experience

the disadvantage of this approach is

that it is repeated every time the chart

is Interactive such as zooming or

changing the asset selection

a TSC SQL connector is available now

and the functionality will be rolled out

for Azure data Explorer and historian

next

you will need the 4.3 release for The

Block enhancement and thereafter simply

load the new connectors as they are made

available

alternatively you can continue using the

original connectors for smaller data

volumes to avoid the load between

interactions

[Music]

have a demo by Dragon another one of our

talented developers of the new connector

in action

we discovered during a trial run through

that my audio is not going to play or

the audio of the video is not going to

play through from you so

this is my first run through with the

script so let's just see how that goes

when we play the video

this is the new TSC SQL connector

which pulling the selected fields that

we have for this time range

and this interval size

we can see that the request was

returning in less than 400 milliseconds

and the size is 44 45 kilobytes

if I open the request now we can see

that we have 179 records or buckets and

for each packet we have the selected

field with their corresponding Min and

Max values that are actually showing on

this one

now what we've said is if we move the

range it's going to send a new request

the same size in the same time

if we move the range

sorry if we increase or decrease the

interval size we should have double the

buckets

Sarah do we have any questions

thanks very much Kim and thank you

everyone for joining us uh yes we've got

one question here about uh where can we

find some more information on 4.3 or any

other release

I would encourage you to go to our

product documentation and look at both

the what's new article as well as the

release notes for further details on the

features presented to you today

as well as the smaller enhancements and

fixes that were released

excellent okay um well thanks thanks

again Kim thank you so much for taking

us through all that thank you everyone

for joining us today

if you're looking for more information

you can contact Kim or our team directly

we are running these webinars monthly

and our next session will be an extended

session on XM Pro AI end-to-end use

cases covering intelligence through

proactive recommendations and

implementing machine learning through X

and pro AI you can register using this

QR code that Kim sharing on a screen or

we'll send you the link when we send out

the recording of this session shortly

um we look forward to seeing you all

next month thank you very much

thank you

foreign
</details>