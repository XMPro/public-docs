# Join Transformation Agent Example - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=HTsVVEpwyhQ" %}



Follow this step-by-step example to configure the Join Transformation Agent in the XMPro Data Stream Designer.

Need help with creating your XMPRO Data Streams? Visit https://documentation.xmpro.co...
<details>
<summary>Transcript</summary>Follow this step-by-step example to configure the Join Transformation Agent in the XMPro Data Stream Designer.

Need help with creating your XMPRO Data Streams? Visit https://documentation.xmpro.co...
this example demonstrates how to use the

join agent to combine the leftleg's pump

event data with the right leg's

contextual data using an inner join on

the pump id to return a combined payload

first drag the join agent onto the

canvas link up the left endpoint to our

streaming events and the right to our

context

and the output to the printer

move it into position

save the data stream

and click on the agent to configure it

select context for the behavior and our

context comes from the right endpoint

tick to apply prefixes only on

duplicated attribute names select all

the attributes

accept the duplicated pump id

add an inner join

on the pump id attribute

our identifier has the same name on both

legs so prefix is added to identify its

source

apply the changes

save the data stream

publish it

and lastly let's look at the live data

view

you can download the files below to try

it out yourself and for more information

about this agent's properties head to

the configuration page

thank you
</details>