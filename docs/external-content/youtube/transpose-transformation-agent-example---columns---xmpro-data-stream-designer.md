# transpose-transformation-agent-example---columns---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=UMMBuUbUR0M" %}



Follow this step-by-step example to configure the Transpose Transformation Agent in the XMPro Data Stream Designer.

Need help with creating your XMPRO Data Streams? Visit https://documentation.xmp...
<details>
<summary>Transcript</summary>Follow this step-by-step example to configure the Transpose Transformation Agent in the XMPro Data Stream Designer.

Need help with creating your XMPRO Data Streams? Visit https://documentation.xmp...
this example demonstrates how to use the

transpose agent to convert granular

columns into a row per asset and

parameter

first drag the agent onto the canvas

link the input to the stream data and

output to clean name

rename the agent

save the data stream and click on the

agent to configure it

change the type to columns

keep the date

add a transposed column for sensor 1 tag

1 its name is transposed to crusher and

value to tag 1 column

add another for sensor 1 tag 2 named

crusher

and value in the tag 2 column

add another for sensor 2 tag 1 named

crusher and value in the tag 1 column

last one for sensor 2 tag 2 named

crusher

and value in the tag 2 column

apply the changes

save the data stream

publish it and let's look at the live

data view

the event is split into a row per

transposed column that includes the

static column the transposed columns

header value and null value for other

transposed columns

the calculated field is handy to remove

tag in the asset name and the group and

merge to collapse the null values

resulting in one row per asset

you can download the files below to try

them out yourself and for more

information about this agent's

properties head to the configuration

page thank you
</details>