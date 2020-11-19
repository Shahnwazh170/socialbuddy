import os

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import api
import requests
import json


@login_required(login_url='/')
def dashboard(request):
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)
    return render(request, "socialBuddy/Dashboard.html")


@login_required(login_url='/')
def post_joke(request):
    url_joke = 'https://official-joke-api.appspot.com/jokes/programming/random'
    return render(request, "socialBuddy/Dashboard.html")


@login_required(login_url='/')
def post_meme(request):
    url_meme = 'https://meme-api.herokuapp.com/gimme'
    meme = requests.get(url_meme)
    if meme.status_code == 200:
        res = meme.json()
        res = {
            "title": res["title"],
            "url": res["url"],
        }
        tweet_image(res)
    else:
        res = {
            "error": "Nothing found!"
        }
    # api.update_status("Test tweet from Tweepy Python")
    return render(request, "socialBuddy/Dashboard.html", {"response": res})


def tweet_image(res):
    filename = 'temp.jpg'
    img = requests.get(res["url"], stream=True)
    with open(filename, 'wb') as image:
        for chunk in img:
            image.write(chunk)

    api.update_with_media(filename, status=res["title"])
    os.remove(filename)
