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