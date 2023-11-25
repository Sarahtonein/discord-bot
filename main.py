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
        cooldowns[cooldown_key] = datetime.utcnow() + timedelta(seconds=45)

        messages = [f'🦅🦅🦅:flag_us::flag_us:', f'Cleanest shirt in the dirty pile they say', f'I"d like some freedom fries with my DXY', f'DUMP ET']
        await message.channel.send(random.choice(messages))

    elif message.content.startswith("morning"):
        cooldowns[cooldown_key] = datetime.utcnow() + timedelta(seconds=45)

        await message.channel.send(f'Good morning sunshine, the earth says Hello :white_sun_cloud:')

    elif "bot" in message.content and not message.author.bot:
        cooldowns[cooldown_key] = datetime.utcnow() + timedelta(seconds=45)

        random_number = random.randint(0, 1)
        if random_number == 0:
            await message.channel.send(f'Who are you calling a bot, bot?')
        else:
            await message.channel.send(f'You rang?')

    elif "food" in message.content and not message.author.bot:
        cooldowns[cooldown_key] = datetime.utcnow() + timedelta(seconds=45)

        await message.channel.send(f'Go make yourself some food then, I ain`t doing it')

    elif "coffee" in message.content and not message.author.bot:
        cooldowns[cooldown_key] = datetime.utcnow() + timedelta(seconds=45)

        await message.channel.send(f'make me a cup too, bitch')
        
    elif message.content.startswith("ping"):
        cooldowns[cooldown_key] = datetime.utcnow() + timedelta(seconds=45)

        await message.channel.send(f'pong')

bot.run(os.getenv('TOKEN'))
