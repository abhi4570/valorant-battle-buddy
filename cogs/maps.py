# Import libraries
import discord
import os
from discord.ext import commands

class maps(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("maps is online.")

    # Commands
    @commands.command(aliases=["Breeze"])
    async def breeze(self, ctx):
        await ctx.send("https://cdn-images.win.gg/news/e046ede63264b10130007afca077877f/f92d7e812aa4b0c6e57c77c3f9f6deb6/original.png")

    @commands.command(aliases=["Icebox", "Shitbox", "shitbox"])
    async def icebox(self, ctx):
        await ctx.send("https://cdn1.dotesports.com/wp-content/uploads/2020/11/12090242/db73bd9e504575ee2e703c1142b68a14.png")

    @commands.command(aliases=["Bind"])
    async def bind(self, ctx):
        await ctx.send("https://assets.rockpapershotgun.com/images/2020/04/Valorant-Bind-map.png")

    @commands.command(aliases=["Ascent"])
    async def ascent(self, ctx):
        await ctx.send("https://assets.rockpapershotgun.com/images/2020/06/Ascent-Callouts.png")

    @commands.command(aliases=["Split"])
    async def split(self, ctx):
        await ctx.send("https://preview.redd.it/4757zxvs7bt41.png?auto=webp&s=0682d26ee4b31450aaff94cc48bce6bbb1b5a947")

    @commands.command(aliases=["Haven"])
    async def haven(self, ctx):
        await ctx.send("https://preview.redd.it/5i9ylqta79v41.png?width=1854&format=png&auto=webp&s=5bca8fd11e876aa78e0e07d0a51d08abd3008dee")

def setup(client):
    client.add_cog(maps(client))