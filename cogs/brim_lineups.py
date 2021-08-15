# Import libraries
import discord
import os
from discord.ext import commands

class brim_lineups(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("brim_lineups is online.")

    # Commands
    @commands.command()
    async def brim_bind_a_triple(self, ctx):
        await ctx.send("https://i.imgur.com/wne77yN.png")

    @commands.command()
    async def brim_ascent_a_generator(self, ctx):
        await ctx.send("https://i.imgur.com/FJOdpd3.png")


def setup(client):
    client.add_cog(brim_lineups(client))