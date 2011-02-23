================================
Hello Monkey, v1.1
================================

Ok, that was fun. Seriously, it was. But let's raise the stakes a bit. When someone calls, we are going to try to greet the caller by name:

.. literalinclude:: /code/quickstart/twiml/1.1/hello-monkey.php
   :language: php

In this example, the code inspects the From parameter passed by Twilio in the request to get the Caller ID of the caller. We then check to see if the caller is known looking up the number in the **$people** array to extract their name. We then Say their name or the word 'Monkey' if their Caller ID isn't known.

If you add your phone number and name to the **$people** array you can listen to Twilio greet you by name. Note that the phone numbers in the $people array have +1 prepended to them. '1' is the international country code for the US and Canada and the '+' formats the number in `E.164 <http://en.wikipedia.org/wiki/E.164>`_ format which is used by Twilio when passing you phone numbers.Let's walk through creating your first application, Hello Monkey. We'll use PHP to construct this example, but almost any web development language could be used.

