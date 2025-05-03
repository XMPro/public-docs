# How To Configure The Anomaly Detection Agent - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=fSGifWBjCw4" %}

Learn how to configure the Anomaly Detection Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>when we are going to do here is look at

how the normally detection agent works

and how to set it up this agent is a

deep learning a script based

implementation of the anomaly detection

model I have already set up and

configured a CSV listener agent double

read the data we want to join from a CSV

file now to add the anomaly detection

agent go to the toolbox and search for

anomaly detection you will find it under

iron machine-learning click on the agent

and drag it to the canvas connect the

output end point of the csv agent to the

input end point of the anomaly detection

agent note that the default name has

been given to this agent to rename this

agent click on the white space and start

typing click somewhere else on the

canvas and click save' to configure this

agent click on it and click on configure

first make sure you using the creek

election if you want to change this

select another collection from the

dropdown they are three anomalies that

this item can be trendy to take the

first being window change reverse

direction like we can see in the first

example the downward trend or the second

half would be reported which is the last

four digits the specific data point

which will be reported depends on

certain settings that you are going to

say the second anomaly that can be

detected or sudden spikes or dips in the

data for example if we look at the

second example we can see that the first

I and the last two would be considered

as spikes of opposing value in the

training session select the learning

other home that you'd like to use

please note that ID stands for

independent identically distributed and

SSI stands for single spectrum analysis

ID and SSI are the names of the

algorithms that can be applied to the

normal is mentioned earlier then upload

your training file

if the has either checkbox is selected

the first row in this file will be used

to determine the number and names of the

fields if this is unselected the fields

in the file will be automatically

generated names

then select your separator character

there's three options available comma

semicolon and tab this is the character

that separates the fields and flower

please double check the file to make

sure that this is correct otherwise

difficult attract errors might be caused

the next value you need to provide is

the input field this is the name of the

field and the training file that

contains the initial training values

that needs to be provided to the agent

the values in this field needs to have a

data type of double then select your

input map this is the field in the data

stream that will be checked for

anomalous readings this field also needs

to contain values that have a data type

of double Advanced Options will change

based on the select algorithm I'm just

going to change the learning algorithm

to a spike algorithm if we look in the

Advanced Options sensitivity influence

our response of the algorithm is the

changes in the map value each stream

object will not actually need to be

tuned individually according to the

users need the value history only

appears for spike algorithms often spike

is reported the algorithm will allow

this number of records to pause without

reporting and other anomaly to give time

for the value to settle for instance if

the p value length is set to 5 and a

spike is detected that lasts for 3 data

points before snapping back to normal

only the initial spike will be reported

higher if the p value is set to 3 the

second spike downwards would also be

considered anomalous spike Direction can

also be set which will make the agent

look for sudden changes in the given

direction I'm going to change this to

change point

let's look at the Advanced Options again

as you can see the options have changed

a change history only appears for change

points algorithms and influences the

length required for an emerging string

before the change will be reported if

you want repeatable results incident

integer into the deterministic seed

otherwise a random seed will be chosen

every time the agent starts click on the

plane click save to run your stream

click on publish to view the live data

click on live view select anomaly

detection agent and click Save give it a

second for the data to start coming

through

you can expand the page by clicking on

maximize the agent will output once for

every event passing through the original

event plus some new fields alert which

is this column here is a double but only

shows one zero

describing if the reading is considered

anomalous or not score which is the

column here is the algorithms initial

score for the record the value which is

the field here and martingale which is

the column here have to do with the

internal calculations determining if an

alert is anomalous or not and can

usually be ignored
</details>