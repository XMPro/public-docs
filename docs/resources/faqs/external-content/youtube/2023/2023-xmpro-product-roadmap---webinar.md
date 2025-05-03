# 2023 XMPro Product Roadmap - Webinar
{% embed url="https://www.youtube.com/watch?v=XeEpso-ykMI" %}

Join XMPro Development Manager, Daniel King as he takes you through our highly anticipated product roadmap covering the Now, Next, and Later product releases.
<details>
<summary>Transcript</summary>welcome to the XM Pro product roadmap

webinar for 2023 I'm Daniel King

development manager at XM Pro I'm based

in Sunshine Coast Queensland Australia

and I'd like to thank you all for taking

the time to attend today

I have a lot to cover off today so if

you have any questions please send them

through and I'll try to answer them at

the end

2023 has been an amazing year so far and

I can't believe it's halfway already

I won't be recapping recently delivered

items in this session but I'd like to

encourage you to go to our website and

check out our latest release notes

there are three key achievements I would

like to call out though 83 of our agency

connectors have been contributed to so

far this year which is massive I'll be

partnered with Dell Technologies to

create a validated design for the

manufacturing Edge and work with Nvidia

to validate XM Pro as GPU enabled or

accelerated and Enterprise ready

I'd like to take a second here to thank

the XM pro team for their contributions

and making all this happen I know a few

of them are watching today so thank you

the intelligent digital twins framework

is a strategy for our product

Peter Van scope fake is CEO of XM Pro

and co-chair for the natural resources

of working group at the digital twin

Consortium

here goes into much more detail on our

strategy and if you haven't already

watched this previous webinar I'd highly

recommend you do so you can find it on

our XM Pro channel in YouTube

the i3c framework is a longer term view

of where we're heading

and the product roadmap represents the

items we're working on now and next to

get us there I won't be able to cover

everything on a roadmap in 30 minutes

but I'll try my best to cover as much as

I can today

four pillars of the XM Pro product are

how we execute on the i3c framework

together they support each of our three

themes faster time to Value distributed

intelligence and secure cost deployments

the triangle layout demonstrates how

each of these Builders support each

other

and the pillars have varying impact on

people processing Technology based on

their proximity to these little labels

here

the robot items will be grouped by

pillar and I'll be talking through each

roadmap item for each of these pillars

distributed intelligence is achieved

through Ai and Engineering where people

and Technology meet to innovate execute

and augment with AI

I think that's pretty cool

we're going to start today with AI and

Engineering pillar

47 of all iot applications will be AI

infused in 2027. that's a 30 increase in

under four years that's that's that's

amazing we want to enable our customers

to be part of that 47 percent

and we're doing this with a number of AI

roadmap items

so we're going to focus on Innovation

with AI first

AI is fast growing and disrupting

markets around us and it offers new

tools to do things differently but these

tools are rapidly changing this is why

we think Innovation with AI is critical

X and pro notebooks is a new product

we'll be releasing as part of our AI

offering it supports Jupiter notebooks

allowing you to use a well-established

product without having to retrain people

or refactor existing notebooks XM Pro

notebooks can be used in data science

scientific Computing and machine

learning and data scientists analysts

and Engineers will be able to access

data to innovate within the XM Pro Suite

each user will have their own dedicated

notebook actively using the product this

makes it very scalable and cost

effective as you experiment

one of the biggest challenges for data

scientists is the access to good data to

innovate with

we're adding integration to our data

stream data so excellent Pro notebooks

can access the rich and near real-time

data in transit

this scenario isn't just limited

real-time data though in data streams

you can also run simulations on your

data streams and access that same data

from Maximum code notebooks the same way

this approach also allows users to focus

on innovation without first having to

develop software and Integrations up

front

it also allows for continuous innovation

and experimentation over time

we currently support the ability to run

simulations on streams visualize the

results in apps

front running simulations is the ability

to run a simulated event just before the

real event to predict what that result

would be

and this example we're simulating an

event right before the real event to see

what the outcome would be and in this

case it would have been a bad outcome

