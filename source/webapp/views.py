from django.shortcuts import render, redirect
from webapp.cat_db import CatDb

from webapp.interaction_with_a_cat import Interaction


def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        name = request.POST.get("name", "")
        CatDb.cat = {
            "name": name,
            "age": 1,
            "happy": 40,
            "satiety": 40,
            "sleeping": False
        }
        return redirect("/cat_status/")


def cat_status(request):
    if request.method == "GET":
        cat = CatDb.cat
        image_url = Interaction.get_cat_image(cat["happy"])
        context = {
            "cat": cat,
            "image_url": image_url
        }
        return render(request, "cat_status.html", context)
    elif request.method == "POST":
        action = request.POST.get("action")
        cat = CatDb.cat

        if action == "feed":
            Interaction.feed_cat(cat)
        elif action == "play":
            Interaction.play_with_cat(cat)
        elif action == "sleep":
            Interaction.put_cat_to_sleep(cat)

        return redirect("/cat_status/")
