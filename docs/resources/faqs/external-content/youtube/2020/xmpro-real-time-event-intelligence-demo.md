# XMPRO Real-Time Event Intelligence Demo
{% embed url="https://www.youtube.com/watch?v=hi_cXYA7xsg" %}

XMPRO empowers business users to create and deploy applications for real-time event intelligence without disrupting operations. 

With XMPRO’s Event Intelligence Platform, your subject matter experts can easily create complex real-time applications that provide situational awareness, are always on, and prescribe and orchestrate appropriate actions.

Visit xmpro.com to learn how you can get more insights from your real-time data with XMPRO.
<details>
<summary>Transcript</summary>in this demonstration I'm going to show

you how to detect and respond to

critical events in real time without

having to look at data in 20 different

systems like you probably have to do now

now the XM pro event intelligent

platform consists of three main

components and the first one or the data

streams that you see on the Left which

is really aimed at connecting and

bringing information from those 20

different systems in the middle we help

you visualize and find those key events

that you are looking for that you want

to respond to and the last part is how

do you respond to those through

recommended actions or having act or

having actions and workflows in other

systems so let me jump in and we're

going to start with what you see on the

left the data streams and how do we

connect all of this information coming

from multiple data sources then we'll

move into how do we set up these

visualizations and in the notifications

that go with them because you don't look

at a dashboard 24 by 7 to be honest you

need notifications around specific

events that are starting to happen and

then how do you respond to those was

recommended actions so let's jump into

the data streams so this is the central

console where you can access all the

different modules within XM pro so the

app designer the data stream process

designer what you'll see I have

different instances running production

simulation demonstration instances so

I'll actually jump into the data stream

designer itself and this is where we set

up those integrations where we can

connect to those 20 different systems

get data from them and the data could be

real-time data from machines from

websites from Web Services from other

business applications and streaming data

that that could come from multiple

sources you can also then decide how to

apply some analytics to it and what

actions you want to drive from it you

can organize it into the into different

areas so in this instance different

categories are based on your business

structure of business organization

supply chains safety and this instance

I'm going to look at equipment

and I'm also just going to show you two

different examples the one is a very

basic simple example for condition

monitoring and the second one we are

adding some smarts in terms of being

able to predict when certain equipment

is going to film so let me start with

this simple version and in this one we

are just going to connect to one data

source in this instance the data source

is through OPC UA which is a protocol

based and we're getting temperature and

vibration readings for this pump we're

getting the make and model of the pump

from a different database system so this

is data in motion this is typically data

traced so this is fast moving fast

changing it could be thousands of

records per second it could be a couple

of records every five minutes it really

depends on the use case in the

application that you set up so in this

instance we're getting the vibration and

temperature data we we contextualize it

with a make and model because we want to

set the rule for the vibration checking

for that specific model and then we want

to start a space and work order request

inside external system like ASAP or

something in this instance we kicking

off a workflow inside XM pro and then we

would like to SMS someone that something

is happening so a very simple structure

in terms of being able to monitor

real-time now I can apply this model for

one or tens or hundreds or even

thousands of pumps that run the same so

if I've got two or three hundred slurry

pumps I can run the same model it's one

instance across all of them and it will

continuously look across all of them for

these conditions I'm trying to find

these events I'm trying to find when the

vibration is above a certain level and

what we have from from a the ability to

bring data in is something we call

listeners so these are all agents our

listening agents and this is just a

subset but there's a broad range of

listening agents so we can listen from

again a broad range and if we don't have

it it's pretty easy for us to get it

to our library that you see here just

different systems where I can get

real-time data streaming in or where I

can actually poll so if it's not a data

that can as a data source I can push it

to me I can also pull it in context data

this is where I make model maintenance

records other information that I may

have which may sit in something like

Maxima or SME or any one of those

systems again this is just a subset of

some other systems where we can get

contexts from so that we can certainly

now which bump or this temperature value

belongs to because the sensor typically

just sends the sensor ID or something

like that along in terms of

transformations this is how we

manipulate the data so how what do we

want to do with it how can we aggregate

how can we filter how can we join how

can we pass through how can we set up

thresholds the ones that you see there

all of these ability to until to

transform the data in one shape of form

in the next example I'll share a little

bit around the machine learning

capability where we just bring in some

machine learning but in this instance we

don't use it but we have standard

machine learning capability built-in so

multi-class classification regression so

this is typically Willet file what is

remaining useful life but you can bring

in things like jupiter notebooks if you

already have models in Watson or or

Azure or those you can you can actually

bring them in as well

functions these are things like fast

Fourier transformations or functions

that you want to perform when you

manipulate things like Python scripts or

R scripts or certain signal folders that

you that you want to do so these are

more function based not so much

transforming the data but just applying

the data and getting an answer and or

something and then lastly and almost

most importantly is what are the actions

that you want to do because we're not

trying to do this just so that we can

detect them we actually want to respond

to them so it's around event response

