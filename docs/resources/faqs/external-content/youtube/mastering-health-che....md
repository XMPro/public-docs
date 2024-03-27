# Mastering Health Check Endpoints: A Guide to Ensuring Service Uptime and Performance with XMPro
{% embed url="https://www.youtube.com/watch?v=W1LWcSUrgTs" %}



Welcome to our guide on how to master health check endpoints for your product or service! Whether you're working with a cloud provider or an in-house team, understanding health check endpoints...
<details>
<summary>Transcript</summary>Welcome to our guide on how to master health check endpoints for your product or service! Whether you're working with a cloud provider or an in-house team, understanding health check endpoints...
now a health check endpoint is precisely

as it sounds

a product service has a health check API

endpoint such as HTTP forward slash help

that Returns the help of the service

when it is called the API endpoint

Handler performs various checks and

responds with the simple status of the

API and its dependencies

are unhealthy

when it is troubleshooting health checks

are the industry standard for the first

diagnostic step

they quickly indicate connectivity

health

either highlighting an issue such as

access to a database

or allowing the troubleshooter to rule

out connectivity and move on to their

next check

we've implemented standard best practice

health check endpoints with two

different ways to consume this

information

in person or utilizing a diagnostic tool

as a baseline a person can monitor the

health UI which sits outside of our

product

has to or you wouldn't be able to access

it if our products were not healthy

however there is more to be gained by

configuring the raw Json API response to

be read by diagnostic tools such as

Azure with app insights

so that the endpoints are constantly

monitored on the infrastructure itself

you can build rules triggered if it goes

from healthy to unhealthy and when

triggered you can build actions such as

an email or a team's message or maybe

even to Auto scale

Health endpoints are crucial for

enabling self-healing functionalities in

your infrastructure

being able to automatically restart

unhealthy services on the edge

is extremely powerful in increasing

product uptime and performance

imagine if your application is running

on kubernetes and you can automatically

restart the service

or the Pod that it's running on and

hopefully get it back to a healthy state

health checks are particularly useful

for customer installations on their own

infrastructure

there's always a risk that connectivity

might not have been opened on a service

that exim Pro needs and it's not

transparent that this is the case

time has been lost in previous

installations going through that

diagnosis process

it requires certain skill sets so it

becomes time consuming and costly to

troubleshoot what may end up being a

trivial issue

with health checks now when you do the

initial installation you could for

example confirm application designer has

connectivity to subscription manager and

to its database

if it doesn't then we can tell straight

away that it can't connect and see the

relevant error message

the problem is narrowed down to

connectivity between two systems and

it's simple to proceed to The Next Step

which could be something like opening an

exception on the firewall

[Music]

there are also day-to-day operations

where the environment in which XM Pro is

installed unexpectedly changes

whether it's the Cloud Server provide

running updates

sorry whether it's the cloud provider

running updates or deprecating

underlying functionality or the customer

themselves making changes

these endpoints are available so that XM

Pro connectivity can be actively

monitored

connectivity is inadvertently broken

someone can be proactively notified of

an issue and investigate further

the loss of connectivity assists in

knowing which area is working as

expected and which area to troubleshoot

Boda

let me take you to our product

documentation for a quick look

this is the

sorry this is the health path of an

application designer Services URL and

the raw API response

note the overall status is healthy and

that there is an entry for each of the

related product Service apis as well as

the database

observe the duration for each individual

check their healthy status as well as

the optional descriptive tags

next we'll look at the same information

using the Baseline help UI

here we can see in the top half the same

information for application designer but

it is a lot easier on the human eye

the overall status is healthy

and again there are entries for each

related product service API as well as

the database

observe again the duration for each

check their healthy status as well as

the optional descriptive tags

our documentation includes an example of

how to configure the Xin pro products as

well as how to add third-party systems

that have health endpoints

a reminder that how you choose to use

these in health checks is up to you

our product is decoupled from any

specific cloud provider so that XM Pro

remains platform independent
</details>