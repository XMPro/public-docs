# stream-hosts-and-how-to-install-them---xmpro-data-stream-designer
{% embed url="https://www.youtube.com/watch?v=o_SEtqNMWTI" %}



Learn how to install stream hosts in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if you want...
<details>
<summary>Transcript</summary>Learn how to install stream hosts in the XMPRO Data Stream Designer. 

Need help with creating your XMPRO data streams? Send an email to support@xmpro.com 

Go to https://xmpro.com if you want...
stream hosts are an extension of the

data stream designer and aware published

data streams are sent to run this video

will detail what a stream house does and

how to install one stream hosts are

external processes that can receive

commands from and send data to the data

stream server it is where data streams

are run when they are published and

where a data streams live data is sent

from some stream objects even need to

connect to the stream host in order to

configure themselves if no stream hosts

representing a collection are connected

to the data stream designer stream

objects using that collection will not

run nor will the live data be viewed and

configuration requests from certain

objects in that collection will fail

including integrity checks to install

the stream host navigate to any

collections blade and download the host

select the operating system you wish to

install it on this example will use

Windows and I have already downloaded a

stream host installer all collections

will let you download the same installer

but it is convenient to download it from

the collection you want the new host to

connect to as you will also need to

download the connection profile as part

of the installation the collection

profile contains all of the information

necessary to connect the stream host to

this data stream designer decrypt any

settings encrypted by your company's

encryption key and identify it as

belonging to this collection give your

device a unique name and click OK to

download when the installer has

downloaded run it the process of

installing will be slightly different on

different operating systems first agree

to the end-user license agreement select

a folder to install the stream host to

this example will be installed as a

console host meaning that it must be

started manually and will open a console

window while running the windows service

option would install the host as a

Windows service allowing it to be run

automatically by windows in the

background when prompted for a

connection profile select the file you

downloaded earlier again there may be

slight differences in the options based

on your operating system

we recommend browsing the documentation

of the installer for your operating

system to start a console stream host

search for XM pro stream host in the

Start menu or navigate to the folder you

installed it and run the program as

administrator this is important if you

installed the stream

an assistant folder such as program

files as the host will generate logs and

download files for agents and running

streams and requires the rights to save

these in its own folder when the stream

host starts it will request a list of

running stream objects assigned to it

and begin running them it will then be

available to send live data from those

stream objects and also to handle

requests for configuration from stream

objects that must be run on a host the

stream host may disconnect from the data

stream designer server due to network

interruption or other factors if a

disconnect occurs the device will no

longer be able to fulfill configuration

requests or send live data that any

streams that were running at the time

will continue to run and the device will

regularly attempt to re-establish a

connection once a connection has been

re-established the list of running

streams will be checked again any

streams that were unpublished while the

while the device was disconnected will

be it stopped any streams that were

published will begin running and any

streams that were unpublished updated

and published again will be stopped

updated and restarted on even

uninstalling the stream host is similar

to installing stop the stream host if it

is running then running the same

installer will give you the option to

uninstall if you have lost or deleted

the installer you can remove from the

add or remove programs option in your

operating system if all else fails it is

safe to delete the folder you installed

it to this has been a demonstration of

the stream host and how to install it

from data stream designer thank you for

watching
</details>