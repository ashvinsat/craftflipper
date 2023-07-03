# pylint: disable-all
import requests
import json
"""
cofl stuff:
https://sky.coflnet.com/api/auctions/tag/NAME/active/bin
startingBid:

bz prices:
https://sky.shiiyu.moe/api/v2/bazaar



"""
#this doesnt need to be changed
bz = requests.get("https://sky.shiiyu.moe/api/v2/bazaar").json()
#

def get_craft_price(tag):
    data=json.load(open(f"{tag}.json"))
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