and then optimizing that response

so these are the different action agents

and again a subset so in MI for example

want to say another email as you can see

we've got a SMA severe I might want to

update a 3m smart contract I may want to

send it to a chat bot I may want to

broad range again and then the generic

interfaces like race type II eyes and

and other standard protocols and formats

that you can send things through so

again just a subset and you can also

send it into XM Pro into the app

designer into the into the application

itself where we run rules and

recommendations and have a user

interface for all of this data that

we've put together again a very simple

example if I double click on this what

it'll show you is just how I set up this

the configuration for this I'll show you

another example in a minute of a PI

server or OSI soft server where the

configuration very similar

it just has different fields and

information you can see this is what

it's bossing me in my OPC UI link that

it's sending so this is the topic that

it sends it to and I just subscribe to

this endpoint and I'm getting streaming

data into the application itself so if I

show a live view of that information I

can actually see some of the data coming

in and this is a unit that sits in our

Dallas office so I can get temperature

vibration readings and just to show you

that this is actually connecting from

live data and this instance this is just

one but it could be reading from from

multiple devices and for those I would

then get the individual ones so this is

just a live data view this is not a

dashboard that we show to the in

customer this is really just to see that

the data that comes out the the thing is

the data that we've all that we are

looking for so very briefly this is what

I this is how we connect up those 20

data sources if I go back

and if we look at and so you just got

back to the pumps and just to very

quickly show a more advanced or expanded

version it's still a predictive still a

centrifugal pump still getting

temperature vibration but now we're

getting pressure and flow from OSI soft

in this instance I still have access to

all the same connectors so I can drag

them on my can have multiple inputs and

again this is how you connect up the 20

different data sources in this instance

is reading from a set beam you can see

from a confer configuration point of

view this is slightly different to the

one that I showed before but I'm I can

and this is looking at the OSI soft

asset framework for example and brings

back the elements as well as the

components and I can choose some of the

others that I might want them I want the

Impella size or something like that so

this is how I set that up in this

instance it's the same we're still

checking for thresholds but I'm also

calling a predictive model in this

instance Azure based model to predict

the likelihood of failure is this thing

likely to fail yes or no if it is I want

to run a sec a second predictive model

so I can join models together and in

this instance what is remaining useful

life how much time do I have before this

pump fails and again I'm sending this

into my ex-emperor ab designer which

I'll show you in a minute how we now get

this data into a user interface but this

is a key aspect in a really important

aspect of being able to build real time

event response solutions is being able

to connect to multiple data sources get

a high volume of data flowing fast and

being able to find the exceptions and

find the key events that you are looking

for and bring the data from from big

data to small data to the action that

you actually want to do just to try and

build a dashboard that connects to all

of these sources it doesn't have the

capability to help you find the key

things it can show you the tank level it

doesn't tell you whether the tank level

is actually a problem and I'll get back

to the tank level

in a minute so this is the data designer

so if I go back to the so this is the

the data stream designer and this is

where we connect all of these data what

we now want to do is create them using

the fly so just show it to someone so

that they can see what's happening they

want to see certain of the areas and

then have some recommendations around

what to do now

we don't call these dashboards for us

they are event boards and the reason is

the purpose is slightly different so if

I quickly go in and show you an example

of such a event board this is connected

to some data flowing at the back and

here's the event board so what this

tells me is there are certain key events

starting to happen or both things are

already happening there's an event right

now or there's a likely event starting

to happen it doesn't show me the tank

level it this differs from an HMI view

or a control system view or something

like that where you can see the speeds

and feeds and the motor amps and all

those information which in actual fact

you don't really care too much about

until you know it's wrong so I need to

know whether a high tank level is a good

thing or a bad thing just having an

indicator telling me this is sitting at

the top doesn't really tell me if this

is a good event or a bad event or and is

it something I should be concerned about

or not and that's the whole purpose of

what we call event board so we put these

event boards together and there's

different ways of displaying the

information so this is one way so in

this instance you can see there's a

problem with this bump and we'll get

into the recommendation that was fired

for this in a minute but B I just want

to show you a slightly different example

of and if I go back to this if I look at

the conveyors on that on that plant

itself I can also have a different view

way for all the different two conveyors

I can see certain properties and I can

have a rule behind the property to say

well in terms of this instance the the

the amps on the motors for this conveyor

is this a challenge and they might be

because the this certain real-time

information and again I can show you

whether this is good or bad and what

does it mean which is more important

than just having a tonnage

it's decide is this tonnage good or is

it bad it's the multi amps good or is it

bad is something starting to happen and

do I need to respond to it

so again just going back to this plant

over here and I could actually have just

gone through into that but I will let's

look at the mod example so in this

instance I can see the discharge

pressures current fluorides I can see

and over a period of time so I can see

certain information around that now

you'll recall a whole bunch of dots Anya

and I told me this is a good event or a

bad event or the way that you decide in

terms of the colouring is at read events

