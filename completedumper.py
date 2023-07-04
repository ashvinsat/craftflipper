# pylint: disable-all

import os
import api2

file = open("craftingerecipes.json", 'a')
file.write("[")

directory = os.fsencode("items")
for filename in os.listdir(directory):