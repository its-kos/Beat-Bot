import discord
from discord.ext import commands

class Tools(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong!")

    @commands.command()
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    async def kick(self, ctx, member):
        await ctx.send("Poustraki 100%")


def setup(client):
    client.add_cog(Tools(client))