# How To Bind Data To A Chart and Get It Working As Expected - XMPro Lunch & Learn
{% embed url="https://www.youtube.com/watch?v=PjPxsEwGydk" %}



This is a recorded version of XMPro's weekly live Lunch & Learn sessions. To join us live, sign up at https://xmpro.com/go/lunch-learn/
<details>
<summary>Transcript</summary>This is a recorded version of XMPro's weekly live Lunch & Learn sessions. To join us live, sign up at https://xmpro.com/go/lunch-learn/
hi all and welcome to another lunch and

learning session

in today's session we're going to go

through how to bind data to a chart

and get working as expected

so what we're going to cover is we

covered this in a prior lunch and

learned around data caching

and how we can actually receive data in

the app designer from a data stream

there are some different caching options

we're going to explore some of them

today around charts specifically and

we're going to touch on a few of the

charting items to make the

configurations easier there as well

some of the concepts we're going to

touch on

some action agents connectors we're

going to also touch on cache all or per

entity again

you will need access to the app designer

you're going to need access to the data

stream designer and you also need an

idea of what type of data it is that

you're looking to to display

skill level for this

we're still at beginner friendly and

intermediate as well

if we move over into the actual app

what we covered here last time is from a

data stream perspective how do we make

the data available

and visual on a app

or something that we generated in a data

stream so previously in a data stream we

configured everything and we only had

the one block we can ignore this one for

the moment

you can just move that down over there

so we were generating some data rounding

it and then we were sending it to an app

if i open up the configuration for this

we've got the

app designer settings we have the cash

amount for entity and we have asset and

asset number coming through in here as

well

now typically how you would actually

configure this is you would set this to

one and we want to cache it per entity

our entity is going to be asset number

and we've got our point asset number

coming in the bottom there

if i apply that and save that

if i click the publish and we go into

the live view we can see the generate

data which is coming through from my

event simulator and we can see the send

data to app down the bottom there as

well

so all we've done is we've configured it

to allow one record to come through

and that is significant now i'll explain

why when we get to the chart

configuration

we then have a different

endpoint here pointing to the exopro app

i'll come back to that for now we have a

generate

we've got a calculated field just

helping us clean up the data we're just

doing some rounding

the rounding helps us from the

display here to make sure we don't have

too many decimal points coming in you

can also round inside the app designer

as well

and then we're sending the data to the

app

so if i go to the

design view of this particular app

at the top

we have the data source which is bound

to the lab data and that's how we're

getting our information coming in

for it so the temperature is bound to

the temperature the vibration is bound

to the vibration field same with the

reading

reading number and then just the asset

number coming in here as well

so that's just bound to the data source

allows us to present the data

one key thing to remember is if i go to

its properties here

and we open up the configuration for

that xm pro

we set its caching to one we've also

told it to cash for entity and we're

using the asset number to do that with

now what happens is if we go to the

block section

under visualization you'll find the

chart so let's drag the chart to the top

let's just change the data so we'll just

say live

lementry

and

google had this fill there

and now we've got a base chart

coming in

the next thing that we want to do is we

want to make sure that we have a data

source for it

so let us get rid of this data source

here

so currently we've only got one data

source it's the data source which is

providing us information that we are

displaying on this card on the top left

if i click the pencil

you'll see that it is bound to

the

send data to app in the luncheon area at

the top here

so it is bound specifically to

this end point here

what we're going to do is we're going to

bind the chart to exactly the same

endpoint

and we are going to see what does that

actually do when we want to render that

data on the other side in the actual app

itself so we click on the chart let's go

to the block properties you'll see that

the data source will highlight and tell

you that it hasn't been selected

if you click the drop down we'll see

live data come in there

as soon as we do that we save it'll drop

the required field off

the next thing is we want to create a

series

if you click the plus it'll open up a

section which is going to allow you to

create a new series for charts

charts need series so that you can

attach the data to them so you can see

for instance temperature

driving on driving or you want to see

pressure and flow or humidity and

ambient temperature together you may

want to see a few different

series on the same axis

that is what we're trying to add

on the side over here

if i scroll down though

my x-axis

is not going to allow me to select asset

number and it's not going to allow me to

select timestamp

if i go down to the y-axis axis will

however what i'm looking to do is i'm

looking to use the time stamp

if i go back in here you'll see there is

a timestamp field coming through i want

to use that timestamp field

for my axis

to do that you need to go to the access

and you'll see the x-axis over here is

set to numeric we need to change that to

a date time

and if we save those changes

and we now go down into the data section

and click plus

you will see that we are now able to

only select timestamp in the bottom so

we're going to select timestamp now

what i'm also going to do is just update

the color there

and we're just going to say this is

temperature

there are a lot of other options in here

we won't be able to go through all of

