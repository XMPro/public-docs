# Predictive Maintenance with XMPro iDTS

{% embed url="https://www.youtube.com/watch?v=5vzqp90uVQY" %}

Predictive Maintenance with XMPro iDTS

Dive into an in-depth exploration of Predictive Maintenance powered by XMPro iDTS. This video aims to provide engineers, subject matter experts, CTOs, plant managers, and executives with a comprehensive understanding of how XMPro iDTS is shaping the future of asset maintenance.

🔍 Video Highlights:

Examine the extensible framework of XMPro iDTS, which includes diverse connectors from fast Fourier transforms to Ethereum smart contract creations. Understand the capabilities of statistical mathematical functions, geofencing, and goal-seeking functionalities. Discover the role of Action Agents in enabling real-time actions, ranging from email notifications to database updates. Observe XMPro's live data flow process, emphasizing data wrangling, context addition, and data conversions. Analyze the predictive capabilities integrated with data historians like OSIsoft, Azure IoT hubs, and context tools such as SAP. Explore the built-in Jupyter Notebook of XMPro that facilitates model creation and deployment. Grasp the nuances of the Recommendation Engine, focusing on error handling flows, triage instructions, and rule construction. Review the web page builder's functionalities, which support advanced 2D and 3D data visualization. For those committed to advancing the field of predictive maintenance and keen on understanding XMPro iDTS's full potential, this video serves as a technical guide. Share your insights, questions, or experiences in the comments below for a collaborative discussion.

\#PredictiveMaintenance #XMProiDTS #DigitalTwin #AssetManagement

<details>

<summary>Transcript</summary>

in our overview of a video we describe

the process that we followed to get from

our assets and real-time data from the

assets through to some actions and

recommendations that we want to drive

and the outcomes that we're looking for

now the typical process is that we bring

in data through our data stream designer

you could then run some analytics

through AI or do some of it inside the

data stream designer see the front end

in the app designer and then lastly have

recommendations and manage

recommendations inside the

recommendation manager from a

demonstration point of view I'm going to

start at the app designer and then we'll

go into that also includes

recommendations we'll go into the data

stream designer and show you how we do

it in the uh behind the scenes how do we

get the data in and also touch on how we

apply AI to this so let's jump in and

get started

this is the app designer the green icons

at the top

this is the data stream designer and

this is AI so we'll go through all three

of those but I'm going to start kind of

at the end I'm going to show you the

result of what what you see when you use

XM Pro and I'll start with uh just a a

simple example around multiple

facilities or assets that we have in

this instance I'm just I've set the

filter just to show me

um

some of my

Wind forms and I can the colors and

things will change based on the severity

the health of the overall Farm not

necessarily the individual ones I can

set that up to so that I can actually

drill down and get into the actual form

itself and drill down right down you'll

see this is a viewport that is using

esri I'll touch a little bit later on

how we can edit this and what all the

different types of viewports that we

support but this is an example of

something like that here I can see some

of the assets that need maintenance

there's also some recommendations on

some of this so at a holistic view as a

maintenance manager facility manager I

can very quickly see the health and

status of my different facilities and

where I need to go now this again is a

specific type you can have a much more

sophisticated example of this as well

I'll um I'll go into and just show you

again as a maintenance manager

maintenance planner looking at all the

facilities that we have

um I can see kind of the alerts to work

requests work requests to work orders

work orders to open work orders to to

closed and how long it takes to actually

resolve it and

um how what is the efficiency how many

open work orders do I have and what are

the recommendations around all the

different machines again this is

everyone's you'll see there's a whole

bunch

listed through here so and they range in

severity in this instance they rank by

severity

I can look at

the different installations or

facilities that I have and in this

facility this is a wind turbine facility

this is a solar array so

I'll go into the wind turbine one so

I'll have a quick look at what's

happening at the wind turbine and this

gives you an idea and I'll share a more

advanced example of this but I can see

some safety and health information I can

see the overall time usage profile

current metrics that it's running some

of the and again

maintenance records maintenance

information some of the corrosion damage

tables and depending on the type of

modeling that you use I can get into it

