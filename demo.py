import tweepy
from textblob import textBlob

import numpy as np
import operator

consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key ,consumer_secret)
auth.set_access_token(access_token ,access_token_secret)

api = tweepy.API(auth)

topic = ['turtle']
since_date = "2018-12-24"
until_date = "2018-12-25"

def get_label(analysis, threshold = 0):
	if analysis.sentiment[0]>threshold:
		return 'Positive'
	else:
		return 'Negative'

polarities = []
public_tweets = api.search(q=[topic],count=100, since = since_date, until=until_date)

with open('%s_tweets.csv' % topic, 'wb') as this_topics_file:
	this_topics_file.write('tweet,sentiment_label\n')
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text, analyzer=PatternAnalyzer())
		this_topics_polarities.append(analysis.sentiment[0])
		this_topics_file.write('%s,%s\n' % (tweet.text.encode('utf8'), get_label(analysis)))
all_polarities[topic] = np.mean(this_topics_polarities)
