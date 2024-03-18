# how-to-configure-the-csv-context-provider---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=eD9TzKOPUnc" %}



Learn how to configure the CSV Context Provider in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
<details>
<summary>Transcript</summary>Learn how to configure the CSV Context Provider in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
we're going to do here is look at how to

set up and configure the CSV reader

agent the function of this agent is to

read data from a CSV file I've set up a

file listener which will monitor the

directory for CSV files once it picks up

a new file I want to read this file you

start setting up your CSV Reader agent

go to the toolbox and search for CSV

you'll find this agent on the functions

click on the agent and drag it to the

canvas to add it to your data stream

note that a default name will be given

to it as soon as you drop it on your

canvas do you name this agent just click

on the white space and start typing

click somewhere else on canvas connect

the output end point of the first item

to the input end point of the second

click Save to configure your CSV agent

double click on it

first make sure using the correct

collection if you'd like to use a

different collection select another

collection from the drop-down then the

find listener has a number of attributes

in its palette that it passes on to the

next agent in the file field I want to

provide the part of the file so I'm just

going to select that from the drop-down

then you need to provide the file path

name if you leave this blank

the constant file path will be inserted

into this field next you have the option

of providing a file definition this will

make it a lot easier for you if you

don't want to manually provide the

definition if you select the check box

you'll be given the option of uploading

a file which is just required to have

the headings of the CSV file that you

read

I'm just going to upload this file as

you can see the headings have been added

in the CSV definition all I have to do

now is to make sure that I all have the

correct data type

next you need to specify whether your

CSV file that you're going to read has a

header or not if he does not have a

header it will assign the headers to the

columns based on the order in your CSV

definition grid specify the delimiter

that you're using in our case it's just

going to be a comma a queue encoding

that you're going to be using and since

some CSV files use double quotes some

seriously files use single quotes just

specify this here if your CSV file is

using a single quote just change this

I'm just going to leave it as is and

click apply and then click Save if at

any time you want to verify the stream

has been configured correctly just click

on integrity check if none of your

agents are I like in red it means

everything is fine and you can go ahead

and run your stream by clicking on

publish to view the live data click on

live view I'm going to select both these

agents and click Save this is the

directory I'm currently monitoring using

my father's in that agent so I'm just

going to add a file in here which I want

to read using my CSV agent

as you can see the foul listener agent

has picked up the foul and move it to

the archive folder the CSV reader agent

has read the file
</details>