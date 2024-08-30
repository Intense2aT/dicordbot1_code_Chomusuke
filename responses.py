import random
from hypixel_api_addition import getHypixelData

operatives: list = ['+', '-', '*', '/']

def getResponse(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'meow' in lowered:
        return random.choice(['Meow', 'Meow >:3', 'Meow :>', 'Meow :3', 'Meow :O', 'Meow :P', 'Meow :D'])
    elif 'tere' in lowered:
        return 'mine ära ma tahan magada'
    elif 'mitu' in lowered:
        return f'{random.randint(1, 69)} sest see on mitu korda ma olen soovinud sind mitte näha'
    elif 'mata' in lowered:
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        oprativechoice = random.randint(0, 3)
        answer: list = [n1 + n2, n1 - n2, n1 * n2, n1 / n2] 
        return f'{n1} {operatives[oprativechoice]} {n2} = {answer[oprativechoice]}'
    elif 'war crimes' in lowered:
        return random.choice(['Nowpee uwu :3', 'Japanse or bruken knees like my friend said ;>', 'no uwu... maybe...', 'uwu :3', 'uwu :D'])
    elif 'hydata ' in lowered:
        lowered = lowered.replace('hydata ', '')
        if 'bedwars ' in lowered:
            lowered = lowered.replace('bedwars ', '')
            return getHypixelData("Bedwars", lowered)
        elif 'arcade ' in lowered:
            lowered = lowered.replace('arcade ', '')
            return getHypixelData("Arcade", lowered)
        elif 'skywars ' in lowered:
            lowered = lowered.replace('skywars ', '')
            return getHypixelData("SkyWars", lowered)
        else:
            return 'game not specified or not implemented'