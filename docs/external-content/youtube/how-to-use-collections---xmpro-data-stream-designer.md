# how-to-use-collections---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=-f2TRr-OQSY" %}



Learn how to use collections in the XMPRO Data Stream Designer.  

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if you want...
<details>
<summary>Transcript</summary>Learn how to use collections in the XMPRO Data Stream Designer.  

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if you want...
welcome to another training video for

Mac central today we will be talking

about the concept of collections in data

stream designer a collection is a

container which enables you to group

stream house which run the same use

cases imagine creating a use case where

you are getting some sensor values from

the device and then you want to run some

thresholds and ultimately you want to

run some action where you might be

creating a work order it's just a basic

small three-step use case you would then

need to deploy this somewhere most

likely on a stream host closer to your

source where these values are coming

from which might be let's say in this

case and all an oil pump now if this was

one use case pending at one oil pump on

wishing things to be deployed it's easy

you can just deploy it and it will run

fine if you have more than one stream

hosts basically more than one devices or

assets on which this use case is

supposed to run or assets that you want

to monitor you would need to deploy this

one by one on to each one of them which

would be a tedious task and will also

become a very difficult thing to manage

in the long run that is where

collections come in collection if the

container which sits in the middle and

allows you to publish your use cases on

to the collection and on the other side

your stream host register or subscribe

to that connection that way your use

case doesn't need to be deployed

individually to each stream host or each

asset it only needs to be published or

deploy on a collection while the stream

host would connect to the that

collection they will just run whatever

they are supposed to run as per your use

case and collection mapping this also

helps

for streamers which have intermittent

connectivity or streamers host which may

come on come in later for example you

may install a new oil oil pump in this

case it will just subscribe to the same

collection and will be up and running in

no time so that is why we have

collections in the dev scene designer

now how do you create one if you are in

the data stream designer you would

notice that there is a collections

option on the left side here if you go

in creating one is as simple as clicking

the plus button and giving it a name

like that once created you can then go

ahead and install stream hosts in there

by downloading a stream hose from here

and using the collection profile which

you can specify here then you will use

the installation file in this connected

connection profile to basically bring a

stream host online which will connect to

this collection once it is online you

will be able to see them in the list of

online streamers over here on this plate

here you're allowed to change the icon

of the of your collection you can also

change the name if you need to and there

are some advanced options which will be

looked at in the next video some of the

other options you have here are revoking

the key or deleting the collection

itself so that was a brief explanation

of collections in the dashing design
</details>