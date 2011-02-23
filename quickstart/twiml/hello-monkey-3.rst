================================
Hello Monkey, v1.3
================================

Hoot. Now, let's also ask the caller if she wants to talk to a real monkey. If she does, connect her to Koko, the famous Gorilla, whose phone number we happen to know is 310-555-1212 :)

.. literalinclude:: /code/quickstart/twiml/1.3/hello-monkey.php
   :language: php

On line 24 we ask the caller to press a key to talk to a monkey or any other key to replay the menu.

Notice how the <Say> block is nested inside a <Gather> block which starts on line 23.

When Twilio sees a <Gather> block it starts looking for input from the caller's key pad. Because the <Say> is nested inside the <Gather>, Twilio will detect if caller presses a key even if the key is pressed while the <Say> is still running.

When the caller presses a key, the pressed key is POSTed to the URL specified by the 'action' handler attribute of the <Gather> verb. In this case, the URL is hello-monkey-handle-key.php.

.. literalinclude:: /code/quickstart/twiml/1.3/hello-monkey-handle-key.php
   :language: php

The keys pressed by the caller are transferred to the action handler as the value of the Digits parameter. In this case, the POST HTTP method is used with the <Gather> block so the value is sent as as url-encoded POST parameter. PHP has a nice feature, the '$_REQUEST' array, that lets you grab the values of request parameters regardless of the request method type. This allows us to simulate the Twilio Digits request and test our response handler using HTTP GET, which is easier to use. For example, putting the following URL into your web browser simulates the caller pressing the digit '1':

    ``http://demo.twilio.com/hellomonkey/1.3/hello-monkey-handle-key.php?Digits=1``

The purpose of the 'action' handler is to forward the caller back to the main menu using the PHP header("Location: hello-monkey.php"); method if the caller did not press '1', and <Dial> a number if the caller pressed '1'.

The <Dial> verb lets you connect one call to another. If you want to initiate a new outgoing call rather than connect an existing call to another number check out the Twilio REST API Calls resource.

Notice how there is a <Say> block below the <Dial> verb. The <Dial> will 'fall-through' if the call fails, the person never picks up, or the line is busy. In these cases the <Say> block underneath will execute and wish the caller goodbye!

The <Dial> verb will also fall-through to the <Say> if the remote caller hangs up the phone. This lets you place additional logic after the call like using <Dial> to connect to another number.
