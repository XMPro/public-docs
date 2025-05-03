# How To Configure The Filter Transformation - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=fEUjU1IGdC4" %}

Learn how to configure the Filter Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>what we are going to do here is look at

how to set up and configure the filter

transformation agent

this agent allows for incoming data to

be filtered according to the conditions

defined by a user i have already set up

and configured

an event simulator agent which will

simulate temperature readings from a

sensor

i am only interested in readings higher

than 50 degrees celsius

anything lower than that should be

disregarded

i have also added an event printer to

the canvas

which will allow us to see what the

filter data looks like

go to the toolbox and search for filter

you will find it under transformations

click on the agent

and drag it to the canvas

connect the output endpoint of the event

simulator agent to the input endpoint of

the filter

note that the filter has two other

endpoints

the output endpoint is for when the

condition specified holds true

the false endpoint is for when the

conditions specified does not hold true

you are only required to connect the

output endpoint to another agent

so i'm going to go ahead and connect the

output endpoint of the filter agent to

the input endpoint of the event printer

agent

also note that a default name has been

assigned to the filter agent

you can rename this agent by clicking on

the white space and start typing

click somewhere else on the canvas and

click save

double click on your agent

this is where you will be configuring

your filter

first make sure you're using the correct

collection

if not select another collection from

the drop down

next i want to configure my filter note

that the default group has already been

added for you

to add a condition click on the plus and

click on add condition

next select the field you want to apply

the filter to

which in our case is temperature

select your equation i'm going to select

is greater than

and then i'm going to add my value which

is 50.

click apply click

save now i want to run my stream so i'm

going to click on publish

to view the live data click on live view

and select your event printer

click save

now that the data coming through is all

above 50 degrees

to expand the page click on maximize
</details>