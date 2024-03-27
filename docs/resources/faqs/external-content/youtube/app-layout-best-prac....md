# App Layout Best Practices for Desktop & Mobile - XMPro Lunch & Learn
{% embed url="https://www.youtube.com/watch?v=2AaPEp7ZltA" %}



This is a recorded version of XMPro's weekly live Lunch & Learn sessions. To join us live, sign up at https://xmpro.com/go/lunch-learn/
<details>
<summary>Transcript</summary>This is a recorded version of XMPro's weekly live Lunch & Learn sessions. To join us live, sign up at https://xmpro.com/go/lunch-learn/
hello everybody and welcome to a lunch

and learning session today my name is

gavin green and today we're going to go

through app layout best practices how to

get it working for desktop and mobile

let's jump in

so today's tech session is around

responsible app layout

now

what do i mean by that so we first need

to get some basics

so a responsive web design is creating a

web page

that looks good on a variety of

different devices

without having to configure

them each independently or separately i

need to be able to open it on my desktop

on my tablet on my phone and work

through it interchangeably as well

so it really is how does it

automatically adjust

to different screens as well as the

different

different viewports

we're going to go through some concepts

so

when you're configuring

for a desktop

you can use all the elements in the

toolbox

when you start transitioning over to a

tablet or even to an iphone

you need to start

working through some decisions on which

design elements to show does it make

sense to show

do we need to adjust some of the

positioning how to use the responsive ui

configuration inside the app designer

and then we'll also touch on the

visibility option how can we actually

make certain features

visible on the the main desktop view but

how can we hide those that are not

relevant on a mobile as an example

we do have some some requirements

you obviously need access to an app

designer for this

highly suggested that you have a mobile

device with you

uh whether it's a tablet whether it is a

phone

this will help you validate the layouts

as we go through it

and lastly but

most importantly is who are the

different personas that are going to use

the layout that you're configuring

people who are constantly on their

phones all the time people who

transition between the two of them it's

good to have a high level idea of who

that persona is

as well as some of the user stories that

will help guide you in what's the most

important information to show

as well as what can you keep on the

desktop what can you lose as soon as you

shrink your real estate onto a a browser

on a phone

and lastly what type of skill level are

we looking at to to configure this and

put this together

this is very beginner friendly

it can start going into an intermediate

but it really is focused around

beginners getting to understand and work

through and know the different concepts

as we go through this

if you do have any questions as we're

going through this please post them in

the chat as well we'll collate them

and reply to them after the session

if we move into the software

the first thing we want to go to is how

do i actually access the mobile

version how do i

log into it where can i find it

so we've logged into the app designer

here

top right you'll see there is a mobile

icon

if you click that it'll bring up a

pane in the pane you'll see there is a

set of different instructions but there

is also a qr code in the middle

if you scan the qr code on either your

tablet or your mobile device it'll ask

you to log in

the browser and you'll have access to

the mobile version the mobile website is

a fully responsive website

it contains the recommendations by

default as well as any of the apps that

you've configured

in there as well

so first thing you want to do is

obviously

log in on either your tablet or log in

on your mobile device

so that you have it handy next to you

you can use the

f12 option in a browser to see what it

looks like

but it's not a true reflection of a

mobile interface so some of the items in

there will still render like the menu

bars etc so it's best to have a mobile

device with you

it'll allow you to validate the the

different settings that we have

if i go into a particular app and i'm

going to pick a app that i have

available

and i'm going to walk you through some

of the different items that we have for

it

so this app is initially configured to

be available on a desktop

so what that means is we have a esri map

in the middle here it allows me to

interact with it it allows me to see the

information i can see my asset status

i can see my recommendations and i've

got my equipment that's important to to

me as well

i have a lot of real estate here

it makes sense to keep this because the

persona is interested in indicators

lighting up the the map i can see my

overall status here

top right resurfacing up the

recommendations because they're

important

but we're also highlighting equipment

requiring maintenance

if i was to leave this

ui as it is right now when i was to open

it on my mobile it will attempt to

render it exactly like this and what

will happen is everything will start

rendering and will be squished here and

it just won't look

appealing to anyone that is interacting

with it

so we need to make some adjustments to

that so how do we actually do that

if i click the pencil so i have added

access to this particular app so i can

actually go in and make these changes

that i'm talking to yeah

the first thing is this app is published

so it won't save any of the changes but

i actually don't need to to do that

what i will be doing is i'll be making

use of these three icons across the top

here

as i mentioned some of the concepts that

we want to be going through

is how can i use the responsive ui

