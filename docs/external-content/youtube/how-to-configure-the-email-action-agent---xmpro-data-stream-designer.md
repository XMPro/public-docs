# how-to-configure-the-email-action-agent---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=xy0Ro52IhfE" %}



Learn how to configure the Email Action Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
<details>
<summary>Transcript</summary>Learn how to configure the Email Action Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
well we are going to look at here is

hard to set up and configure the email

action agent what I already have on my

canvas is an event simulator which will

simulate readings coming from senses

such as vibration and temperature then I

have a data conversion agent which will

convert the temperature data reading

from the double data type to int then I

have a filter agent which will fold out

any temperature readings that are higher

than 100 degrees for these readings I

want to send an email to someone lastly

I will have an event printer which will

just help us look at what the data looks

like now go to the tool box and search

for email you will find it under action

agents to add this a gentle stream click

on the agent and drag it to the canvas

connect the output endpoint of the

folder agent to the input endpoint of

the email agent and the output endpoint

of the email agent to the input end

point of the event printer agent you

will see that a default name has been

given to your email agent to rename this

agent click on the white space and start

typing

click somewhere else on your canvas and

click site to configure this agent

double-click on it

first make sure you using the correct

collection if not select another

collection from the drop-down next you

need to add the name for your SMTP

server at the SMTP port you'd like to

use then add your username and your

password

then at the address you'd like to send

the email from click enter to add it to

the list click something else on your

phone

add the address you'd like to send the

email to I'm just going to send it to

myself press ENTER then add a subject

for your email click somewhere else on

your phone not that you can use

placeholders in either the subject or

the message I'm going to use

placeholders in my message

not that I've added the placeholder 9

temp

as soon as I click out of the message

box this placeholder will be added to

the place all the mapping grid

be sure to map all the placeholders

selecting a value that this placeholder

needs to be replaced with I'm going to

select it then click apply and click

Save verify if you've setup your dream

correctly you can just click on

integrity check since none of my agents

are red everything is fine and I can run

my stream by clicking on publish to view

the live data click on live view select

your event printer and click Save

now you can see that I start coming

through and yeah you can see the email

that I've just received but the

temperature applies all that being

replaced with the temperature
</details>