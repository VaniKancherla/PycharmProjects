# Databricks notebook source
# Databricks notebook source
import json
from kafka import KafkaProducer
import tweepy
import configparser
from tweepy.streaming import StreamListener
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
# import findspark
# from pyspark import SparkContext, SparkConf

class TweeterStreamListener(StreamListener):
  def __init__(self, api):
    self.api = api
    super(tweepy.StreamListener, self).__init__()
    self.producer = KafkaProducer(bootstrap_servers='52.172.201.33:9092',api_version=(0, 10, 1))
  def on_data(self, data):
    self.producer.send('twittertopic', data.encode('utf-8'))
    print (data)
    return True
  def on_error(self, status):
    print (status)

if __name__ == '__main__':
  consumer_key = 'j0wdchi5B59LzsVxXqQiUFgDx'
  consumer_secret = '1CxQvQTFw8c7jbFqTfiqQN9NIrlb1zfzozvgOQryKzurrDmG0K'
  access_token = '1089230750468190208-OD7ZcxoJk5vuNaijpIYj9wSA2mh1h8'
  access_secret = '89fcC3Ld8AbhhOL7K2WNpDOwQ1w3Va7vBrIraYWgs7TP6'
   # Create Auth object
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)
  api = tweepy.API(auth)
#    for tweet in api.search(q="trump", lang="en"):
#     print(tweet.text)
    
   # Create stream and bind the listener to it
  stream = tweepy.Stream(auth, listener = TweeterStreamListener(api))
  stream.filter(track=['trump'], languages = ['en'])

