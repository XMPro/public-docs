# how-to-configure-the-mqtt-advanced-action-agent---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=hYbVgPVVaYQ" %}



Learn how to configure the MQTT Advanced Action Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro....
<details>
<summary>Transcript</summary>Learn how to configure the MQTT Advanced Action Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro....
we are going to do here is look at how

this set up and configure the imputed

the advanced action agent this agent

allows you to pass data to a configured

in TTT system I already have a new event

simulator setup and configured which was

similar to sensor readings that can be

posted to MQTT I also have an event

printer set up and configured which will

help us see what the output data looks

like go to the tool box and search for

MQTT advanced you will find it under

action agents click on the agenda and

drag to the canvas connect the output

endpoint of the events simulator agent

to the input in point of the MQTT agent

and the upper endpoint of the MQTT agent

to the input end point of the event

printer agent no 34 name has been given

to the MQTT

agent to rename this agent pick on the

white space and start typing

click somewhere on the canvas and click

Save double-click on your MQTT agent

this is where you'll be configuring your

agent first make sure you using the

correct collection if not select a

little collection from the drop-down

next you need to add your broker host

name I'm going to use a public broker

if you'd like to use a dynamic topic

select the checkbox

then select a dynamic topic for example

if you choose temperature what's inside

temperature will be used as the topic

for this example I'm not going to use a

dynamic topic but I'm going to manually

specify that my topic name

next you need to set your board I'm

going to leave the default port as is if

needed specify your client ID then you

need to select your quality of service

which can be one of three options at

most once at least once or exactly once

I'm going to select at most once if you

need messages to be retained select the

check box a retained message is just a

normal in PTT message that has been

retained flag that is set to true the

broker will store the last message for a

specified topic if the Bursar's batch

option is selected this agent will

publish all messages it receives in one

batch in the form of an array for now

I'm going to leave this unchecked if you

need messages posted using a secure

Channel click the check box for this

example I'm going to leave this

unchecked if you'd like to use anonymous

authentication select the check box

otherwise specify a username and

password in this example I'm going to

use anonymous authentication if you'd

like to create an S at payload select

the checkbox

then add your nested pilot object

properties by selecting them from the

drop-down and clicking somewhere else on

the forum also specify an object field

name if you'd like to up it to be posted

as an array select the check box for

this example I'm just going to leave

this option as unchecked click apply

click Save

you ready to run the stream click on top

publish to view the live data click on

live view and select your vein printer

and click Save and give it a second

if you subscribe to the same topic in

MQTT FX that you subscribe to in data

stream designer you can see what the

outfit looks like
</details>