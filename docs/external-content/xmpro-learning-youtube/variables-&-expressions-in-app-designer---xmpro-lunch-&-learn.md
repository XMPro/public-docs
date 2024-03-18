# variables-&-expressions-in-app-designer---xmpro-lunch-&-learn
{% embed url="https://www.youtube.com/watch?v=Fs4XOVC8NPg" %}



This is a recorded version of XMPro's weekly live Lunch & Learn sessions. To join us live, sign up at https://xmpro.com/go/lunch-learn/
<details>
<summary>Transcript</summary>This is a recorded version of XMPro's weekly live Lunch & Learn sessions. To join us live, sign up at https://xmpro.com/go/lunch-learn/
hi all and welcome to another lunch and

learn

today what we're going to be covering is

variables and expression

with a focus in the the app designer

itself

so what is it so variables are

essentially placeholders

they are

are they used to to maintain static

values but you can update them

through the course of interacting with

the actual app itself

you can use variables in the expression

editor

you can use other variables with them

calculated fields etc

and an expression

you can think of that as an extra column

on a data source

it allows you to to calculate a

different additional fields different

values

that you can actually use when binding

that data source

to

to the actual form itself

so

we're going to cover two main areas of

variable use in the app designer

there are three

we're just going to focus on the two

that are within the app design and the

third one is actually in the data stream

designer uh we'll cover that in a

another luncheon when we tackle some of

the items in the data stream designer so

for today we're just going to focus on

the two areas of variable use

in the app designer itself

we're going to tackle variables within

an app so where are they how do we get

to them how do we view them

etc

and some basic requirements you always

need access to the app designer

to tackle the one the second area it is

an administrative area

um typically it's something you'll set

up and configure once so you might not

have it depending on your access into

the actual site itself

uh skill level for this um there are

some beginner pieces in here but we're

starting to move into more of the

intermediate skill levels um as we start

configuring these as well

there are two external links as well

i've got them on the right and i'll walk

through what those are as we get into

this

so as i mentioned the first thing is

inside the app designer there's there's

two areas of where variables

are used

and you can interact with them

the first is obviously you need

administrative access or the ability to

manage create update the variables

on the left if you click the hamburger

you can expand the menu and see all the

different options you'll see a variables

i've got at the bottom here

if you do not have this option

it means you do not have the right to

maintain or change the variables as we

go into it

if you click the variables it'll

actually open up a different blade which

is listing all the variables that is

currently available for the apps

now this is where you can set up your

your access to the different systems

it's also the area where you can come

and actually make specific changes

to the variables themselves

so let's say you have a specific service

account that you're using to access

systemx

and you update the service account

instead of having to go through all the

apps

and try and find all the apps that users

have created either you know all of them

or you might even not know all of them

you can change it in one place instead

of having to go through all of them

individually

what the icons mean

is i have not actually configured

anything for these variables at the top

so there's a few options in here you can

manage categories

so you can actually create specific

categories all that does is allows you

to easily group them in this particular

view so you can find what you're

actually looking for as you go through

them

when you create variables

there's a few

options here

main one is around the encrypt value

so you give it a name provided a

category and the encrypt value is very

important

as you'll see when i create a connection

to a particular data source and i want

to use the variables

only encrypted variables will be

available in password fields typically

so if you find something is not showing

up in the field where you think it is

just make sure we've got the correct

encryption type

for that as well

so this is typically done

from a an i.t perspective typically done

once

and you don't really need to come in

here and edit it

and make any changes in it

however where do we actually use these

if i go into a particular app

and i'm just going to go into an

existing app that i have here

when you go into the app data and you

actually click the plus

to add

a new

data source to your your app itself

it's going to ask you some questions

so this is for a sql connector as i

click that it'll open up the properties

for me

over here if i open up the the next one

it'll open up we'll use this one's a

little smaller we can see everything

now the first thing you'll notice

is it has a use variables option here

this example we're not making uh use of

the the variable option the downside to

doing this as i've got it in here

means

i need to make a change to every single

app

if my service account details actually

change or the passwords change or the

usernames change

it's much better to make sure you click

the use variables

and we can now go in and we can see all

the different

options that are available

the ones which are not

password fields

