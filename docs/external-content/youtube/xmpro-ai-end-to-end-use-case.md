# xmpro-ai-end-to-end-use-case
{% embed url="https://www.youtube.com/watch?v=HHXKgu_gaoY" %}



XMPro End To End AI Use Case Webinar

Join us as we delve deep into XMPro's integrated platform that seamlessly ties in data streams with machine learning models for predictive asset maintenance...
<details>
<summary>Transcript</summary>XMPro End To End AI Use Case Webinar

Join us as we delve deep into XMPro's integrated platform that seamlessly ties in data streams with machine learning models for predictive asset maintenance...
hello everyone welcome to this webinar

on an end-to-end Solution by example my

name is John Van hedden I'm part of the

Strategic Solutions team as an engineer

so today we'll be talking around the

exam Pro AI part of our four pillars of

X and Pro

uh that's this guy right here

and it is a distributed intelligence

that is achieved through AI engineering

where people and Technology meet to

innovate execute and augment with AI

uh so I'll just note as well we are

currently in our XM Pro notebook here so

it is part of our suite of applications

that's this guy here

and we'll step into our end-to-end

solution example

so going through this end-to-end

solution we will Define over the pro go

through the problem definition

look at some of the related data the

characteristics of that data visualize

the data identify what is um

the suit more suitable machine learning

models that we might use develop these

models all within the notebook

and then we'll step into the deployment

of uh sending these models to our data

streams

running live data through them

getting some results

pushing that up to applications to

recommendations and also touch on how to

manage your models

so looking at the problem definition for

this example

we have a subject matter expert that has

multiple pumps in remote areas

this subject matter expert wants to

analyze some sensor data and we actually

have a lot of sense of data I think

plus 50 50 plus sensors and the goal for

this subject matter expert is to be able

to identify which pumps are likely to

fail and estimate their remaining use of

life

the key for this subject matter expert

is to be able to create prioritize and

create a maintenance schedule

ultimately reducing the optimal downtime

as the key Focus

so

breaking this up into the components we

can see that we have a need for a

classification model for being able to

identify pumps that are likely to fail

and a regression model for the

estimating riding use of life and we'll

be stepping through that part

um at first through our uh stepping

through data analysis first to get to

those two models

so the Crux of this problem is that we

need the right people at the right place

at the right time

the data analysis part

utilizes our data streams to bring in

our data and our example notebook to do

the analysis so this is a Jupiter

notebook style notebook so it's very

familiar to data scientists and

Engineers who commonly use this platform

so stepping into the data analysis we'll

be loading in our data so this data is

coming from our data streams so

if I click into this guide here

where we have a listener so we have a

set of a whole bunch of listeners in our

toolbox this is

XM Pros set you can also build your own

through our extended school library

so you can bring in any types of

live data like mgtt your OPC UA

Etc we can then filter some invalid data

points out so if your sensors go offline

we might not want to bring that into our

model and we can choose to write this to

a set of

action agents is what we call them a set

of data storages so we also have a wide

array of choices here

in this example we'll be choosing just

to write it to CSV and pull it into our

notebook

put the data now in our notebook we can

go through

extensive or basic in this example basic

analysis looking at some of the

characteristics looking at the the top

top 10 rows of data summarizing our data

and

something to note about this data as

well is from our maintenance system

we've now labeled this data with our

machine status so we can see that

there's a there's three states normal

broken issue so ideally we want to

identify these issue States for our

classification model

yeah

the next step is to visualize our data

get a good idea of

how our data relates to each other since

we have a lot of sensors we're going to

push our data to a principal component

analysis space that brings it down to

two dimensions that's a different

transformation of the data for us to

visualize and identify clusters for our

classification

so here is the code for for visualizing

the data so there's just a contour plot

with the principle component space and

here's our results so we've got a nice

interactive uh

plots here I've got a console plot on

the right side and and a

density Contour on the on the left side

and if we actually just pull away all

our normal points we can see there's a

nice clustering of our issue

issue States and where we find our

machine breaks down

so we can see that there's significant

groupings for the issue States closely

related to the broken States and this is

a nice indication for us that this could

be suitable for our classification of

course we can go a lot deeper into this

and um

look look at a deeper analysis and

Transformations on this data but this is

just a simple example

um

please also take note that this type of

data that works really well is not it's

not always viable it depends on the data

characteristics and how we transform the

data how we clean the data how we bring

uh do feature engineering Etc

so now that we've had a nice idea look

at our data we've got a good idea of

