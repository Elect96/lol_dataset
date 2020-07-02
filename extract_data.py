""" Purpose of the file:
This program extracts champions's data from the current patch provided and then saves it as a json file
"""
import json
import os

# data path
path = "D:\\Python\\League of Legends\\dragontail-10.13.1\\10.13.1\\data\\en_GB\\champion\\"
# dictionary; "champion": stats
champions = dict()

# loop over the whole folder tree in the given path
for dirs, subdirs, files in os.walk(path):
    # loop over every file
    for file in files:
        # if the file exists do following
        if file:
            # open that file and save it to data
            with open(path + file, "r", encoding="utf-8") as f:
                data = json.load(f)
            # extract a champion's name from a file's name
            champion_name = file.split(".")[0]
            # save every champion to a dictionary
            champions[champion_name] = data.get("data").get(champion_name).get("stats")

# save champions to a file
with open('champions.json', 'w', encoding='utf-8') as f:
    json.dump(champions, f, ensure_ascii=False, indent=4)
