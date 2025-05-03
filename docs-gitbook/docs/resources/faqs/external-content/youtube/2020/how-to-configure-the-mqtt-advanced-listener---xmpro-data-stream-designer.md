# How To Configure The MQTT Advanced Listener - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=Mxo1EWfBRGo" %}

Learn how to configure the MQTT Advanced Listener in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>we are going to do here is look at how

to sit up and convey the Inka to the

advanced listener agent this agent

allows the user to receive data from a

device or other source by listening to a

specific MQTT topic as little device

publishes the data to that amputated

channel or topic I'm going to add this

agent to my canvas now so I'm going to

go to the toolbox and search for it

you'll find it on the listeners to add

it to the canvas click on it and drag it

to the canvas and drop it you will see

that this agent has a default name given

to it you can rename this item by

clicking on the white space and start

typing click some mouse on the canvas

and click Save you configure this item

click on it and click on configure first

make sure you using the correct

collection if you'd like to change this

just select another collection from the

drop-down next you need to specify your

broker address I'm going to use a public

channel for this example then specify

the name of your channel or topic at the

port number you'd like to use and

specify unique client ID

next you need to select your quality of

service three options is available at

most once at least once and exactly once

I'm going to leave it with the default

option then you have to the choice

whether to create a clean session or not

I'm just going to leave the default

option as is if you need to use a secure

Channel when publishing or listening to

messages you can select this checkbox

you they need to specify your protocol

from choosing one of the options in the

drop-down and upload the appropriate

certificates and specify your client

certificate password this example I'm

not going to use a secure channel if you

have credentials configured you can add

your username and password in here if

not just leave these options empty then

you need to specify the format of your

file light which can be either JSON or

hex my pilot will be in JSON so I'm

going to leave it as is if your panel

has a nested structure you need to

specify the path for your Jason so then

you need to select this box use this

sample here to specify your path

you'd like to include those messages in

your pilot you can select the box lastly

you need to specify the payload I'm

going to add a new row by clicking on

the plus and add my items

then specify a datatype click somewhere

else on the canvas take apply click Save

now I'm going to use MQTT effects to

publish the readings to mqtt to run your

stream click on publish to view the

library click on live view select your

agent and click Save I have one

temperature reading here which are going

to publish as you can see in the

background it came through in my live

you
</details>