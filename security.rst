========= 
Security
=========

SSL
----
Feel free to use SSL to protect communications between Twilio and your web application. Just specify an HTTPS url. Note: Twilio cannot currently handle self signed certificates.

HTTP Authentication
--------------------

Twilio supports HTTP Basic and Digest Authentication. This allows you to password protect your TwiML URLs on your web server so that only you and Twilio can access them. You may provide a username and password via the following URL format.

    ``https://username:password@www.myserver.com/my_secure_document``

Twilio will authenticate to your web server using the provided username and password and will remain logged in for the duration of the call. It is highly recommended that you use HTTP Authentication in conjunction with SSL. For more information on Basic and Digest Authentication, refer to your web server documentation.

Validating Requests are coming from Twilio
--------------------------------------------------
If your application exposes sensitive data, or is possibly mutative to your data, then you may want to be sure that the requests that hit your web application are indeed coming from Twilio, and not a malicious third party. To allow you this level of security, Twilio cryptographically signs its requests. Here's how it works:

1. Turn on SSL on your server and configure your Twilio account to use HTTPS urls.
2. Twilio assembles its request to your application, including the final URL and any POST fields (if the request is a POST).
3. If your request is a POST, Twilio takes all the POST fields, sorts them by alphabetically by their name, and concatenates the parameter name and value to the end of the URL (with no delimiter).
4. Twilio takes the full URL, with query string and all post parameters, and signs them using HMAC-SHA1 and your AuthToken as the key.
5. Twilio sends this signature in an HTTP header called X-Twilio-Signature

Then, on your end, if you want to verify the authenticity of the request, you can re-assemble the data string by going through the exact same process. If our two hashes match, then the request was authentic. You can then be sure that all the data used to construct the hash, including the full URL, query string and POST parameters were all sent to you by Twilio. Here's how you would perform the validation on your end:

1. Take the full URL of the request, from the protocol (http...) through the end of the query string (everything after the ?).
2. If the request is a POST, take all of the POST parameters and sort them alphabetically.
3. Iterate through that sorted list of POST parameters, and append the variable name and value (with no delimiters) to the end of the URL string.
4. Sign the resulting string with HMAC-SHA1 using your AuthToken as the key (remember, your AuthToken's case matters!).
5. Base64 encode the resulting hash value.
6. Compare your hash to ours, submitted in the X-Twilio-Signature header. If they match, then you're good to go.

Let's walk through an example request. Let's say Twilio made a POST to your page:

    ``http://mycompany.com/myapp.php?foo=1&bar=2``

And let's say Twilio posted some digits from a <Gather> to that url, in addition to all the usual POST fields

* Digits: 1234
* To: +18005551212
* From: +14158675309
* CallSid: CA1234567890ABCDE

1. Create a string that is your URL with the full query string:

    ``http://mycompany.com/myapp.php?foo=1&bar=2``

2. Alphabetize the list of POST variables by the paramter name:

   1. CallSid: CA1234567890ABCDE
   2. Digits: 1234
   3. From: +14158675309
   4. To: +18005551212

3. Append each POST variable, name and value, to the string with no delimiters:

    ``http://mycompany.com/myapp.php?foo=1&bar=2CallSidCA1234567890ABCDEDigits1234From+14158675309To+18005551212``

4. Hash the resulting string using HMAC-SHA1, using your AuthToken as the key. Let's suppose your AuthToken is 12345. Then we take the hash value returned from the following function call (or its equivalent in your language of choice):
   
    ``hmac_sha1(http://mycompany.com/myapp.php?foo=1&bar=2CallSidCA1234567890ABCDEDigits1234From+14158675309To+18005551212, 12345)``

5. Now take the Base64 encoding of the hash value (so it's only ASCII characters):

    ``HpS7PBa1Agvt4OtO+wZp75IuQa0=``

6. Compare that to the hash we sent in the X-Twilio-Signature HTTP header. Match them up FTW!

Here is an example written in PHP:

.. literalinclude:: /code/api/signature-validation.php
   :language: php

A Few Notes
------------

The HMAC-SHA1 secure hashing algorithm should be available in all major languages, either in the core or via an extension or package.

If your URL uses an "index" page, such as index.php or index.html to handle the request, such as: ``http://mycompany.com/twilio`` where the real page is served from ``http://mycompany.com/twilio/index.php``, then Apache or PHP may rewrite that URL a little bit so it's got a trailing slash... ``http://mycompany.com/twilio/`` for example. Using the code above, or similar code in another language, you could end up with an incorrect hash because, Twilio built the hash using ``http://mycompany.com/twilio`` and you may have built the hash using ``http://mycompany.com/twilio/`` . Something to be careful of.

Validation using the Twilio Helper Libraries
---------------------------------------------

All of Twilio Helper Libraries ship with a Utilities class which facilitates request validation. Head over to the libraries page to download the library for our language of choice.

Your Auth Token
--------------------

Just a friendly reminder to keep your AuthToken secure. It not only enables access to the REST API, but also to request signatures.
