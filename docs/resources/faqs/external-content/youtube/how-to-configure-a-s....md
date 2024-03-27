# How To Configure a Stream Object - XMPRO Data Stream Designer
{% embed url="https://www.youtube.com/watch?v=sXSrWvYthxo" %}



Learn how to configure a stream object in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if...
<details>
<summary>Transcript</summary>Learn how to configure a stream object in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if...
configuring a stream object is the

second part of building a functioning

stream in the data stream designer this

video will demonstrate how to access the

configuration blade and explain several

of its functionality quirks to access

the configuration blade select a stream

object and click the configuration

command you can also double-click a

stream object the configuration blade

will open and display the save settings

of the stream object however newly

created stream objects cannot be

configured as they have not yet been

saved and a warning will appear to

remind you to save your stream if you

try in addition many stream objects ask

objects further up the stream for the

properties they will output when

determining options in their

configuration if you have altered the

connections or the configuration of

these objects but not yet save them the

old configuration settings will still be

used

therefore it is usually best to save

your stream every time you alter

configurations or whenever you finish

rearranging the stream the settings

displayed in the configuration blade

depend on the agent your stream object

was created from for instance the event

simulator agent needs to know the

properties of the events it will

generate and how often while the SQL

listener agent requires information

about the instance of SQL server that it

is to connect to more information about

each agents configuration will be found

within their documentation for now we

will use the SQL listener as an example

notice that whenever the server field

changes the configuration blade loads

briefly not all settings will do this

only certain ones depending on the agent

usually pertaining to login details or

uploading a file this is because such

settings affect the options displayed in

other settings so the entire blade must

be recreated using the new value for

instance when the correct login details

are supplied the agent will be able to

fetch the list of databases and populate

the database setting this can even

change which settings are shown for

example the password field is only

needed if the SQL authentication

checkbox is ticked therefore it will

hide or display accordingly whenever

that value changes also note that the

password field hides its contents and

even appears to change them after a

brief delay

this is normal it is because the

password setting is secure meaning that

the value you enter will be hidden from

view and will and the value will be

encrypted until it is needed by the

stream object finally note that the

blade offers the ability to discard and

apply your settings this card resets the

configuration to the value stored in the

designer while apply since the settings

you have entered back to the designer

and modifies the stream object to use

the new settings these changes can then

be discarded or permanently saved on

that blade agent configuration also

plays a part in assigning remote

configuration it is accessed by the

configure button under the remote

receiver or remote publisher if they

have been assigned and otherwise works

exactly the same way as in the designer

this has been how to configure a stream

object in the data stream designer thank

you for watching
</details>