elements here to set up different

experiences if i want to

yet i've got exactly the same

application

i have exactly the same set of data

sources coming in and i have exactly the

same set of rules that i may have

configured on this particular app as

well for it

the first thing looking at this is

obviously

you have a lot of different layout

options here

on a desktop it would make sense to keep

an entry map

if i go and look at the blocks

you will see there's a lot of different

components in here as well

for it

if we look at the layout options the

next question to go through is what

makes the most sense on a tablet

can you keep the esri map yes you can

you have a lot of real estate there as

you start shrinking to a

a mobile you start asking is it relevant

to keep the the big energy map there

versus the other information

that we're looking at here so we've got

overall asset status recommendations and

again we've got equipment requiring

maintenance

one of the key questions to answer is

who's the audience that's going to

consume it on a device versus the the

desktop

are they interested in looking at in

this instance an esri map or they're

more interested in the recommendations

the overall status and maybe equipment

requiring maintenance as well

so the first thing that we want to do

is how can we actually

hide some elements

from the uh the different rendering so

on on a desktop i want to see everything

but on a mobile device i actually don't

want to see them

the first thing where we can do that is

we can actually make use of

the if i go up into the box

we can make use of the appearance

there's a visible option

most likely when you've configured this

it will say visible is true

for most of the apps that you've created

now what you'll notice is if i go into

the page layers i can actually see all

the different layers that i have

configured

and page layers becomes a little

important when you are trying to work

out the different orientation what's

going to flow above in the middle and

below as well

if i click on the esri map itself

can i just hide the esri map yes you can

there's nothing stopping you from hiding

the actual control itself

however by doing that

you still got this container that sits

around it and you still have the heading

that's going to show

so you actually don't want to just hide

that particular control

what you want to do is you want to have

a look at how are the different layers

set up in here

so we have a vertical stack layout you

can see as i click on it on the right in

the blue it's going to highlight

everything that is selected for me

if i go to the first box you'll see

that's the one which is containing my

history map

that's the one that has a heading that's

the one that has a asrie map

that is the one that i actually want to

hide if i'm going to view this on a

mobile device

so what we want to do is just click that

so we're going to select that

we're then going to go into the block

properties as i mentioned by default

yours is probably going to be set to

true

as its normal state you can go and set

this to false

however it's going to be false on pretty

much all three uh desktop browser as

well as mobile device

if you click the icon on the left where

you see an a so currently we're in

static mode if i click that once

it's going to turn into dynamic value

if i click that a third time it's

actually going to bring a quick

expression out for me as well

if i click into the middle it's going to

bring up the quick expression and allow

me to edit it so if i delete everything

that's in there

by default this is what yours is going

to look like if you go into the quick

expression

so what we want to do is we want to put

a condition in here

we want to put a condition that if the

browser is identified as mobile we want

to hide this particular block

if it's not mobile we want to render it

paranormal

so first thing we're going to do is

under functions we are going to look

under logical

here is our if statement

on the right it will walk you through

how you can actually configure that but

for now if we just double click that

it'll start filling it in for us across

the top

if i click into the first area we're now

going to go to constants under constants

you'll see a few fields

we have an is mobile and we have an is

desktop

both of these are used

specifically

to show or hide

or to do various calculations if you

want to

or to move things around on the ui in

the different modes

if i double click is mobile

it'll fill that in for me so what we're

filling in here is

if the render mode is mobile

we want this to not displace we're going

to set that to false otherwise the

default is going to be true

if you click out of that

it'll keep that

expression configured for you

so as we walk through this

when we open up this app

the first thing it's going to do is it's

going to tell this app i'm rendered on a

mobile device or i'm rendered on a

desktop

if it is rendered on a desktop

it'll render as true

if it's not

it'll set this to false which means this

entire block is not going to render

itself

if you were to unpublish this app and

save it

you need to open it on your mobile

device to be able to view it

i mentioned earlier that you can

actually open this up using your f12

now for those who are not aware

f12 allows you to view

the the actual layout of this particular

page and there is an option in here

where you can go into it and you can

change it to specific

however this is just an emulation

as you can see here what it does it

still keeps the heading and it still

keeps the bar here

it'll give you a good indication of

things which have been made visible and

things which are

still visible i.e not hidden

but you'll notice that you do have a few

styling items to

to work through here

it gives you a good indication so here

you'll see exactly the same

form if i was to switch that off and go

back to the main desktop

there is my map view here is my overall

status my recommendations and my

equipment requiring maintenance

if i was to go into that

and

