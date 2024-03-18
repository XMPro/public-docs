# how-to-export,-import,-and-clone-a-data-stream---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=--42hTU0TPU" %}



Learn how to export, import and clone data streams in the XMPRO Data Stream Designer.  

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.co...
<details>
<summary>Transcript</summary>Learn how to export, import and clone data streams in the XMPRO Data Stream Designer.  

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.co...
sometimes you may want to copy a use

case to another data stream environment

or to make a copy of the stream to

modify it for a different purpose

this video will demonstrate how to

export import and clone use cases to

achieve these goals

exporting a use case is performed from

the use case properties blade

accessed from the designer once it is

open

locate and click the export button a

dialog will appear

asking if secure settings in your stream

object's configuration should be

included in the exported file

such as the password field in the sql

listener

click yes to export while including the

decrypted secure settings

click no to export the use case without

the secure settings

or click cancel to not export the use

case at all

once you have clicked yes or no your

browser settings will take over and

either automatically download the

exported use case file for you

or offer you a choice of where to save

it please note that the export tool will

only export the latest version of the

use case

exporting a use case is of course

pointless on its own without the ability

to import

to import a use case navigate to the use

cases blade from the app bar on the left

and click the import command here

upload the exported use case file you

want to import

if you are importing into the same data

stream designer as the original

or another version of the original has

been imported already a notification

will appear

at this point you'll be able to choose

to import as a new data stream or is a

new version of the

existing data stream you are only

eligible to import as a new version if

you have at least write access to the

existing data stream

in this case you will not need to edit

most of the properties that will be

shown later

if you have read only or no access at

all to the existing data stream

you will not be able to save as a new

version and the notification will inform

you as such

you will only be able to proceed by

choosing to import as a new data stream

this is the default option and if there

is no pre-existing data stream these

options will be hidden you will have the

option to edit the name and description

of the use case before it is saved

you'll also need to select a category

for the use case

finally you will need to map the

collections used in the use case

to the ones in your data stream designer

my stream objects all use the same

collection so there is only one entry in

the list

and because i'm importing into the same

data stream designer it is able to map

to the same collection automatically

clicking the value field of the list

item displays a list of collections you

can assign from

but i'm happy to import into the same

collection so i'll leave that option

alone

however the import process can fail if

the inversions of the agents

the imported use case users are not

present in the new data stream designer

application

if this happens please contact your

company's admin to request that the

correct versions are uploaded

when you are done click save the

imported use case will open

automatically

but my example was a roundabout way of

copying the use case to the same data

stream designer

the clone tool is a similar faster

method for copying use cases in the same

application

it is accessed from the properties blade

like the export tool

simply click the clone command the

dialog that opens will allow you to give

the use case a new name to set it apart

from the original

and to change the category that it will

be found in clicking save will complete

the process

and open the newly copied use case

this has been how to export import and

clone a use case

thank you for watching
</details>