# XMPro Overview & Fin Fan Failure Demo
{% embed url="https://www.youtube.com/watch?v=CKunaPTI0Io" %}



In this video, you'll learn what a Rapid Application Builder for Industrial IoT is and why it matters to companies in industries like manufacturing, mining, oil and gas and utilities. You'll...
<details>
<summary>Transcript</summary>In this video, you'll learn what a Rapid Application Builder for Industrial IoT is and why it matters to companies in industries like manufacturing, mining, oil and gas and utilities. You'll...
in this presentation I'll quickly run

you through what a rapid industrial I at

the application Boulder is an approach

around this is how can you very quickly

build out in a lean way a Minimum Viable

Product where you can test hypotheses

because quite often we find this IOT

things is quite new for a lot of

organizations they don't really know how

to start that I know where the ROI is

going to be and really it's a discovery

kind of process so using a lean approach

where you start off with a Minimum

Viable Product and what do we need to

build out what hypothesis do we need to

test how do we check that the data comes

through this can be done in X and

probably a very very quick and easy

visual way and once you've found those

use cases where there is ROI and there's

a meaningful business case you can then

look at how do i scale this out to the

enterprise and all of this is just so

that we can realize quick time to value

and then spend time and resources and

money on on things that don't work well

so when you look at X and prototypical

we call the mega use cases or big

buckets of problems that we solve what a

lot of organizations are currently

looking at how can we become smart at

our operations and things like

maintenance it's quite at the forefront

but it's just one typical use case that

sits inside this predictive operations

operational intelligence how do I make

sure I'm not blindsided I know I have

this real-time situational awareness in

terms of operational excellence again

safety quality asset integrity key big

buckets of problems that many of the

customers are looking to address

likewise with operational risk how can

we look at it from a loss prevention and

tracking how do we make sure that we

know where risk events are and how we

can potentially mitigate them how can we

run a digital business where we do

digital transformation how can we

integrate different operations and have

that visibility across them

and one of the one of the key things

that we got out quite often find us how

can we respond to events quickly how can

we reduce the latency between when

events happen and when we take action

and quite often that relates back to

things like process health where what is

the overall status of the different

areas of my business process and so that

I have that awareness so that I can

respond quickly to two things that might

impact my business and lastly one of the

key things around running businesses

these days is making sure that you have

customers that you have a good custom

and employee experience and again

real-time responsiveness is becoming

more and more a key part of that

and so looking at Exim Pro what is it

well it's essentially a model driven

application builder by model driven we

mean we can drag and drop blocks on you

and in a visual way we can construct

what the problem is

what it does it's essentially the

software glue that connects real-time

data sources to analytics whether it's

simple analytics or complex analytics

and then what we really want these

actions that come out of the business so

how do we connect this to actions like

work orders or any other business

processes or even workflows that might

be customized and what it means for

organizations that that that leverage

this capability is that their subject

matter experts like the engineers

technicians and architects can create

and deploy in a very agile a way as I

mentioned earlier from a lean approach

perspective in an agile way and in an

iterative way real-time IOT applications

that can serve a range of different use

cases so it's not just a single problem

that you can solve but you can use this

approach and reuse the blocks on here to

address multiple challenges inside them

inside the business and the whole

objective is to do this with as little

coding as possible and most of it in the

usual in the visual user interface that

you see

so what does ex-emperor consist of there

are two main components we talk about

the agile design studio and this is

typically where we design applications

and components for that and I'll take

you show you an example of that and then

how do we plot deploy this in the action

console where we take action the best

way to show you what that is and how it

works is actually to do a quick

demonstration in the demonstration are

we talking about fan fans and a fan fan

you can see the flatbed truck this is

typically the units that fit on top of a

cooling tower in an industrial plant

typically typically used in mining oil

and gas and energy and utilities and

broad range of those industries and

again if you look at the impact of this

if one of those fan fans file you have

to shut down the whole cooling tower

operation which in in in again quite

often impacts the operations and

sometimes you have to even shut down

your whole operations plant some

customers run hundreds some literally

run thousands of these inside the

organization and if if the bearings wear

out and we have misalignment on any of

these shafts here the vibration on these

fans will shake the whole building

depart so let me quickly show you how we

address this kind of problem inside

ex-emperor so this is a typical user

interface for an engineer this is called

the ex-emperor use case manager and inia

I can see multiple different use cases

or problems that I'm trying to solve

inside the business so it might be

anything from monitoring power and

variable speed motors it could be the

fan fans which we will discuss in this

example it could be vibration analysis

logistics deviation failure of

deliveries but access monitoring and up

and but mining bearing failure so as you

can see as an engineer I can address

multiple different

business problems in the in the use case

manager so with the fan fans those

massive big fan fans on the top of the

cooling tower we will start off with a

very basic model and quite often we find

this is our customers go through the

process as they as they get more

sophisticated as they get more data and

as they understand the problem that

they're trying to solve them much better

that will go through a more going from a

basic model like we have here to more

advanced which I will also show in this

example so before I go into the backend

and how a lot of this constructed let me

quickly run you through the logic of

what we seen here so we're going to get

a vibration and temperature which is

currently stored in our in a historian

system in this instance always icesoft

so the vibration and the temperature on

the on the shaft and bearing that all

that fan fan in place and from the ERM

system in the process it management or

the as an intelligence network or

depending on on which system you use to

store the mic and model for example

we'll get some information some

contextual information around the fan

fan in this instance we want to know

which make and model it is so we can

pass that together by combining it with

