# pylint: disable-all
import requests
import json
import os

#this doesnt need to be changed
bz = requests.get('https://sky.shiiyu.moe/api/v2/bazaar').json()
#

def get_craft_price(tag):
    #now need to check if an item is bazaar or ah
    items_in_recipe = get_recipe(tag) #this is a dictionary
    instabuy_price = 0
    order_price = 0
    for name in items_in_recipe.keys():
        #implement how if the quantity is >= 160 then dont go further down the recipe
        try:
            print(name)
            instabuy_price += bz[name]['buyPrice'] * items_in_recipe[name]
            order_price += bz[name]['sellPrice'] * items_in_recipe[name]
        except:
            print('key not found, have to look at ah')
            try:
                secondlayer = get_recipe(name)
                print(secondlayer)
                for neam in secondlayer.keys():
                    n = get_craft_price(neam)
                    order_price += n[0]
                    instabuy_price += n[1]
            except FileNotFoundError:
                print('filenotfound')
                try:
                    print(name)
                    ah = requests.get(f'https://sky.coflnet.com/api/auctions/tag/{name}/active/bin').json
                    print('mew')
                    #ingred_price_from_ah = ah[0]['startingBid']
                    print(ah[0])
                    print('mea')
                    #order_price += ingred_price_from_ah
                    #instabuy_price += ingred_price_from_ah
                except:
                    print(name + "ZZZZ")
                    print('item not found on auction house!')
            
    return int(order_price), int(instabuy_price)

def get_recipe(tag):
    recipe = {}
    recipe_dictionary={f"{tag}": recipe}
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'items', tag + '.json')
        file = open(file_path)
        data = json.load(file)
        print(file_path)
        for i in data['recipe'].values():
            if i == '':
                pass
            else: 
                key, value = i.split(':')
                if key in recipe:
                    recipe[key] += int(value)
                else:
                    recipe[key] = int(value)
        file.close()

    except FileNotFoundError:
                print("AAAA")
                pass
    for item in recipe:
        create_layer_recipe(item, recipe)
    recipe_dictionary.update()
    return recipe_dictionary

def create_layer_recipe(tag, dict):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'items', tag + '.json')
        file = open(file_path)
        data = json.load(file)
        del dict[tag]
        get_recipe(tag)    
    except FileNotFoundError:
        pass

print(get_recipe("FLORID_ZOMBIE_SWORD"))




