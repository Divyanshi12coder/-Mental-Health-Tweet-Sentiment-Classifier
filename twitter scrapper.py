import tweepy
import pandas as pd

def fetch_tweets(api_key, api_secret, access_token, access_secret, query, count=100):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count)
    data = [{"text": tweet.full_text, "created_at": tweet.created_at} for tweet in tweets]
    return pd.DataFrame(data)