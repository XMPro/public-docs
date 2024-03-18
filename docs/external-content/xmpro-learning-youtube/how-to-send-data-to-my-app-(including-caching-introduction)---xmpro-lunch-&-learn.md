# how-to-send-data-to-my-app-(including-caching-introduction)---xmpro-lunch-&-learn
{% embed url="https://www.youtube.com/watch?v=Mbza0AlCt6g" %}



This is a recorded version of XMPro's weekly live Lunch & Learn sessions. To join us live, sign up at https://xmpro.com/go/lunch-learn/
<details>
<summary>Transcript</summary>This is a recorded version of XMPro's weekly live Lunch & Learn sessions. To join us live, sign up at https://xmpro.com/go/lunch-learn/
hi all and welcome to another lunch and

learn

so today what we're going to go through

is how do i send data to my app

we're also going to touch on a brief

intro into caching

we'll uh we'll go through that in a

future lunch and learn as well

so today we're going to be talking

around apps and and data

so

first things first is what is it

apps have two modes where they can

essentially render data to

to the end users the one is what i would

call static which means when you design

the app it'll appear there the second is

what i would say is dynamic

so information that's going to change

information that gets calculated

information that could be from an

expression etc so static values are done

at design time

dynamic value is either provided now

there's a few mechanisms of how you can

provide it we'll touch on both of them

one is through a data stream

and the second is a connector inside the

app designer

we'll also touch on caching so when you

do caching in a data stream

it is how often and how much data should

be cached that is made available to the

app

when it is rendering

some of the concepts we're going to

touch uh example action agent that'll be

the first one with inside a data stream

the second is going to be connectors

inside the app designer

we'll also touch on briefly caching all

or per an entity

some basic requirements that you're

going to need

it's going to

require access to the app designer

access to the data stream designer and

you need a basic idea of what data is

that you're looking to to display so

what information are you looking to

present to the screen

and where do you want it to be how do

you want to access it is any filters etc

skill level for this we're still in the

beginner friendly area

it can start to go into the intermediate

area

as well

so first area is let's jump into the

actual software itself

so

before we can actually start tying data

to to an app let's go and create

ourselves a new app

we're just going to call this

lunch and learn for today

we're going to put it into

my sandbox

and we're going to keep everything else

as the default

now if i go into this actual app itself

and i try and launch it it's going to

not give me anything

it's going to be bare basics there's not

much information in here

as well

now what i can start doing is i can

start going through here and i can start

configuring information

so let's say i want to to actually

create

some additional columns

i can do that

if i want the first one to be

asset information i can just double

click and change that information there

if i now want to start bringing in um

a little bit more

like dragging a box into there

i can now go back and from layouts i'm

going to drag in a stack layer and bring

that into the other side as well so you

configure your form exactly the same way

as you would have previously

however now what you can start doing is

when you start bringing information into

the screen here

so i could very well call this asset

number

and if i go and duplicate that and i'm

just going to change the flex so that we

go from left to right

so i can see that

i can come into the asset number

and i can rename it from a static

perspective and if i go and render the

screen

you'll see as asset number will come

through so you can very quickly create

static information on a screen however

that's not very useful

most of the information you want to have

changed so you need to pass this

information through to the form

so that you can actually access it and

make it available

so we're just going to go back into the

edit mode for this particular app we'll

come back to to the app itself

so the first area of where datic is

made available to an application

is inside the data stream designer

i've got an example

here but i'll show you how we can

actually create one

so for this particular example

we are using the event simulator to

generate some data so we've got specific

data that we're interested in

we are then creating

some asset numbers we are rounding it to

make sure that when we get to the ui

side that the information is consistent

two decimals three etcetera

if you don't round here

you can still round inside the app

designer

then you start going into

the expressions on an actual data source

we'll start covering that in a in a

future session as well

we're then going to broadcast and then

we publish to an app

however what i'm going to do with this

example

is i'm going to

clone it

and we're going to configure it

for different bits and pieces

so for now what i'm going to get rid of

is the last two pieces to my data stream

it does not matter where your data is

coming from there's a lot of different

listeners of where my information coming

from to the point i made earlier

you need to have at least an idea of

what data are we trying to present on