this allows you to build functionality

into a stream to modify the path

an event takes ultimately ensuring that

you get a good outcome

so let's talk about when these things

are coming so the now Title Here

represents an item that's actively in

development or scheduled for release

soon and the next title represents work

with developers not yet commenced or is

blocked by another item

we practice hypothesis driven

development at xmpros this means that

items can shift or change the scope

based on what we learned

development for the X and pro notebooks

has completed and the team are working

on productizing it for our supported

platforms and

Cloud providers

it will be the first available on our

free trial offering which is probably

only days away at this stage or really

close and it'll become available

incrementally on our installers for

different clouds and platforms

next we'll be releasing support to

consume stream data in those notebooks

and we're in the early stages of

planning for this

front running simulations is also in the

early stages of planning

once you've innovated and produced new

AI Solutions you need a way to execute

them

running AI in our streams is one way to

do this and up until recently you'll be

limited running these on the CPU

the GPU is well suited for running

certain workloads and involve a lot of

concurrent processing

moving processing to the GPU can vastly

improve how much processing you can do

in the same time frame compared to the

CPU mathematical algorithms Machine

Vision neural networks and deep learning

are examples of workloads that involve a

lot of concurrent processing

in this example we're using a Machine

Vision to process apples and oranges

differently in our data stream

images of our fruit are ingested by a

data stream as an agent compares the

images pixel by pixel to determine if

the if it's an apple or an orange

by using the GPU to run pixel comparison

algorithms we can process a lot more

images

this stream can still be run on the edge

Fogle cloud

and it can also dynamically detect if

there's a compatible Nvidia GPU and use

it falling back to the CPU when the GPU

isn't available

there are a handful of scripting

languages that are fast becoming

standard for executing AO workloads by

supporting these scripting languages we

support customers in running their

existing Solutions in our streams this

reduces the need to refactor or retrain

staff and you can adopt new

functionality faster as is the large

open source Community currently

innovating using these scripting

languages

we're extending our current agents to

support more of these scripting

languages

we're also adding support for more

governments around these scripts in this

example you can see we can run a script

directly in an agent or reference the

latest published version of a script

from the common storage layer

for now I think of the common storage

layers kind of like GitHub and I'll talk

about this later

these scripts can be edited from the X

and pro notebooks allowing users to

operate completely in our suite of

products

data streams are executed for us to buy

our stream hosts and these stream hosts

can be run on the edge of fog and Cloud

allowing you to distribute your

processing fully strict scripts uh

providing like a very flexible and

composable architecture

thank you now we've recognize you may

have your own machine learning

operations or mlops

they're focused on streamlining the

process of taking machine learning

models to product and then maintaining

and monitoring them

mlop space it's it's growing very

quickly and there's a vast variety of

different third-party Solutions our

approach here is to create agents to

integrate these third-party Solutions

mlflow is our open source platform for

managing the end-to-end machine learning

life cycle

and is fast becoming the the most

popular in the space

we have created an ml flow agent that

can get the latest published version of

a model

and invoke it with data from the our

data stream and then return those

results back this prevents the the need

for a data science to actually go into a

data stream and update that stream each

time a new version of the model is

created

it also allows heavy processing of ml

models to be run on the customer systems

optimize already for these workloads

it also allows access to be restricted

to the data stream supporting the

principle of least privilege

mlops can be orchestrated from XM Pro

notebooks allowing you to run

experiments create models publish those

models and then invoke them directly

from The Notebook then using the results

foreign

GPU acceleration support is currently

available you can design Aid install

leverage Nvidia gpus using agent

documentation and we'll be extending

this documentation to provide more

examples and support

we're also working on adding GPU

acceleration support to some of our

existing agents

we currently have a python script and

we're close to releasing an R script

agent we'll be adding more governance

controls and integration to these to

these scripts using the common storage

layer after it's released and I'll talk

about talk more about that common source

layer layer later

we've recently developed the ml for

agent for integrating to customer lmops

and we're updating our public docs right

now before we actually release it

now the innovating and executing with AI

