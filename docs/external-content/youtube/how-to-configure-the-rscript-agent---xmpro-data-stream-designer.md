# how-to-configure-the-rscript-agent---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=ldr4jdBJqwQ" %}



Learn how to configure the RScript Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if...
<details>
<summary>Transcript</summary>Learn how to configure the RScript Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if...
but we are going to do here is look at

how to set up and configure the a script

agent this agent allows you to perform

computations using the on language on

data it receives as input I already have

a CSV listener set up and configured

which will get data for us from a CSV

file which the our script agent can uses

input to add the a script agent to your

canvas go to the toolbox and search for

our script you will find it on the I on

machine learning click on the agent and

drag it to the canvas you'll see a

default name will be given to it to be

name this agent click on the white space

and start typing now connect the output

end point of the first agent to the

input end point of the second click

somewhere else in your canvas and click

Save to configure this agent click on it

and click on configure first make sure

you're using the correct collection if

you'd like to change this select another

collection from the drop-down next

you'll notice notice that there is a

bulk input option the Oscar languages

main strength lies in statistics and

graphics and it can handle large sets of

data take advantage of this capability

select this option this will cause every

event to be inserted into a single data

frame called input as you can see from

the description below next you can add

your code the temperature field derives

reference here comes from the preceding

agent the average field arrive reference

here is a new variable which means I

have to scroll down on this form and add

it to the outfit script to do this click

on the plus to add a new row and specify

it here

choose its data type in my case it will

be double-click something else on the

form when you're done writing your code

and you're happy with it and you've

specified all the variables you're going

to use in the outputs grid you'll see

that there's another option on this form

name payload this will define how your

pilot will be forwarded to it the next

agent there's three options available to

you the first same is existing the

structure of the input payload look the

same as the structure of the outgoing

payload meaning no columns have been

added or removed existing with addition

the structure of the input and the

output payload will contain the same

columns but everything that you've

defined in the outputs will be added to

that new will contain only the columns

you've defined in your output I'm going

to leave it as existing with addition

then I'm going to click apply and click

Save to double check if you've

configured your stream correctly click

on integrity check if none of your

agents are highlighted in red it means

everything is fine you can now go ahead

and run your stream by clicking on

publish to view the live data click on

live view select your own script agent

click save and give it a second

to expand the page click on maximize and

you can see that the column has been

added for our applet

and publish the string to stop it click

on your a script I don't think click on

configure again now I'm going to uncheck

this box meaning that the script that's

in here is going to be executed for each

event it receives this also means that

how you write your code is going to look

a little bit different the demonstrate

how this works if this bulk input option

is not checked I'm just going to add

some code in here this will convert this

temperature which is currently in

Celsius to Fahrenheit hence I've

declared a new variable temp F which I

now need to add to the bottom first I

need to delete my average variable

I've add my new output variable now I'm

going to click apply click Save double

check if my stream has been configured

correctly but clicking on integrity

check none of my agents are highlighted

in red which is good so I can publish my

stream by clicking on publish then click

on the live view as you can see my data

start coming sir then if my output

column has been added and the script

that I've added is executed event that

is coming through
</details>