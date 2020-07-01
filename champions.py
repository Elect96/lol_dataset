# This file is meant to extract champions information from the current patch provided to it
import os
import json

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

# print(champions)
# TODO: save champions into a text file
