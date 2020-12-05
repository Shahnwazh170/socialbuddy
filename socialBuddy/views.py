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
    print("---------------- ", request.path)
    print("---------------- ", request.get_raw_uri())
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


types = ["random-meme", "indian-meme", "programming-meme"]


@login_required(login_url='/')
def post_meme(request):
    print("---------------- ", request.path)
    type_ = None
    url_meme = None
    if types[0] in request.path:
        type_ = types[0]
        url_meme = 'https://meme-api.herokuapp.com/gimme'
    elif types[1] in request.path:
        type_ = types[1]
        url_meme = 'https://meme-api.herokuapp.com/gimme/india'
    elif types[2] in request.path:
        type_ = types[2]
        url_meme = 'https://meme-api.herokuapp.com/gimme/programmerhumor'

    meme = requests.get(url_meme)

    if meme.status_code == 200:
        res = meme.json()
        res = {
            "title": res["title"],
            "url": res["url"],
        }
        if request.user.username == "Shahnwazh170":
            print("uu---if ", request.user)
            tweet_image(res, type_)
    else:
        res = {
            "error": "Nothing found!"
        }
    # api.update_status("Test tweet from Tweepy Python")
    return render(request, "socialBuddy/Dashboard.html", {"response": res})


def tweet_image(res, type_=None):
    filename = 'temp.jpg'
    programming_meme_tags = " #programmerhumor #programming #coding #java #javascript #100daysofcode"
    india_meme_tags = " #india"
    img = requests.get(res["url"], stream=True)
    with open(filename, 'wb') as image:
        for chunk in img:
            image.write(chunk)

    status = res["title"]
    if type_ == types[0]:
        pass
    elif type_ == types[1]:
        status = res["title"] + india_meme_tags
    elif type_ == types[2]:
        status = res["title"] + programming_meme_tags

    api.update_with_media(filename, status=status)
    os.remove(filename)
