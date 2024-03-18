# how-to-use-stream-host-local-variables---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=Xw1Vvbwpk-o" %}



Learn how to use stream host local variables in the XMPRO Data Stream Designer.  

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
<details>
<summary>Transcript</summary>Learn how to use stream host local variables in the XMPRO Data Stream Designer.  

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
variables are a useful way to reuse the

same setting value across different

stream objects

it is possible to override these values

on the stream host to individualize

their behavior

this video will show you how to do this

as well as provide an example of why you

might want to

as an example this sql stream object

uses these three variables to connect to

and insert data in an sql server

database

the stored procedure it is using will

read and insert the name of the database

user making the change along with the

data

we can use this to identify which device

created which records

by creating a user for the device and

overwriting the login information

using local variables

navigate to the collections blade and

select your collection then select the

variables command

this page will display all of your

company's variables

for our example we want to override the

user and password fields

just like regular variables if the

variable is encrypted the value will be

hidden

any variables that are left empty will

keep the non-local variable so we can

leave the server variable alone without

breaking our stream

click download to create the variables

file that we need

we could also upload a variables file to

displayed if we want to make a few

changes to the variables that are

already there

upload the variables file and click

apply

if you make a mistake while editing you

can click reset to restore the

original values from the file once you

are done editing click download as

normal

or to start from a blank slate again

click upload and then clear

the stream host will read the variables

file from its data subfolder

create the folder if it does not exist

already and copy the variables file here

the stream host only reads the variables

file when it first starts up

and most stream objects will only read

their variables once when the stream

begins running as well

therefore you need to make sure to stop

and restart the stream host after you

have made changes to the variables file

in order for the changes to be applied

let's publish the stream and see the

results

as you can see the local variables have

taken effect logging in our device user

to insert several records

this has been how to create and apply

local variables to your stream host

thank you for watching
</details>