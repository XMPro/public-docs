# how-to-create-and-publish-a-use-case---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=DrbJtlrshXo" %}



Learn how to create and publish a use case in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
<details>
<summary>Transcript</summary>Learn how to create and publish a use case in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com...
use-cases in the use case designer are

the core element of data stream designer

this video will demonstrate the process

of creating and publishing a use case to

start click the new use case button in

the sidebar to open the new use case

blade alternatively you can click the

use case button to access the use case

blade then click the new command once

here fill in the details of your use

case name a description and help

identify your use case and its purpose

clicking the blank icon field lets you

upload a unique or thematic image for

the use case or you can leave it blank

and a default icon will be used

assigning a category helps you group

your use cases default collection will

determine the initial collection

assigned to your stream objects which

will be described in more detail later

on when you are done click Save this

will save your new use case and open the

designer blade once you have an existing

use case you can navigate to this

designer blade from the Welcome page by

clicking on the category than the use

case alternatively click the use case

button on the side bar to access the use

case played then search for and click on

your use case the details of your use

case can be edited after its creation by

clicking the properties command on the

designer blade notably attempting to

change the default collection will offer

you the choice of retro actively

applying your selection to all existing

stream objects additionally the metadata

field is available this lets you assign

tags to your use case which can be

helpful in further categorizing your use

cases and searching through them from

the category dashboard the designer

blade is where you build your data

stream the bar on the left is the agent

toolbox searching for and dragging items

from here will allow you to create

stream objects which make up your data

stream each agent has a specific purpose

which is described in their

documentation for now we will create

stream objects from the event simulator

and event printer agents the simulator

will constantly generate data events for

the stream and the printer will display

the events it receives in the console

window of the stream host the stream

objects must be connected so data can

flow between them the green boxes on the

bottom of the stream object represent

outputs while the green boxes on the

side of the stream object represent

inputs most agents have one output and

one input but some have more or less in

these cases the documentation for the

agent will describe how each input or

output is used read outputs are special

error than outputs but they will be

described in another video for now it is

enough to know the event simulator has

one real data output click and drag the

output of the event simulator to the

input of the event printer this error

represents a connection between these

stream objects which data flows through

stream objects can be rearranged by

dragging their icon or renamed by

clicking their name clicking and

selecting a stream object will allow you

to delete it by clicking the delete

command you can also access its

configuration by clicking the

configuration command or by double

clicking the object each agent has its

own configuration which is again better

described in their own documentation the

configuration plate also allows you to

train to the stream objects collection

affecting which stream hosts it will run

on click the apply button to pass the

change to configuration back to the

designer and then the Save button to

save the changes

however newly created objects cannot be

configured if you try you will get a

warning reminding you the same to save

your stream first and try again in

similar ways connections can be selected

and deleted

they can also be dragged from either end

to delete the existing connection area

and recreate it with a different stream

object finally now that the stream has

been set up and the agents configured we

can publish the use case by clicking the

publish command this will run the data

stream on any stream host assigned to

the collection I have a stream host

running here and the event printer is

printing the data as it flows through

publishing a stream will prevent any

changes from being saved to the designer

to prevent altering and possibly causing

errors in a running stream if you want

to edit or update the data stream it

must first be unpublished by clicking

the unpublished command which will stop

the running stream on the stream hosts

this has been how to create and publish

a use case in data stream designer thank

you for watching
</details>