there's a great opportunity to augment

what we have now with these results

we currently have recommendations

capability and for those that aren't

familiar at a very high level you can

create recommendations with rules that

when are met generate alerts

we found that existing recommendations

can be augmented with AI anomalies can

be dynamically detected and visualized

with inside the recommendations

new recommendations can be automatically

generated or discovered

and rules within those recommendations

can be created or augmented

and alerts themselves can be augmented

with copilot like functionality and

assisting assisting engineers in in

resolving these alerts

chat GTP and open API services are

continuing to provide new and easier

innovative ways of doing things

accent Pro notebooks will be released

with a sample notebook demonstrating

integration to chat GTP in this sample

notebook it includes an end-to-end beer

quality example which incorporates chat

GTP and who doesn't like quality beer

data stream designer Integrations will

allow you to augment your event data

with chat GTP and app designer

Integrations will allow you to make

custom calls

from your apps enabling co-pilot like

functionality

the security of our data we will we uh

security fuel data and and how we

implement this is really important to us

we use the third-party services like GTP

takes a lot of our consideration and

we'll be factoring this into you know

how we solve these problems and deliver

these new product roadmap items

visualization of AI outputs is a really

powerful and effective way of

communicating the insights you're making

excellent Pro notebooks will allow you

to generate visualizations that you can

share in apps in this example we'll be

using chuckttp to generate a linear

regression visualization for us

it's using the data for my data streams

and it's checking to be savings a lot of

time because we're not having to find

the suitable libraries and write the

code to do this ourselves

Excel Pro notebooks will be released

with chat GTB integration support and

samples on how to get going quickly you

can currently integrate you integrate to

check GTP via our Python scripts and run

these in agents right now

and these Python scripts can be designed

and managed in X and pro notebooks

we will have importable end-to-end

Solutions as our starting point to get

you going faster for our common use

cases and additionally planning for app

designer and data stream designer

integration

as this is currently underway and it

will provide more additional no code

approaches

AI generated or discovered

recommendations is in the early stages

of planning there are some core

technical pieces that are needed before

we can start this work and the

development team are busy work on these

right now

generating analytics and visualizations

is currently available through a mix of

approaches we're currently planning on

how to extend these approaches to closer

integrate x and pro notebooks allowing

from a more seamless experiment

experience from right through from

Innovation through to augmentation and

the visualization

all these new AI roadmap items need

distributed computing and network

infrastructure management to support an

edge ecosystem

this is the cloud to Edge continuum

we currently support deployments to a

wide variety of cloud providers and

on-prem platforms using cloud and

platform native services

this creates additional overhead for us

and our customers as we add more

features demanding more capabilities in

this area

these environments can be configured in

many different ways and also change and

sometimes without our control and this

makes it difficult for us to deploy and

support our products simply as

seamlessly

there are new more modern approaches

that are quickly become industry

standard for the type of architecture

that underpins our suite of products

these more modern approaches require us

to change our deployments to embrace

them

we'll be creating a cloud agnostic

deployment for our suite of products

that will become the default deployment

method

the aim is to provide a product that is

more portable allowing for business

better business continuity planning more

reliable with self-healing properties

and more performant allowing for better

performance for Less cost

now we currently support distributed

deployment and in this example we have

products used most by our users in the

cloud in regions closest to those users

making the products feel fast and snappy

in the fog we have our AI capabilities

closest to where most of our data is

reducing the time to transmit large

volumes of data over the wire and on the

edge we have our stream hosts these are

our engines that run our data streams by

putting them on the edge we put them

closest with the devices and Edge

systems are

the challenge with this approach is

managing all these Edge deployments

without some form of centralized

monitoring alerting and management it

can become difficult and time consuming

for iot to manage these systems

this is why we're building support for

third-party systems that provides

centralized monitoring alerting and

management capabilities

we're adopting industry standards and

best practices to allow us to easily add

additional providers over time and this

also provides customers with the

flexibility to use their existing

providers if they have them

the solution would be composable with

the ability to select different

providers from different functions