the form

what shape should that data be and where

is it coming from do i need to join data

from different data streams etc

if i were to run this particular data

stream now

and i go into my live view

and i bring the rounding and i bring my

generate data

up

you'll see my values will come through

if i expand that

i can see the generate column and i can

see the rounding column so my data is

flowing through my particular data

stream

however it is not available

on my upside

um i can't actually view it or see it

now how i know that is i'm looking for

lunch and learn from a data stream

perspective so if i go back to the app

now

how we bind data to an app

is on the page data side of things

if i scroll all the way to the left

you'll see there is app data on the

application level

the page level allows me to use data

sources that have been defined

data sources get defined at an

application level

now do i have to remember every single

time to scroll left and go to the app

data to create them no you don't

if you've forgotten

or you haven't got that for yet you can

click the plus on the data sources side

of things

it's going to ask you for a name but

you'll see in the connection

it'll give you some options in there

however if the one you're looking for is

not available

in the section here you can actually

click the plus and it'll bring up a list

of a lot of different connections that

you can actually use as well

so how do we actually do that

if i go all the way to the left

i'm going to go and

delete these two

let's say we go and get rid of those and

they're not available

if i want to add a new data source to

this page i go to the page data and i

click the plus

so what we're doing is we're trying to

bind a data source to be able to be used

on this particular page

on the right you'll see connections we

have nothing it says no data to display

there

if i click the plus it's going to give

me some options so i'm looking for the

data stream we're going to give it a

name

and everything else we can leave as

default and we can click save

now what will happen is under the drop

down you'll see i have a data stream

that is now available

so what we've just done there is instead

of me scrolling all the way to the left

and clicking app data to add it i'm able

to add it at the page layer as well

very handy if you

haven't done it or you only get to it

halfway through the app page when you're

configuring it versus having to remember

every single time

we can now give it a

name at the top

however if i go into entity

and i search for lunch and learn i don't

get anything

nothing's available here

and the reason for that is

the only data streams that will appear

here are ones that have been configured

to make its data available to a data

stream so what do i mean by that

under action agents if you scroll all

the way to the bottom

or you can type in the search at the top

and it'll filter the list view you need

to drag on an xmpro app

and add it to your data stream

so i'm going to unpublish my data stream

and we're just going to save that so the

first thing is you need to tell

the

data stream you're going to be making

your data available

to the app designer so that's step one

step two

make sure you give it a name that is

appropriate the reason for that is when

you come into the app designer here

it's going to

register those different endpoints and

you can have multiple

so i can have one in here as an example

so let me say i have a broadcast

and

i send that to the broadcast

and my first value

comes to that x and pro and then if i

search for x

again

now we put that here

i could have the next one go to the same

you can have multiple

of these on a data stream

why would you want multiple

if your data stream is doing different

calculations on the data you may want a

certain section of that to be in a

certain area on the app you may want the

results of the calculation in another

area of the app

so there are reasons why you want to

have

duplicate

example apps on a data stream

it'll become obvious when we go into a

lunch and learn around caching

and making data available to charts why

you would have to

but just remember you can have multiple

of these

on a data stream

the second thing is

if you double click that

you need to configure it you can't just

drag it on and leave it there is

configuration that you do need to do on

the xm pro app first thing is

where is the url this will point to the

app designer url

integration key this will point to your

app designer key as well

if you scroll down

you can ignore the cache settings for

now it's going to ask you for an

identifier so what is the identifier for

this data flowing through

typically it is an asset number

um

but you have flexibility to use other

fields as a identifier as well

if i go in there i can pick asset number

it's also going to ask you what's my

primary key 9 out of ten times it'll be

an asset number as well

if i go back to the second one

and i do the same thing there

we're going to configure both of those

and i go all the way to the bottom

identifier is going to be asset number

and primary key is going to be asset

number make sure you click apply at the

top

if you don't you'll notice if i go back

to the first one it hasn't saved my

changes

very important to remember that

so we go into the first two

we're going to scroll down

we're going to fill the asset number in

and select it

make sure you click apply to persist the

changes you made and then make sure you

click save or ctrl s on your keyboard to

save the data stream

now if i go back to my

my app that i am configuring

and if i try and

