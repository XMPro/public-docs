# How To Create Recommendation Rules - XMPRO App Designer
{% embed url="https://www.youtube.com/watch?v=AM7tNX23IOs" %}



Learn how to create rules, set up auto-escalation and configure the execution for your prescriptive recommendations in the XMPRO App Designer.

Need help with creating your XMPRO apps? Send...
<details>
<summary>Transcript</summary>Learn how to create rules, set up auto-escalation and configure the execution for your prescriptive recommendations in the XMPRO App Designer.

Need help with creating your XMPRO apps? Send...
hi in this video we're going to continue

with our new recommendation what we're

going to focus on here is how do we add

rules I'll explain a bit about the

execution order and why it's important

as well as the auto escalate before we

jump into that in the solution

development process which area are we

focusing of the three right now we're

focusing on number two the

recommendation creation and the rules

the Assumption here is that you've

already gone through the number one

you've already got some data sources

that have been created and you're ready

to create some of the recommendations in

the rules it's jump into the software so

this is the app designer where we're

going to go to is on the Left we're

gonna go to recommendations and then top

right we're going to open manage

recommendations this will open a list of

all the recommendations that have been

created if we open the one that we've

created previously which would be the

temperature threshold you'll notice that

it is still blank what we want to do

here is we want to add some rules to

this particular recommendation to do

that we click the + what that'll do is

it'll open up a new blade for us on the

right which will allow us to now

configure the recommendation rules the

first one is to give it a rule name the

second is a headline and in a

description now where these all get used

is the rule name gets used when you are

actually within a data stream and you

want to do something with

recommendations read them out see which

ones have been closed not closed so it's

very important to to make sure that

their name implies what the rule is

actually doing I've got a few examples

I'll show you what I mean by when we

when we get there the headline is what

will appear at the top of the

recommendation and in the description is

what will appear in the description of

the actual recommendation where do these

two appear if I go to a list of

recommendations I already have and I

just open one up you'll see here is the

title and here is the description if we

drill into the recommendation across the

top

you will see the title and again you

will see the description so this is

where it will appear and the last area

that it will appear is if I go into a

particular event board you will see

across the top you will have the title

and then underneath it you will have the

description as well so again when you're

configuring your recommendations with

regards to their name their titles make

sure they are something in end-user can

actually relate to and explain what it

is that the rule is addressing a bit

further down we have notification

ranking so you can rank your specific

notification for this rule is it a low

medium or high all that this does is

affect how it appears when you see your

recommendations on the event board side

you can give it a specific icon and you

can start going through some of the

other details here we will follow in a

lot more detail some of the specific

items in here this is more just to give

you an idea of how do I create a new

rule to click the plus and it'll bring

up the rule once you fold everything in

you can click Save and the new rule

appear if I open up an existing rule

that we have already configured what

you'll see here is this is for discharge

pressure and if I click it you'll see I

have two rules that has been specified

for this particular recommendation I

have my name I have my headline and I

have my description the name I can very

quickly see what the rule is actually

about that's one naming your rules is

very important

this is ranked as a high if I click the

out of optimum range you'll see that as

ranked as a medium and what the numbers

actually mean here is you'll see I've

enabled execution order across the top

so what execution order allows me to do

is I can actually run these rules in a

sequence what that means is the first

rule will evaluate if it evaluates to

false it moves on to the second the

second value waits to false it moves on

to the

and so it continues down as many roles

as you've got configured if I was to

untag that you will see both my rules

are available but I don't have numbering

attached to them what this means is as

soon as this recommendation is triggered

both of these rules are going to execute

it exactly the same time if both of them

evaluate to true you are going to get

two recommendations there may be a

scenario when you need to do that if

however your rules need to be very

structured you can use the execution

order for those what you'll notice is I

don't have auto escalate ticked here as

well so what auto escalate does is let's

say you have a scenario where your

second rule which in this instance would

be my my medium ranking one was actually

triggered so there is a current pending

recommendation for this if the data

comes through and your first rule holds

true what the auto escalate will do is

it will close out the first and it will

escalate the rule to the next one so

auto escalate allows you to only have

one recommendation available at a time

for in this instance discharge pressure

if you were to leave it unchecked if

both of these evaluates it to true over

different time spans with different sets

of data you would get two

recommendations coming through as well

so what do we have a look at today in a

prior video we created a new

recommendation so how did we actually do

that here we went through how do I add

new rules to a recommendation and we

also briefly touched on how do I go

through the auto escalate and the

execution order for a particular role as

well
</details>