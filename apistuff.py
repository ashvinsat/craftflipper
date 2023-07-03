# pylint: disable-all
import requests
import json
import os

#this doesnt need to be changed
bz = requests.get("https://sky.shiiyu.moe/api/v2/bazaar").json()
#

def get_craft_price(tag):
    #now need to check if an item is bazaar or ah
    items_in_recipe = get_recipe(tag)
    instabuy_price = 0
    order_price = 0
    for name in items_in_recipe.keys():
        try:
            instabuy_price += bz[name]["buyPrice"] * items_in_recipe[name]
            order_price += bz[name]["sellPrice"] * items_in_recipe[name]

        except:
            print('key not found, have to look at ah')
            try:
                secondlayer = get_recipe(name)
                get_craft_price(secondlayer)
            except FileNotFoundError:
                pass
            ah = requests.get(f"https://sky.coflnet.com/api/auctions/tag/{name}/active/bin").json

    print(int(order_price))

def get_recipe(tag):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "items", tag + ".json")
    file = open(file_path)
    data = json.load(file)
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
    file.close()
    return items_in_recipe


get_craft_price("FLORID_ZOMBIE_SWORD")

