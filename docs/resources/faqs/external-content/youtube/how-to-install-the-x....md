# How To Install The XMPRO App Designer
{% embed url="https://www.youtube.com/watch?v=1nBPeI3dyoI" %}



Learn how to install the XMPRO App Designer. Download the installer from https://docs.xmpro.com/
Download Installation profile as per the instructions at https://docs.xmpro.com/docs/subscription-ma...
<details>
<summary>Transcript</summary>Learn how to install the XMPRO App Designer. Download the installer from https://docs.xmpro.com/
Download Installation profile as per the instructions at https://docs.xmpro.com/docs/subscription-ma...
in this video we will be looking at app

designer installation

in order to install that designer there

are some prerequisites

first of all you must download the

installer from this website

and then you need to have the

installation profile from your

subscription manager

instructions on how to download an

installation profile can be found in

this link

next we will need to have sql server

2014

for a later version available

if you're installing onto an is that is

that you are running the installer

from the machine which has iis on it

and that's where you want to deploy and

of course you need is

7.0 or later you will need to have

dotnet core 3.1 module installed on the

is

and also https and web circuits enabled

if you want to install to a folder um

which is that you want to create some

sort of a deployment package and we'll

then deploy it onto maybe

cloud or some other server which is not

directly accessible by the installer

and all you need is the dns name now

once you have downloaded the installer

you can double click on the exe

and this will now set your machine up

for the installation

once it completes you should go to the

start menu

and search for app designer

and run it as administrator

click on next button and then choose to

install

choose the components you want to

install in this case i will choose both

database and the web application

you can then choose if you want to

install to an is or a folder

i'll show you both options let's choose

iis first

now we need to provide the database

server details

first of all i will provide the sql

server

which in this case for me in app is in

azure

next we should provide some

authentication details

for our user that we will be using to

install but also

configure our application

next you must choose the database that

you want to install on

you can choose to create a new database

however if you are installing on azure

or

cloud platform then it's best to have

the database already created

even if it's just blank

i'll choose an existing database that i

created and then click next

on this screen i'm supposed to provide

the is server details

i can choose the name for my application

pool

which security account it should use and

then the dns name under which this site

is going to be installed

if you want to install as a subdirectory

you can provide the version directory

name over here

click next to continue and you will then

be asked for

the installation profile now let's

backtrack a bit

and look at the other option which is

folder

now on this screen you will notice since

we chose to install to a folder it is

asking me

where where we should install i can give

it a path which must be an empty

directory

next i need to provide the dns name

that's the name under which it is going

to be running

on the server you can then choose the

application name

this is required um for the subscription

manager to uniquely identify this

installation that you're about to do

you can also add the virtual directory

um if you want to and then

the url it will set up will be the dns

name slash

this name

clicking on next will bring us back to

the same screen we were on before

where we are supposed to provide the

installation profile

i'll upload the installation profile and

next

i can choose to create the subscription

by default

to the account that i'm going to use to

install app designer

if you don't want that to happen you can

leave this unchecked

clicking on next

will make the installer ask for the

credentials it should install

under these credentials must be of

your super admin which is an admin user

on excel pro company

on your subscription energy once you

have provided that

you're ready to install click next for

the installation to proceed

once the installation completes you can

finish the installer

and now your database should have been

set up on the sql server you provided

and the folder path that you used to

install

would now have all the all the required

files

if we had installed on iis our ios would

have

already been set up and we would be

ready to browse to it now

however since feature is installed to

folder

we can now zip these files and deploy

them onto the server

if you're using a key vault or a key

store to store config settings on

cloud you can modify the app settings

form here as per the documentation

found on the dock side to replace

the config with your keystroke

parameters

it is a good idea to keep this path and

folder on your machine

so that next time you can upgrade the

same installation

when the new version comes around

so that is how you install app designer

you
</details>