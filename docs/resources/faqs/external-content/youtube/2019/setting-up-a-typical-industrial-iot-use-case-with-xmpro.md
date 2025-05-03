# Setting up a Typical Industrial IoT Use Case with XMPro
{% embed url="https://www.youtube.com/watch?v=Z23vUw-XYm8" %}

See how to set up a use case using XMPro's Agile Application Suite for Industrial IoT.

The video uses the example of continuously monitoring thousands of solar panels in the desert to predict which are dirty or broken. It also shows how to easily connect to third-party applications like SAP EAM or OSIsoft. To learn more visit [http://xmpro.com](http://xmpro.com)
<details>
<summary>Transcript</summary>the use case manager in our exemplar

agile design suite allows you to

visually orchestrate IOT data sources

services and applications to grade

multiple different IOT applications in

this example we will look at a solo form

a thousands of solar panels each

generating IOT data that we may want to

use to create work orders inside sa baam

for example for those solar panels that

are likely to be dirty and which we

would like to be cleaned by a field

services team we will start by dragging

active listeners onto the canvas

now extemporize active listeners is an

extensible library of predefined

streaming connectors to connect to a

vast array of IOT data sources we also

have transformations to manipulate and

manage the data and provide analytical

capability on the canvas context

providers are used in richly information

and finally we have action agents to

trigger actions inside s ap or other

third-party applications and can also

create tasks inside the XM pro console

in this example we'll be bringing data

in from OSI soft as a time series

database we will drill into that in a

little bit more detail later but we

combine this with weather data from a

REST API some MQTT data coming off the

sensors on the panels itself and combine

that data contextualize it with si Pei M

information to know which make and model

it is and finally we will run it through

a Hana model to predict the dirty panels

for those panels that are likely to be

dirty we're bringing in additional

information from ASAP ERP and we show

that on analytical dashboard inside s IP

Hana the most important step though is

to create a work order inside ASAP EAM

finally we would also like to do a root

cause analysis or a failure mode inside

and start that inside XM pro each stream

object have a property pane so let's

look at the OSI soft property pane and

in here we can see how we set up the

data connection to is always a softer

read the data from a specific PI server

in the same way we can also set up the

properties for in

tt in this example and in this instance

it is a push so it means it's a

real-time data feed from the sensor data

we combine all of this data through a

join transformation and in this join

transformation it shows up all the

properties from all the various data

sources what we want to do is create I

join based on the customer number so as

you'll see right at the bottom here we

combining all the different data sources

for a specific timestamp and connect

them via the customer number the next

one we will look at from a property

perspective is the ERP information so if

we look at the information coming out of

from the ERP side you can see it is a

get action to read information from the

casts that which is specific to the

customer next what we want to do is kick

off an action to create a work order

inside a CPE I am in this instance it's

a put action so we push the data through

and if you double click on the arrow you

can actually set up the mapping of the

data sources on the left hand side the

data is coming out of the event stream

and on the right hand side the fields

are available from s IP to map this to

this is a visual mapping making it very

easy to take data from the event streams

and push it to the right place into the

work order I'd also like to create a

task inside the X and proc action

console to do a root cause analysis and

for that we also want to identify which

task it is and how we want to kick off

the action again mapping the data to the

form you'll see the data appear on the

form itself the data that you see over

here will be on the XM platform we've

now set up an event stream inside

ex-emperor IRT application suite what

I'd like to show you next is what this

data looks like inside sa Pei M and also

on the X and production console let's

look at the work order created in ASAP

eim in this ASAP instance I know the

transaction code that I'm looking for

and I also know that we've created a

service order for this specific example

around this

the panel's so I will interrogate and

return all the open service orders for

this example I'll also look for the ones

that are created or generated through XM

Pro integration in the event stream and

here's an example of one of those as you

can see in the header the order was

created from inside X and prevent stream

in ants also assigned to the right

responsible party as well as the

operations and cost centers using X and

Prez visual designer project can now

ensure that you have the right

integration with the right information

income coming from the right sensor at

real time without any manual

interventions and this is all done

through X and price event streams now

let's look at this in the ex-emperor

action console we can display data from

census as well as SFA eim and ERP into

the dashboard but what we're really

interested in is the task list for the

root cause analysis that was initiated

by this event stream information for

this can come from ASAP as well as the

PI system and we can also get readings

off the live since the streams to

display to the engineers for decision

support I can also show infrared images

from a drone for the panel for example

and all of this is part of the decision

support that we trying to create for the

engineers you can create customized

forms as part of all of these actions

you may have some special instructions

that you want to do before you create a

work order inside si p4 from this user

interface for those who go out and do

something around this specific panel see

I am work orders can also come from this

user interface not only the event

streams you can also collaborate inside

X impress so I could talk to other

engineers and other users of the system

to find out if they've had similar

experiences around panels in in their

area with sensors I can also create an

addict task if say a specific action

that I that I want or predefined action

is not there so I can go and set up an

adduct task for someone to go and do

something similarly you can create case

files that contains information like

reports photographs and

artifacts that you may want to keep for

a specific incident here we provide

contextual information coming out of CAD

systems and other business systems for

decision support in order to drive the

next steps of what we want someone to do

in this example we've taken data from

IOT systems created an event stream and

created actions inside of a CPI M and

other business systems
</details>