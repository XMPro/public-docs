# How To Use Charts: Series - XMPRO App Designer
{% embed url="https://www.youtube.com/watch?v=15LxvXhZ05s" %}

In this video, you’ll learn how to configure chart series in the XMPRO App Designer.

Need help with creating your XMPRO apps? Send an email to support@xmpro.com

Go to [https://xmpro.com](https://xmpro.com) if you want to learn more about how you can build real-time applications with our Event Intelligence Platform.
<details>
<summary>Transcript</summary>hello and welcome to another training

video from xm pro

this is an advanced training video on

how to use the chart

specifically around the series

i have created an app with charts of all

the series types that we support

this will help give a better

understanding of the differences between

them all

the line series type always has straight

lines between each point

on the other hand the spline series type

smoothly interpolates between each point

the area chart shades the graph below

each point

the spline area chart also shades the

area

underneath the line created but the edge

is again

interpolated to be smooth the bar chart

has

bars the scatter chart scatters points

as well as the bubble chart and range

area and range bar

shade an area between a maximum and a

minimum value

or in the case of the range bar have

bars between a maximum and minimum value

step type charts that is the step line

in the step area have steps as you can

see

stacked type series such as the stacked

line

spline area spline area

and bar build on top of each other

they will never overlap because the

bottom most

series value is added to the next series

which is added to the next series

so for instance if we have the values 1

1 2 and 1 then the second series

value would actually be 2 because 1 plus

1 is two

and then the third one would be four and

five

etc

full stack series such as the full

stacked line spline

area spline area and bar also build on

top of each other

but make sure that the values are a

percentage of the full

value as these use the same data you can

see how that works

so even though that this first value on

the stacked bar

is around six the full stacked bar still

counts that as one hundred percent

and the last value on here

rises up to fifteen but that is still

one hundred percent in the full stacked

bar to configure series go to the block

properties and drop down

the data section you can add a series

with the plus button

or you can edit a series by clicking on

one of the series in the list

the properties in here are name which is

just for your own use it doesn't

actually show up anywhere when it is

rendered

visible which if you uncheck will make

the

series invisible note that if you check

the

hide series on legend click you will be

able to

make the series visible again by

clicking on its series in the legend

unless you uncheck show in legend in

which case

the series will not be shown in the

legend and so you won't be able to click

on it

color is the color of the series

we have type with all of the available

types

styling mode which is only available if

your type is

line spline stacked line stacked spline

or step line which is the styling mode

of the line so you can have solid dash

long dash or dot i'll choose long dash

pane and y-axis which you can choose

separate panes

and y-axis for more information on this

please look at the advanced chart video

on multiple panes

and axes the x-axis

data which is the column the data is

coming from

for the x-axis y-axis data

which is the column the y-axis data is

coming from

if you choose different series types

like range area

range bar or bubble there will be

different data

options available i will show those in a

minute

we have overlap x-axis which makes the

x-axis overlap i will show an example of

how to use this later

we have ignore empty points which if

checked

doesn't render any points that have a

null value

we have show points which if checked

show

the points on the line if you type is

line spline stacked line stacked spline

step line or scatter otherwise this will

not be available

and the point size which delineates the

size of the points and

point shape which is circle

square diamond cross triangle down or

triangle up

we have show label which is on hover or

always

which will show the value of the

connected point

we have label format in which you can

format the label

we have some default options and you can

also enter in

a number type like this for more

information on

the label format you can click on the

help button

and we have aggregation which will

aggregate the number of points

into a single point if there are too

many points

for more information on this please

watch the video on pan and zoom

and aggregation so i'm going to apply

this on the series

and save and then we can see what

happens

so we can notice that the line is now

dashed the shape

is a diamond it is not in

the legend because we turned that off

coming back to the settings

if you have a bubble type series you

will also get

point size data which determines the

size of the

bubbles or points that appear on the

chart

if you have range area

then you will get y axis data start and

end

as well as range bar

again y-axis data start and end

and if you choose overlap x-axis which

you need to choose for

all series that you want to overlap

and this is how the chart will look as

you can see

the axes are not side by side they are

now on top of each other

this setting can only be applied for the

range bar

and the bar this has been an advanced

video

on how to use the chart series
</details>