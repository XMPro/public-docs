# How To Do Integrity Checks - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=K-XQ1rp5ljM" %}

Learn how to do integrity checks in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>the integrated check-in data stream

designer is a valuable asset allowing

you to validate the settings in your

stream objects with one click this video

will demonstrate how to perform an

integrity check in how to interpret the

results an integrity check is performed

by clicking the integrity check command

in a designer blade it cannot be

performed in on data streams that have

been edited so save your work or discard

changes first it is wise to perform the

check whenever you complete a stream and

also just before publishing to catch

mistakes in configuration before they go

live once clicked the stream objects

will begin showing a loading bar once

all the loading bars have disappeared

the integrity check is complete

depending on how complex your stream is

this may take some time once it is

complete inspect the background color of

your stream objects make sure to

deselect all the objects by clicking the

canvas so that you can see all the

results objects with a blank background

have passed their integrity checked with

no errors objects for the red background

are reporting errors in their

configuration the errors you see will

depend on the age in your stream object

users and the exact configuration of the

object to view these errors mouse over

the object the list of errors will be

displayed in the tooltip the errors are

saved to the stream object and will not

be removed until another integrity check

is performed once you know at the era's

are you can begin to correct them using

the canvas and the configuration blade

in this case the filter agent was

referencing a property of the event

simulator that I had later deleted I can

fix the issue by reading the property to

the event simulator or by removing the

property from the filter performing the

integrity check again will clear the

errors this has been a demonstration of

the integrity check in data stream

designer thank you for watching
</details>