will appear in the unencrypted so

typically your username your instances

your client id etc

if we go into the password field this

your list you'll see is a lot shorter

it will only show encrypted fields

so in this field here

it'll only show me and allow me to

select the actual password

field in the username it'll allow me to

select all the different usernames that

we have

and now i can very easily

make sure i select the correct database

and actually go from there

so the first area with regards to

variables is

an area that

is how do i access my data

so how do i get

the data in who controls that where do

you set that up

typically you you do that once um and

you'll go back to it over time to to

make some changes and adjustments to it

and then you use that on the actual app

itself so if i go into a particular page

as an example

and we want to add a new data source

it's going to ask me the same question

if i click the plus it's going to ask me

well where's my connection

if i do not have a connection and i

click plus there again it's going to

walk me through adding that connection

to the actual

app itself and i would suggest use the

variables in that option as well

so that's the one main area to use

variables the second area where you can

use variables is as i've got this

particular screen open

you'll see under page data we have a few

different sections so up to now we

pretty much just focused on the design

sources session or the data sources

section rather

where we can add different data sources

parameters allows me to define some page

parameters if i want to move values

between different pages

and very useful if you've got drawdowns

etc

the variables here this allows me to

create a variable for use in this app

page

now important to note your variables are

specific to the app page

you can't share variables between pages

if you want to do that

you need to make use of the parameters

and actually pass the variable down to

be able to use it on any drill down

pages that you want to use

so variables here are very much linked

to the page that we've actually got

in here

so when you create a new variable you

have a few options

for it

now before i go into those options

i did mention there were two links on

the the slide that i had open

the first link will actually walk you

into using the variables adding

variables and managing the variables

here

if you go to our documentation site so

documentation.xmppro.com

top right there's a search

in the search if you just search for

variables

it'll bring up all the different items

on variables

the how-to guide at the top is the one

that we have open now this is how can i

define a variable that i want to use

across all my apps

so typically your rt will set those up

for you

and then you just use them as you run

through the apps

the second area if we actually scroll

down

the

the search results you'll see variables

and expressions so the second link is

actually variables and expressions that

we've opened up over here

and this will walk you through how do we

add a new how do we edit

how do we configure them etc

but the one point i want to make here is

there's two modes that you can actually

create a variable in

the one mode is what we would say is a

value mode which means you can keep

updating a variable as you work through

the page

the other mode is an expression where

you can actually write an expression

which will hold the value of that

variable

now what do i actually mean by that

you'll see i've got two variables here

if i click the edit and go on to the

first variable you'll see here it is

defined as a value

now what that means is this variable

will store

in the the name selected time

anything that i actually select

so it is a

a placeholder for me to use on this

particular app now i've been provided a

value through any of the other fields

here that have a value option and i'll

show you where we're actually using it

on this page

the second variable if i click its

pencil this one actually opens up an

expression

and

how we change that is you click the

value you go to expression it'll give

you the expression

now what's important here when you are

creating variables make sure your data

types are correct

um any of the

parameters operations functions that

you're trying to do here are specific to

the data type it's not going to allow

you to save this if you're trying to

you know convert text into a date time

or integer and it's not compatible so

always make sure your date time is

correct

this particular expression here is

adding days to the exact same variable

that we've selected at the top

we are then getting the date difference

and we are using a local time so how do

we actually create this

all expressions in the app designer

follow a very similar approach

you have access to your parameters if

you have any defined if you click

variables you can actually see the

variables will be listed here

how you add them to the expression

editor if i just push enter a few times

to given you a few new lines

if you double click the time

it'll actually fill in the values in the

expression editor for you automatically

again you just double click time and

it'll fill that in for you you don't

have to figure out how do i type it out

um what's the correct spelling i need to

use etc just double click anything in

the

editor at the bottom and it'll add it to

the top for you as well

constants

um when we are talking about true false

is mobile um how do we define constants

and use them as well

functions anything that you want to do

from a daytime logical you know maths

business role

etc will be in constant functions and

then you have operators coming down the

bottom and here as well

so the date time you have a lot of

options in here

if we go all the way down to the

add days

if i click on that so single click not a

double click if i double click it'll add

it into the editor at the top