select for instance an iphone

and i was to switch that around what

you'll notice here is some of the

styling is not configured

but my map is not actually rendering

so it knows between the different modes

when to render something and when not to

render something

so the first thing is to identify which

of the different we call them blocks

which of these different components in

here should be visible on a mobile or a

tablet

or a desktop

you may want to change up what you're

showing instead of showing a map here

you may have another controller in mind

that you want to make visible when

someone is interacting with it on a

mobile the other thing to consider on a

mobile is you're very limited on real

estate so the most important thing

should be the ones that you see first

less important as you start scrolling

down

the same applies on a desktop

it's a good rule of thumb to make sure

that the most important things you're

trying to illustrate to the end users is

across the top

and as you start going down the page

they're still relevant but the

importance is not as great

now why am i mentioning that

if we go back into the edit mode here

so we've now hidden

the

entire esri map

so the map is now not visible however we

may want to adjust

and move around

the the remaining elements so as soon as

you open it up the most important things

at the top so how do we do that across

the top

by default

it'll have the desktop

selected

if i was to click the phone

what you'll notice is it actually swaps

to a

much shorter

amount of space that i can configure but

you'll also notice that quite a few of

these fields have moved around a bit

so now

my esri map is not top left

it's been adjusted

my equipment requiring maintenance is

moved to the top

so if i open this up on a mobile i get a

different visual experience but it's

exactly the same app so how did we

actually do this

if i go to the tablet view

you'll see the tablet view

mirrors what we have on the desktop

so if i go back to the desktop view

and i go to the tablet view you'll see

they mirror each other

the first thing that we want to do is we

want to adjust and move some things

around

the reason i've picked the

the tablet view i've just got more real

estate that i can show you the impact of

the the changes we're going to make

again as i mentioned earlier page layers

allows you to move things around that

makes sense

important to to understand is in the

layout if i was to click the vertical

stack layout now what vertical stack

layout is if you go to blocks

you'll see under layout

one of these

is actually called vertical stack or

horizontal stack

if i was to click

that

and i go to its properties you'll notice

there is no visible option there

they do not have any block property

options on them

you need to make sure that if this is

something that you do want to move

around shuffle around

make visible or not it needs to be

within a container of sorts which is why

i have the box in here

if i now click the box

and i go to its block properties you'll

see i have an appearance

that is what we did with the entire so

if i click the

the map box this is the one that we

configured that is visible on as well

now why is this important

it's important to understand

as we're going to adjust some of the

flex layout now we're going to start

moving some of the field elements around

what you'll notice is because i've got

this selected my screen is currently

split

into a two-thirds to one-third

the one i've got selected is two-thirds

if i select the other one you'll see

it's one-third

if i want to move items around my

horizontal layout

i'm going to go to the first one

i'm going to go to the second one

i want to actually put

these two fields above

my my map

so we're hiding the map

so i don't actually need this field

anymore but as soon as you open the

phone for the first time i actually want

my

equipment requiring maintenance to be

right at the top currently it's bottom

bottom right so how do we move that

around

if i go to the horizontal

and i go to the box one and i go to my

box two

again on the horizontal

we are going to go into the block

styling

and we're going to go into flex layout

flex layout allows me to adjust how

the different elements react in relation

to each other

we do have a video on our youtube

learning channel which goes into a lot

more detail around flex

i highly recommend you watch that we're

just going to scratch the surface on

flex

right now

so what you'll notice here is the

direction is going left to right we're

actually going to adjust the direction

north to south top to bottom

so the first thing that you'll notice is

we've still got our map

we still got our overall status but now

instead of that recommendation equipment

required maintenance being on the right

it's now at the bottom

if you're unsure

we can go back

to

the the desktop view this is where we

started

if i go back into

the

tablet view this is where we've got to

so again what we did

is we've gone into

the container around those two boxes and

we're just adjusting its flex loud we're

just adjusting how these are being

rendered in relation to each other

what we can do as well is we can

actually reverse that

i'm more interested in equipment

requiring maintenance be near the top

overall asset status

that could be a little bit further down

on my page so we've actually reversed

the two of these

remember

this box in the middle here is going to

be hidden as soon as this renders on a

tablet in this instance or on a mobile

device

if i go into this box though

so you'll see

the horizontal at the top that's the one

that we've adjusted the flex on

so instead of going left to right we

went top to bottom and then we reversed

that so now bottom to top

if we go into the one box here i want to

do the exact same thing

with the items inside it

if i go to its block styling i'm going

to reverse those two as well

so now equipment requiring maintenance

