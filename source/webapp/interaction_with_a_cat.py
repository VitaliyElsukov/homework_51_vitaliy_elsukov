from random import randint

from webapp.cat_db import CatDb


class Interaction:

    @staticmethod
    def get_cat_image(happiness):
        if happiness < 30:
            return CatDb.cat_image_3
        elif happiness > 70:
            return CatDb.cat_image_1
        else:
            return CatDb.cat_image_2

    @staticmethod
    def feed_cat(cat):
        if not cat["sleeping"]:
            cat["satiety"] = min(cat["satiety"] + 15, 100)
            cat["happy"] = min(cat["happy"] + 5, 100)
            if cat["satiety"] > 99:
                cat["happy"] = max(cat["happy"] - 30, 0)

    @staticmethod
    def play_with_cat(cat):
        if cat["sleeping"]:
            cat["sleeping"] = False
            cat["happy"] = max(cat["happy"] - 5, 0)
        else:
            if randint(1, 3) == 1:
                cat["happy"] = 0
                cat["satiety"] = max(cat["satiety"] - 10, 0)
            else:
                cat["happy"] = min(cat["happy"] + 15, 100)
                cat["satiety"] = max(cat["satiety"] - 10, 0)

    @staticmethod
    def put_cat_to_sleep(cat):
        cat["sleeping"] = True
