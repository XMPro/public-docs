# how-to-use-the-select-box---xmpro-app-designer-toolbox
{% embed url="https://www.youtube.com/watch?v=rsakkRABMFM" %}



In this video, you’ll learn how to use the select box in the XMPRO App Designer.

Need help with creating your XMPRO apps? Send an email to support@xmpro.com

Go to https://xmpro.com if you...
<details>
<summary>Transcript</summary>In this video, you’ll learn how to use the select box in the XMPRO App Designer.

Need help with creating your XMPRO apps? Send an email to support@xmpro.com

Go to https://xmpro.com if you...
welcome to another training video from

mixin bro today we will be looking at

the control slick box and how to use an

app designer so as you can see I have a

black page here and if I want to add a

select box I can find it under the basic

controls called select box and to add it

I simply can drag it but let me add a

layout control first like that and in

there I will add my select box so as you

know a select box is just a drop-down

which shows the user some options and

which one can make a selection from now

to configure it we have a few options in

block properties starting with

appearance we have a standard option for

to control the visibility of the control

and then we have the standard styling

option which has been explained in many

of the other videos then we have a have

a placeholder which basically says if no

value is specified what should be the

background over the background text or

the placeholder text that should that

should be displayed which can be simply

something like that

and then if no value is specified you

will see that tooltip is

self-explanatory

you just add the text you want to be

displayed when the user hovers over the

control show clear button basically

shows a button which a user can use to

clear the value that he has selected

then if you go to behavior we have

standard options like read-only and

disabled and then we have a spell check

option which basically tells the browser

if the spell check should be enabled or

not enabled on this control now in order

to configure this further we need to

give it some data source as you know a

drop-down is supposed to show a list of

items that are user concern

so I will go in datasource and for this

control we have two options either we

can choose static items or a dynamic

data source adaiah source comes from an

outside third party system why they're

connected but static items can be

defined straight away over here I'll do

that for an example let's say we want to

capture asset type which can be fixed

and fixed can let's say have a value of

1 or it can be movable which will have a

value of 2 so these are the items that I

have defined and they will be displayed

on runtime as a drop-down list so I can

save that much and one last thing I

would like to do is let's say I want to

give it a default value of moveable

which was number 2 so I'll give it that

value and now when we launch this app we

will see that there I have a drop-down

which has two values that can be

selected as we defined and the default

value was moveable I have my Clear

button showing up which I can use to

clear the control and then it will

display my placeholder now let's go back

and look at how we can assign this

control a dynamic data source I'll use

the one I have for example the furnace

one and that's it it has a valid air

source but when you use a dynamic data

source you also need to come in and

define out of that data source

what column or what item should be

displayed as the as the display

expression so basically the data source

might be sending you five columns but

you don't want to display all all five

of them in the control so I can choose

that one name to be displayed and the

value which should be captured should be

the corresponding asset ID so once I do

that and I launch my app

it will go ahead and load that from the

third-party data source the list of

items that it should display and then

you can see that it is displaying the

names but in the background it will be

storing the asset ID and this is how you

bind the control with an external data

source lastly if this control was part

of a data source bound container for

example this container which I have

given some data source to I can then go

ahead and bind its value to a dynamic

item which is coming from my data source

and then it will take the value that is

sent by the live external source so this

is how you use a select box in app

designer thank you so much for watching
</details>