# Error Endpoints - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=KWlKnqoWfuU" %}



Learn about error endpoints in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if you want to...
<details>
<summary>Transcript</summary>Learn about error endpoints in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if you want to...
welcome to another training video from

XM pro in this video we will be looking

at the error endpoints and how to use

them interesting designer so you would

notice when you drag certain agents onto

the canvas that they sometimes have this

red end point at the end that is what is

called an error endpoint what it means

is that when data flows from one agent

to the other every agent is supposed to

process each data point and then pass it

forward so that other agents can perform

their logic but in an odd scenario if

that Aden fails to process a certain

data point it will not appear on the

green regular endpoint it would then

appear on the red endpoint along with

the reason why it failed for example

just to demonstrate I can put in an even

printer here and I will intentionally

make this fail and come over here and we

can then view what happens so let me

save and publish this use case if I go

to live view and say I want to see the

even printer we should soon see an error

happening now if I maximize the screen

you would see that on that error in

point I received the agent ID on which

the error happened the time stamp and

basically telling me the time when it

happened some more information on

exactly where it happened and what was

the error message in this case as you

can see I initially made it violated

violate the find Ricky lastly it also

sent me the exact data point which

failed to listen publish dead stream and

now look at a more useful way of

handling errors so it is quite possible

that

once I've created the stream I want to

be notified when an error happens while

an agent is processing I'm so that I can

then go in and correct those errors so I

can add for example an email agent and I

can map it to the red end point and that

way when an error happens I can

configure this agent to send me an email

now on top of this you would notice that

I may have error endpoints at multiple

agents of my stream for example I may

have more than two let's say I have I

have another agent here who just goes to

run some recommendations and I'm gonna

handle all the exceptions or errors

happening and in one go so what I can do

is I can collect all the errors using a

union somewhere at the end of one stream

and basically route them all to the flow

that I want to run when there happens

which is I want to send an email so you

can see I'm routing all my errors down

to this Union which will then send out

an email and I will receive the exact

agent ID which goes there along with all

the other details so these are the air

endpoints and that's how you use them in

their stream designer thank you so much

for watching
</details>