# How To Pass Parameters Between Pages - XMPRO App Designer
{% embed url="https://www.youtube.com/watch?v=z7jsXESzXCY" %}

In this video, you'll learn how to pass parameters between pages in your XMPRO apps.

Need help with creating your XMPRO apps? Send an email to support@xmpro.com

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>hello and welcome to another training

video from Exim Pro today we'll be

looking at how to pass page parameters

between pages as a prerequisite you

should have already gone through the

video on how to create app pages and

navigation if not then I recommend doing

that first I've created an app with

three pages the landing page navigates

to a secondary page which navigates to a

tertiary page but what if I wanted these

pages to pass some information between

them the way to do this is with page

parameters parameters are like slots on

a page that another page can put some

information in inside to create a page

parameter go to page data on the command

bar and press + next to the parameters

heading then enter the name of your

parameter and the type to make use of

the information that the page will be

passed we can use dynamic values for

example I'm going to drag a text box a

text block into the page click on it go

to the blog properties and appearance

change the static value to a dynamic

value then select the parameter that

we've just created now to send the data

over I'm going to go to the landing page

select the button go to block properties

and go to the action then I'm going to

press the pencil next to past page

parameters and there's the parameter

that we just created so for this value

I'm going to send through I have to

landing page and apply and then I have

to save this page now if we run this and

then I click go to a secondary page it

says I have been to the landing page if

we go into the edit and then launch this

page it will give you all the parameters

that you have on this page to enter info

into so I can say anything here and then

it will launch the page as if this page

had been past that and for info from a

different page now if we want to send

something dynamic to the next page for

instance whatever this page got as its

parameter we can do that by going to the

block properties of the button and then

go to past page parameters and because

we haven't created any parameters on the

tertiary page we can do that here note

that this creates parameters on the page

that this button is going to and not

this page itself so we create tertiary

info and also secondary info so the

secondary info will be the the parameter

that came from this page which is a

dynamic value and the tertiary info is I

came I have been to the secondary page

so this dynamic info is going to get

passed one page and then to the next

page so I apply that and then safe and

we actually need to display it on the

tertiary page so we'll go in here and

there's already some text here so we'll

make use of this and we'll say private a

secondary info and then we can duplicate

this and then this can be the parameter

tertiary info

now if we run this page straight away

it's going to ask us for this

information and if we launch it from

here it's not going to actually say

anything because we didn't didn't have

any information sent through so we go

back to the landing page we go to the

secondary page which passes I have been

to the landing page and then we go to

the tertiary page which has I have been

to the landing page and I have been to

the secondary page this has been how to

pass page parameters between pages
</details>