if i single click it

it'll actually bring up the help text

for me on the right

so it'll give me a explanation of what

it's expecting

and it'll also give me a description of

what it is trying to do

so if i go into the logical and i click

the if as an example you'll see there

it'll give you just a breakdown of what

it's expecting

and then a brief description of what

it's looking for

if i double click the if

it'll fall that in for me

i can now click into a particular area

and i can go into the variables and i

can actually use a variable in there as

well

so we're just going to discard those

changes for now

and we'll come back to that

so selected time again this is just

defined as a value which means we're

going to keep updating its value for it

so

what do i mean by that if i just open up

another

tab here and i just go into this actual

app itself so we can see what it is

displaying

so as the app loads you'll see i have

data live data coming through i have

live data coming through but i have a

drop down at the top here

and i have certain fields in this drop

down as well

if i select anything in the drop down

what you'll notice is i am now not

getting my loud data anymore

but i've got a specific snapshot in time

that i'm viewing because i've selected

at the top

if i go and delete that and tab out of

that you'll see it'll bring back my live

view as well

this was done using a combination of

variables and expressions so let's break

this down

if i come back into this particular

app itself the first thing is we've got

the selected time defined

the second thing is on our date selector

at the top if we go to its properties

you will see in its properties here

we've got appearance

we've got behavior where we want to go

into is value

typically when you will drag this on its

value

would be using the static option

if you click that it'll swap to a

dynamic option

and in the drop down you'll be able to

select the variable

so what we're doing here is we're saying

the

whatever i'm selecting as a user in this

drop down

we need to make that information

available into this variable so getting

it's getting stored into that variable

itself so

if i select in this drop down to 12 am

my variable when i say 12 am if i do

that to the 12 20 it'll have the 1220.

so how do we actually see that how do we

know it's doing that

but across the top we're just going to

edit the the particular app so i'm just

going to create

a new

label we've just cloned the first one

we're just going to give it some spacing

on the left

and

instead of it having the the words of

pump data in there

we are going to

set it to variable.time

uh actually select the time that's what

i'm interested in

so now if we go back to the actual app

itself and we refresh this

there's no value currently for that

particular field

if i select something in

you'll see

i now have a

a value that has been selected

for it

if i go down it'll select the next one

and if i keep going down it'll select

the next one as well

because we are dealing with date times

it's going to bring up the raw date time

information for me as well that's why

it's very important to make sure you're

using the correct data sources and

you're not trying to do this as a string

when it should be a data or string when

it should be an integer or a double or a

long so very important there

so again

if i come back and reload this the first

time you'll notice that nothing will be

displayed

until i actually select something in the

field that i've got coming in as soon as

i select something it'll make that value

available into that field which is

across the top there and i can now use

it on any of the other fields on the

form that i want to

so where is this actually being used

so we're just going to get rid of the

top

and we're going to come back to the

actual date selector itself

and we go into the box

we can just minimize all the items

the the two boxes that we've actually

got here

if i highlight the one and how i know

they've got data bound to them is they

have a yellow border around them as well

so looking at this page i can see that

there is data for them

so that is how i know to look at them

for their data sources so if i just

click the one that we're looking at here

you'll see this is bound to its pump

history data

however

the visible we're actually using a quick

expression value

so again if we come back to variables

the first one

we were using it as a value

the second one we were using the

expression editor here and we're going

to add some days when you've selected it

and we're going to convert it

etc

so you're using expression editor as

part of the variable itself

the other way you can use this as well

is on any of the fields

that allow you to change static to

dynamic to quick expression you can use

the expression editor as well

so typically this field looking at it

here you would have a true or false

however we only want this to display

if you have selected something in the

top

we could

bind it to a variable

and we could have the variable handle

that as well

but what we're going to do in this

instance if i click that as a second

time it's actually going to give me the

quick expression value field

if you click into that field

you'll see exactly the same window pops

up

it's exactly the same window

that popped up when we were doing this

on the variable side

if you click parameters

variables you can see my two variables i

have all my constants i have all my

functions coming in here as well

so typically you would have your static

value

you would check the one to be able to

select something either on the data

source that binds around you

or on the actual variables or parameters

or if you click it again you get access

