# how-to-configure-the-rest-api-context-provider---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=lrhxz1oJpL8" %}



Learn how to configure the REST API Context Provider in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.c...
<details>
<summary>Transcript</summary>Learn how to configure the REST API Context Provider in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.c...
we're going to do here is look at how to

set up and configure the rest api

contacts provider but this agent does is

it allows you to get static or reference

data using restful api to add this to

your data stream go to the tool box and

search for the agent you'll find it on a

context providers click on the agent and

drag it to your canvas next you'll see

that a default name has been given to it

you rename this agent click on the white

space and start typing

clicks a mouse on the canvas and click

Save to configure this agent click on it

and click on configure

first make sure you using the correct

collection if you'd like to change this

just select another collection from the

drop-down next you need to set your

polling interval because this agent is a

contacts provider it will get all the

data it needs and stored in memory if I

leave this as 10 seconds that means that

the cache will be refreshed every 10

seconds next in the service detail

section at the URL that you need to

connect to then you need to upload a

JSON metadata file this file needs to

conform to a specific schema

if the URL that you're connecting to

requires authentication select the user

authentication box and specify your

username and password this URL doesn't

require me to add a username and

password so I'm going to deselect this

then select the operation you would like

to perform I'd like to get the weather

by city then select your result entity

in our case that will be weather in the

input mapping section you need to make

sure that all the parameters that you

need are added in here you can add more

parameters by clicking on the plus and

adding a new row two parameters have

already been added for us which is an

app ID and the city so now I need to add

my app ID then I need to specify my city

I want to get weather data for London

click apply and click Save to run your

stream click on publish to view the live

data click on live view select your

agent and click Save and give it a

second

then you can see data starts coming

through

to expand the page click on maximize
</details>