you can see this updates in real time if

it's a Unity or Omniverse or a a more

interactive model or a card based model

I can actually get into it and I'll show

you an example of one of those but this

is

with this I can now actually get to a

recommendation so I can see there's low

gearbox oil on this reported and there's

the instance of that that triggered that

so there's a rule that runs and when it

goes below a certain threshold this is

very simple rule around a certain

threshold on the on the on the gearbox

oil low warning and there's potentially

some triage instructions this one

doesn't have too much I can also see how

many times this has occurred and if I

look at kind of a longer duration what

are all the other things that are

happening to this specific asset that

has happened over time I could create a

form or I can fill in a form right here

and this could be a work order request

this could be a root cause analysis a

failure mode analysis

um

you can associate

a large number of different act action

forms do this in terms of the kind of

action that you want to take I can also

Mark this as a false positive so that

later on we can start analyzing how many

times are we getting this kind of false

positives out of this so this is one

example of a

facility predictive maintenance I'll

show you a slightly more advanced

example in in this example this is a

processing plant in this instance plant

but it could be a Water Filtration plant

it could be

any processed plant and in that

again analyzing the data looking at

real-time anomalies and looking at

defects where certain type of defects

that are that are happening so this is

on the quality side so I could bring in

some of the process information

there's fill rates efficiency on on the

energy consumption but likewise with

that esri map where I had a

um uh Green Dot or radar or whatever

represent that there's an issue you can

actually see on this one that

there's a there's an issue here so these

will appear or disappear depending on

the recommendations and the current

state so it's very quick to see as a

planner

or maintenance supervisor maintenance

manager plant manager you know what is

happening and I can have a very simple

2D model of a pump with some real-time

data coming through for the pump from

sensors that we have I can see the

nameplate data for the pump

what is writing at or what it's writed

at so just very quickly I can see how

far is it off in terms of its actual

performance I might be running a

predictive model which again will touch

on a little bit later a predictive model

that's pretty predicting the the

remaining is for life

so that I can determine how much time I

have before there I may have an issue

again I can get into the recommendation

in a minute but here's a bunch of

real-time data and around temperatures

vibrations

and all the maintenance records so I can

see maintenance schedules maintenance

history

and I can see what is currently planned

I can also see what has been what has

been recently completed in terms of work

order history really just helps with

um and again I could drill down on this

next level before we do that what I'd

like to do though is actually get a

better view of this type of pump and

if you if if for certain type of

equipment you may want to

expand the capabilities and being able

to see you know what is really happening

so if I look at the discharge exception

or the remaining useful life on the

bearings

I can move this around and actually have

a view on that now

if I click on this view more you'll see

I get to that same recommendation that I

complete but before I go there this was

a discharge exception and I may want to

go to something like cha GPT or

or

generative AI large language models and

actually ask it and I've typed this in

before so that's why it comes up but I

can actually ask it top five root causes

for centrifugal pump where there's a

loss in discharge pressure

and what it does it gives me just some

direction and what I could potentially

do with this

is just copy that

so that when I do go to the the the

recommendation itself

I can kind of create a bit of a starting

point in terms of you know where we

should potentially be looking for

um

for certain issues or and again it's the

same and this again this is a work order

request but it could be root cause

analysis could be different types of

forms that you want to associate with

associate with it this could be have

more advanced triage instructions so you

know these are the typical things that

you could look for Block suction by

blocked impellers

um

it's not necessarily the information

that you send right through to the work

order level it might just be something

for you to help triage what is the

potential issue based on the combination

of this as well as the drills

instructions that we have here and again

the analytics across this to say well

you know I want to know what are all the

issues that we've seen on this pump

lately is it a kind of recurring pattern

or what is happening so that's a key

application for us around

predictive maintenance in facilities

to be able to and condition monitoring

is to be able to get a view of the

um the overall acid and then being able

to get down right into a recommendation

I'll show you how we set up the

recommendation data in a minute but

before we do that I would like to show

you how we do the back end data that

goes into this

now

for that pump we'll just go to the smart

asset that bump that I just showed you

there are two different data streams

here we refer to these as data streams

