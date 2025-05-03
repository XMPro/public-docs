# Use Case Versioning - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=MiHNlcNSfZA" %}

Learn how to use use case versioning in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>welcome to another training video from

Exim crow in this video we will look at

use case versions and how to use them in

Dallas game designer so you would notice

that when you're on the scanner screen

for any use case there is an option for

versions over here first of all why

would you use them there might be a

scenario where you have a string which

is published and running in a production

environment as you know it's the canvas

would not allow you to make a change to

a running or a published stream but you

may want to do another iteration on it

or a new version of it if you stop the

stream in order to make those changes

you will be stopping maybe a business

critical data stream or a flow to avoid

that what you can do is you can create a

new version that way your existing

stream can still be published and be

running while you work on the next

iteration of it and will also prevent

you from making a change to your

production or your running

use case which may result into some

unintended behavior if you create a new

version you would at least have a

rollback point or a check point to go

back to and recover what you had earlier

so you would notice I have a stream here

and the version I have open is 2.11 if I

go in the versions I can see list of all

the versions of this use case the first

thing that I can do is I can click on a

version this is selected and then I can

copy it but that will do is it would

create me a new major version which will

be the copy of the last one but it will

be a new version as you can see it has

created a 3.0 for me if I go back in

versions you could see that now I have

two versions you would also notice that

there is a current indicator written

next to 3.0 that is basically telling

that I

currently on 3.0 and my canvas an

important point to note is that whenever

you open a use case it will always open

the latest version similarly if you

export a use case or clone it they will

always use the latest version now if I

have a certain version version that I

want to look at other than the latest

one I can select it and click open that

will take me to that version um if that

version was running or published you

would notice it over here that it would

say published version 2.1 1 and also in

the list over there you will see a green

indicator showing that that word and is

published if I go to my latest version

and assuming I have made some changes

here and now I want this version to be

published I can simply click publish and

in one click it would go ahead unpublish

the old one and replace it with this one

replacing my replace I mean it was

publish this and now in the version we

would notice 3.0 is running 2.1 one has

been stopped so this is use gates

versioning and how you use them in the

data stream designer thank you so much

for watching
</details>