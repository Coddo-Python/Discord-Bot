import discord
from discord.ext import commands, tasks
from discord.ext.tasks import loop
import sys
import random
import asyncio

client = commands.Bot(command_prefix = '?')

print("Program Started...")
print("Bot Started...")
print("Init Started...")
lock = 0
prevmessage = None

@client.event
async def on_message(message):
    global lock #making sure that the variables work accross diferent functions
    global prevmessage
    if lock == 1:
        if prevmessage != message.content: #if the previous message is the same as the new one, nothing should hapen
            channel = client.get_channel(711137574642516008) #McChat Channel
            await channel.send(message.content) #Mimic Message
            prevmessage = message.content #Part of system to stop dupes
            await asyncio.sleep(2) #To Avoid bot overload
    if "/support" in message.content.lower():
        print("/support Activated")
        channel = client.get_channel(710934053901303828)
        role = discord.utils.get(message.guild.roles, id = 683627319713071104) #Used to define the staff role
        msg = role.mention + " Support Activated" #Used to mention the role
        await channel.send(msg)
        content = message.content
        newcontent = content.replace("s", '#')
        await channel.send(f"Triggered by: {newcontent}")
        await channel.send("The s's were replaced with # for coding reasons.") #S is replaced to not trigger /support again and to stop duping.
    await client.process_commands(message) #To allow other commands to function

@client.command()
async def say(ctx, arg1, arg2):
    global lock #making sure that the variables work accross diferent functions
    channel = client.get_channel(711137574642516008) #McChat Channel
    if arg1 == "s" or arg1 == "S":
        await channel.send(f"{arg2}") #if arg1 is s, it will not show who sent the message
    else:
        await channel.send(f"{ctx.message.author}: {arg2}") #if arg1 is NOT s, it will show who send the message

@client.command()
async def saylock(ctx, arg1):
    global lock
    if arg1 == "Activate" or arg1 == "activate": #To set to activate mode
        await ctx.send("Lock Activated")
        await asyncio.sleep(3) #To stop Overload
        lock = 1 #Configure On_Message
    else:
        await ctx.send("Lock Deactivated") #To set to deactivate mode
        await asyncio.sleep(3) #To stop Overload
        lock = 0 #Configure On_Message

@client.command()
async def ping(ctx):
    await ctx.send(f'My ping is {client.latency} (ms)!')

@client.command()
@commands.has_any_role('Moderator')
async def purge(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)


client.run('TOKEN')