or needs immediately action a yellow

events might be longer this is really

completely up to to you to configure

when you design these apps and I'll show

in a minute how we put these together

but before I do that I just want to show

you what a recommendation is so here's

an example of a pump that we drill down

to and I can either access it from here

or let me go into the pump itself I look

at some of the information I can see

what's happening and now I click into

the recommendation another

recommendation is how we act on the

event and what you'll see is this is the

data that fired that instance so you can

see in the past it's been resolved this

is the this is the real time data that

fired this is the I can put in a

recommendation recommendation here to

see to say or to say please check

something or do something or what or

make a suggestion to the maintenance

planner or in terms of what they should

put on the work order to say this is a

test impeller

and I'm not going to this is a tasting

Bella up can't spell please discuss with

manufacturers so I can now so the

reliability engineer or some subject

Mattox but can actually look at we're

going to type all of it out so you can

talk to the manufacturer I can either do

this automated or what we find a lot of

organizations want I want to create a

work request number so in the ASAP or

Oracle or Maximo system they were going

create a work request number and we

would then Paul that system to see when

a work order is created by the

maintenance planet this could be done

fully or automated as well so right at

the india you could actually just create

a work order inside sa p if you wanted

to but in this example we are doing that

you can also put together different

instructions and the way that you set

this up which is actually kind of more

important in a way is setting up these

rules for these recommendations is and

I'm just going to go into manage

recommendations this is the area where I

can manage a lot of all of these rules

that I set up around specific events

that I want to fire and these are the

ones that you saw the red dot and you

saw the yellow dot appears for that red

threshold this is the rule that and you

can see this is a very simple rule that

we've got with the data that that's

that's coming out of our taste system

but I can do I can just create that red

threshold what could be a low suction

pressure or in this instance distance

pressure high threshold or in this very

simply named red here and then the

information that flows in this data

stream that you see word game weight

it's this this is the data that actually

flows out here so I've got access to all

of these different fields that I can now

put a rule against then when this rule

is true it will put that dot on there

for me or whatever other indicate that

the dot is just one that we find is

pretty pretty Universal but you could

put any indicator or any notification

that goes with that I can either have a

value or it could be something another

variable that comes in that so if the

flow rate is less or equal to the power

this one doesn't make sense but it

illustrates the concept of what we are

doing here and I now have a rule and

when the con when the data flows through

this data flow it finds the true

condition it would then give me the

notification it would put the it would

put the dot on the on the equipment for

me and also give me this recommendation

which I saw earlier that I can now

either great work requests have stand

procedures around how to fix this and

use this as a recommended action now the

benefit of this is this can be done by

someone who's been there like 45 years

you captured it in their knowledge

around what would you do when these

conditions exist what would you

recommended actions be and through that

you also build up in your knowledge base

the best actions under certain certain

circumstances the other benefit is that

person who's who knows how to operate

and use this doesn't always have to sit

in the control room they can sit in the

in the office in the boardroom they

could even sit in the bedroom and be

able to monitor look at things and then

make decisions on what are the best next

actions that you could do now there's a

lot more to this but one last thing I

just want to show you is how do you set

up these now this is running on live

data so I'm just going to use this a

slightly different system but we'll

still have the same

view this is how I manage and set up

those applications so I'm just going to

use the landing page for now and this is

how you design those event boards it is

a user interface for that and we have

all the you build it up completely

through a drag-and-drop user interface

so different layout components so and

I'm not going to go through all of them

but you can see this charts these

checkboxes is data selectors is file

uploaders grids lists sliders sparklines

graphs different kinds of charts and

graphs the certain actions like

hyperlinks it'll take you around and

most importantly widgets so I can make

this so if I take the whole area that

you see here I can actually turn this

into a widget I just save it and now

next time I can reuse this sorry and

just go back to the blocks I can reuse

this as a widget now wiring this up to

the page data and the underlying data

this is all handled through through the

data stream and the data stream

connectors for the app so the app can

get its real-time information from that

data stream it can display it to you and

then you set up the logic or the way

that you want to display this

information with what you want where how

and again we've got templates for

different layouts but you can also take

components like this that you reuse a

lot and make them into widgets so that's

kind of the 50,000 foot view of what

ex-emperor is how we put this all

together and again just the reiterate it

consists of three different components I

can get my 20 different systems that I

look at combine the data get a logical

for flow of data going through it and so

I can go from Big Data all of these

different systems

into smarter data into the actions that

I want I can visualize it but also

behind this I can set up the rules to

send emails SMS notifications to systems

like themes slack or whatever it is

where you want these actions to be

notified

I can then drill down into a

recommendation and decide what action I

want this could automatically create an

action into a back-end work or the

system for you for example but this is

how we help you to detect and respond to

critical events in real time without

having to look at data or systems or 20

different things where the data could be

thank you for your time if you have any

additional questions or would like to

have more information please contact us

and we'd happy to give you a more

detailed presentation and demonstration
</details>