what we're working with we're jumping

into our development of our two models

so this will be achieved through our

data streams so this is where we keep

bringing in that data and our notebook

that we're in currently

so the first step classification

classification of the at-risk pumps

choosing a model that's uh up to you so

I'm choosing a random Forest classifier

typically someone might start off with

something that's that's very basic or

use an automl library is optimized your

model selection and the hyper parameter

tuning it gives you a good starting

block so this one will just be a vanilla

random Forest classifier nothing too

special in the hyper parameters just

something that gets us nice basic clean

results

so

this is the code that does the

classification we do a test train split

for for our data that we've now pulled

out of we're using our data data streams

into that CSV

and we run this classification model and

we look at some of the evaluation

metrics and we can see it's actually got

a very very nice score broken it doesn't

have uh there's not many cases we've got

heavy class in Balance there and we're

not too wide we are we would like to

know that there's a good distinction

between our issue cases and normal so

this gives us great results for for that

in the accounting that this model will

do a good job at classifying our at-risk

pumps

so once we've created these models we

can now save the model files and use

them into our data streams which I'll

show ahead on the deployment stage

so this is our classification model we

can now jump into our regression model

so we've now taken our data

and creating these two models uh to

bring into our example application

Fuller regression model what I've done

here is I've just uh in this first block

uh

created a calculation to identify the

number of hours until the next broken

time

and in the second part similar to the

first I've chosen just a gradient

boosting regressor just a Model A very

basic I have a testing train split and

I've run this and it got some evaluation

metrics at the end here again very nice

scores on on for this data set so we can

see that there are squared score is is

above 0.9 which is very a very good

indication so we can see this will give

us a nice uh prediction for the

remaining use of life

once again you save these model files

you know just recap on that one

so for the deployment stage we now have

our models and

we will want our subject matter expert

to be able to interact with these models

so I'll click through here

um

sorry where this slide

so this is what we have at the moment so

we have our two models and we've brought

that in from our data

now we want to be able to apply live

data to these models and surface this to

a interface that our subject matter

expert can open up on is a laptop

wherever he's at

DLC

um so looking at the problem definition

we've got our models but we would now

like to create the maintenance schedule

and start getting value out of these

models

your deployment options are wide and uh

there are many options available through

XM Pro

there might be various reasons why you

might need Edge for for computational

Speed or security cloud or a hybrid and

we've got a range of methods to to apply

these models and um

and so as our entire set of data streams

can be configured

through through these options

so taking our models we will now put

them into our data stream

and we're actually going to model change

these models until you save on some

computational power if needed apply live

data to them

and this live data will then

um the results from this live data will

now go into our recommendation engine

and also surface into our application uh

giving us insights and and of for event

intelligence

so I will just open up our data streams

and recommendations

and applications just to show how the

three

um

gel into each other

so in our data stream

this is where we now we are now applying

our two models so we're using the python

agent here and

we've got our model scripts in there

and we can point this to any python

instance we like so if we want to go

execute this on the GPU we can set that

up

and

this is the other model there

so how this data stream works is we

bring in our live data

we prepare our Json package it goes into

our first at-risk pump classifier this

will give us a true or a sorry a normal

or issue classification so I'm just

looking at the live viewer here this is

just primarily used for for visualizing

what's going on here it's not our main

point of

of analysis

just to get the the flows working so

this data is coming through we'll be

waiting for a data set to come through

now so we can see we've got some some

data come in

uh we've got a range of sensor values

and it's gone into our model and we've

got a normal result so

at this point here

the normal result gets filtered out and

that's the end of that

um

of that

set of data

the model the the data points that

identified as a fault or their sort of

issue they go into our prediction

remaining use of Life model this will

now on that app on that pump give us our

remaining use of life

we extract our asset name and then we

broadcast this to our recommendations

and our application our recommendations

so that we can write some rules for um

for some events intelligence alerts and

our applications so that we can

visualize the type of data that's coming

through

here's our recommendations so

this is a recommendation rule I've set

up called pump at risk

I've added one rule here for the

remaining use of life

and in my alert headline I can

um

push live data into this alert headline

so from a glance you can see how many

hours it has left

uh I've created a set of

um

alert description so this rule is around

if I have a pump that has a remaining

use of Life less than 100 hours so these

are the ones that maybe I have a couple

of pumps that have a certain level of

urgency but these ones are imminent

failure critical risk

so I've set this as a high ranking and

the rule said for this recommendation is

when this remaining use of life is less

