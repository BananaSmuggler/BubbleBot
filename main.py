import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
#client = discord.Client()

@client.event
async def onready():
    print('Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!kill Mateen'):
        await message.channel.send('AC-130 has been called to 4*** Blac***** A** L* Ver**, CA 917**')

    if message.content.startswith('!kill arsh'):
        await message.channel.send('kys bootyeater')

load_dotenv()
client.run(os.getenv('TOKEN'))