to a machine learning model that will

give us a prediction whether this

machine this fan fan is likely to fail

if it is likely to fail we will just

very simply create a work order so a

very simple model again we take

vibration and temperature data we

combine that with model and make and

model information run a machine learning

model get a prediction if this is going

to fail and if it's going to fail

creative work order inside the eim

system now the way that we bring

information in or we have a concept of

extensible library so this this means we

can extend the library

you can extend the library or your

systems integrator for example could

extend the library of what we call

listeners or data sources where we can

bring data from this is a small subset

of available listeners transformations

how can we change the information like

you can see we can combine the

information contextualized those are

typically transformations and that we

can do it can even run scripts there to

do very specific data cleanup if the

missing value substituted for example

doesn't address your specific

requirement bringing in context as I

mentioned previously we wanted to bring

in the Mikan model from a certain for

certain piece of equipment again

extensible library concept so very easy

for us to add additional library

components and we can add it you can add

it and your systems integrator can also

add it action agents this is what at the

india what do we want it to do so action

agents again broad range of action

agents built on the exact same

extensible library construct so that you

can add new specific applications that

you may have in your business where you

want to send the data to and then lastly

statistical and other mathematical

functions for example doing forcefully

transformations running or scripts from

an analytics perspective if you have

your own algorithms all of these are

available as drag and drop items once

I've dragged the item on I can configure

the properties so what you'll see in

this instance with this RSI example this

is the RSI server setup so and this

looks actually looks at the asset

framework structure that is inside I was

also so it will expose all the

properties and values of the underlying

services that have connect what we're

doing here is we we because it's not a

real-time streaming data source which we

will California by having a channel to

push it to well you have to pull the

date that we did every 10 seconds

and we do it based on the specific asset

framework we'll be looking for the

information so very easy for an engineer

or a subject matter expert to construct

these once the the blocks are deployed

and this is typically done within the IT

organization to ensure governance access

controls and security everything that we

need around IT governance and once it is

available and published it then becomes

object that the engineer someone like

that can drag on let's step onto a

little bit more of a sophisticated

example of this our fan fans are very

very basic very simple but you can see

how we can monitor real-time for certain

conditions I'm going to jump right to

the extended model I'm skipping the one

in the middle and in this extended model

it is essentially exactly the same

process we are reading data evaporation

and temperature from here we're bringing

an information make and model from the

manufacturer here we run that exact same

predictive model to see if it's likely

to fail if it is likely to fail we want

to take certain actions so I want to

publish to a dashboard

I want to send out a SMS and we want to

in the XM Pro action management side of

things want to create failure mode

analysis root cause analysis push it

with visualization dashboards what we

also do with the same data so by

broadcasting the data over here and

broadcasting it over here we can now

call a second predictive model now that

we know it is likely to file we can call

a second predictive model which will

dictate will will give us a remaining

useful life so say for example in this

instance we get a remaining useful life

of a hundred hours it means we have a

window of opportunity to maintain that

piece of equipment within a hundred

hours the challenge with that is way in

the hundred hours is the best time to do

that

and with XM Pro as you can see you can

join multiple algorithms and logical

components

and analytics together so by joining is

a first predictive model a second

predictive model and a third

optimization model with this one we'll

look at production schedules customer

orders at maintenance work orders and

find the best slot to do the maintenance

so for example if this was a hundred

hours we have a window of remaining

useful life we may find the most optimum

slot to do any maintenance is 62 hours

and we would then also go and look

inside the EAM system against that

specific equipment identifying critical

space and see if that if those spares

are available if it is we will then go

and check if there is a work order if

there is currently a work order we'll

check whether it's at the 62 hour point

if not we can create the work order

there or we can put it in the task list

of the work of the maintenance planner

to create the work order inside the 62

hour time frame if there's no work order

then we create it so as you can see the

same approach but in this instance a

little bit more expansive in terms of

being able to create work orders based

on three predictive models one is it

going to file yes what's remaining is

4life hundred hours what's the best

maintenance lot 62 hours do we have

space and through this whole process

we've collected all the data that we

need to create a really smart and

intelligent work orders again the same

logic applies for creating actions so if

I create a work order for example in

here this is the the back end to do that

and if I want to map the data by

clicking on the on the arrow I can now

map as you can see I can map my my data

fields coming in to what the integration

component expects on the other side the

last thing that I want to do and show

you in years now that we have this

running so now that we've set this up

can run this model and this is a key

element of XM products not just to have

a visual model but how do you execute

the model how do you now run it and push

the data through and in this example

what you'll see is it starts the

different services and if the service

starts successfully it will turn green

if there's a challenge or a problem with

any of the services don't start up or

doesn't function properly and the blocks

will turn red instead of the instead of

the green that you see here and that'll

give you what the current health the

status is what you see now is a system

where it actually pumps the data through

so it reads the information from all of

this combines the information and run

the predictive models and create the

work orders on the on the back inside so

let me stop this and again it's now

stops all the underlying services this

could be deployed in a hybrid

environment so this could be run on

premise this core part could be run on

the cloud and this part could be run

back on premise it's a key deployment

benefit of using X and Pro is that not

all your data needs to reside on premise

not all your data needs to reside in a

cloud you can construct these so that

the pubsub model the publication of this

one we are publishing with in the end

where this one subscribe is dictated by

the ex-emperor orchestration engine very

powerful approach and feature so with

that it concludes the the overview of

how X and Pro you can set up real-time

data listening capability and how it can

create actions based on the analytics

that you apply to it
</details>