to the quick expression value this one

here is

using a conditional check

if that variable

is a valid date

then it's going to use it on this

particular data source in here as well

if it is not a valid date then it is

going to

set the visibility of this to false so

this here you'll see there's actually

two boxes in this example

all it's doing is it's taking the one

making the one visible

and taking the other one making the

other one invisible

for it

these particular boxes here have a data

source and on the filter

here you can see we're actually using

that variable as well

when you create any filters

or any of the the options uh in here and

you're using the filter control

it'll default to the static

value

if you click that

again

it'll turn into

a selectable so it's more of a dynamic

option

here

you can see there's the data source

around it but we're interested in the

variable

so we can actually define and select

that variable that we're interested in

in here as well

so variables can be used and have their

values assigned

by interacting with different fields on

the form and to do that

on the actual control that you want to

update the variable

you need to make sure that you set its

value to that variable

you can then use this variable

in different ways one of them in a

filter

which is what we've got in here so again

if i go all the way up here and i go to

its filter you'll see a variable gets

used in this filter as well

you can use it again

in anything that has a static to a

dynamic to a quick expression editor in

here as

well

one more area you can use expressions i

just discard all those changes coming in

here

and we can close the filter there we go

on the page data side

you'll see i have my pump data so i have

all my data coming through

from a particular data source so if i

click the pencil you'll see this is

coming from a data stream

what you can also do here is you can

create expressions on this data source

as well so what i want to do here

i'm going to call it indicator color

we're going to keep it as a string and

i'm going to go into functions

we're going to use the if

so here what we're going to say is if

and what you'll see is because i'm in a

data source

i have a new section called fields

available

if you are not in the data source you

will not get the fields option but what

this allows me to do is interact with

these fields

coming through here

so what i can do

is let's have a look at

the data flowing through here

what we want to do is just put a simple

conditional clause in there that if my

temperature goes above

let's say 95 for long drive end

so if my non-drive in temperature again

click where you want

double click so if my non-drive

temperature is upwards of 95

then what we want to do is we want this

to be red otherwise

we want this to be green

we can click save

what we're doing here is we're creating

a

expression on the data source

itself so

right at the bottom indicator color was

not available in the original data

source however there are conditions

there is logic

i actually want to use the conditional

indicator now so now what i can do is i

can have a look at the actual

item

here

and

if i select

the box in question

this is bound to the pump data

i'm going to just move this

up a little bit so we can actually see

what it looks like

and we are going to drag on an indicator

i'll just put it at the top

for now

now on the indicator you'll see i have

the color option here i can provide a

static color

if i click that i then get access into

the data source

because there's a data source that is

sitting around this particular

indicator there is my indicator color

i know it's a expression because of the

fx i can actually click that and now i

can use that

in my my app itself

so if i just save that

and we just refresh the app

you'll see the color will start changing

as the condition

is met that i've actually defined for it

in as well

so the color indicator you could

work that color out in an actual data

stream there's nothing wrong with doing

it there

you can also do it within the app

designer on the actual data source

itself like we've done over here

you can get a lot more complex in your

expressions using the functions

using the constants using the fields etc

another example of what you could do is

if i go into the variables here and i

say

i just want to create a variable called

full name

for for the user again it's going to be

a string

and we can say expression

if we go into constants you'll see there

is a first name there is a last name if

i double click first name it'll fill

that in for me

we're just going to add a space in there

and double click last name

for that as well and click save

so creating variables is very easy

the the one thing to keep in mind is

what are you wanting to use the variable

for um and where do you want to update

it and where do you want to

use it in a filter etc

if i go into the top here again and

we're just going to create a

little space here

this one here we're again going to click

the static

and in there we are just going to use

the full name

and if we refresh to see what that

actually looks like

you'll see it'll bring

the full name coming through

for a variable which means if i now need

to update the data source or pass this

down into a system that i'm trying to

integrate with or update

or insert i can actually pass who was

the user through there as well using a

variable

thank you for your for your time today

um and for attending another lunch and

learn

one thing to remember we only touched on

two of the areas of variable use these

are mainly used inside the app designer

there is a third inside the data stream

designer which we'll get to in a future

lunch and learn

thank you again for the time
</details>