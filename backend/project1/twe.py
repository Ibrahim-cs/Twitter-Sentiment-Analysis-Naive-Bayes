from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from project1.naive import naiveClassifier
from textblob import TextBlob
import re


# keys and tokens from the Twitter Dev Console
consumer_key = 'XBUZDeDXzQl2sTEcF57nS1wpo'
consumer_secret = 'iepcIn8ObNcKLMTprk8wWJ7qNn4YQhWmveY2g1WExO4J6g5rVc'
access_token = '1103704856253120522-qtWTHG6HjLm1ORg9tkPUcq7qUdFeFC'
access_token_secret = 'hD5IsMjPz1O4nfaI7ZXo2IZdoiZKJx87eS4vtODdNAIkz'


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self):
        self.decode = {}
        self.naiveClassifier = naiveClassifier()

    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def on_data(self, data):
        try:
            self.decode = json.loads(data)
            prediction = self.naiveClassifier.getPrediction(
                [self.decode['text']])
            self.decode['nbKey'] = prediction[0]
            # create TextBlob object of passed tweet text
            analysis = TextBlob(self.clean_tweet(self.decode['text']))
            # set sentiment
            if analysis.sentiment.polarity > 0:
                self.decode['nlpKey'] = 0
            elif analysis.sentiment.polarity == 0:
                self.decode['nlpKey'] = 0
            else:
                self.decode['nlpKey'] = 1

        except Exception as erro:
            print(erro, 'ooooooooooooooooooooooooooooooo')
            pass
        return True

    def on_error(self, status):
        print(status, 'ggggggggggggggggggggggg')
        return True


def getTweet():
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Algeria'],
                  locations=[-180, -90, 180, 90],languages=['en'], is_async=True)
    return l
