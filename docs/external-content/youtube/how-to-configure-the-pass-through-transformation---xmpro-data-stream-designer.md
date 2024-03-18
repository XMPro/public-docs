# how-to-configure-the-pass-through-transformation---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=JV3lJHtGka8" %}



Learn how to configure the Pass Through Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro...
<details>
<summary>Transcript</summary>Learn how to configure the Pass Through Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro...
but we are going to do here is look at

how to set up and configure the Paso

transformation agent this agent allows a

selection of attributes of interest in a

pilot to pass down a stream instead of

passing the entire pilot to the rest of

the stream I have already set up and

configured an event simulator agent

which will generate a number of readings

I've also set up and configured an event

printer agent which will help us look at

what the data looks like when it's

passed through go to the tool box and

search for boss 3 you will find it under

transformations click on the agent and

drag it to the canvas

connect the up endpoint of the events

I'm not the agent to the input end point

of the boss through agent connect the

output end points of the password agent

to the input end point of the event

printer agent now that a default name

has been assigned for the bathroom agent

to rename this agent click on the white

space and start typing

click somewhere else on the canvas click

save double click on your agent this is

where you'll be configuring your agent

first make sure you're using the correct

collection if not select another

collection from the drop-down next

select the attributes in the payload

that you would like to pass through I

would like to pause for only temperature

so I'm going to select this attribute

and click apply click Save now I want to

run my stream so I'm going to click on

publish to view the live data click on

live view and select your event printer

agent click Save give it a second as you

can see only temperature is being passed

through to expand this page click on

maximize

you
</details>