close that out and i go back to the data

source side

and we select data stream and in here

we're looking for for lunch and learn

so now if i expand that

it'll show me my lunch and learn coming

in there as well

for it

so previously

it was not available here you can see i

have availability to pretty much

everything that has an end point

for all the different data points coming

through

so if i go down to my

my examples they'll appear in here as

well

however

what we forgot to do on this side is we

forgot to name them appropriately

now because we haven't named them

appropriately it's going to be quite

hard when we get to the app side to make

sure we're using the correct one

as i mentioned you can have multiple of

these on a data stream so it's good

practice to make sure you name them

appropriately

for now we're just going to say

then data to app and i'm going to leave

the other one we'll come back to this in

a future lunch alone as well make sure

we name our broadcast so that

we understand what this particular data

stream is doing

if i go back into

the

configuration for

for this

you'll see there's a caching section

here

what the caching section here is saying

what's my initial cache size

so how much data do i want to keep in

cash

and then you have a few options

the first one says replace cash what

that does is

if my cash size is 20 and i have

21 items coming through my payload by

the time it gets here it's going to drop

off the first one and add a new one at

the back and it's going to keep doing

that

as the data is coming through the data

stream and being made available

if i tell it replace cache what that

does

is any new payload that comes all the

way through to this endpoint replaces

the prior cash payload

so

if you have a record that only comes

through let's say every five minutes but

your data is flowing every minute

what will happen is if you were to set

replace cache you could end up with a

situation where in that four minute

window you might have no data displaying

on your actual app side itself as well

so replace cache will allow you to

replace everything every time but just

be aware if your data comes in at

different intervals for different asset

types as well

the other one is cash for entity

cash per entity allows me to make use of

this cash

but per

the identifier that we've got at the

bottom

if i was to select that what this is now

saying

is my cash size is going to be 20

per asset number

so if i have 10 assets and each of those

has

records coming through i can catch 20

percent so suddenly my 20 has gone up by

a factor of 10. so my cash size is going

to be 200 in that scenario

the defaults

is everything unchecked

so replace cash is unchecked and cash

for entity is unchecked as well

if i run this now and i go to live view

i can now

open up the send data to to app and we

can keep the top one

so generate data is coming from my event

simulator

send data to app is what's coming

through my endpoint here so step one

before you can get data into your app

designer is to make sure do you have an

excel pro app agent on your canvas and

have you configured it correctly

now we can go into our app designer here

and i can actually go into my data

source

and i can say we're going to connect to

some live data

and in here you'll see i have access to

a lot of different

areas for it

if i go back and i have a look at

the launch unknown

just rename that differently

here

and it's in display data so let's

unpublish that

and let's republish that

so if i go down in here to

my display data

and i scroll all the way down

i'll be able to see there is my lunch

and learn

and there are my two fields

that have been bound

this is why naming is important if you

were to leave them both as x and pro

underscore zero x and per app underscore

one x and pro up under school two

you won't know

which of those endpoints are the ones

you're looking for which of them has the

calculations you may have done which of

them has the raw telemetry data and

which of them maybe has data with a

different caching option that you want

to use for charts as an example

if you haven't named them appropriately

you're going to struggle

getting to this point

especially if you are sharing this data

stream with other users

and they are using them to consume the

data but they're not necessarily fully

across how the data stream functions

where it gets its data etc

so the first thing we want to do

is we select

the send data to the

app itself

what you'll notice it'll do is it

interrogates it and gets the primary key

now what you'll notice is i made the

entire configuration

maximized and the reason i do that is

that i can see everything on the screen

to do that

you can double click the header

or you can click the maximize option at

the top there

this is especially useful if you have a

lot of data streams to go through that

have been bound to the example app

connector

and you want to find what you're looking

for

so it's interrogated the configuration

and it's automatically brought in the

primary key

as you've configured it down the bottom

here so if i go down here remember we

set the primary key was asset number

primary key is important over here

for the data when you start doing

advanced data

manipulation and advanced data work in

the the app designer

the next thing to make sure you tick

is when you're accessing live data

make sure you tick live data updates if

you hover over the eye it'll tell you

what it actually does but the live data

updates is what enables you to get the

record constantly

