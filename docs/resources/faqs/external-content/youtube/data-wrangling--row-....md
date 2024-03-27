# Data Wrangling: Row Transpose - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=753z0e0pHdc" %}



Learn how to transpose a dataset in the XMPRO Data Stream Designer to convert rows into columns or vice versa.

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com...
<details>
<summary>Transcript</summary>Learn how to transpose a dataset in the XMPRO Data Stream Designer to convert rows into columns or vice versa.

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com...
good and welcome in today's video we're

gonna go through over the data wrangling

we're going to be focusing on raw data

transpose before we go into an example

of that what is data transpose

transposing a data set means converting

a row of data into columns or vice versa

ultimately it's focused on a particular

problem so the problem statement for

this particular data wrangling is when

I'm receiving data by row per parameter

for multiple assets so I'm getting

multiple rows of data coming in how do I

pass a single asset with multiple

parameters to a downstream agent for

example a predictive model or any EAM

integrations to further explain that

what we want to do is we want to go from

multiple rows to a single row for the

asset but with multiple parameters ie

multiple columns

so to do that let's open up an example

and walk through some of the details of

that so the first thing I've got is I've

just got a blank data stream here and

we're going to create this to see the

different results using some of the

transformation agents that we have

before we go into that this is an

example of the data that I'm going to

use this is just a normal CSV it has

just got three columns as a trigger type

and a value and using this I'm going to

create a data stream to just show you

how you can actually wrangle this into

multiple columns and group are the

particular asset themselves so the first

thing that we're going to do is we're

going to drag it on a CSV listener I'm

just going to name it properly

and we're just gonna save that we're

gonna keep this very simple and we're

just going to output it so we can

actually see what does this data look

like coming from the CSV file itself

so now we've got the basic structure of

our data stream set up and configured

what we're looking to do now is this

double-click the CSV we've got our

default collection we've got our default

interval we've only got four records in

there and the CSV reader it takes one

record every 10 seconds based on the

interval here I'm just going to change

this to 5 we can click our select file

and what you'll notice is the CSV list

or actually automatically go through the

file and it'll work out

my definition for me as well so I can

click apply here we can click Save and

if we keep publish and go to the live

view we can actually see what is the

resulting data for this look like

so as you can see every five seconds

we're going to get a record coming from

the CSV listener itself once the CSV

Lister runs out of data we're not going

to get any more records coming in for it

what we want to do is we want to

actually change this now we want to

transpose them so I would like the

pressure and the flow pressure to

actually be columns versus rows so let's

unpublished that what we're going to do

is let's just create a new version for

this and it's going to transformation if

we scroll down to the transpose we'll

just drag that in and we'll just

configure that up again make sure we've

got our name correct so we are gonna

transpose rows to columns and we're

still going to keep the resulting data

set so that we can actually see the data

coming in if we double click the

transpose agent the default is row you

can do columns as well for this video

we're just going to focus on row we want

to group by asset the static columns

ieave which columns do we want to stay

the same in the same order

we'll just keep acid in there as well

the field we want to transpose this

value if I bring you back to the value

is the field that we want to transpose

we want pressure head and flow pressure

to actually be the column names

themselves so field to transpose value

Row 2 transpose will be trigger type and

right at the bottom here what are the

values that it's expecting so pressure

head is the first one and flow pressure

is a second one what it's going to do is

it's going to try and match these two in

the data coming in and it will use that

to convert the road to a column or if

you select the alternate transpose type

it'll do the inverse of that

let's click apply we click save and

let's click publish to see what that

looks like

the first one we just had the CSV going

straight to the resulting data the

second version what we've actually done

here is we've put a transpose in the

middle and we are transposing the

multiple rows into the different columns

and having a look at some of the data

coming out the first thing that you'll

notice in the data coming out is I'm

only getting individual records coming

out what I'd actually like to do is

group them a lot closer to each other

so instead of having to pump two records

coming up I'm actually gonna get one the

same with pump one if I unpublish this

then I republish it together to start

from the beginning of the CSV file

you'll see pump 1 has got its pressure

head pump tours has got its pressure

head and these are coming in at five

second intervals so because of that five

second interval for these new records it

thinks that they are different records

and we actually need to bring them

together so what we're going to do to do

that is if we unpublished this again I'm

just going to create a new version of

this so we can come back to it later

what we going to do different here is

we're going to drag a window on we're

gonna window the data before we actually

pass it through to the transpose and we

are gonna wait for all the data to come

from the CSV before we actually

transpose it so we're just gonna call

this from now we're just going to save

that and if we double click that what

we're interested in is 20 seconds for

records coming in a 5-minute intervals

our size here is gonna be 20 seconds

that we want to actually wait for we can

leave the rest of the settings as

default and now we can save them now if

we run this and go to live view

previously we were getting a record

result coming through every 5 seconds

this time round it's actually going to

wait for 20 seconds then it's going to

pass it to the transpose agent to

convert the rows to columns and then we

will see the results coming out in the

window

the top right

and there we go so after 20 seconds its

buffered the data coming in it's past

that to our transpose agent and now it

can group by them properly and it can

create them into their specific columns

properly if you all remember if we come

back to the excel sheet so this is what

our input data looked like we had

pressure head for pump coming in we had

flow pressure coming in and what we

wanted to do is take that transpose it

so instead of two rows we're going to

get one row of data with multiple

parameters coming in now I can use this

further downstream and I can actually

pass the pressure head to a predictive

model or the pressure head and the flow

pressure to a predictive model is how we

configure a transpose using a data

stream in excel problem
</details>