# How To Configure The IBM Maximo Listener - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=ahm_tHfvB1A" %}

Learn how to configure the IBM Maximo Listener in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>what we are going to do here is look at

how to set up and configure the ibm

maximo listener agent

what it does is it allows you to monitor

and read data from

an ibm maximo system to edit your data

stream go to the toolbox and search for

the agent

you will find it under listeners click

on the agent and drag it to your canvas

as soon as you drop it on the canvas you

will see that it will be given a default

name

to rename this agent click on the white

space and start typing

click somewhere else on the canvas and

click save

to configure this agent click on it and

click on configure

first make sure you're using the correct

collection if you'd like to change this

just select another collection from the

drop down

next you need to set your polling

interval which is the rate at which

the agent will check for new records i'm

going to leave it as the default which

is 10 seconds

the authentication section add the url

of the maximo instance that you'd like

to connect to

then add your username

then add your password

next select your authentication method

i'm going to leave it as native now you

need to select the object you'd like to

connect to

select one or more output properties

select the unique id from the list

click apply and click save

now you can publish your stream by

clicking on publish

to view the live data click on live view

select your agent and click save

to demonstrate how this agent works i've

downloaded a rest api

app called postman which will allow me

to send the post request to a specific

address as you can see i've already set

this up in the app

i've started by selecting the method as

post

then i've added my address with one

parameter called lean and i've set the

value of that to one

in the headers i've added two headers

one is called

max off and then i have a value set here

which is a combination of my username

and password that has been converted to

base64

then i have another header in here

called content type

which is set to application json

in the body i have the record that i

need to post and the type is set to raw

to send this request i'm just going to

click on send

as you can see it came back as

successful

and there you can see the request has

come through and i can see data in my

live view

you
</details>