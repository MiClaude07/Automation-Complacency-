import discord
from dotenv import load_dotenv


import re
import os

import const
import src.app_commands as app_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv(".env")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content
    if not content.startswith('$'):
        return
    if content.startswith('$help'):
        await message.channel.send(app_commands.help())
    elif content.startswith('$day'):
        await message.channel.send(app_commands.day(content))
    elif content.startswith('$lastday'):
        await message.channel.send(app_commands.last_day(content))  
    elif content.startswith('$def'):
        if content.endswith('$def'):
            await message.channel.send("Provide a term to define. Use `$dictionary` to find terms.")
        else:
            await message.channel.send(app_commands.define_term(content))
    elif content.startswith('$dictionary'):
        ret_dict = app_commands.dict_print()
        await message.channel.send(ret_dict)
    elif content.startswith('$resource'):
        await message.channel.send(app_commands.get_resource(content))
    else:
        await message.channel.send("Invalid Command. Check `$help` for list of all commands.")
client.run(os.getenv('DISCORD_TOKEN'))