them around if you want to show the

legend different chart types so what

chart type are you looking to to

actually represent and visually show

if we scroll down

we have created the

timestamp we found that we are now going

to go for the temperature

everything else we can leave

as default click apply and close

and we can click save

now if we go back to our app and we

refresh the app

you'll see we're still getting the the

live data coming through we do have a

chart on the right

the problem with the chart though is

you'll notice we've only got one value

coming through

the value is correct it's the the

temperature value coming through here

but we're not actually getting a trend

of data coming through

and this is typically how people will

configure a chart um the first time

around

the reason for this is if you go into

the data stream

it is because we are only caching one

record

per asset

which means the chart only has one

record per asset that is actually able

to

visually display

so again

what we did in here

is we used exactly the same data source

that was bound to the top left

we just bound that to our chart

and we created the the series on that

and we

used the x-axis for the time we use the

y-axis for the temperature

we're getting the correct values come

through

but we're not actually getting a trend

that we're interested in so how do we

fix this

so the first thing that we have to do

is you'll see we have a broadcast in

this data stream that allows me to have

as many

endpoints after the broadcast using the

same payload of data

for different things

so the first one is actually used here

the second one is we've dragged on

another xm pro

agent

if i double click this one this one's

configured a little different

this one has a cache size of 20. we're

still caching per entity

however if you scroll down you'll notice

here under the primary key we are

selecting timestamp as well as asset

number as our primary key

and that's important when you're trying

to bind data to a chart

it needs to know what is the primary key

so that can render the data correctly

the second part that's different here is

we're increasing our cache size i'm only

interested in 20 records

for this current asset

versus one

that keeps getting replaced

so the first thing that we want to do is

we drag that on

we configure it

you can have multiple of these on a data

stream so the top one send data to app

the second one send data for chart now

what's very important here is to make

sure you name these correctly

this is why naming is important here as

well because as soon as we go into the

app design and what we want to do this

time is we want to go to the data source

we're not going to use live data

we're going to click the plus we're

going to create a new data source here

we're going to call this chart editor

we're going to point this to a data

stream and in the data stream we're

going to go all the way down

make sure i find

where it is it's in display data

so we're going to go all the way down to

our lunch and learn version one

and you'll see data for chart in here as

well

if you had not named it appropriately

and you just left it as a default you're

going to start getting x and pro app 0 x

and pro app 1 x and pro app 2

and you're not going to be

clear as to which end point you should

be selecting

so now we're going to select chart

make sure we select the live updates

you'll see here it'll automatically fill

in the primary key for me we can click

save

so all we've done there is we've added a

new data source

to the page

and what that's allowed us to do is we

can automatically bind it

to the the data stream

or to the the chart itself

so now if we go to the drop down and i

go to the chart data

i can leave everything else as i had it

and i can actually see what

what results this will have

for me

if we go to to that let's just click the

refresh

so all we've done in here

exactly the same chart configuration

but we bounded to the first data source

and that was only getting us one record

so we changed

the temperature is exactly the same so

you'll see that i need to remap that i

just changed the source of where my data

is actually coming from

however now if we go to the app

you'll see i have access to the data

coming in but i can actually see the

live data coming through

on that as well from a chart perspective

different question um

is how do i know what type of data i'm

getting

yes you can look in the live view i can

go through the live view here i can

publish my data stream

and i can see what's this data looking

like but i'm inside my app

um and i'm not sure if i'm getting the

right data or not

how can i actually see and just make

sure

the one way we can do that is you'll see

at the bottom here i've just got two

cards

i've just set their flex to a size of

two

what we're going to do in the first one

is we're going to drag in a grid

so i'm going to drag in a grid and i'm

going to drag and grid to the second one

i'm just going to save the page

and go to properties

for the first grid what we're going to

do here is we're going to bind that to

the exact same data as what is being

used above

for the second one we're going to bind

that to the exact same data source as

what has been used above

and let's click save

what that's going to allow me to do

is i can now see

the data coming in

across the top but i can also see the

raw data coming in down the bottom as

well

so if you're unsure why is my data not

showing

or it's not in the correct format or i'm

not 100 sure if i'm getting the correct

number of records that i'm expecting

you can just drag on a grid very simple

way to to actually work out and see well

am i getting the amount of records i'm

expecting this is why the chart

initially was only getting one record

that kept changing

um constantly

where now where it's bound to

a much bigger data source you can

actually see the data coming through all

that as well

because we put this on the the app all

you've got to do is we can just go into

the the app itself

we can just delete those two grids

and we can continue configuring our app

as we need to

there's a few other items on the chart

if we go to the property side of things

appearance

this is where you control your different

visibility

if you want to

enable the series on click we'll just

set that to true for now

