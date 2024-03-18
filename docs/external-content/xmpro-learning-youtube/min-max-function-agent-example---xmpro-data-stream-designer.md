# min-max-function-agent-example---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=1ItuZrtrI_g" %}



Follow this step-by-step example to configure the Min/Max Function Agent in the XMPro Data Stream Designer.

Need help with creating your XMPRO Data Streams? Visit https://documentation.xmpro.com...
<details>
<summary>Transcript</summary>Follow this step-by-step example to configure the Min/Max Function Agent in the XMPro Data Stream Designer.

Need help with creating your XMPRO Data Streams? Visit https://documentation.xmpro.com...
this example demonstrates how to use the

min max agent to group a batch of pump

data by asset id and output the event

per asset with the lowest x reading

first drag the agent onto the canvas

link the input endpoint to the batched

pump data and the output to the printer

save the data stream

and click on the agent to configure it

group by asset id

keep the aggregation type as minimum

x for the aggregation column and return

all columns

apply the changes

save the data stream

publish it

and let's look at the live data view

for every batch of six records with

three per asset the event with the

lowest value for x is printed per asset

you can download the file below to try

it out yourself

and for more information about this

agent's properties head to the

configuration page thank you
</details>