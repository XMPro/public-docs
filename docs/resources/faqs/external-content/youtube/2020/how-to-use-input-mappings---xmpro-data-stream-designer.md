# How To Use Input Mappings - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=sBANCrqrw_4" %}

Learn how to use input mappings in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>welcome to another training video from

Exim pro today we will be looking at

input mappings what they are and how to

use them interesting designer so what

our infant mappings infant mapping is

the way an agent uses to define the sort

of inputs it would it would like to

receive one once an agent has defined

that structure of payload or input that

it acquires they need to be mapped and

that is where infant mappings come in

mostly you would notice that action

agents would have input mappings on them

first of all the documentation of the

agent would explain them but you can

also click on the arrow that is leading

into an agent and you will notice that

this configure button with will get

enables whenever that agent requires

input mappings so how do you configure

them you can either double click on the

arrow or you can click the configure

button after you have selected the arrow

and you will notice that the screen will

show up you can maximize it to work with

the screen and over here you will see

there are two sides right hand side

basically lists all the inputs that this

agent is expecting on the left hand side

you would see all the properties that

your preceding agent is sending its

sending in and you can then go ahead and

map them to map them you simply select

the option from the drop-down and then

the mapping is done and then you can

save by clicking on the apply and then

save your use case for them to persist

now if you look at some of the advanced

options in there you would notice that

across the top over there you have a few

options first of all we have an option

to say let's say if you want to filter

this list and to only show the ones

which are unmet so you can click on that

and you'll see they know that only the

unmapped rows are not visible this is

very useful if you had a big list let's

say this agent was

hundred or more inputs then and there is

only one that is unmapped so finding

that through a big list would have been

a problem and that's where you can use

this filter next we would notice that we

also have an automatic feature which

basically if you click on it would try

and find if there are any direct matches

it can automatically do for example it

found that on the left hand side it has

an option coming in called time stamp

and on the right side the same option is

being expected so it would automatically

make that mapping you would also notice

here that some of the options are

automatically disabled they are disabled

because the ton of those items don't

match the input that is being asked over

here a handy tip here would be if you

want to map something and the type

doesn't match you can simply go ahead

and drag data conversion transformation

which will let you convert the data type

of your attribute and then you will be

able to map them getting back to the top

bit over here you will see we have

another option which says match my

expression starting with the prefix

option where you choose what the prefix

should be so what that will do is let's

say I say device underscore is my prefix

and I click OK it will go ahead and try

to find items which match if that prefix

is added to the right hand side so it

went ahead and found device underscore

pressure would match pressure and it has

put that in again these are the things

which would help if you had a mess of

this list here similarly we have options

for postfix where you can type in the

postfix and it will do rest of the

mething for example I can do that and

you'll say and you'll see it has done

vibration underscore current to the

vibration and lastly and we have an

expression option where you can define

an expression for example if I want

let's say device underscore and wherever

you want to substitute the right-hand

side you would put dollar 1/4 for that

expression and then you can type in the

rest of your expression so what this

will do is it will try to match any

property coming in which is device

underscore name of the right-hand side

which is expected underscore change you

will notice that it has mapped it has

mapped device underscore temperature

underscore change to temperature here so

those are some of the advanced options

here and that is basically how you use

input mappings I hope this was helpful

thank you so much for watching
</details>