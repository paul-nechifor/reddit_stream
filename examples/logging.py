#!/usr/bin/python2

import os
import time
import reddit_stream

userAgent = 'Testing a bot by /u/<your username here>'
commentStream = reddit_stream.CommentStream(userAgent, waitSeconds=2.5)

logDir = os.path.join(os.path.dirname(__file__), 'logs')
listener = reddit_stream.LogWriterListener(logDir)
listener.start() # This is a Thread, so you have to start it

commentStream.addListener(listener)

commentStream.start() # Also a thread.

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    print 'Exiting...'
    listener.stop() # The thread will exit as soon as possible.
    commentStream.stop() # The thread will exit as soon as possible.