instead of having to commit to one

system to do it all

we're bringing devsecops capabilities to

our sweeter products

we're not building these capabilities

into our products but again leveraging

existing industry standards and best

practices to allow you to use your own

providers

in this example we have a pre-pro

environment that we want to design our

streams and apps before we publish them

to production

these new versions of apps and streams

are automatically exported to the common

storage layer and from there UI test

automation can be run leveraging our XM

Pro test automation Library

secure testing can be performed on any

changes to say Integrations to mitigate

any potential vulnerabilities and when

all these pre-checks pass the change is

then approved and these versions can be

published to our products or your

product environment or the customer

support environment

we can take a similar approach to

upgrades to X and pro new versions can

be automatically and programmatically

installed in pre-prod manual regression

or just automated UI testing performed

and then deployed to production

we've just released automated database

installs and upgrades

which allows for a fully automated

deployment our current deployment

options required a customer though to

set up Automation in their third-party

systems

best practices have evolved since some

parts of the process were first

developed and we need to redesign these

and we'll provide be providing improved

deployment automation incrementally

product by product

we've completed several proof of

Concepts around Cloud agnostic

deployment

with commence development and are taking

our product by product approach and

we'll continue to support cloud data for

some time shifting to Cloud agnostic

deployments as default and they're done

we're looking to cater for customers who

want an out-of-the-box experiments where

they can use all the default deployment

configuration that we provide right

through to those that want to consume

the individual product artifacts and

build them into their own custom

deployment

we've completed a proof of concept I

distributed deployment management based

on our Cloud agnostic approach and we're

in the planning state of considering a

mix of internal and external third-party

tooling to be rolled out incrementally

faster time to value is achieved through

roadmap items that combine people

and process to accelerate transformation

we're providing more support for what

you have when it comes to visualizations

we use blocks to compose apps and

already have a large library of blocks

to do this however some scenarios it's

quite difficult to create a block for

example

if a customer system uses an

incompatible technology or uses an old

technology that performs slowly or is

just custom or an in-house system

meta blocks will allow us or you to

create custom blocks to overcome these

challenges

it'll allow you to run visualizations

side by side that traditionally just

wouldn't be possible

with this capability you will be able to

create an industrial metaverse that runs

on the same backbone of event data

without first needing to re-platform

your existing exist existing systems to

like a common technology

this gives you the flexibility to delay

deciding when that common technology

needs to be and what it needs to be

until that Industrial metaverse

Technologies and processes stabilize and

you can make a better decision about

that

I've mentioned the common storage layer

a number of times already in this

presentation

and that's because it will unite

artifacts across XM Pro think of it as

kind of like GitHub

except we'll be implementing it in a way

that allow you to choose the provider so

it doesn't have to be GitHub it'll also

be comprised of several different

Technologies allowing for the best

technology for the job and using best

practices to do it

the common storage layout will allow you

to collaborate faster and safer

providing well-known interfaces and

governance controls to do this

anything you can currently export or

import can be managed here and all the

new artifacts discussed today will be

stored here

the provider you choose for the common

storage layer will also support

integration most likely and allowing you

to automate and tie in artifacts from

Max and pro into your current existing

systems

we're introducing some new artifacts the

common series later get you started

quicker and keep you innovating

blueprints are pre-built Solutions

providing end-to-end working samples

accelerators can be imported into your

environment as a starting point

from which you then can extend from

and patents are pre-configured data

streams at servers building blocks that

you can compose and extend out

you'll also be able to create your own

versions and collaborate internally and

externally

so we currently have a library

predefined Solutions in our XM Pro

GitHub project which you can now check

out

we'll also continue to add to these over

time and next we're looking at adding a

library UI into our accent pro products

to access and integrate them a little

bit more easier

we've completed a perfect concept of

meta blocks and are planning on studying

development soon and we've selected

several new and existing blocks to be

candidates for that first release

we're currently using several providers

for my common storage layer internally

for collaboration and we'll be exposing

these publicly

we're beginning planning We Begin

planning on how we'll integrate these

