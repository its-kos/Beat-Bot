import discord
from discord.ext import commands

class MemberEvents(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("{} has joined the server.".format(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print("{} has left the server.".format(member))


def setup(client):
    client.add_cog(MemberEvents(client))