# How To Configure The Twilio Action Agent - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=jSXn2Y_zdxY" %}

Learn how to configure the Twilio Action Agent in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>we are going to do here is look at how

to set up and configure the Twilio

action agent this agent allows a user to

send an SMS to a mobile number I already

have an event simulator set up and

configured which will simulate

temperature readings coming from a

sensor then I have a data conversion

agent set up and configured which will

convert the temperature readings to the

entire time

lastly I have a filter which will filter

all temperatures that are higher than

100 degrees if there are higher than 100

degrees I want to send an SMS to someone

so go to the toolbox and search for

Trulia you will find it on the action

agents click on the agent and drag it to

the canvas connect the output endpoint

of the filter agent to the input

endpoint of Julia agent and note that

the default name has been given to the

Strela agent you can rename this agent

by clicking on the white space and start

typing click some mouse on your canvas

and click site

to configure this agent double click

connect

first make sure you using the correct

collection if not select another

collection from the drop-down next you

need to add your account ace ID then at

your authentication target then you need

to add the number the SMS is going to be

sent from

at the number the SMS is going to be

sent to press enter now you need to type

your SMS message now that you can use

placeholders in your message using the

example alarm when you're done typing

your message click someone else on the

phone

now that I've added the placeholder

called temp in my message and that this

placeholder got added to the placeholder

script when I click somewhere else on

the phone

be sure to map all your placeholders so

that I could get the correct values I'm

going to map it attempt which is a field

that is coming from my filter agent

click apply and click Save you can

verify if your stream has been

configured correctly by clicking on

integrity check none of my agents are

marked with red which means everything

is configured correctly to run the

stream just click on publish
</details>