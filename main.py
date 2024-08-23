from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import getResponse


#load token from safe place DONT UPLAOD TO GITHUB OR U STOOPID
load_dotenv()
TOKEN: Final[type: str] = os.getenv('DISCORD_TOKEN')

#setup bot
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

#funcionaality
async def sendMessage(message: Message, user_message: str) -> None:
    if not user_message:
        print("error not 404 nyan")
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = getResponse(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as expectedException:
        print(expectedException)
        print("error meow ur code kinda bad")

#paneb toole
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now in session')

#sonum incoming oh no
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await sendMessage(message, user_message)

#i dont know anymoar aidake plz
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()