# How To Use Lookup - XMPRO App Designer
{% embed url="https://www.youtube.com/watch?v=PadQkX7qp8U" %}

In this video, you’ll learn how to configure a lookup in the XMPRO App Designer.

Need help with creating your XMPRO apps? Send an email to support@xmpro.com

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>hi and welcome to another training video

from xm pro

today we will be looking at how to use

the lookup component

as a prerequisite you should have

already gone through the video on how to

create and use data sources

if not then i recommend doing that first

the lookup component can be found in the

basic blocks section

you must give the lookup a data source

this can be

static items or a dynamic data source

if you choose static items you can add

items in the grid here

and those will show up in the lookup

or you can give it a dynamic data source

from

the page data data sources

if you give it a dynamic data source you

must go into data

and then select the display value and

group by expressions

group i is optional

so i won't set it for now if you set

group by

it will group the options by the group

by expression

so if i don't select a group by

expression

then it'll show all the items just like

this

and if i do select a group by expression

then it will group them

there are some appearance properties to

play with

visible is self-explanatory this can be

bound to

apparent data source styling mode if you

select

outlined it will create an outline

around your control

underlined will create an align

underneath the control and filled

as you can see we'll give it a gray

background

placeholder will appear before you enter

a value

drop down title will give the drop down

of

of the lookup a title at the top

tooltip will show when you hover over it

if you check show clear button then if

it has a value

it will have a button in the drop down

that says clear

and if you click that clear button it

will

clear the value

in the behavior section we have read

only if this is checked then

you won't be able to enter a value into

the control and it will appear as if it

was read read-only with a dotted border

around it disabled is again

self-explanatory

if you check it if you set it to true

then the control will be disabled and

grayed out and you

also will not be able to enter a value

and

enable search enables the search bar in

the drop down

so we can see there's this the

placeholder please select a task if i

hover

over it then we get the tool tip

we've got the title and the search bar

and the clear button

the value can be bounded to a parameter

or a variable

or from a parent data source so for

instance if i add a field set in here

i give the field set a data source task

progress

i only need two rows so i'm going to

delete this one

we've got task

and progress and we're going to put the

lookup in task

we're going to put a slider for progress

i'll just set up the range slider as

this isn't part of the video

and then for the lookup value we can

bind it

to task of the task progress

and then save so now we will have one

field set per row

of the parent data source

which has two tasks

the type the progress for task create a

game plan

is zero and the task for and the

progress for the task research the topic

is 10

so we can change this task to do the

need for

and change it to 44 done

and if we save this then it will we'll

change that in the database

and we also have validation more detail

can be found

in the validation video

this has been how to use the lookup

control
</details>