so they're streaming real-time data this

is a very simple condition monitoring

and then I will also show you a little

bit more then and bonds predictive

maintenance example this is using Azure

digital twin as an example it doesn't

have to be but it uses Azure digital

twin as the digital twin repository or

the the

asset master or the asset model for for

this it could be any existing eam or

other system that you that you have

what we have here is we're getting

real-time pump Telemetry using mqtt

which is a protocol so I'm getting

real-time data in I clean up that data

because industrial data is never clean

and in this instance I just I take this

and I send it to go and update my Azure

data Explorer which will give me a

really nice time series visualization of

all the information that I can drill

down on that and do thumb series slice

and dice

uh information but I can also

do some calculations around the pump

efficiencies and you know all the pump

metrics that we are trying to calculate

and update that state to Azure digital

twin so that we have the lightest on

that I also take that same data and I

will

I run it through to the recommendations

but before I do that I will

contextualize it using pump make model

all of that again from an eam system or

a maintenance system or the digital twin

system so that I have Rich data that

sits over here now how we put that

together so these are all listeners

you'll see the blue ones that's how we

get real-time data in and this is just a

subset but you'll see there's a huge

bunch of different protocols and

applications and services

and streaming platforms and and that we

pre that we support in in putting this

together the context might model all

this this is all fast moving data all

the slow moving data

um I can get through from all the

contextual data mic model

um

yeah again

weather patterns anything that I require

so if I'm doing flood predictions or

that kind of thing you know I can get it

for Weather Services or against

different

contextual data sources Transformations

is when we change the shape of the data

so cleaning it doing calculations I'm

changing it and you'll see there's a

there's a number of ones that are around

cleaning the data missing value

substitution

aggregation calculations uh

normalizing

setting up thresholds and um

and a number of these where we actually

transform the data this one doesn't have

machine learning in I'll show you an ex

machine learning example in a minute but

this is where we can bring in I can just

drag on anomaly detection and it's not

probably the right place to do it here

but just to illustrate the concept and

then I configure that each of these are

configurable so you can see this

pantelemetry one there's the

configuration for that so in order and

it will interrogate the underlying

service and come back with what are the

fields that this thing actually has and

I can now use that in my data stream or

if I go to something more sophisticated

like as a digital twin example it will

use some of the

xero trust capability credential

management which is all in our

subscription and in our in our

subscription manager installed in the in

the in the variable side but this is

where I would create for example I can

create a whole new instance in Azure

right from the application in here so

these are the kind of applic the the

configuration in a no code way of

setting up these data streams and each

of these have their own unique set of

properties

that we activate for each of those

I just discarded

um and then

that's the machine learning part so I

can bring in machine learning I'll show

you an example in a minute I could this

calculation might be quite Advanced and

I may actually want to do that in like

python so I want to maybe use my my

um bump calculations and efficiency

there might be a library that I'm

already using and again we support all

of those libraries out of the box

um in in this

the functions so that's more statistical

mathematical things like fast four years

geofencing and a whole bunch of goal

seeking similar to what you find in

Excel recommendations area that I'll

touch on in a minute but that's a whole

area on its own and then lastly action

agents so this is where we create

actions so it could be something like

send an email

or create ethereum smart contract

completely to ends of the scale but

that's really or create work orders in

Maxima update other databases

send it back to systems a very

comprehensive set now these are all this

is an extensible framework so if we

don't have a connector or don't have the

function that you that you require here

it's very easy to put that together we

can do it our partners do it our

customers do it and there's a framework

in order to create these connectors

yourself so this is at a really high

level what we're doing here so this is a

very basic one and there's actually a

live view of this so this is live data

coming through this is not the user

interface that I use every day to look

at my data but it helps me just to

understand am I getting the right data

at the right

point of this data flow and the way that

I for example

um

map and configure the endpoints or

getting the data in so you'll see in

this data flow it's interrogating adx

service and so what can you accept and

then we can bring in

from the from the

um

from the

next effect let me see if the Azure

digital twin one is configured to

show that up

so yeah as you'll see this one is

already configured to send the data into

