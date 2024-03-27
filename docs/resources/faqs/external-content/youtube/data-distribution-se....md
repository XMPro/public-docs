# Data Distribution Service: Using DDS in Your IoT Applications
{% embed url="https://www.youtube.com/watch?v=ypmEC1WyjzA" %}



XMPro’s integration library includes pre-built connectors for a variety of popular IoT connectivity standards like MQTT, OPC UA and DDS. In this video, we’ll demonstrate how you can use...
<details>
<summary>Transcript</summary>XMPro’s integration library includes pre-built connectors for a variety of popular IoT connectivity standards like MQTT, OPC UA and DDS. In this video, we’ll demonstrate how you can use...
good and welcome today we're going to go

through a stream that's being configured

to consume data through DDS now what is

DDS it's the object management group or

oMG their data distribution service or

DDS standard we've logged in as a

particularly user interaction priority

and the first thing we get to is the use

case groups these are categories that

you can configure and set up that allow

you to group together your various use

cases we're going to drill into the

downstream so we just click into that

that'll take us to the various use cases

which have been associated to this

particular category we can click into

one and that'll take us into the actual

use case itself what we're looking at

here is a stream designer it's a

graphical interface that allows me to

drag drop and configure all the various

elements that I need for this particular

stream in this example we're consuming

data coming off of RTI's DDS we're

collecting the edge outliers that we're

looking for we're gonna filter those out

we're then going to do two things based

on what matches our particular filter

the first thing we're gonna do is we're

gonna send an SMS notification the

second thing we're gonna do is we're

going to push it through to a predictive

model we then going to gainful to those

results and anything that matches we're

going to start a maintenance or a work

order Spears BPM process so this is for

rotating equipment predictive

maintenance as a particularly use case

using the data that is going to be

pushed through the DDS the first thing

we've got is on the left you'll see your

various toolbox with those items the

first one is a listener where is our

information coming from so if I expand

that you can see there's a multitude of

different options that are available one

we're focusing on today would be the RTI

DDS subscriber this allows us to read

topic data from the RTI DDS server and

consume that information coming in from

there as well

the second thing that we've got is a

transformation so what type of

high-level transformation do we want to

do on this data and information that is

coming through the DD

the first one is we're looking for

outliers the second one is a filter

third one is a broadcast and again

another filter those are all types of

transformations that we've dragged on

and configured from a function

perspective just to highlight what we

have in here whether you want to bring

on some R scripts some FFT algorithms or

RCA in this example we don't have any

functions that we're currently using but

they are still available in the library

if you want to use them and then lastly

action agent what type of action do you

want to take with this information that

is actually matching the data as its

flown through DDS the first action that

we wanted to touch on was we wanted to

push information to an SMS we want to

notify soul immediately we also wanted

to put something on a exome Pro VPN

process form you could also push

information back as a publisher to the

DDS server if that is something that you

want to do from a use case perspective

if I close the tool box here so we've

got this running it is currently

published and we're consuming data

coming off of our TR now to that end

what I'm going to do is I'm going to be

using the RTI shapes demo just to

illustrate information and data flowing

through and the various options that you

have when you're actually but to

configure this and how do you consume

the data for that if I come back to the

stream there's a live view option so

we're going to click that on the right

what the live view does is it shows me

data that is flowing currently through

those particular points I'm interested

in the edge art layer so that's

information that's coming directly off

of the DDS server and I'm also

information looking for information that

comes out in the filter as well so those

are the outliers I'm actually looking

for so if I go back to the the shapes

demo everything that we've configured is

around the square so I'm gonna publish a

square I'm just going to keep it blue

and we're just gonna let that what

you'll see in the background is as soon

as I've published the square we're

automatically picking up the data coming

through the the DDS it is sending us the

particular edge

and in this instance is only looking for

blue as a particular colors if I go into

the square again and I say I'm looking

for another color again we'll have two

sets of information and if I scroll down

here and we go to the end you'll see the

two colors start coming through here as

well so if I go back in there the

squares are what we're actually looking

for so how is this actually configured

if I move out of that not close the live

view if you double click any of the

components on your what it'll do is will

open up this configuration pane that'll

allow you to configure this particular

stream object in this instance we're

configuring the RTI DDS subscriber we've

got a particular polling interval we've

got a particular domain that we're

looking for and if I click the drop-down

we're looking for the various items now

I have two squares published so it's

going to give both of those as

particular topics for me if I go back to

the RTI it's got and delete everything I

want one square which is gonna be blue

and I want one triangle and it's make it

orange so I've got two very different

shapes which are generating data for me

through the show to demo if I come back

and I just close that and I go back into

it again so again we're opening up the

configuration for the RTI stream object

if I go down to the topic you'll see I

have access to square and triangle for

the topics coming in here as well so

this is a live look up on the actual DDS

server as those topics are available you

can actually select them and make use of

them here as soon as you select them

you'll see topic properties down on the

bottom here so this is again made

available through the DDS integration

and says for that particular topic these

are the properties that are available I

can select all of them or I can delete a

few that I'm not interested in actually

using if I found that a particular topic

doesn't exist so I'm looking for circle

as an example I can actually create the

topic from within the configuration

window here as well

then I would need you to specify the

properties and that'll actually publish

that particular topic to the DDS server

and it'll also start listening on that

particular error for me as well so this

is how we can configure the various

items for the DDS that we're looking for

so what I'm going to take you through

now is what do we actually configure

here with this information as we made

available so let's go back to the live

view that'll bring us the blue coming

through so what we've configured is when

the Blue Square is bouncing around the

screen and generating the data for us

that's what we're seeing down the bottom

here come up with us what we're

interested is in when that actually

changes to yellow so I'm gonna delete

that and I'm only interested when the

square is actually coming in as yellow

as soon as the square comes in as yellow

let's see across the top there that is

the filter item that I'm looking for so

that's the one anomaly in this set of

information as soon as is made available

I won't trigger an SMS and I want to

trigger off for a particular work order

you'll still see down the bottom here

we're still consuming the data as it's

been made available but I'm interested

in when a change to yellow and as soon

as that happened I want to send out an

SMS and I want to start a particular

work order coming down the bottom here

again if we double click into any of

these you can get access to the

configuration which is how we are able

to connect to this particular DDI server

it also allows us to connect to a

particular topic and consume the

particular properties off of that so

first item from a subscriber perspective

or considering data from the RTR DDS

server we're looking for some particular

outliers in this instance when the

square was not blue but it was actually

yellow we're filtering that out we're

gonna do two things one which is to send

an SMS the second is to send that to a

predictive model filter out the results

from a predictive model and then we'll

create a particular work order inside

excellent performer bpm perspectives

you
</details>