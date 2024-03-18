# how-to-configure-the-run-recommendation-agent---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=CeRv2N64c-o" %}



Learn how to configure the Run Recommendation Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.co...
<details>
<summary>Transcript</summary>Learn how to configure the Run Recommendation Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.co...
okay so what I'm going to show you is

how to set up and configure the run

recommendation agent now before I want

to do that I just want to give context

around how you can use this agent now if

you look in front of me I have a CSV

file open and where you can use the run

recommendation agent is for example I

have weights of different packages that

have been weighed which I want to add up

and then I want to compare whether it's

the same as a balance that has been

given to me if it's not the same I can

go and set up a recommendation in app

designer that's that says that if it

differs by more than two kilograms the

Red Alert needs to be issued if it's

listened to kilograms a yellow alert

would be issue would be issued now to

set this up

firstly what you need is an agent to

provide data to the run recommendation

agent and then what you need to do is

you need to go to your toolbox and

search for the agent you'll find an

under action agents or functions and you

can just click on the agent and drag it

to the canvas clear your search connect

the output end point of the first agent

to the input end point of your run

recommendation agent now to rename this

agents just click anywhere inside this

little block and start typing then say

if your data stream how to configure

this agent just click on it and click on

configure first you need to make sure

that you're using the correct collection

if not just select another one from the

drop-down then there's a space that says

server and it has a URL that you need to

provide now the URL that you need to

provide is the URL that points to app

designer so I have app designer open and

I'm just going to copy this URL and

paste it in here then there's also a key

that you need to provide this you'll

also find an app designer so I'm just

going to go to app designer click on

settings get my key and copy that

and place my key in here then you have

an option that says output on first

occurrence only now this option is

self-explanatory now what this does is

it ask you do you want to run the

recommendation just on the first

occurrence given a specific condition

that you've set up in a designer then

you need to specify your identifier now

I have already set up the csv agent and

this is the idle has a number of fields

such as reading knowledge and

temperature temperature units operation

in the description and my identifier in

this case would be my reading number so

this would be a unique number lastly you

need to specify the columns that you'd

like to have returned so you can just

click on the tag box and select all the

columns that you'd like to return I'm

just going to click select all and then

click apply and save my data stream

thank you for listening
</details>