================================
Hello Monkey, v1.4
================================

Easy so far... how about letting the caller record her own monkey howl? Sounds like fun.

.. literalinclude:: /code/quickstart/twiml/1.4/hello-monkey.php
   :language: php

We added an extra option in the <Say> block telling the caller if she presses '2' she can record audio. The next step is to add an additional processing instruction to our <Gather> 'action' handler.

.. literalinclude:: /code/quickstart/twiml/1.4/hello-monkey-handle-key.php
   :language: php

We added a new option to handle the case when someone presses '2'. We can again simulate the pressing of the '2' key by adding ?Digits=2 to the URL.

    ``http://demo.twilio.com/hellomonkey/1.4/hello-monkey-handle-key.php?Digits=2``

The handler now outputs a new response asking for your hoooooooooowl. The <Record> tag lets you record audio from the caller.

* The 'maxLength' parameter tells Twilio to record up to 30 seconds of audio.
* The 'action' parameter tells Twilio what to do after the caller is done recording. In this case we pass off to the hello-monkey-handle-recording.php page.

.. literalinclude:: /code/quickstart/twiml/1.4/hello-monkey-handle-recording.php
   :language: php

The recording handler simply plays the recording back for the caller and says goodbye. The URL of the recording is passed to the handler in the request as the RecordingUrl parameter. The URL is externally accessible so you can send the URL of the howl to your friends or reference it in a webpage. Check out the Voice Recorder demo for another example of making voice recordings.
