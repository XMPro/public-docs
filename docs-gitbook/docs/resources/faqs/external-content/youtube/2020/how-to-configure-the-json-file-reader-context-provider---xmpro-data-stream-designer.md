# How To Configure The JSON File Reader Context Provider - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=24RK435NMts" %}

Learn how to configure the JSON File Reader Context Provider in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>what we are going to do here is look at

how to set up and configure the JSON

file reader agent the purpose of this

agent is to read a JSON formatted file

containing an array of Records and

provided us context to the rest of the

data stream to see this agent start by

adding it to the canvas to do this go to

the toolbox and search for Tyson you

will find it under contacts providers

click on the agent and drag it to the

canvas you will see that a default name

will be given to it to rename this agent

click on the white space and start

typing click somewhere else in your

canvas and click Save now you need to

configure this agent to do this

double-click on the agent to open the

configuration page first make sure you

using the create collection if you'd

like to change this select another

collection from the drop-down next you

need to set your polling interval I'm

going to set this to 30 seconds because

this agent it's a contacts provider it

will get the data it needs from the JSON

file installed in memory setting this

field to 30 seconds will result in this

cache being refreshed every 30 seconds

next we'll have to provide the file path

to your JSON file and lastly you need to

specify your parallel definition which

is just the names of the attributes in

your file

you

when you're done click apply and click

Save to run your stream click on publish

to view the live data click on my view

selector jason's file and click Save

and there you can see the data starts

coming through
</details>