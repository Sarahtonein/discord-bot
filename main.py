import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random
from datetime import datetime, timedelta

load_dotenv()

intents = discord.Intents.all()

# Create a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store cooldown information for each condition
cooldowns = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Process commands
    await bot.process_commands(message)

    # Check if the user is on cooldown for any condition
    cooldown_key = f"{message.author.id}-{message.channel.id}"
    if cooldown_key in cooldowns and datetime.utcnow() < cooldowns[cooldown_key]:
        return

    if message.content.startswith("dxy"):
        # makes it so you dont have to do extra work to choose a random message, random.choice() picks 1 element from a list at random
        messages = [f'🦅🦅🦅:flag_us::flag_us:', f'Cleanest shirt in the dirty pile they say', f'I"d like some freedom fries with my DXY', f'DUMP ET']
        await message.channel.send(random.choice(messages))


    if message.content.startswith("morning"):
        await message.channel.send(f'Good morning sunshine, the earth says Hello :white_sun_cloud:')

    if "bot" in message.content and not message.author.bot:
        random_number = random.randint(0, 1)
        if random_number == 0:
            await message.channel.send(f'Who are you calling a bot, bot?')
        else:
            await message.channel.send(f'You rang?')
    if "food" in message.content and not message.author.bot:
        await message.channel.send(f'Go make yourself some food then, I ain`t doing it')

    if "coffee" in message.content and not message.author.bot:
        await message.channel.send(f'make me a cup too, bitch')
        
    if message.content.startswith("ping"):
        await message.channel.send(f'pong')

    # Set a 45-second cooldown for the user and channel
    cooldowns[cooldown_key] = datetime.utcnow() + timedelta(seconds=45)

bot.run(os.getenv('TOKEN'))
