# Tips on how to use cache in agent configuration and get live updates

{% embed url="https://www.youtube.com/watch?v=s6ME9bR5n3U" %}

🎥 Title: Tips on how to use cache in agent configuration and get live updates | In-depth with Gavin Green

🔍 Description:

Join Gavin Green in our latest installment from the "In-depth with Gavin Green" playlist as he delves deep into XMPro agent configurations. In this video, you'll learn:

The ins and outs of agent identifiers, cache sizes, and how to best utilize them for your needs. The distinction between caching 20 records overall vs. caching 20 records per unique identifier. A crucial tip on ensuring live data updates on your app without the constant need to refresh the page. How different data sources, like SQL, might affect your live update configurations. Whether you're a beginner trying to understand the basics or looking to refine your XMPro knowledge, this tutorial offers valuable insights and tips to ensure optimal performance and user experience. Make sure you don't miss the often-overlooked live update checkbox that can significantly elevate your app's responsiveness!

Don't forget to like, share, and subscribe for more in-depth tutorials with Gavin. Leave your questions in the comments below and we'll get back to you. Happy configuring!

\#XMPro #AgentConfiguration #LiveUpdates #GavinGreenTips #DataStreaming #TechTips #XMProTutorials #CacheTips #AppData #RealTimeData #XMProDatastreamDesigner

<details>

<summary>Transcript</summary>

so if I come back into this

um I logged on with the user that

doesn't have access but that's perfectly

fine if you look at the agent over here

you can see that we have the URL the key

but down here where we start seeing

identifier typically the identifier

would be you know a unique identifier

and asset key Etc so I'm assuming stop

ID is the identifier yeah

and then down the bottom if you're

looking for multiple from the cache size

so you want 20 records from the cash

site typically you would include the

identifier in that option as well as you

know a timestamp or I'm assuming if the

uh the longitude is going to change

that will allow you to get the 20

records

so the the only thing here would be to

make sure that you just select the the

stop ID there and then just apply it

now when you come to cash per entity and

replace cache how the cache works is

this is storing data

that will be rendered and and visible on

the actual app side of things

so the the data coming in here because

you've specified a cache of 20.

and you haven't said cash per entity

you're only ever going to get 20 records

which might be what you're looking for

however if you want 20 records per stop

then what you do is by ticking this here

here and you select that option there

you're essentially going to create 20

per entity for stops that's how you

let's say you read the agent piece

coming down here so you got everything

else spot on

this is just an extra item here if that

is what you're looking for there are

times when you don't need it you just

want 20 records irrespective of you know

the the unique identifier or the stop ID

or the asset ID

however there are times when you

probably do want to have 20 per you know

stop ID

so just switch that option on there and

that'll help you with the caching pieces

um so now yeah let's not save the

changes

the data coming now when we come in here

um

this was some of the access rights that

I had to just make sure what accent

yes I do

um to just reallocate to to your user so

how you configure it is correct so here

what you want to do is

um let's set it

live data is coming in

for for that connector and then here you

just want to scroll down and actually

look for

your data stream now you may have

noticed you have access to a lot of

other data streams yeah I'm going to

explain I'll explain where those came

from and why we gave you access to them

once you've clicked that it'll bring in

the primary key for you

this bottom option here you need to

select it and then you can click save

now once you've selected that option now

you can actually pass some data to the

screen the reason you select this option

here

is

you want to be able to show this data

constantly changing on the app

without having to refresh the page

so what that means is if I

um if I don't tick the live option I

have to press F5 on the page every

single time to actually load it

okay

what the the live update so you'll see

it keeps changing for the 20 the 20

records I don't have to let's just leave

the master I don't I don't have to

refresh the page or change the page

Etc it's the one item a few people tend

to miss the first time is they don't

check that box or know what that box

means and then when they get to this

page it'll load the first time

but to see the changes you have to press

F5 to to do that if you don't want that

you can just go back into the edit on

the page data and you just untick that

however whenever you're connecting to a

data stream like you're doing here it's

generally a good it's generally a good

thing to to take it because you don't

want to have to press F5 on the page

every single time the the point is to

get the live data coming through

okay

now there are some data sources where

you can't do this

SQL is one of them

so if you create a new connection so if

we go into the app data here and you say

you know what I actually want to connect

to to SQL and you configure all of this

you'll find that when you get to the

other side to actually use it SQL will

not have that option for you so it's not

something that every single one of these

connection has it's specific to the

connection that we're talking to make

sense

</details>
