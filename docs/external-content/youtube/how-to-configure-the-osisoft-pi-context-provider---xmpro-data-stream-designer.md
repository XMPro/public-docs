# how-to-configure-the-osisoft-pi-context-provider---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=qVxx3beX3fY" %}



Learn how to configure the OSIsoft PI Context Provider in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro...
<details>
<summary>Transcript</summary>Learn how to configure the OSIsoft PI Context Provider in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro...
but we are going to do here is look at

how to set up and configure the oSIsoft

by context provided what this agent does

is it provides context of reference data

originating from an oSIsoft PI system to

the rest of the data stream what I want

to do now is to add this edge into my

canvas so I'm going to go to the toolbox

and search for it you will find it under

context providers to add it to your data

stream click on the edges and drag it to

the canvas as soon as you drop it you

will see that a default name will be

given to it you rename this agent click

on the white space and start typing

click somewhere else on the canvas and

click Save

to configure this agent click on it and

click on configure

first make sure you using the create

collection if not select another one

from the drop-down then you need to set

your polling interval because this agent

is a context provider it will get all

the data it needs and store it in memory

if you set your polling interval to 10

it will refresh the cache every 10

seconds but this example I'm just going

to leave it as default which is 10

seconds in the identification section

add the Web API URL you'd like to

connect to then add your username then

add your password

in the configuration section select the

server you'd like to connect to then

select the database where the data can

be found then select the template you'd

like to use and the elements that you'd

like to include I'm going to select

Houston and Little Rock lastly select

the attributes you'd like to include

click apply and click Save

to run your data stream click on publish

to view the live data click on live view

select your agent and click Save and

give it a few seconds to expand the page

click on maximize

you
</details>