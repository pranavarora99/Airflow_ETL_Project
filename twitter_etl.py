import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "wZjkQfI5G2ZxcfUlAaC5Sbgkv"
access_secret_key = "rnV8JLnFqz5YlxVqiZAePwXNdhendbeGbVh5kJvLnGIQ5eFnxt"
consumer_key = "1668065007920115716-dXukE57gTNVyUKupfNmfNUTBYNkvIy"
consumer_secret_key = "nkYatazErnVyOD2jzs5Z5yWTyCRHMQNEh03bY8SD4nXyi"

#twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret_key)
auth.set_access_token(consumer_key, consumer_secret_key)

#create an api object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                            count=200,
                            include_rts=False,
                            #we'll keep full text
                            tweet_mode='extended'
                            )

tweet_list = []
for tweet in tweets:
    text = tweet._json["full_text"]

    refined_tweet = {'tweet': text,
                    'retweet': tweet.retweet,
                    'likes': tweet.likes,
                    'date': tweet.date}

    tweet_list.append(refined_tweet)


df = pd.DataFrame(tweet_list)
df.to_csv("elon_tweets.csv")