than a hundred

I can now add additional triage

instructions and information around this

recommendation and I'll show you how the

this configuration surfaces in the

application as well

so clicking into application what we

have here is we've got an interactive

map on the left hand side here

a list of our Assets in a table and

these recommendation rules that have

come up from our recommendation we've

set up so also note here that we can

we can set up

notifications for this recommendation as

well for more uh specific

uh urgent for more urgent action so we

can set this up as

soon as the basic name

and we can

send this out to the email or SMS

coming back to application so here we

have our list of pumps so this data is

getting fed live from our data stream

and we can see here we've got a remote

location very remote uh potentially

requires a helicopter for this type of

servicing and we can identify just

visually our issue pumps and how many

how the remaining use of Life on them

so I can now zoom in here and just uh

this by visual inspections can start

doing my scheduling and mapping out

there so looking at the recommendations

that I get for these at-risk files

I can now click into a recommendation

so this is the recommendation we set up

in the previous configuration

and I can look at some of the the event

data coming through so I can see okay

I've got 94 hours left on this guy this

is a critical one

um I can start writing notes on on this

pump and

uh submitting work requests

my maintenance crew can now go to this

pump

follow some triage instructions

uh looking at how to diagnose this pump

and how what is the best course of

action

we can build a discussion around this

pump uh look at a timeline of

what has been done to this

recommendation

look through some analytics for this

specific recommendation so if we see

this pump continually it has a low

remaining use of Life there may be a

persistent issue there

after we've resolved our issue we've

done our diagonal

excuse me

um

analysis on the diagnosis on the pump

and we've amended an issue or identified

the issue we can come down to the bottom

here

and we can either mark this uh pump as

resolved or mark it as a false positive

and this can then come back into our

data set and for a refraining and

refining our models

so that's a very nice feature there

so from point of view from our subject

matter expert

we want to open up our laptop in the

morning after our of our coffee or tea

and we come to this map here

and now we can have a look in look at

our pumps set up our scheduling

and this might be manual for this first

instance and I'll show you just in a

second how we can bring optimization

into this and we can keep iterating on

this application as as our as our models

become more refined and advanced so just

going into the edit mode for this

application we see we've got a range

similar to our data streams we also have

a toolbox for our visualization elements

so I can bring in something like a

calendar

rearrange and adjust my layout as well

as additionally creating template pages

and additional pages that I can drill

down into so I can dive into specific

assets

I'll just cancel that one

fantastic so this is uh what I've shown

here so we've got our two models from

before we've brought them into our data

stream here

and um we're we're pushing that data

through we've got our chained models so

that only the at-risk pumps go through

for prediction or remaining use of life

and we surface this all the way to our

application uh let's start up again

our application here where we also have

alerts set up for remaining use of Life

less than 100 hours for our more

critical events

so on top of this now I can bring in a

scheduling model similar to my machine

learning models I can go and bring in

any type of Library I I require to set

up the scheduling optimization problem

I can go through with real data I can

store some real data look at some of my

maybe I've gone and created a few manual

scheduling

sheets I bring all that in I can analyze

it I can bring it into this and compare

it with this algorithm see if I get any

get a performance boost

and uh so so this is the process of

going through developing this or tools

model

uh it's just a constraint solver

and at the end I get some results out

for okay if I need to travel to my six

most critical pumps this would be my

um optimal route and it gives me a

distance metric for for this so in in a

similar fashion as what I've brought in

my machine learning models I can now

bring in that model through through a

python agent as an example that's very

as aforementioned there's a few

different options you can choose I might

bring that in here

and then from my list of pumps

I can tie that in and then from there on

out I can take that schedule and present

it boil it up here so I've got an

automated schedule that reacts to live

data so every time I get a new live data

point in and I might set it up to wait

for every every hour before running uh

my scheduling model

but I've got an hourly updated live

scheduling that I can access by just

opening my laptop

so the last Point here on the end

into in use cases the management so

now that I've

gone through and I've developed my

machine learning models and the benefit

the beauty of of using these notebooks

and and getting your data in with XM the

data streams is that I can iterate

quickly on these models I can get

results quickly I've got graphical

interface files I don't have to do

mappings to to extensive mappings to get

a point solution uh visible on a page

and usable

um I can iterate quickly on these on

these models and then I step into my

refinement process and this performance

process can can lead to very complex

models so that may be in my optimization

model or my two machine learning models

and this is where management comes in to

to look at some of the uh sorry about

slides kicking up

to look at some

