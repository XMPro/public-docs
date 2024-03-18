# how-to-configure-the-data-conversion-transformation---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=1_2QuS0zyF0" %}



Learn how to configure the Data Conversion Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xm...
<details>
<summary>Transcript</summary>Learn how to configure the Data Conversion Transformation in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xm...
we are going to do here is look at how

to set up and configure the data

conversion transformation agent what

this agent does is allow you to change

the data type of an existing column with

the result being either the values of an

existing column being replaced or a new

column being created I already have an

event simulator agent set up and

configured which will simulate a few

different readings coming from census I

also have an event printer set up and

configured which will help us see what

the output of the data conversion agent

looks like now I want to set up and

configure my data conversion agent go to

the tool box and search for data

conversion you will finally learn the

transformations click on the agent and

drag it to the canvas connect the output

end point of the event simulation to the

input input of the data conversion agent

connect the output in one of the data

conversion agent to the input end point

of the event printer agent default name

has been given to the data conversion

agent you can rename this agent by

clicking on the white space and start

typing

you

click some miles on the canvas and click

Save

double-click on your data conversion

agent this is where you'll be

configuring your agent

first make sure you using the great

collection if not select another

collection from the drop-down now you

have to configure the data conversion

editor click on maximize to make the

page bigger click on add to add a new

row select the column that should be

converted from the input column

drop-down you want to convert

temperatures so I'm going to select

temperature next specify the alias of

the output column if this is different

from the input column a new column will

be created if the values specified in

the input column and output column or

the same the input columns values will

be replaced I'm going to specify a value

that is different from the input column

mostly select the data type the data

needs to be converted to we want to

convert it to in 32 from double so I'm

going to select in 32 and click

somewhere else on the phone nothing you

need to specify how the results should

be returned select an option from the

drop down options available include a

painter current which will paint the

results to the current pilot and new

which will return the results as a new

pilot I'm going to select new let's see

what the data looks like click apply

click save click publish to view the

live data click on live view select your

event printer agent click Save give it a

moment and now that the data is returned

as a nearby load

now I want to see what the data looks

like if I had chosen a pin to current so

stop the stream by clicking on unpublish

double click on your agent again instead

of new select a painter current click

apply click Save publish the stream

again and click on live you

give it a second you can expand the

bytes by clicking on maximize and that's

the difference between temperature and

temp temp is my new column as you can

see the data has been converted from

double to eat

you
</details>