# XMPro Case Management Example
{% embed url="https://www.youtube.com/watch?v=K9fB6isunAM" %}



XMPro iBOS Case Management example demonstrates how XMPro event-based approach address case management. XMPro iBPMS is a Business Operations Platform that supports both case management and...
<details>
<summary>Transcript</summary>XMPro iBOS Case Management example demonstrates how XMPro event-based approach address case management. XMPro iBPMS is a Business Operations Platform that supports both case management and...
this is a brief example of a case-based

bid management process

this is often referred to as an

unstructured process as the flow is not

really defined upfront and the next step

will emerge as you complete the current

one

it uses xm pro's unique event-based

architecture and before we look at a

process example let's have a quick look

at what the process model behind it

looks like so

this is the

example design environment and it's used

by business champions and process

analysts to create either workflows or

event based processes and in this

example we will focus on the bid

management process which is an

event-based or case-based

process so if i

just double click on the market and sell

products and services i will look at

opportunity management as you can see

there's versioning inside this but what

is what is

evident from this model is that

these are independent events that can

occur and that is the event-based

architecture if i wanted to do a

workflow i could draw arrows between

this and that will enforce the workflow

but from a case based or unstructured

point of view

a typical bid process tends to the next

step will emerge as you do the current

one so what we don't want to do is

enforce what the flows are we will use

business rules to set up

guard rails and we'll touch on that as

we step through the example so let's go

back to the example itself

this is the example

end user front-end so this is one of

them i'm just going to log in as

keith

in here

this is the web-based

front end there's also outlook

salesforce

and

sharepoint and also mobile so any

process that you see here is

automatically rendered you don't have to

do anything else to get it to render as

a mobile process

as a mobile process or mobile user

interface what you'll see from this and

what makes case based processes unique

is that those are all those independent

tasks so these are some of them so some

of the ones that you see here we've

actually allocated to do um to

do this activity and i can choose each

one of these they are independent and

they're not they are not workflowed to

this one at the back later on towards

the end of the example i will show you

how i dynamically add another activity

to this

so let's look at this example

the first thing i'm going to do is to

read some data from an external data

source and in this instance i'm using

salesforce so it uses the xm pro connect

the the xm pro connector

integra and it goes off and brings

information back from the cloud-based

sales force in this example so what

we'll do it'll read some information off

there

and bring back some of the crm

information now the same way that we

read we can write back

from this case point of view

the one thing with with

unstructured processes as you can see

here is that they still not uncontrolled

it's really important to understand that

unstructured doesn't mean uncontrolled

from a business rules point of view we

can still put up guard rails to make

sure that certain things happen

with inside the compliance requirements

of our business so in this example uh

we will

if it's a new customer and the

and that's a new target segment and it's

a new technology and the opportunity

value exceeds a certain number there's a

business rule that look at any

combination of this

and in this instance say this is a

million dollar deal or opportunity what

will happen you'll see at the moment

it's optional to send it to a bid review

board as soon as i put the value in

there

it will then make it compulsory so it

doesn't once again it doesn't dictate

when the bit review board will happen

but what it does require is that there's

a better view board that's going to

look at this because it is a new

technology it is quite a significant

deal and it's a new customer that we

haven't dealt with before so as you can

see you can still use business rules to

set up

the guard rails for compliance to work

with in this some of the other things

that we can do at this point in time

is

attach documentation

we can set up questions and all of this

we can once again update back to

salesforce

in this example

if you're using another crm system it

would then write it back to the other

crm system exam connect is covered in a

different

video in terms of how we handle the

and how we set up business entities for

that

one last item i'd like to cover on this

before we step onto the next step in

this in this example is process goals so

because because i have all these

options down here we need to provide

people with some decision support to be

able to make the right decision around

what do i want to do next so some of the

things if there were certain other

conditions here we would

remove some of the

these buttons dynamically and only for

example leave legal or credit check

but in this instance we can once again

bring in information from the financial

system we can bring in information from

the crm system and look at

some of and and put that on the

dashboard

uh for business users to and to help

them with better decision support for

this

so in this instance uh keith

read something in the paper or we know

something about this organization and

what it'd like to do is to send it off

for a credit check at this point in time

if it was a different scenario or

different requirements you may have you

