# Agents and Their Types - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=b5ljPmDs-0I" %}



Learn about the different agents and their types in the XMPRO Data Stream Designer.  

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
<details>
<summary>Transcript</summary>Learn about the different agents and their types in the XMPRO Data Stream Designer.  

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
welcome to another training video from

Mexico in this video we will be

discussing agents and their types agents

are basically a piece of code or logic

which gets encapsulated in Excel Pro

agent framework to become these blocks

which are configurable and reusable

among different use cases we provide a

library of agents which is extensible

and our users have access to the

framework that they can use to create

their own agents and add them to the

library here as you can see agents are

categorized into different categories

there are some fundamental categories

for agents and then there are some which

are derived from them

so I'll go through all of them one by

one so usually a stream starts with a

listener a listener is an agent which

doesn't have any input endpoint it would

always only have an output and that is

primarily responsible to talk to third

party systems or outside and the system

here and fetch new data as it up as it

becomes available

edan can be agents can be of two types

one is a polling agent which basically

has a polling interval on which can be

let's say five seconds ten seconds the

user is allowed to configure that and

that polling interval is what if he uses

to ping its data source or the third

party system to ask for new data so for

example a sequel listener and would ask

the database for new records that may

have become available in last 10 seconds

and then it would push them down on the

string to the next agent the other type

of listeners is the push base where they

don't have any polling mechanism but

they just subscribe to an endpoint and

as soon as something is published on

that endpoint they receive it and they

pass it down the line over here an

example would be an MQTT listener for

example which subscribes to an MQTT

broker

soon as it receives a data point it just

sends it down to the next agent next

category which is very similar to the

listeners is of context providers

context providers also do not have any

input endpoint hence they're usually

also format the start of your stream how

they are different to listeners is that

context providers work with slow

changing for context or reference data

rather than live data which listeners

are listening for context providers just

look at a reference data source cache

them in memory and whenever live data

which is coming at a speed comes through

they are able to provide that context

wire join or some other way to those

records example would be lets say you

have a device which is sending

temperature or a pressure value it

wouldn't be sending its make model when

was last serviced its location etc

though the things which are not changing

so it would only be sending live data

which are the things which mostly

changed as you would receive that

deference better from your context

providers you will do a join on let's

say a device ID and that way you will be

able to add context to your data next we

have transformations transformation is

basically are always found in the middle

of your stream they are required to

change or transform the data the key

difference here is they would rarely or

most probably never be talking to an

outside system there would always be

internal in memory agents which would

receive data change its shape or form

based on how you have configured them

and then output them alone for example

there is a Dalek and we region

transformation what it would do is it

would allow you to change a data type of

a certain attributes for example you may

want to change a string to a number or

vice-versa then I'll jump on to action

action agents are usually found towards

the end of your data stream they are

your call to actions there again agents

which talk to third party systems

outside the this environment and that is

where you would mostly krigger a work

order or or send a notification etc

action agents usually have an input and

an output endpoint where they can

perform the action they were supposed to

and then they would simply pass the same

data point out on their output so that

if you want to create a pipeline or line

up multiple action agents you can do

that and take multiple call to actions

in one for the same data point then if

we come back and we have a category for

AI n machine learning where you will

find agents which are related to machine

learning algorithms like binary

classification anomaly detection etc so

you can use those if you want to call a

model or get a prediction for your data

set next we also have functions which

are basically agents which call some

mathematical function like Fourier

transform or any signal filtering that

you may have to do lastly we have

recommendations these are action agents

which classify and the recommendation

category basically these are the ones

which you use to integrate to app

designer where you can trigger some

recommendations or resolve them as you

may like so that was a brief explanation

of agents and there are different types

thank you so much for watching
</details>