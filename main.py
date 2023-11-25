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

# Function to handle cooldown logic
def set_cooldown(author_id, channel_id):
    cooldown_key = f"{author_id}-{channel_id}"
    cooldowns[cooldown_key] = datetime.utcnow() + timedelta(seconds=45)

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
    
    content_lower = message.content.lower()

    if "dxy" in content_lower and not message.author.bot:
        set_cooldown(message.author.id, message.channel.id)
        await message.add_reaction("👎")
        messages = [f'🦅🦅🦅:flag_us::flag_us:', f'Cleanest shirt in the dirty pile they say', f'I"d like some freedom fries with my DXY', f'DUMP ET']
        await message.channel.send(random.choice(messages))

    elif "morning" in content_lower and not message.author.bot:
        set_cooldown(message.author.id, message.channel.id)
        messages = [f'Good morning sunshine, the earth says hello. :white_sun_cloud:', f'Is it really though?', f'Time for some coffee or what? :coffee']
        await message.channel.send(random.choice(messages))

    elif "bot" in content_lower and not message.author.bot:
        set_cooldown(message.author.id, message.channel.id)
        messages = [f'Who are you calling a bot, bot?', f'You rang?']
        await message.channel.send(random.choice(messages))

    elif "food" in content_lower and not message.author.bot:
        set_cooldown(message.author.id, message.channel.id)
        await message.channel.send(f'Go make yourself some food then, I ain`t doing it')

    elif "coffee" in content_lower and not message.author.bot:
        set_cooldown(message.author.id, message.channel.id)
        await message.channel.send(f'make me a cup too, bitch')

    elif "sandwich" in content_lower and not message.author.bot:
        set_cooldown(message.author.id, message.channel.id)
        await message.channel.send(f'Get me some of that Wi-fi bread!')

    elif ("bitcoin" in content_lower or "btc" in content_lower) and not message.author.bot:
        set_cooldown(message.author.id, message.channel.id)
        await message.add_reaction("🚀")
                
    elif message.content.startswith("ping"):
        set_cooldown(message.author.id, message.channel.id)
        await message.channel.send(f'pong')

bot.run(os.getenv('TOKEN'))
