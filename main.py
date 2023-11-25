import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
from commands import *

load_dotenv()

intents = discord.Intents.all()

# Create a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
@bot.event
async def on_message(message):
    if message.content.startswith("dxy"):
        # makes it so you dont have to do extra work to choose a random message, random.choice() picks 1 element from a list at random
        messages = [f'🦅🦅🦅:flag_us::flag_us:', f'Cleanest shirt in the dirty pile they say', f'I"d like some freedom fries with my DXY', f'DUMP ET']
        await message.channel.send(random.choice(messages))


    if message.content.startswith("morning"):
        await message.channel.send(f'Good morning sunshine, the earth says Hello :white_sun_cloud:')
    
    if "bot" in message.content and not message.author.bot:
        await message.channel.send(f'Who are you calling a bot, bot?')
    # Process commands
    await bot.process_commands(message)

    if "food" in message.content and not message.author.bot:
        await message.channel.send(f'Go make yourself some food then, I ain`t doing it')

    if "coffee" in message.content and not message.author.bot:
        await message.channel.send(f'make me a cup too, bitch')
        
    if message.content.startswith("ping"):
        await message.channel.send(f'pong')

##@bot.command
##async def 

bot.run(os.getenv('TOKEN'))
