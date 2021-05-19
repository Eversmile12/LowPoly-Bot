import tweepy
import random
from keys import *
from datetime import datetime, timedelta
import time

class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    
    def on_status(self, tweet):
        try:
            tweet_id = tweet.id
            status = api.get_status(tweet_id)
            action = random.randint(0,20)
            time.sleep(4)

            if not status.retweeted and not status.favorited and status.lang == 'en' and tweet.author.screen_name != "BotPolygon":
                print("New tweet fetched " + tweet.author.screen_name)
                if action < 5:
                    print("Liking")
                    api.create_favorite(tweet.id)                
                elif action < 10:
                    print("Retweeting")
                    api.retweet(tweet.id)
                elif action > 10:
                    print("Retweeting and liking")
                    api.retweet(tweet.id)
                    api.create_favorite(tweet.id)
        except:
            return        



    def on_error(self, status_code):
           if status_code == 420:
            return False

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

tweets_listener = StreamListener(api)
stream_tweets = tweepy.Stream(api.auth, tweets_listener)
stream_tweets.filter(track=["#indiedev"], is_async=True)


# with open("latest_id.txt") as file:
#     max_id = file.readline()
#     print(max_id)
#     while True:
#         tweets = api.user_timeline(user_id="1292738130441908224", max_id = max_id, exclude_replies = True)
#         for tweet in tweets:
#             print(tweet.text)
#             file.
