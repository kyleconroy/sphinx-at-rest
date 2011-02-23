================================
TwiML Quickstart: Hello Monkey
================================

Let's walk through creating your first application, Hello Monkey. We'll use PHP to construct this example, but almost any web development language could be used.

Prerequisites
---------------
1. To begin, you'll need a Twilio inbound phone number. You can use a free Twilio trial account or upgrade your account and get your own dedicated phone number.
2. You will also need a web host that lets you host PHP applications. There are lots of web hosting services that with host your PHP application for a few dollars a month.

Code
------
You can download the (minimal) code used in this example if you want:

* tar.gz: twiml.tar.gz
* zip: twiml.zip

Hello Monkey, v1.0
---------------------
1. Let's say your web server answers HTTP requests at companyfoo.com. Create a file called hello-monkey.php in the document root. The URL should be ``http://companyfoo.com/hello-monkey.php`` and will be the initial voice URL for your phone number.
2. If you are using a trial Twilio account, browse to your Dashboard page on the Twilio website. Locate the "Developer Tools" box and paste the URL of your hello-monkey file (e.g. ``http://companyfoo.com/hello-monkey.php``) in the "Voice URL" box. Hit save and your sandbox account will now point to your new hello monkey code.
3. If you are using a paid Twilio account, browse to the Phone Numbers page in your account on the Twilio website. If you don't already have a Twilio phone number, you can purchase your own phone number using the "Buy a Number" button on the right hand side of the page. Click the "Edit" link next to the phone number you would like to use. Next, check the “Voice” box, and paste the URL of your hello-monkey file (e.g. ``http://companyfoo.com/hello-monkey.php``) in the "URL" box. Hit save and this phone number will now point to your new hello monkey code.
4. Now, open up the hello-monkey.php file on your web server. Let's start with this basic php example code:

.. literalinclude:: /code/quickstart/twiml/1.0/hello-monkey.php
   :language: php

Now, pick up your mobile or landline phone and dial the number of application. Twilio will now fetch your URL, ``http://companyfoo.com/hello-monkey.php`` in our case, and execute the XML instructions above. First, it will Say 'hello monkey' and then it will hang up because there are no more instructions.