is going to be at the top so that's the

first thing i'm going to see as soon as

i open my tablet or i open my mobile

device the next thing i'm going to see

is a list of recommendations come

through there as well

and then the third thing i'm going to

see is my overall asset status coming in

as well

now what you'll notice is as you go back

between all the different layouts

it's going to remember what you've

configured in the different states

so what this means is

if i go into

my chart as an example here

i may want to adjust

again

the layout of this i don't want them

next to each other i want them on top of

each other

i can go to its block styling here and

again i can set that

up

what you'll notice here is i don't have

any padding between the two so if this

renders they're going to render quite

squashed on top of each other we want to

give them some breathing room

in this as well

so i can click the chart

and if we go to its dimension

i can actually give it a border at the

bottom

or we can give it a greater border

so now when it renders there's some

breathing room between the chart

as well as the contents underneath it

i can further specify because we're on

mobile

you can be a little bit more restrictive

on having the the heights of the charts

as well

so what should the minimum height of the

chart be but you can also restrict its

maximum height as well

if i go back to my desktop view

you'll see here this chart

has its desktop property set

if i go back into my tablet view

you'll see it'll have the tablet

property set on it as well

the block styling section here

is smart enough to know which mode are

you configuring your app in

and remembers those settings

so if you're configuring something for a

desktop which is the default you

configure everything as you normally

would

if you're interested in configuring

something for a mobile device

you can just click the mobile device and

change the look and feel the styling etc

as well

block properties the visible properties

the legend visible all of these you can

control in exactly the same fashion we

only touch the visible so again

i could make this

chart hidden

if i'm on mobile if i really wanted to

to do that we go into functions logical

double click the if statement

go to the first item

go to constants and we say is this

mobile

then visible is going to be false

otherwise

we want it to be true

because i've selected the chart you'll

notice down the bottom here we can

actually have a lot more control over

the actual component as well

again i can go into

the legend of a chart

and i can apply the same thing in here

so if we are

on a mobile

i don't want the legend

to be displayed if we're on a desktop i

do want the legend to be displayed as

well

the box that is what we set the default

for the actual edge remap here

but each different component

in the block properties also has

different options so hide series on

click

allow exports

so again

you can

anything that has a true or a false

option in here

you can ask the same question

and either enable or disable it from the

mobile experience

while we're in that mode the second area

you can influence is on the block

styling

typically the main items you want to

edit and change in here will be around

flex itself

influences everything inside a container

that's why if i select a vertical stack

layout or even if i select this vertical

stack layout it'll affect everything

that's inside that container

so if you want to adjust the the flex

layout make sure you select the parent

and then adjust your flex from there

at the same time because we're in the

different modes you can also change your

justification you can align differently

you can also change how you want items

to wrap as soon as you reach the edge of

the the render space or the viewport you

want the actual items to wrap underneath

each other versus vanishing into the

left or the right of the screen as well

there are different options in here on

topography

decorations and extra

applies to the block styling as you are

selecting the different modes that we're

going through in here

so if i come back here what are we

trying to go through here

we're trying to make sure that when we

put an app together

we create it from a responsive app

perspective

key item to to ask whenever you put an

app together is who's the end audience

who's the persona that's going to be

consuming and interacting with the app

is that audience mobile

first is that audience tablet first was

that audience

desktop first or a combination

second thing to consider is for each of

those different display modes

what ui elements make the most sense

does it make sense to have a for

instance

grid

all the way to a

mobile device versus only presenting the

information that is applicable

or having a full 3d unity rendering on a

tablet that takes up two-thirds of the

space and you have to scroll all the way

down to find what's important and

relevant

to to view so some of the key items to

consider is really around

what information do we need to display

on the different modes

and then using the visual responsive ui

side how can you configure those without

having to configure different apps

across the top you have your three

different modes

you have your tablet

you have your mobile device and the

default is

to the desktop

each of these three

allows you to change the block styling

that is applicable to that particular

mode that you selected

the other thing that you can do is if

you go into the block properties

you can start using the quick

expressions

along with the

constant field either is mobile or is

desktop

you can use these in any of the

expressions we'll touch expressions and

variables in a future lunch and learn as

well

where you could use these in specific

calculations or a lot more advanced ui

configuration

for now you can use them around

displaying the visibility of components

or enabling certain features on those

components as well

thank you for the time today

and for attending our lunch and learn

if you've got any questions please post

them into the the questions section

we'll collate them afterwards and we'll

report them back for for everyone to

view as well

thank you have a great day

you
</details>