products in the UI shortly

where process and Technology meet we

need strong governance to be secure

across deployments and we do this with

zero trust architecture

zero trust architecture is not new for

us at X and pro and something we take

really seriously

we aim to give you more control over

what users can access with finer grained

Access Control

the product rights will align closer to

API endpoint functionality and not UI

components we'll still have product

roles to manage any additional

complexity this might introduce and in

this diagram you can see a user

accessing data via connector or

recommendations functionality previously

these would have been these five rights

here would have been three different

rights this change allows for greater

control over what users can access

and by aligning these rights to API

endpoints it makes it simpler to apply

the principle of least privilege at

scale

we currently run several security scans

every three months months and uh and

publish these results to our website

in addition to this we'll be running

incremental scans on every code change

for each product to pick up potential

vulnerabilities earlier this change will

ensure that any new vulnerabilities are

identified and addressed as soon as

possible

so XM Pro currently supports integration

to Azure ad ID provider providing an

easy way to leverage existing user

logins and security policies and

features like SSO and MFA

we're extending this functionality to

include support for more scenarios like

a Federated tenancy model

this integration has been done using

industry standards making it easier for

us to add new providers when it's

necessary

as we implement the edge to Cloud

Continuum and monitoring and managing

product performance is critical

we need it we're implementing support

for application Performance Management

tooling and we're doing this using

industry standards so adding new

providers will be easier using this

integration you'll be able to monitor

performance of our products

be alerted when there's issues and if

needed do basic troubleshooting yourself

so we're applying finer grade access

controls incrementally to each of our

products with the first product in

development now

we have continuous security scanning set

up on most of our products are in the

process of updating the remaining right

now

and we currently have support for Azure

ID and like I mentioned before we're

just extending this to support more

scenarios like a Federated tenancy model

and we're currently adding support for

Azure app insights as a APN provider

so

we'll be running webinars on the items

shown today as they become available and

diving into a lot more deeper detail

if you have any questions please send

them through and I'll try to answer them

now thanks

thanks Dan um so we've got two questions

here already

um the first one is where can we find

more information on XM Pro AI

okay great question ah thanks Sarah

so that segues really nicely uh next

month Gavin Green will be doing a

webinar on AI and he'll go into a lot

more detail

um I'd encourage you to sign up for that

and attend

um we're very close to releasing X and

pro notebooks in our free trial soon

um I think it's a couple of days away at

the stage just keep an eye out for that

uh sign up have a play around with our

free trial and the different AR

capabilities that are in there and I

also believe we're publishing a web page

specifically around Ai and our website

and the features that you can leverage

there so keep an eye out for that as

well

awesome there's another question here um

it says with Edge to Cloud continuum

providing any

s around containerized architecture

good question uh yes really really

excited about this one

um so actually we currently have Docker

images for our stream hosts these are

the engines that run our data streams

we're adding Docker images for other

products and we'll be creating a

container registry that will be

publishing these two

um we will likely do webinars on this as

this becomes available

um

so yes

awesome and then one very important

question asking will we receive a copy

of the webinar from today

yes yeah this is probably where I do the

uh like And subscribe Us on YouTube

um yes we'll be putting this on YouTube

on our XM Pro Channel all of our

webinars are on there including uh Peter

Scott fakes previous one I mentioned

please jump on there and look at it look

at it um Sarah do you know how long

it'll take for it to get up there

um hopefully we'll get it up today

sometime later on today okay

thanks

that's it for the questions

oh I head over to you oh thanks

okay

um so if you just want to change science

then

cool

thanks everyone um so thanks very much

Dan for taking us through and thanks

everyone for joining us if you're

looking for more information uh you can

contact Dan directly or the team via

these email addresses as Dan mentions

we're running these webinars monthly and

our next session will be on XM Pro AI

presented by Gavin Green so you can

register by scanning the QR code there's

a link in the chat box and I'll also be

sending the link

um shortly when we send the recording

out sometime later on today and we look

forward to seeing you all next month

thank you very much for joining

thank you
</details>