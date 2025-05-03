# How To Configure The MQTT Listener - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=qJHRCuD59hE" %}

Learn how to configure the MQTT Listener in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>when we are going to do here is look at

how to set up and configure the MQTT

less than agent this agent allows you to

listen to or read I deposit to a channel

in MQTT I already have an event printer

setup and configured which will allow us

to look at what the output data looks

like go to the tool box and search for

MQTT you will find it under listeners

click on the agent and drag it to the

canvas connect the output end point of

the mqtt agent to the input end point of

the event printer agent after the

default name has been assigned to the

MQTT agent to rename this agent ik on

the white space and start typing

click somewhere else on the canvas and

click Save

double click on your MQTT ident this is

where you'll be configuring your mkdd

agent

first make sure you using the correct

collection if not select another

collection from the drop-down next I

need to configure my settings for MQTT

start by adding your broker address I'm

going to use a public broker next you

need to add your topic I'm going to use

amputated effects to post the values to

mqtt thus I need to make sure that the

topic that I enter in here corresponds

with what I configured in the amputee

the effects

if you'd like a clean session to be

started make sure this checkbox is

checked next select the format of your

payload which can be either hex or JSON

I'm going to leave it as Jason if your

jason has a nested structure in its

payload make sure this checkbox is

checked if it hasn't necessary we'll

have to specify the name Jason path and

type if it doesn't have a nested

structure you only need to specify the

name and type of your attributes click

on the + to add a new row and as your

attributes

I'm going to add temperature

and vibration each having a data type of

double-click someone's on the phone

click apply and click Save now I want to

run my stream so I enter click on

publish to view the live data click on

live view selecting event printer and

click Save in mqtt effects I have

connected to the test server which is a

public broker now I want to post values

on this channel to mqtt

let the format isn't Jason click on

publish

and that the data came through in the

live you
</details>