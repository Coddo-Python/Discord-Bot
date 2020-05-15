import discord
from discord.ext import commands, tasks
from discord.ext.tasks import loop
import sys
import random

client = commands.Bot(command_prefix = '.')

print("Program Started...")
print("Bot Started...")
print("Init Started...")
StopCode = random.randint(0,9999)
StopCode = str(StopCode)
number = number(0)
print(f"StopCode = {StopCode}")

@client.event
async def on_message(message):
    if "/support" not in message.content or "/Support" not in message.content:
        print("/support Activated")
        number = number + 1
        channel = await message.guild.create_text_channel(f"Support {number}")
        channel = discord.utils.get(message.guild.channels, name = f"Support {number}", type = "ChannelType.text")
        await channel.send('@Moderator')


client.run('NzEwODUzNTU4ODI4MDA3NDQ3.Xr6gAA.2Aa5ciSSSkuzexPvY3b1fOAJ1Mc')
