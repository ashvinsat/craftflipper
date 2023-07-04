# pylint: disable-all

import os
from api2 import DumpToFile

file = open("craftingrecipes.json", 'w')
file.write("[")
file.close()
directory = os.fsencode("items")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        itemnamestring = f.decode('ASCII')
        unused, name = itemnamestring.split("/")
        name, unused = name.split(".")
        DumpToFile(name)

file = open("craftingrecipes.json", 'a')
file.write("]")