may have chosen to send it off to a

margin approval so as you can see these

are dynamic so in this instance example

will be that he sends it for a credit

check i'm just going to log in as i

as

two or three steps down the process i'm

going to log in as time

and

i'm just going to do to go to his to-do

list

and in that to-do list under market and

sell products and services now there's

notification and escalation so it'll

automatically send a notification

to him via email or sms

and if there's no response the normal

escalation processes will happen but in

this instance

let's look at that one that came through

from

from keith that was originated uh of

from keith so if we look at the history

just to see how it came to us so it was

initially done by keith as you can see

it was a form based that he completed it

then

and he sent it on for a credit check

it came to john and i

this icon here depicts that john

actually

uh wanted to know some more information

and he entered into a discussion so he

clicked on the discussion there and if

we quickly look at the discussion

history

you can see that there's some

unstructured discussions happening

inside this so

john went back to keith and say is this

the same opportunity as we looked at

last month keith yes but it was

re-issued as a new project and then john

sure will work on this so you can see

the collaboration trail is contained

within the side the case trail or the

process trail so this is a

a live audit trail of the information

and it's not only the forms based

information that is captured in here but

also the unstructured conversations that

happened at the you'll also see there's

an

add-on task or unstructured

task

that

term initiated now the example of that

would be that looking at this there's

certain information and i may realize

that

the crm system is not updated with all

the right information for express

logistics so i may just send a addock

task to someone and i can send a task to

so i can just say

please review and i'm not going to go

through the whole example here but i can

say please review

crm

info

for this

client

and i can

i can upload uh attachments uh

screen samples i can send it on to

someone and i can say it needs to go to

ted to do something due dates the

important thing is if i link it to this

task it will then appear inside this

order trial as you saw the example if i

don't link it then it just puts a new

task on someone's to-do list and it's

not linked into the history as we have

in this example over here where you can

see it's actually currently linked into

so that gives you the ability to handle

events that is not even defined on here

but that do require action immediate

action from someone to do

so looking at the rest of this

screen you can see we've embedded some

more analytics inside that

looking at documents that were

associated now this one just has one

example but as you step through the

process and at any time at any event at

any step in the process by any diff by

any specific user you can you can see

all the

documents that were associated to this

process it creates a single view from a

case file perspective you can even

preview documents in here so i can look

at that document

and it'll download it from wherever the

repository in this example

it's a sharepoint uh it can be

in a xmpro file based solution or

it can be sharepoint or

any one of the document management

systems

out there

it's taking a few seconds to load off

the server

and the cloud

so there you can see there's the preview

of the document itself

once again the process goals you can add

additional so in the first step it

didn't have the actual versus budget it

just showed the budget and now it shows

actual to this manager because managers

got a slightly different view on things

the last thing i'd like to cover on here

is the

best next action now this is a simple

best next action but this is really

trying to help them with decision

support once again there's a number of

things that need to

that they have options to choose from

and in this instance we will look at the

previous history and the similar

circumstances and based on that it

advises that a legal review be done

these best next actions there's actually

a separate video on this

with a number of different examples

using external web services using policy

guides all sorts of things like that to

show you how

or to advise the what the best next

action is key thing for these kinds of

processes you need is that you want to

provide decision support uh based on

these so that is really just

an example of how you would step through

a

a

case-based or unstructured process where

the events in the back end are not

workflowed into it and you can handle

a large number of potential events on

as the process emerges or as it steps

through the process i'd just like to

make one change and show you example of

the dynamic capability of and i'm just

going to go back as keith

as you'll recall on his first screen

i just get the password right

as you'll recall on the first screen

keith had five different options on here

if i go back to the design environment

in the back end

and

looking at the properties of that what i

can do is under dynamic allocation

if i for example want to be able to add

a

finance review in there or

and what i'll do is i'll just call this

finance

review

i save that

and when i go back to the front end if i

reset this screen

you will see that finance review now

appear as an option i didn't have to do

any manual wiring in or i didn't have to

draw any flow diagrams i didn't have to

do anything to get

that option onto the screen so that's

really how easy it is to

add new activities or events on the fly

thank you for watching this video and

please come back to watch some of the

others showing some of the other

functionality inside xmpro thank you for

your time

you
</details>