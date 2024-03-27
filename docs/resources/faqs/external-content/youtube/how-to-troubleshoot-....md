# How To Troubleshoot a Use Case - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=Yh2CMt78LZQ" %}



Learn how to troubleshoot a use case in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if you...
<details>
<summary>Transcript</summary>Learn how to troubleshoot a use case in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if you...
welcome to another training video from

ex and grow in this video we will look

at how to troubleshoot a use case in

data streaming design so I have a very

simple use case here I'm just simulating

some data and then I've configured a

sequel writer where I want to write that

data into a sequel table there there is

a chance that something may not be

working as I expected and I may have to

find out more information around the why

it is not behaving as I wanted it to

there are a few options available to you

which you can use to couple suit your

use case so if I publish this use case

the first thing I can do if I have an

indication that it is not working

properly is to try it and look into the

live view so the live view gives you

this opportunity to look at each one of

these agents and see if one of them is

not producing data in this case as you

can see the data is being produced by

the top agent but it is somehow not

being output outputted by the the

database agent here as that one is empty

so that tells me that something is going

wrong in this agent now in order to find

that out once we have established the

the point where the problem is what we

can do is we can look at this error

endpoint which was explained in the

video on air endpoints so I'll quickly

just put an even printer here even

printer is an agent which doesn't do

anything with the data except that it

gives you sort of a point where you can

take a snapshot of the data in your

string of what's passing through so now

if I publish this and I go to the live

view and I look at my Eamon printer I

might get some error messages as you can

see over there so I I can see what is

going wrong with my agent and it is

telling me why it's Aaron

point that the priority is being

violated and said can't insert those

records and that's why it is failing to

process them and each point is also

being shown over here so another

scenario might be that you are trying to

troubleshoot your use case but you see

no data at all none of the aliens are

showing any data in live view however

your use case is published well one

thing we can try is that we go to the

collection where this music is supposed

to be running and look at the stream

host where there will be some logs and

they can give us an indication why

something might not be working as you

can see over here I have an error

message saying that the stream was

actually failed to start the stream and

the reason was that the object which is

supposed to log to the database faulted

on startup because it could not find a

certain table in the database which it

was supposed to write to hence the

stream did not start at all and you can

see that in the logs over here so that

gives you further information about why

you may not be seeing any data in your

use case along with that you can also

see that anything that ended up on the

air endpoint that we looked at before

also ends up over here in your logs and

you can and you can go through them and

the last scenario could be that your

stream of is just not online at all and

in that case what you may have to do is

look at where the stream host was

installed and in the installation folder

you will see that there will be a folder

called blogs you can go in there and

look for those logs directly on the file

system and try to find out why that

string was it's not starting or not

connecting to the server maybe there is

some connectivity issue

a key or the password has expired so

those are some of the options you can

use to troubleshoot your use case thank

you so much for watching
</details>