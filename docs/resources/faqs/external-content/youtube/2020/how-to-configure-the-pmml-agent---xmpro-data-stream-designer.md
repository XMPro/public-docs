# How To Configure The PMML Agent - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=mc9NSwenkRQ" %}

Learn how to configure the PMML Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>we are going to do here is look at how

to set up and configure the PMML iron

machine learning agent this agent allows

you to perform predictive analytics

using the PMML execution engine I

already have a CSV listener set up and

configured which will get data from the

CSV file let's look at how this agent

has been configured as you can see

there's a number of CSV definitions that

have been map let's look at the file

that's been uploaded here the CSV file

contains records of tips received by

waiters in a specific restaurant now we

need to set up and configure the PMML

agent so I'm going to minimize this and

close the configuration screen for the

csv agent to add the PMML agent to your

canvas go to the toolbox and search for

the agent you will find it on the I iron

machine-learning click on the agent and

drag it to the canvas now connect the

output end point of the csv agent to the

input end point of this agent note the

default name has been given to this

agent to rename this agent just click on

the white space and start typing

click something else on the canvas and

click Save to configure this agent click

on it and click on configure first you

need to make sure that you're using the

correct collection if you'd like to use

another one just select it from the

drop-down next you need to browse to an

uploaded PMM file that contains details

of your predictive model that you'd like

to execute as soon as this file is

uploaded you will see there's a number

of things that you need to map map the

data field column for all rows in the

grid this applies to all models except

the Association rules model for the

Association rules model there will be an

item's field that you will have to map

I'm just going to go ahead and map these

values quickly

now click on apply click Save to run

your data stream click on publish to

view the live data click on live view

select your PMML agent and click Save

then give it a second or two to expand

this page click on maximize there you

can see the tip that has been predicted
</details>