it allows you to automatically update

the values without refreshing the page

there are some

connectors for instance if you're

connecting to

sql

and the options not enabled on sql you

won't get this option here

but when you're connecting to data

streams there's no reason for you not to

take this option

um it's also

one of the first things i suggest people

check when they're saying well my data

is not flowing through to my app

even though i am getting data in the

data stream first thing to check and

make sure is have you enabled live

updates um here

we're going to click save

and as soon as we've done that what

you'll notice is data sources here has a

new option underneath it

it's got the name that we've defined so

again make sure the names you're using

inside your app here

make sense

and if someone else wants to use them

and look at them make sense to them as

well

we bring in all the data fields

they're also bound to what their data

type is so you can see

their decimal strings date times etc

there is an area for you to calculate

and create expressions we'll cover that

in another lunch and learn as well

so if you're not sure what fields i'll

be made available what can i actually

view and read

just go to the page data

expand the data sources and you have

access to the information here

now what we can do is we can actually

bind this information to the

element we're looking for

again if you're looking for a data

source that's not here so let's say we

don't want to bind this to live data you

can click the plus

brings you to exactly the same place

so you do not have to go back to the

page data and click the plus here every

time to add a new data source you can do

it from within the area that you're busy

with

pull the information in

once you've done that it'll refresh the

drop down for you here

close that out and we can now select the

data source as soon as we've done that

you'll see we get a yellow border that

comes around

and if i go into the text

and i go to the appearance i can now

click the a

which is static

it then turns into a dynamic and now i

get a drop down this drop down is now

bound to that same data source so now i

can actually bind it to the asset number

field coming in

if i was to save that and i run the

you'll see the asset number now is being

passed through from the actual app

now what i can start doing is if i go

back and edit the the app

i can actually go through this

particular box and i can duplicate that

and this one here we can say is reading

number

and i can go into that field

go to its appearance

and change it to reading number as an

example

we can now save that

now what you'll notice

is the number keeps going up so the live

data

the checkbox that we selected is what is

enabling this to constantly change its

value without me having to refresh the

screen

there are areas where you get i would

say static type information coming

through

but

without taking that you would have to

refresh the screen every time to get

that information to come through

the second area where you can actually

configure it in a

an app

is if i go to the app data side

they are

specific

um

[Music]

sql

there are specific connectors that will

allow you to connect directly to data

sources as well

each of those is available

for you to connect as you need to

the primary one that gets used is the

data stream connector here

but there are other connectors that do

not require a data stream and you can

connect directly to the systems

the the only

functionality that you might lose by

doing that is the live view option

so again if i click the pencil next to

my existing

data stream here

this option might not be supported if

you connect directly to the systems of

choice

it's not all of them supported which

means if you are connecting to those

systems and you do want that data to

refresh

the the screen will need to be manually

refreshed to do that

as well

so just to recap

if we come back to

the data stream so where's the first

area that i go to to connect data to

my app

inside a data stream

what you want to do is under x and pro

agents right at the bottom you'll see

the axon pro app

that is the key that allows you to

connect it

to a app and make it available

make sure you name them appropriately

otherwise when you're configuring it on

the other side you might have some

problems trying to remember which one is

for which one

we'll go into a lot more detail on

caching options in a future lunch and

learn as well for now

you can use the the defaults

to return the data coming in

step one is done in the data stream step

two you do in the app designer side

again you can scroll all the way and at

an app data level add a new connector

or you can do it at the page level

so page level is where you're creating

an instance connecting to a specific

data stream connecting to a specific

table

um or whatever system it is that you're

connecting to

the plus will walk you through the steps

so if there's something in the

connection that you know is available

but you can't see it here click the plus

there again and it'll walk you through

that as well

once you've selected your items make

sure you remember the live data update

section

otherwise what's going to happen is your

information is going to stay static on

the screen

and you're not going to get the

information constantly refreshing itself

coming through as well

you all for attending today um

how do i bind data to to my app

most of it gets done through a

data stream using the app agent

there are ways to do it directly through

data sources in the app designer you

however will lose some functionality

there as well but it is very possible to

do that as well

thank you again for attending today's

lunch and learn hope to see on some

future ones
</details>