if i go down to to data what we want to

do here is let's bring in

vibration

again make sure you have a palette

predefined

for for your site

we can then choose that as our color

we're going to go down

we're going to select timestamp and now

we're going to pick the vibration

click apply and close

and let's view what that actually looks

like

so now you'll see i have

two data points coming in however

they are very different scales my

vibration is typically in between 0.1 to

0.7

where my temperature sits

in the high 30s across the top

if i click any of these it'll actually

hide it off the chart

and allow me to view the other one as

i've enabled it

so it doesn't matter how many of these

options um

or how many of these series that you add

to a chart

if you switch them

and enable the ability to to hide them

you can hide and show as many as you

need to

however

we've got that data coming in on the

chart but we've got it on different

scales so you've got a few different

options

for that

the one is you can create a different

access for it or the two is you can

create different panes for it

as well

so i've got my one access here if i

create different accesses for it i can

go in and i can name this

vibration

i can keep everything else the same

for it

and we can say apply

i now have two y-axis

that i've got available on my chart

now what i can do is if i go down to the

bottom

and i go to the

the data section i can go to my

vibration

and i can put my vibration

on a different

y-axis

we can apply and close that we can save

all the other options we're going to

leave as paranormal

i don't need to change anything else in

here i can go into the vibration side

over here

display labels is fine range start

position that's what i'm looking for i

want its position to be on the right and

we can apply

that what i mean by position on the

right is you can get the position coming

through on the right or you can get the

position coming through on the left

however when you start doing that you

start getting some um

flashing etc that happens

both of the uh series here don't really

belong with each other so i want to put

all the vibrations with each other i

want to put all the temperatures with

each other so another way of actually

doing that instead of using the axis is

to use different panes

so what you can do with that is i can

actually start creating different panes

for them so if i go into my vibration

what i want to do here is i want to set

it back to the default

and i'm actually going to create a new

pane here which is what i'm going to

call

vibration

we're going to apply and close

and we're going to save that as well

now what that does is it will create two

panes for me however i need to actually

assign i forgot to assign that to

the new pane that i created

so again go into the block properties

we'll go into the data section on

vibration

and we will select the vibration pane

down there

and let's have a look what that looks

like

i've now got my data coming through

on two very different panes

um which will allow me to see both of

them together

if i really need to

one other item to to note those charts

is charts need a certain amount of space

before they start removing certain

visual elements

what i mean by that is

you'll see i'm compressed for space here

which means we start losing some of the

y-axis headings you may lose some of

your

your series if you move them to the

bottom so always make sure when you're

configuring charts you give them enough

space

for as much data as you're trying to

present on the screen itself

for this example here um if i just keep

it at

um

one

so i'm just going to go and delete the

one series we just want to keep it at

temperature let's have a look at that

you'll see it even though i've only got

one pane with data it's going to show

both panes

so again if you're configuring your

charts

and you're not using certain things

remove them

um because you will be pressed for for

space in them so we're going to go into

the series here

we're going to go down to the pain we're

going to get rid of the vibration and

we are then going to be back where we

started from where i can see everything

come through on my chart

so where we started from

is it starts in the data stream where

we're actually getting our data

so the first thing is on our agent we

had one cache

and we were only binding it to the asset

number for our primary key

if you were to bind this to a chart you

would only get one record come through

constantly

second record coming through

over here or second object rather

change its cache size to 20 so i want 20

of the latest records always showing

cash for entity means for as many

entities that are coming through the

data each of them will have 20 records

so if i have 40 assets each of those

assets will have 20 records coming

through for them

if i untick that

and i was to save this

this means i would have 20 records

irrespective of how many assets i have

as well

so you need an idea of what is the shape

of my data coming through what do i want

to do with it

and that will direct you as to which

options to select here

so we're going to cache for entity and

then down the bottom here the one

difference is we are adding timestamp to

the primary key and we're still using

our identifier as asset number

the next thing that we have to do

is inside the the app designer we had to

come in here and we had to add a new

data source

we can't use the the data source here

because that is bound to the

um

the single cache

so we had to create a new one

bound to

the uh the 20 cache in this instance

even though the chart was bound to the

first data source and configured you can

just rebind it

because the data the data structure is

exactly the same

there's nothing that you'll need to

change

from the actual configuration of the

chart specifically

if you're unsure if the data is not

matching what you're expecting not sure

you can use the grid option down the

bottom here

which will again allow you to see what

is the raw data coming through right now

versus what i'm actually displaying at

the top

and is it in the shape that i'm

expecting it

so i've got my timestamp

down the bottom i have my reading for my

y-axis etc

as always if you have any questions

please put them in the in the chat we'll

collate those and answer them

and send those answers out as well

thank you for your time today and for

attending another lunch
</details>