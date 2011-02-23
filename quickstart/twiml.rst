===================================
Twilio Markup Language Quickstart
===================================

Overview
-----------
The goal of this quickstart is to understand how Twilio lets you control phone calls using the Twilio Markup Language (TwiML).

Twilio Markup Language
------------------------
Twilio Markup Language (TwiML) defines a simple set of instructions for letting your PHP/Java/Ruby/C#/Python/etc web application control live phone calls. New TwiML instructions are fetched by Twilio from your server at the start of each phone call and then again each time there is input from the phone. Just like a web browser, whenever the phone connected to Twilio performs an action such as a key press, Twilio makes a request to your server with the new data asking your application for a new set of TwiML instructions.

For example, when someone calls your Twilio-powered phone number, Twilio looks up the voice URL of the web application you've previously configured for that phone number and makes a request to the server, providing information about who called and asking the web server what to do on that call. Your web app can then respond with a set of TwiML instructions that begin an interactive dialog between Twilio and your web server.

How Twilio Interacts with Your Application
---------------------------------------------
When a new phone call starts or there is a user input e.g., a key press or a Dial ends, Twilio makes an HTTP GET or POST to your web server (as specified by your app). If you use HTTP POST, Twilio passes parameters as form-encoded variables in the body of the POST. If you use HTTP GET, parameters are passed in the URL query string.

Let's look at a real example.
