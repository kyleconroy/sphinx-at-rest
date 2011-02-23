============================
Availability and Reliability
============================

Fallback URLs
---------------

Twilio maintains a redundant, clustered architecture designed to ensure reliable high availability service. This is only half of the challenge. Because of the distributed nature of a Twilio application, your web application must be reliable and highly available as well. To aid you in this task, Twilio allows the configuration of "Fallback" URLs on incoming phone numbers via your Account Portal or the REST API's IncomingPhoneNumbers resource.

A Fallback URL is a URL that Twilio requests in the event of a fatal error while executing your call. If Twilio is unable to retrieve or execute TwiML from your web server, a request is immediately made to the appropriate Fallback URL. Twilio will submit the 'ErrorCode' and 'ErrorUrl' parameters, indicating the error code of the failure and what URL the failure occurred on. You can reply to the fallback URL request with more TwiML, returning a custom application error message, or attempting to recover and continue your call or SMS session.

Example Use Cases
>>>>>>>>>>>>>>>>>>

Primary Web Server Failover
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: you want to make sure your Twilio application continues to accept calls, even if
your primary web server goes down.

**Solution**: Configure your incoming phone number's Voice URL to ``http://www.mysite.com/index`` and Voice Fallback URL to ``http://fallback.mysite.com/index``. If Twilio requests ``http://www.mysite.com/index`` and receives an HTTP error or connection failure, it will then request ``http://fallback.mysite.com/index``. If the fallback URL responds with valid TwiML, Twilio will use it to continue the call as if there was no problem.

Custom Error Message
~~~~~~~~~~~~~~~~~~~~~~~
**Problem**: You do not want your callers to hear the default Twilio application error message.

**Solution**: Create an error TwiML document to <Say> or <Play> a custom error message. Configure the Voice Fallback URL for your phone number to point at this document's URL. If Twilio encounters a fatal error, callers will hear your custom failure message instead of Twilio's.

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8" ?>
   <Response>
       <Say>
         An application error has occured.  
         Please call back later
       </Say>
   </Response>

Catching Errors
~~~~~~~~~~~~~~~

**Problem**: You want to be notified of errors as they occur.

**Solution**: Configure your Fallback URL to point at a URL that looks for the 'ErrorCode' and 'ErrorUrl' parameters. Your application can log these errors, email you an alert, etc. You can respond to the request with TwiML containing an error message for the caller or attempt to recover and continue with the call.
