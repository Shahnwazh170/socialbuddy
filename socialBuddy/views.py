import os

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from . import api


@login_required(login_url='/')
def dashboard(request):
    return render(request, "socialBuddy/Dashboard.html")


@login_required(login_url='/')
def post_joke(request):
    print("uu---", request.user)
    # url_joke = 'https://official-joke-api.appspot.com/jokes/programming/random'
    url_joke = 'https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,racist,sexist'
    joke = requests.get(url_joke)
    res = joke.json()
    print("--- type ---", res['type'])
    if joke.status_code == 200:
        if res["type"] == "twopart":
            res = {
                "joke": res["setup"] + "\n" + "\n" + "\n" + "\n" + "\n" + "\n" + res["delivery"],
            }
        else:
            res = {
                "joke": res["joke"],
            }
        if request.user.username == "Shahnwazh170":
            print("uu---if ", request.user)
            api.update_status(res['joke'])
    else:
        res = {
            "error": "Nothing found!"
        }
    return render(request, "socialBuddy/Dashboard.html", {"response": res})


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
        if request.user.username == "Shahnwazh170":
            print("uu---if ", request.user)
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
