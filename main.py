import discord
from dotenv import load_dotenv


import re
import os
import logging
import asyncio

import const
import app_commands
from quiz_app import Quiz

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

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
    if content.startswith('$quiz'):
        quiz = Quiz(message, client)
        print("Quiz Created")
        await quiz.start_quiz()
        print('Quiz started')
        author = quiz.get_author()
        def check(message):
            return author == message.author and message.content.isnumeric()
        try:
            print('Waiting for response')
            response = "Not Found"
            response = await client.wait_for('message', timeout=60, check=check)
            print(response)
        except asyncio.TimeoutError:
            await message.channel.send("Timeout")
        else:
            if quiz.correctIndex + 1 == int(response.content):
                await message.channel.send("Correct!")
            else: 
                await message.channel.send(f'Incorrect. The correct answer is **{quiz.correct}**')
    elif content.startswith('$help'):
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
client.run(os.getenv('DISCORD_TOKEN'), log_handler=handler, log_level=logging.DEBUG)