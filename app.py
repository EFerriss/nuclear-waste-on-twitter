# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:15:52 2017

@author: Elizabeth Ferriss
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return('Hello World')

if __name__ == '__main__':
    app.run(port=33507)

#import tweepy
#from tweepy import OAuthHandler
# 
#consumer_key = ' 1UkCDco2NKAiW8z4eA3pxWUC0'
#consumer_secret = ' LfRz5mhXqPDywxMCHaCWIuZAWBr5TMrKdtEAesE1Si485N5emk'
#access_token = ' 2883190569-wqpZ9FxaUT8zOCGEzFlYfRb6SoybmRl0mglh6DR'
#access_secret = ' C0TEGjXRawlkXBjTmgQKtfeJyhiRtcHLZUMcWgHbG15Q7'
# 
#auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)
# 
#api = tweepy.API(auth)

#print('hello world')