Azure digital twin it will interrogate

the twin service and see what it can

accept this is what I have in my

Pipeline and we can Auto map that and it

will get that

into the data flow very simple example

but really effective in terms of getting

condition monitoring on assets going

as you get more advanced and more

sophisticated you may want to start

adding some predictive capability and in

this instance we're reading some some of

the data from a historian like osisoft

we're getting some other data from a

sensor based solution which has got IPC

UI running we've got some

Azure iot hubs and some of the other

capabilities and these are all the data

wrangling data cleaning and everything

that I need to do

and adding context from sap on mic model

and geolocation a whole bunch of other

information before I can actually and

converting failure tags and doing all of

this this is really hard if you do it in

code

what if you do it yeah it's really easy

to understand the logic but also to

troubleshoot and it's much easier to to

understand the logic of what you've done

in order to get this to this point what

I can now do is do my pump calculations

as you saw exactly the same calculation

as in the previous example but I'm going

to update my Azure digital twin in this

instance so I've got three actions

coming out of this block go and update

it with that data run an anomaly

detection on the pump performance

simple anomaly detection or have a more

sophisticated binary classification to

say to say is it likely to fail yes or

no and if it is you know what's a

remaining useful life model which we may

have for the pump

and um

and I'll show you an example of how that

can be put together merge all those data

and again send it to the recommend to

the what we call the recommendation

engine and run that recommendation you

may notice some little red legs on here

this is where you can configure a error

handling flow so if there's a problem

with this what do you want it to do who

must it alert what what must it let you

know

and or whatever system do you want to

activate when you have an error or

whether this data from the historian is

not coming through so this is the data

streams very very powerful this is where

80 of the work happens if you remember

the tip of the iceberg this is a nice

visualization all the heavy lifting

happens at the bottom this is what

happens over here

before we go back to the app designer

and recommendations and how we configure

them so as I said this remaining useful

life regression model

so where do you get them well inside XM

Pro we've now built in

jupyter Notebook so you can create these

models here and deploy them here here's

an example of reminding useful life

using a random Forest

um

to do the to do the um

the the model and I can see what what

senses and what influence and what is

the Affinity of and the correlation of

the data on this and then based on that

so this

um regression model that's built on

random forests

\[Music]

um as an as an example we'll then output

the right model for me we also big

supporters of things like Auto ml so if

you don't know what model to use it can

suggest and um and the output of this

model then goes into something like ml

flow so just another one you saw the

example of the beer the beer quality

what we're doing in this one is we can

even generate synthetic data if we don't

have the right data we can kind of

generate the data that the more that we

want the model to be trained on

and we can even use chat GPT to ask it

to

help us with the

um the visualization of this information

so it will write the code so you can see

here we're asking GPT we've got a magic

command for charge GPT built into this

so how can I visualize the data as a

correlation Matrix and it gives you the

code we can I can then run that code and

this gives me the correlation Matrix for

that

this is where I get into creating the

actual model and deploying that to

something like ml5 there is a webinar on

our website that goes into a lot more

detail I'm not going to spend more time

on this right now but just you can

automate building models right through

so that in the data stream if even if I

retrain my model I don't have to go and

update it here it will automatically be

updated

the last thing I want to touch on is the

um

recommendations and as you see we've got

a recommendation here now how did we set

up these recommendations there's another

one over here so for the pump discharge

so how did we set up this recommendation

and there's a whole area where I can

manage all of them look at how and look

at Who's got what and where it is but

there's also rules where I set up the

rules side so if I go to the bump you'll

see these all the different categories

so the pump discharge pressure was the

one that we had a rule

so there were actually two rules

so it would First Look for out of

efficiency range and then it will look

out of optimal range so if this one is

not if it's not true then it will

continue and to go so it enforces a

execution order and it gets data from my

pump Telemetry data stream

that that sends the the data through and

that's how it interrogates that

um if I look at I'll just use this quick

example to show you this is the nice

description that you saw at the top with

a nice icon and everything but this is

the heart of it where I have the

um

flow rate

and less than a third between a certain

band and the discharge project is

listening as soon as that rule is true

