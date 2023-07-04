# pylint: disable-all
import copy
import requests
import json
import os

bz = requests.get('https://sky.shiiyu.moe/api/v2/bazaar').json()

# make the file
    
def GetDict(tag):
    #open the file for the item
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(scriptDir, 'items', tag + '.json')
    file = open(filePath)
    data = json.load(file)
    recipe = {}
    #find the recipe
    for i in data['recipe'].values():
            if i == '':
                pass
            else: 
                key, value = i.split(':')
                if key in recipe:
                    recipe[key] += int(value)
                else:
                    recipe[key] = int(value)
    #lol find a better automated solution for this eventually that terminates once there isnt anything left
    re1 = MultilayeredRecipe(recipe)
    re2 = MultilayeredRecipe(re1)
    re3 = MultilayeredRecipe(re2)
    re4 = MultilayeredRecipe(re3)
    re5 = MultilayeredRecipe(re4)
    re6 = MultilayeredRecipe(re5)
    re7 = MultilayeredRecipe(re6)
    re8 = MultilayeredRecipe(re7)
    re9 = MultilayeredRecipe(re8)
    #create a dictionary that can be dumped into the bigger json
    jsonableDict = {tag:re9}
    return jsonableDict

def MultilayeredRecipe(oldDict):
    newrecipe = copy.deepcopy(oldDict)
    for i in oldDict.keys():
        try:
            scriptDir = os.path.dirname(os.path.abspath(__file__))
            filePath = os.path.join(scriptDir, 'items', i + '.json')
            file = open(filePath)
            data = json.load(file)
            for j in data['recipe'].values():
                if j == '':
                    pass
                else: 
                    key, value = j.split(':')
                    if key in newrecipe:
                        newrecipe[key] += int(value) * oldDict[i]
                        #but some day make it so that if that value goes over 160 u can just leave it as the previous form
                    else:
                        newrecipe[key] = int(value) * oldDict[i]
            del newrecipe[i]
        
            file.close()
        except FileNotFoundError:
            pass
    return(newrecipe)

def DumpToFile(tag):
    dumpy = GetDict(tag)
    print(dumpy)
    with open("craftingrecipes.json", 'a') as f:
        json.dump(dumpy, f, indent=4)
        f.write(",")
    print("success")