# How To Configure The Join Transformation - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=BtUbXjkEiDQ" %}

Learn how to configure the Join Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>we are going to do here is look at how

to set up and configure the join

transformation agent this agent joins

data arriving from two payloads into one

single payload I already have two sequel

server context providers set up and

configured which will get products and

they purchase orders I also have an

event printer set up and configured

which will show us what the data looks

like after the join has been performed

go to the toolbox and search for join

you will find it under transformations

click on the agent and drag it to the

canvas connect one of the contacts

providers output endpoint with the left

input endpoint of the join connect the

other contacts providers output

endpoints with the right input endpoint

of the join connect the output in front

of the join agent with the input end

point of the event printer agent note

that a default name has been assigned to

this agent to rename this agent click on

the white space and start typing

you

click somewhere else on your canvas and

click Save

double click on you join agent

this is where you will be configuring

your agent first make sure you using the

great collection

if not select another collection from

the drop-down

next you need to choose which columns to

select click on the tag box and select

them from the list

you

click somewhere else in the forum now

you need to select which type of join

needs to be performed options available

include inner join outer join left outer

join and right outer join I'm going to

choose in a joint if at most one match

per record should be returned

select the checkbox if the data coming

from one of the endpoints needs to be

treated as context in other words

reference data select the context

provided checkbox then you need to

choose your endpoint either left or

right

I can't easily leave this item object

next you need to specify what the joy

needs to be performed on click on the

plus to add in euro click on maximize to

make the page bigger on the left you

need to select your left column the

clause I want to add is where the left

product I ID equals the right product ID

so I'm going to select the left product

ID next I'm going to select my operator

equals and then I'm going to slip my

right column which is product ID click

some nails on the phone next you can

configure the dative unit and the date

of max when configuring this the context

provided box should be unchecked I'm

going to set my tightest unit to second

and my died of max 210

what this is going to do is if a record

comes in at either the left or the right

the record will be made to wait ten

seconds before it becomes available

click apply click Save now I want to run

my stream so I'm going to click on

publish the view live data click on view

and select event printer click Save

maximize the page

you
</details>