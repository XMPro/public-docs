# how-to-configure-the-normalize-fields-function---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=BllrNO-j404" %}



Learn how to configure the Normalize Fields Function in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.c...
<details>
<summary>Transcript</summary>Learn how to configure the Normalize Fields Function in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.c...
while we will be doing here is look at

how to set up and configure the

normalize fields agent certain agents

have strict requirements regarding field

names in the data stream they have to be

met in order for them to function

correctly an error will occur if a field

name containing a special character is

encountered an example of such an agent

is the a script agent which uses a

different programming language this

prelude language treats spaces and some

other symbols as a command the

normalized field agent sanitizes the

field names by replacing all characters

that are not letters numbers or the

underscore symbol with the Unicode

equivalent of that symbol in this

example we will be using an event

printer agent instead of the AA script

agent to demonstrate how the normalized

field agent works how to set it up and

how to configure it I already have an

event simulator agent an event printer

agent set up and configured go to the

toolbox and search for normalize fields

you will find it under functions click

on the agent and drag it to the canvas

connect the output end point of the

event simulator agent to the input end

point of the normalized fields agent

connect the output endpoint of the

normalized field agent to the input end

point of the event printer agent click

on save

double click on your normalized fields

agent this is where you will Nobile

normally be configuring your agent

however this agent doesn't have any

configurations that need to be set

except just make sure that you're using

the correct collection

if not select another collection from

the drop-down and click apply I'm going

to close this page always make sure that

you've saved your stream

now I'm going to publish the stream in

order to run in and view the data that

is sent to the event printer agent with

that I'm going to click on the publish

button and click on live view and then

select event printer give it a second

and you'll start seeing data expand the

page and note that something some balls

have been replaced such as the opening

bracket between Tim and F
</details>