some management options like a model

registry so some benefits getting in

some metadata of the models the lineage

versions I can put models into

production uh I can I can iterate on

these models add annotations and all

this type this type of um

extra information about the model that's

not just a set of a file with weighted

values in there so if I go back to my

data Stream So an option of of this is

ml flow

we've got a right a wide range and

there's a set of options you can choose

so the example there would be that

I have my model repository sitting here

in place of where I've execute my model

here I can select my model so I might

have version 10 running and I push my

live data through and I get it all

surfaced up to here and I've got a team

working hard in the in the basement and

they're working on the next the greatest

best model with some brand new data and

they've upgraded this to version three I

can click into this save it to version

three and it automatically comes into

this through this data stream

so this is the end-to-end solution for

this specific example where we've

defined our problem

we've identified what kind of models are

required what kind of actions would the

subject matter expert

how they would interact with this

application

we've looked at our data this has come

from our data streams so we've got live

data we've stored it's in some storage

and we've then looked at the

characteristics of this data we've

transformed it into into a different

space the PCA space and visualized it in

a 2d way so we can identify those

clusters

we've then stepped into our development

so that's looking at developing our two

machine learning models looking at their

results the metrics that come from them

and getting an idea of whether they're

suitable for the task and it it will be

dependent on your task if you have

something that's more at risk something

with the that it may have a lot of false

positives may not be well made good so

we do all these kind of decisions here

at this stage there and then we step

into our deployment of how do we get

this into the streams where do we want

this to run what kind of security do we

need do we

do we need this at the edge is it highly

computational those types of questions

then we look at

taking our resulting models getting into

a management system and continually

iterating back on so once we've got to

end of one stage we've got some good

results we might have a bit of feedback

from our subject matter expert that will

tell us this is not quite how this works

this model gives us too many false

positives

Etc

we go through we redefine our problem

um well we enhance our problem we bring

in some new data might need to bring in

some more

different variables that will account

for some variants in our in our

resulting data

um go through the development we might

use Auto ml we might actually now hyper

parameters the data might change so

there's a there's a set of different uh

there there's a lot of variance through

this process and that's why it makes it

such a benefit to have a fast iterative

process through these Excel Pro

notebooks and

and we stepped through all the way

again back to deploying these models

getting them through building up our

application

uh creating maybe potentially some drill

Downs where we get to the pump level and

we might look at the the pump data

visualizing that directly at the pump

from this um

interface and we can even step this

further back into looking at maybe I

have for each state I've got a set of

pumps and I want to look at the set of

pumps for those States

and I can allocate a person to to look

at a unique page that's focused purely

on in territory for example

okay thanks very much Sean um we've just

got a few questions that have popped in

during the session

um so the first one is why and when

would you use the python agent rather

than Jupiter notebook

yes so the

um

so the python agent would be if you have

a pre-existing solution or you have a

very simple type of

a script that needs to be needs to run

or maybe a library that just takes in

data uh your notebooks is is a lot

around investigating uh visualizing uh

all on a common common platform that

that everyone on your team has the

um the same set of libraries you can

share the notebooks so this is a

collaborative type

process here

um so that yeah that would be the reason

why

where so so the results from from this

notebook investigation it ends up being

a python script that you bring into this

to this agent here

awesome and just one other one I've got

time for one more question does it

support decoupling of development

platform versus deployment platform to

be different providers for example if

deployment is on AWS slash Azure while

development is on X and pro platform

yes yes so they um so it would

um it depends on

um what the setup is but that's uh

if sorry can I get that the last part of

that question against you yeah so

um can you just support decoupling of

development platform versus deployment

platform so can it be on different

providers for example deployment is on

AWS and development is on XM Pro

yes that's right yes yes so you you can

go into you can go and deploy uh sorry

develop your models uh anywhere and uh

you through our extensible library you

can also build agents to even interact

with those um

deployment points depending on if if

they can actually serve models for

example

um but that's uh that's 100 viable to to

go and create and develop somewhere else

and bring it into our data streams um

separately

excellent um okay well with that's all

the time we have for questions today um

thanks very much Sean and thanks

everyone for joining us today uh if

you're looking for more information you

can contact Sean or our team directly

and we'll send out the recording of this

this session shortly

um join us next month as we share how to

accelerate your digital twin use cases

with our blueprint accelerators and

patterns repository and you can register

um via these links in the chat box

um here and we look forward to seeing

you all next month thanks very much

everyone

thank you everyone

foreign
</details>