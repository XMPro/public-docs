# how-to-configure-the-calculated-field-transformation---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=kz3ARqfZVSM" %}



Learn how to configure the Calculated Field Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://x...
<details>
<summary>Transcript</summary>Learn how to configure the Calculated Field Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://x...
what we're going to do here is ticket

how to set up and configure the

calculated field transformation agent

this item allows you to create new

column values through the use of

expressions the result will be either

nearly define column or it can replace

the values in existing columns I've

already set up and configured an event

select agent which will symbolize

fibration readings from a sensor I have

also set up and configured an event

printer which will show us what the

output looks like go to the toolbox and

search for calculated field

you will find it on the transformations

click on the agent and drag it to the

canvas connect the output endpoint of

the events simulator agent to the input

endpoint of the calculated field agent

and the output in front of the

calculated field agent to the input

endpoint of the vein printer agent let

the default name has been assigned to

your calculated field agent to be nine

this agent click on the white space and

start typing

you

click somewhere else on the canvas and

click say double click on your

calculated field agent this is where

you'll be configuring your agent first

make sure you're using the correct

collection

if not select another collection from

the drop-down next you need to configure

editor click on maximize to make the

page bigger click on add to add a new

room if you want the calculated values

to be added in an existing column select

the column from the drop down if you

want a new column to be created at the

new columns name in here

I want in your column to be graded

clicks announced in the forum now I need

to add my expression if the vibration is

higher than a certain value

I want height to be returned otherwise

medium should be returned

you

then select your data type I'm going to

leave it as string click something else

in the form now choose how the result

should be returned options include a

painter current which will append your

results to the current by load or new

which will return your results as a new

palette I'm going to select new and show

what the data looks like click apply

click save to run your string click on

publish to view the live title click on

live view select your event printer and

click Save

now that the new values are returned as

a new payload now I want to show you

what it looks like if you have selected

a bin to current stop the stream are

clicking on unpublish

double-click on your calculated field

agent instead of new select a Penta

current click apply click Save publish

the string and click on live you

now that a new column has been added to

your current payload

you
</details>