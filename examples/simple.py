#!/usr/bin/python2

import time
import reddit_stream

class SimpleListener(reddit_stream.StreamListener):
    def processMessage(self, message):
        if message['type'] == 'comments':
            for comment in message['comments']:
                print comment['author'].ljust(20, ' '),
                print comment['body'].replace('\n', '')[:50] + '...'

userAgent = 'Testing a bot by /u/<your username here>'
commentStream = reddit_stream.CommentStream(userAgent, waitSeconds=2.5)

listener = SimpleListener()
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
