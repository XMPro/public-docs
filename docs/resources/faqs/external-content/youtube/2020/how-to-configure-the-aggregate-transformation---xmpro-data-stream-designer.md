# How To Configure The Aggregate Transformation - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=ucc8wtz_hJo" %}

Learn how to configure the Aggregate Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>but we are going to do here is look at

how to set up and configure the IP and

transformation agent the aggregate agent

allows you to apply function to data

captured in a specified period of time

for example calculate the average

temperature recorded over a period of 10

seconds I already have an events I'm

going to set up and configured which

will seminar the number of readings

coming from census I have also added an

event printer to my canvas which will

allow us to see what the are created

data looks like go to the tool box and

search for applicate you'll find it

under transformations

click on the agent and drag it to the

canvas connect the output endpoint of

the events unlike the agent to the input

endpoint of the aggregate agent and they

are in point of the aggregate agent to

the input end point of the event printer

agent note that the apical agent has a

default name assigned to it you can

rename an agent by clicking on the white

space and start typing

click somewhere else on the on the

canvas click 'save double-click on your

aggregate agent this is where you will

be configuring your agent first make

sure you're using the correct collection

if not select another collection from

the drop-down next select the attributes

to group on I'm going to select reading

number next you need to add your

aggregate function expand the page click

on the + to add a new row select the

function from the list in the drop-down

that you want to apply to the data I'm

going to leave it as average then I'm

going to select my parameter which is

temperature and I'm going to give it an

alias

and click somewhere else in the forum

then I need to specify my window you can

find an entire list available when you

click on the drop-down I'm going to

click second and add the size as five

then I'm going to click apply save now I

want to run my stream so I'm going to

click on publish to view the live data

click on live view and select your event

printer agent and click Save

give it a second and the data will start

coming through to expand the page click

on maximize

you
</details>