# How To Use Data Sources - XMPRO App Designer
{% embed url="https://www.youtube.com/watch?v=UsBSizEB6HI" %}

Learn how to use Data Sources to display dynamic real-time data in your XMPRO apps.

Need help with creating your XMPRO apps? Send an email to support@xmpro.com

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>welcome to another training video from

accent growth today we will be looking

at how to create and use their sources

as a prerequisite you should have

already gone through the video on how to

create AB direct connections if you

haven't I highly recommend you do that

first let's just let's let's jump in so

I have an app here as you can see

budgets all blanket and I wanted to

display some data so the first thing I

would like to do is over here where you

see page data I would like to add some

data sources so if I click plus over

there it will give me this screen where

I have to specify a name for my data

source let's say I say it means furnace

health store then I can choose a

connection as for the last video we

created a connection and call it first

and I will choose that and that will

bring back all the entities that that

connection can provide me the entity I

am looking for is called

furnace tab once that part is done I can

click Save and then that data source

will be available for me to use in my

page I can reuse it as many times as I

like on this page clicking the expand

button here shows me all the columns or

attributes that are being returned by

the data source now how do I put it on

my phone or on my screen there are a

couple of controls here which are

actually their amount controls for

example a chart or a grid or a drop-down

these are all the controls which can be

bound to an air source and they will

behave accordingly so let's start with

one control which is the easiest and

that is

director and I will go to better over

there click on it and let's say I want

my furnace data to appear in this

directed I will then go to the block

properties and you will see I have a few

options here from the static rent I'll

go I'll skip the others and just go to

the data source which will then present

me in the screen the first thing it asks

me is which tell source I want to use so

I'll use the one I just created and then

I have an option to either create a

filter on it select if I want the data

to be sorted by a certain column there

are also some advanced options but I'll

leave all of them for default I'll click

Save and when I launch it I expect to

see data in the data grid which is

coming from my data source as you can

see it loaded that up now let's go back

and try a few other controls and see

what are the other options to present

data on the screen so let's try and put

a chart in this area so I put a chart

over there and when I click on it I can

go to its block properties and under

data source again I'll choose the same

data source and then very quickly I'll

go and add a series where the pipe movie

line perhaps let's say bar chart I will

choose X X to be the asset ID and the

y-axis to be health score I'm not going

to go into much detail of this because

this will be covered in the chart how to

use a chart control video on song

anywhere but once I apply and save I can

launch the app again and my daughter

should appear both in the chart and the

grid

now one last things

these are the controls which know how to

display the data source they have their

own way of Miss playing each record that

they receive from your data source the

data grid knows how to display it in

certain lines chart knows how to put it

as bars but what if I don't want to

stick to how these controls are present

there I want to create something on my

own if that is the case what you can do

is you can use a control called data

repeater box I will drag it over here

once it is dried I'm gonna expands the

whole area by default I'm gonna give it

a smaller height for example 70 pixels

now what I want to do is for each record

that might a social dance I want to

define how it should look like on the

screen this data repeater box will allow

me to do that by specifying what Dell

source introduced which will be the same

one much like moths that you set and

save it

this box is then gonna going to repeat

itself for every row it's gonna find in

that data source and now I have the

opportunity to define how each line

should look some that is it's done from

the data source so I'll go ahead and

create a bit of a template here for my

data items so in the blocks I'll put a

vertical stack layer I'm gonna quickly

make it so that and then I'm gonna put a

text in it and next I'm gonna put text

again actually I should since I had some

styles are in fashion just long this is

quite depth if you

use your existing styles you can just

clone them don't have to stop every box

again and again now in the last box

let's say I wanna put an indicator right

so I have that layout that layout is

going to repeat itself for every line

that it receives from the data source

now but I want this text will actually

display the text coming from my data

source so I can go to the block

properties and in the appearance change

this text from static to a dynamic value

and then it will give me all the options

that I have in my repeater box so I'll

choose the name to be displayed over

there and for this one I will choose the

health score and for the last one I will

go ahead and choose its color to be

dynamically set by what is being

received as status from the terror

source once I saved this and launched it

I expect to see a lying over here or my

repeater to repeat for every record that

it forms and we can see it is showing

that the template ID I created is being

repeated for every okay and that's how

you choose yourself how each item in

your - source should be represented or

displayed on the screen so that was a

video on how to use the sources and bind

them to certain controls

thank you so much
</details>