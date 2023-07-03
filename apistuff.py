# pylint: disable-all
import requests
import json
import os

#this doesnt need to be changed
bz = requests.get("https://sky.shiiyu.moe/api/v2/bazaar").json()
#

def get_craft_price(tag):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "itemsfolder", tag + ".json")
    data = json.load(open(file_path))

    items_in_recipe = {}
    for i in data["recipe"].values():
        if i == "":
            pass
        else: 
            key, value = i.split(":")
            if key in items_in_recipe:
                items_in_recipe[key] += int(value)
            else:
                items_in_recipe[key] = int(value)
    print(items_in_recipe)

get_craft_price("BAT_WAND")

