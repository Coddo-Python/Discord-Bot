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
number = 0
print(f"StopCode = {StopCode}")

@client.event
async def on_message(message):
    if "/support" in message.content.lower():
        print("/support Activated")
        channel = client.get_channel(710934053901303828)
        role = discord.utils.get(message.guild.roles, id = 683627319713071104)
        msg = role.mention + "Support Activated"
        await channel.send(msg)
        await channel.send("Triggered by following message:")
        await channel.send(message)


client.run('Token')
