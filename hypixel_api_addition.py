#IT NOT WURK ILL TRY ANOTHEER SOLUTION SEEMS PACKAGE BRUKEN
"""
import requests
import typing
import hypixel

API_KEYS = ['d606b894-3469-4425-8d6c-3a4d97349424']
hypixel.setKeys(API_KEYS)

def getHypixelRank(nameOfPlayer: str):
    Player = hypixel.Player(nameOfPlayer)
    PlayerName = Player.getName()
    PlayerRank = Player.getRank()
    return PlayerName + " is rank: ", PlayerRank['rank']
"""

import json
import requests
from hypixel_apikey import Hypixel_Key
from getplayerUUID import getUUID

def getData(link):
    data = requests.get(link)
    return data.json()

def getHypixelData(nameOfGame, nameOfPlayer: str):
    uuid = getUUID(nameOfPlayer)
    ApiLink = f"https://api.hypixel.net/player?key={Hypixel_Key}&uuid={uuid}"
    newdata = getData(ApiLink)
    stat = newdata["player"]["stats"][f"{nameOfGame}"]["coins"]
    answer = json.dumps(stat)
    print(str(answer))
    return str(answer)