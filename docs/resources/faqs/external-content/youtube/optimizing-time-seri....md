# Optimizing Time Series Chart (TSC) Performance
{% embed url="https://www.youtube.com/watch?v=Sm5plue7P2A" %}



In this walkthrough, we explore the key improvements we've made to enhance the performance and scalability of Time Series Chart (TSC), one of our most utilized data visualization tools. We'll...
<details>
<summary>Transcript</summary>In this walkthrough, we explore the key improvements we've made to enhance the performance and scalability of Time Series Chart (TSC), one of our most utilized data visualization tools. We'll...
application designers time series chart

or TSC is one of our most popular data

visualizations

however we found that performance is not

satisfactory with large volumes of data

and as you know this is usually the case

with time series data

all relevant data is returned to the

client for processing so that it doesn't

need to be refreshed

unless certain parameters are changed

but large volumes of data are slow to

return and slow to process on the client

[Music]

we've made changes to the block itself

and released a specialized TSC connector

that only Returns the data points

displayed on that chart

the block sends the requested parameters

to the connector which retrieves the

data from the data source crunches the

numbers and sends back only the data

actually displayed

for example rather than sending 60 000

records for 180 buckets we're only

returning 180 records

this results in a fast and scalable user

experience

the disadvantage of this approach is

that it is repeated every time the chart

is interacted with such as zooming or

changing the asset selection

a CSC SQL connector is available now

and the functionality will be rolled out

for Azure data Explorer and historian

next

you will need the 4.3 release for The

Block enhancement and thereafter simply

load the new connectors as they are made

available

alternatively you can continue using the

original connectors for smaller data

volumes to avoid the load between

interactions

[Music]

have a demo by Dragon another one of our

talented developers of the new connector

in action

we discovered doing a trial run through

that my audio is not going to play or

the audio of the video is not going to

play through from you so

this is my first run through with the

script so let's just see how that goes

when we play the video

this is the new TSC SQL connector

which pulling the selected fields that

we have for this time range

and this interval size

we can see that the request was

returning in less than 400 milliseconds

and the size is 44 45 kilobytes

if I open the request now we can see

that we have 179 records or buckets and

for each packet we have the selected

field with their corresponding Min and

Max values that are actually showing on

this one

now what we've said is if we move the

range it's going to send a new request

the same size in the same time

if we move the range

sorry if we increase or decrease the

interval size we should have double the

buckets
</details>