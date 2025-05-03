# How To Configure The SQL Server Action Agent - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=n0hglX8R6LM" %}

Learn how to configure the SQL Server Action Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>but we are going to do here is look at

how to set up and configure the sequel

server action agent this agent allows

full stream data to be written to a

sequel server database I already have an

event some like the agent set up and

configured which will simulate sensor

readings such as temperature vibration

and load wait I also have an event

printer set up and configured which will

help us see what the outlet looks like

now I want to set up and configure my

sequel server action agent go to the

tool box and search for sequel server

you will find it under action agents

if you're going to agent and drag it to

the canvas make the output in front of

the events another agent to the input

input of the sequel server agent connect

the above in front of the sequel server

agent to the input in front of the event

printer agent note that a default name

has been given to the sequel server

agent to rename this agent click on the

white space and start typing

you

pick something else in the canvas and

click Save double clicking a sequel

server agent

first make sure you're using the great

collection if not select another

collection from the drop-down next in

the service section specify the name of

your Segal survey instance then add your

user name

if you need to use sequel server

vindication click on the checkbox and

specify your password

you

if you leave this checkbox unchecked

witnesseth indication will be used in

the database section select the database

from the job done that you'd like to

connect to then you can either leave the

agent create a new table in the database

you've selected and write the data to

that table or select a table from the

drop-down I want to create a new table

so I'm going to select the checkbox and

give my new table a name

click apply and click Save

now I want to run my swim so I'm going

to click on publish to view the live

data click on live view and select event

printer and click Save

give it a few seconds that is as you see

here is all being written to the sequel

server database that you've specified
</details>