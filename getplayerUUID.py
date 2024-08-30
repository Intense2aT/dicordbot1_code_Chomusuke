import json
import requests

def getData(link):
    data = requests.get(link)
    return data.json()

def getUUID(username):
    apiLink = f"https://playerdb.co/api/player/minecraft/{username}"
    jFile = getData(apiLink)
    uuid = jFile["data"]["player"]["id"]
    a = json.dumps(uuid)
    a = str(a).strip('"')
    return str(a)