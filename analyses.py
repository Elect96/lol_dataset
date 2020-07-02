""" Purpose of the file:
Describe it.
"""
import json


def compare_stat(champions_list, to_compare):
    champ_stat_value = dict()
    for champion in champions_list:
        if champions_list[champion].get(to_compare):
            champ_stat_value[champion] = champions_list[champion][to_compare]
    return champ_stat_value


champions = dict()
with open("champions.json", "r", encoding="utf-8") as f:
    champions = json.load(f)

hps = compare_stat(champions, "hp")
print(hps)
# TODO: make a top 10 list of champions on a given stat e.g. champs with highest hp
