import discord
from discord.ext import commands, tasks
from itertools import cycle
import json
import random
import os

token = open("token.txt", 'r').read()
client = commands.Bot('$')

responces = json.loads(open("responces/eightBall.json", encoding="utf-8").read())
status = cycle(['Gay Hentai Simulator', 'Furry masacre', 'With my dick'])

##################EVENTS##############################
@client.event
async def on_ready():
    changeStatus.start()
    print("Bot is online!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing arguments!")
    else if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I dont have enough persmissions to do this!")
    else if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command doesn't exist (Use $help to see the available ones)!")
    else 
        print("Something went wrong.")


################COMMANDS##############################
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.send(f"*{random.choice(responces)}*")

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command()
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()


################TASKS##############################
@tasks.loop(seconds=10)
async def changeStatus():
    await client.change_presence(activity=discord.Game(next(status)))


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)