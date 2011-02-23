=============
Debugging 
=============

.. toctree::
   :hidden:

   errors

Writing an application on Twilio is easy as momma's pie. But here are a few tips we've found helpful...

Check the Logs
-----------------
Twilio logs information about it's interaction with your application, including all errors and warnings. You can check the contents of those logs to help you debug. There are two ways to do this:

* UI: Visit the `Twilio Debugging Interface <http://www.twilio.com/user/account/debugger>`_
* Web Service: Use the :ref:`Notifications REST API` to query for logs.

Check the Response Body
----------------------------

While all errors and warnings are available in the the `Twilio debugging interface <http://www.twilio.com/user/account/debugger>`_, the REST API will also return a Twilio REST Exception XML block which contains the HTML error code, Twilio-specific error code, error message, and a link to the Error Code Reference.

.. code-block:: xml

    <?xml version="1.0"?>
    <TwilioResponse>
        <RestException>
            <Status>400</Status>
            <Message>Dial: Invalid phone number format </Message>
            <Code>13223</Code>
            <MoreInfo>http://www.twilio.com/docs/errors/13223</MoreInfo>
        </RestException>
    </TwilioResponse>

All Twilio-specific errors are listed in the :doc:`errors`

The Browser Is Your Friend
--------------------------------

Remember, you're just writing a web application. There's nothing Twilio does that you can't test right there in your browser. Visit the URLs in your web browser, and see that you don't have any errors.

* Firefox treats XML files really nicely, highlighting any invalid XML in your document. We're not forcing you to use Firefox or anything, we're just saying it's cool... that's all.
* Using Firefox, you can easily see if your application is returning valid XML. Firefox will show you encoding or other errors in your XML, which is helpful.
* Mimic Twilio's data passing by manually adding data to your URLs. For example, if you ask Twilio to digits and the action is http://www.myapp.com/handleDigits.php, you can open your browser to http://www.myapp.com/handleDigits.php?Digits=1 to verify what happens if the user presses 1.

Debug Output From your Application
-------------------------------------

Make sure your application isn't sending debug output, because that will nearly always cause problems XML validation problem. You can, however, wrap any such output in XML comment blocks... they're the same as HTML comment blocks: <!-- COMMENTS HERE --><br/>
