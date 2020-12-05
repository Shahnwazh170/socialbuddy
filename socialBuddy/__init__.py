import tweepy
import os
from socialBuddy import settings

# print(os.environ['API_KEY'])

auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)

auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
# print(settings.API_KEY, settings.API_KEY_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
