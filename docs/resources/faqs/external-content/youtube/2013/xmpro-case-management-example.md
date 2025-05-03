# XMPro Case Management Example
{% embed url="https://www.youtube.com/watch?v=K9fB6isunAM" %}

XMPro iBOS Case Management example demonstrates how XMPro event-based approach address case management. XMPro iBPMS is a Business Operations Platform that supports both case management and workflow in a single tool.

This Bid Management example is a sales process with integration to Salesforce that demonstrates the typical "unstructured" approach of sales processes. These processes are nearly impossible to draw in a flow diagram and the next step emerges as the process evolves.

The video demonstrates the adaptive nature of XMPro and how to add additional steps or events without any flow lines or coding.

Download the XMPro iBOS Maturity Model here : [http://xmpro.com/info/ibosmodel/](http://xmpro.com/info/ibosmodel/)
<details>
<summary>Transcript</summary>this is a brief example of a case-based

bid management process this is often

referred to as an unstructured process

as the flow is not really defined up

front and the next step will emerge as

you complete the current one it uses XM

Pro's unique event-based architecture

and before we look at a process example

let's have a quick look at what the

process model behind it looks like so

this is the XM Pro Design environment

and in it used by business Champions and

process analysts to create either

workflows or event based processes and

in this example we will focus on the bid

management process which is an event

based or

case-based uh process so if I just

double click on the market and sub

products and services I will look at

Opportunity management as you can see

there's versioning inside this but what

is what is um evident from this model is

that uh these are independent events

that can occur and that is the event

based architecture if I wanted to do a

workflow I could draw arrows between

this and that will enforce a workflow

but from a casebase or unstructured

point of view um a typical bid process

tends to The Next Step will emerge as

you do the current one so what we don't

want to do is enforce what the flows are

we will use business rules to set up uh

guard rails and we'll touch on that as

we step through the example so let's go

back to the example itself

this is the exm pro um end user front

end so this is one of them uh I'm just

going to log in as

Keith in

here uh this is the webbased front end

there's also Outlook

Salesforce and um SharePoint and also

mobile so any process that you see here

is automatically rendered you don't have

to do anything else to get it to render

as a mobile process as a mobile process

or mobile user interface what you'll see

from this and what makes case base

processes unique is that those are all

those independent tasks so these are

some of them so some of the ones that

you see here we've actually allocated to

do um to to to this activity and I can

choose each one of these they are

independent and they're not they are not

workflow to this one at the back later

on towards the end of the example I will

show you how I dynamically add another

activity to this

so let's look at this example uh the

first thing I'm going to do is to read

some data from an external data uh

source and in this instance I'm using

Salesforce so it uses the XM Pro connect

the the XM Pro connector interrogate and

it goes off and brings information back

from the cloud-based um Salesforce in

this example so what it'll do it'll read

some information off there and bring

back some of the CRM information now the

same with that we read we can write back

from this case point of view um the one

thing with with unstructured processes

as you can see here is that they're

still not uncontrolled it's really

important to understand that

unstructured doesn't mean uncontrolled

from a business rules point of view we

can still put up guard rails to make

sure that certain things happen um with

inside the compliance requirements of

our business so in this example uh we

will look if it's a new customer and the

uh and it's a new Target segment and

it's a new technology and the

opportunity value exceeds a certain

number there's a business rule that look

at any combination of this um and in

this instance say this is a million doll

deal or opportunity what will happen

you'll see at the moment it's optional

to send it to a bid review board as soon

as I put the value in there it will then

make it compulsory so it doesn't once

again it doesn't dictate when the bit

review board will happen but what it

does require is that there's a bid

review board that's going to um look at

this because it is a new technology it

is quite a significant deal and it's a

new customer that we haven't dealt with

before so as you can see you can still

use business rules to set up uh the

guard rails for compliance to work with

in this some of the other things that we

can do at this point in time is um

attach

documentation uh we can set up questions

and all of this we can once again update

back to Salesforce in this example um if

you're using another CRM system uh it

would then write it back to the other

CRM system XM connect is covered in a

different uh video in terms of how we

handle integration and how we set up

business entities for that uh one last

item I'd like to cover on this before we

step on to the next step in this in this

example is process goals so because

because I have all these options down

here we need to provide people with some

decision support to able to make the

right decision around what do I want to

do next so some of the things if there

were certain other conditions here we

would uh remove some of the these

buttons dynamically and only for example

leave legal or credit check um but in

this instance uh we can once again bring

in information from the financial system

we can bring in information from the CRM

system and look at uh some of and and

put that on the dashboard uh for

business users to and to help them with

better decision support for this so in

this instance uh Keith uh read something

in the paper or he know something about

this organization and what i''d like to

do is to send it off for a credit check

at this point in time uh if it was a

different scenario or different

requirements he might he may have chosen

to send it off to a margin approval so

as you can see these are Dynamic so in

this instance the example will be that

he he sends it for a credit check I'm

just going to log in as a as uh two or

three steps down the process and I'm

going to log in as

Tim

and I'm just going to do to go to his

to-do list and in that to-do list under

market and sell product and services now

there's notification and escalation so

it'll automatically send a notification

to him via email or SMS um and if

there's no response the normal

escalation processes will happen but in

this instance uh let's look at that one

that came through from

um from Keith that was originated uh

from Keith so if we look at the history

just to see how it came to us so it was

initially done by Keith as you can see

it was a form base that he completed it

then um and he sent it on for a credit

check uh it came to John and this icon

here depicts that John actually uh

wanted to know some more information and

he entered into a discussion so he

clicked on the discussion there and if

we quickly look at the discussion

history you can see that there's some

unstructured discussions happening

inside this so um John went back to

Keith and say is this the same

opportunity as we looked at last month

Keith yes but it was re reissued as a

new project and then John sure will work

on this so you can see the collaboration

Trail is contained within the side the

case traal or the process Trail so this

is a a live order traal of the

information and it's not only the forms

based information that is captured in

here but also the unstructured

conversations that happened at there

you'll also see there's an un adoc task

or unstructured task um that um them

initiated now the the example of that

would be that looking at this there's

certain information and I may realize

that um the CRM system is not updated

with all the right information for

Express Logistics

so I might just send a adoc task to

someone and I can send a task to so I

can just say please review and um I'm

not going to go through the whole

example here but I can say please review

um um CRM

info for this

client uh and I

can I can upload uh attachments uh

screen samples I can send it on to

someone and I can say it needs to go to

Ted to do something due dates the

important thing is if I link it to this

task it will then appear inside this

order Trail as you saw the example if I

don't link it then it just puts a new

task on someone's to-do list and it's

not linked into the history as we have

in this example over here where you can

see it's actually currently linked into

so that gives you the ability to handle

events that is not even defined on here

but that do requ require action

immediate action from someone to do so

looking at the rest of this um screen

you can see we've embedded some more

analytics inside

that um looking at documents that were

associated now this one just has one

example but as you step through the

process and at any at any event at any

step in the process by any diff by any

specific user you can you can see all

the um documents that were associated to

this process it creates a single View

from a case File perspective you can

even preview documents in here so I can

look at that document and it'll download

it from wherever the repository in this

example um uh it's a SharePoint uh it

can be um in a exm Pro File based

solution or um it can be SharePoint or

any one of the document Management

Systems uh out there it's just taking a

few seconds to load off the server uh

and the cloud so there you can see

there's the preview of the document

itself once again the process goals you

can add additional so in the first step

it didn't have the actual versus budget

it just showed the budget and now it

shows actual to this manager because

manager's got a a slightly different

view on things um

and the last thing I'd like to cover on

here is the best next action now this is

a simple best next action um but this is

really trying to help them with decision

support once again there's a number of

things that need to that they have

options to choose from and in this

instance we will look at the previous

history under similar circumstances and

based on that it advises that a legal

review be done this these best next

actions there there's actually a

separate video on this um with a number

of different examples um using external

web services using policy guides all

sorts of things like that to show you

how um or to advise the what the best

next action is key thing for these kinds

of processes you is that you want to

provide decision support uh based on

these that is really just um an example

of how you would step through a a um a

case based or unstructured process where

the events in the back end are not

workflow into it and you can handle a

large number of potential events on a um

as the process emerges or as it steps

through the process I would just like to

make one change and show you example of

the dynamic capability of and I'm just

going to go back as

Keith as you'll recall on his first

screen I just get the password

right as you'll recall on the first

screen Keith had five different options

on here if I go back to to the design

environment in the back endend and um

looking at the properties of that what I

can do is under Dynamic

allocation if I for example want to be

able to add a finance review in there or

um and what I'll do is I'll just call

this

Finance

review I save

that and when I go back to the front end

if I reset this

screen you will see that Finance review

now appear as an option I didn't have to

do any manual wiring in or I didn't have

to draw any flow diagrams I didn't have

to do anything to get um that option

onto the screen so that's really how

easy it is

to add new activities or events on the

Fly thank you for watching this video

and uh please come back to watch some of

the others showing some of the other

functionality inside exm pro thank you

for your time
</details>