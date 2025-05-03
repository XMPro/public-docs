# How To Configure The IBM Maximo Context Provider - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=oSjq2DDZBnc" %}

Learn how to configure the IBM Maximo Context Provider in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>but we're going to do here is look at

how to set up and configure the IBM

Maxima context provider what this isin

does is it allows you to read data from

an IBM axle system and provide that

context to the rest of your data stream

what I want to do now is to add this

agent to my canvas so I'm going to go to

the toolbox and search for it you'll

find it under contexts providers to add

this item to your data stream click on

it and drag it to the canvas as soon as

you drop it you will see that a default

name will be given to it to rename this

agent click on the white space and start

typing click somewhere else on the

canvas and click Save to configure this

agent double click on it first make sure

you're using the correct collection if

you'd like to change this just select

another one from the drop-down then you

need to set the polling interval I'm

going to leave it as 10 because this

agent is a context provider it will get

all the data it needs and store it in

memory if the polling interval is set to

10 it means that the cache will be

refreshed every 10 seconds in this

indication section at the URL of the

maximal instance you'd like to connect

to at your username and your password

then select youth indication method I'm

going to leave it as native then select

the maximum object you'd like to get the

context from select one or more

properties that you would like to

include in the output I want to include

asset ID asset numb and description then

you can add any filter criteria that you

would like this is just a statement that

determines which records are led through

given a certain criteria for example I

only want records that have an asset ID

over 500 closely set the maximum number

of records returned for example I want

this to be 10 click apply click Save to

run your data stream click on publish to

view the live title click on live view

select your agent and click Save

and give it a second and you will see

that start coming through as you can see

anything records are returned at a time

to expand this page click on maximize
</details>