# Import libraries
import discord
import os
import random
from discord.ext import commands

class tips(commands.Cog):

    def __init__(self, client):
        self.client = client

    valorantTipsList = ["The spike takes 7 seconds to defuse.",
                        "Remember to keep your crosshair where enemies will be.",
                        "It takes 45 seconds for the spike to go off."]

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("tips is online.")

    # Commands
    @commands.command()
    async def tip(self, ctx):
        tip = random.choice(valorantTipsList)
        await ctx.send(tip)

def setup(client):
    client.add_cog(tips(client))