it puts that little red dot on there for

me and puts the it puts the

recommendation on the on the list and I

can now get that information now where I

get this flow rate you'll see there's a

whole bunch of parameters that's

actually what comes out the bottom here

so that what comes at the end of the

pipe over there

is what I now have available

to build this for me and I can use

different calculations and this can be a

value or it could be another parameter

so I can actually build a very Dynamic

set of rules including predictions and

everything that can come down the pipe

now this is not a valid rule where the

flow rate is not equal to the motor

current well hopefully that's not the

case but

that is gives you an idea of how you can

construct this so it could be completely

different because I can bring in very

different information I can bring

weather information I can bring all

sorts of

um I can bring maintenance record so if

there's if there's no

um

if the

if a certain condition exists then it's

minus 40 degrees outside then don't

create the work order because no human

can work in those conditions we have

seen some of those applications as well

so if a safety factor and all of those

you can bring in if they're or if

there's hot equipment nearby then notify

that

so that's how I built the rule and as

you saw in this instance I've enabled

the form and the form was a work request

but there are some other form types and

you can build your own forms as well and

this is just some of the how many times

does it need to log it can it

automatically resolve it so if it

condition is not true anymore will it

automatically resolve

these all capabilities that are built

into our recommendation engine very

sophisticated capability that you can

track but also this is what I put in

triage instructions notifications so

do I want to know when there's a new

alert when there's a status change how

might you know if there's certain

thresholds being not met on time because

we're waiting too long for someone to

respond to it so those are all

capabilities of

the um and the last thing I want to do

is just very briefly touch on as I said

I'll explain a little bit you can see

now that I've played around with it

um

there's definitely a higher

probability of failure that has gone up

due to some of some of the things that

I'm doing at the back here

um that's not what I wanted to do

this is um so when I clicked on the

pencil I have access to be able to edit

this you can actually see both of these

the 2D and the 3D they just overlaid on

top of each other and there's the name

black so that's how I got that done this

is a page builder web page builder in

this instance this is a Unity model and

this is just a 2d graphic both of them

have the same data that it displays and

these are all wired up data sources

and when I'm what I mean by a wired up

data source if I click on this Unity

block well let me first explain the

concept of a block there's a whole bunch

of different types of blocks

there are recommendation blocks action

blocks

and visualization blocks so that's where

we had Autodesk Forge and esri and unity

and all of these different visualization

capabilities that we have and we can

also create widgets so if I like this

style of something that I've built I can

actually go and create a widget for that

and these are just some examples so we

just can be saved and they can be shared

so if I've built a really nice widget

based out of a grouping of things so for

example I just press the

save there and whatever built in here

and now is available as a widget next

time I just drag the implied on and I

have a a name plate available they might

even be on here already

but that's typically how I create

widgets the data that sits behind this

so again I'm clicking on the unity model

here you'll see it gets the yellow line

around it

this is just how I'm the layout style

how it will react when it goes on a

mobile device in terms of its Flex

layout or but the block properties this

is where the actual

models reside

and we support both newer and older

versions of

of unity as an example these are where

the files reside and if I look at the

data the that is that resides on this um

certainly just um

so the data sources is the pump readings

um but on this overall page these are

all the data sources and if I look at my

live data where it's coming from

that's actually from the data source so

you'll see the

um

this is this is not the expression don't

want to bring the expression so I just

want to find the data source for it so I

can build very sophisticated

data connectivity this one is using

um that that data stream

connector it could be using a digital

twins it could use maintenance schedules

SQL data there's many different

connectors that we have oops

don't want to delete that as you can see

there's some some built-in capabilities

for people like myself that are not

coders or so it will help with not

screwing it up completely so

this is and also starting a new

application you can start from templates

so you can say well this one with the um

this pump one I'm not sure what so

you'll see this one has actually got a

series of drill down pages and

everything that's already associated

with it so I can use this as a starting

template to get started quickly

so this is how we look at

um

providing digital twin capabilities in

terms of Maintenance predictive

maintenance condition monitoring for

facilities management

if you have any questions please reach

out and happy to address them thank you

</details>
