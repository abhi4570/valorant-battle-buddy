# Import libraries
import discord
import os
from discord.ext import commands
from decouple import config

token = config("token")    # Bot token
client = commands.Bot(command_prefix = "$")    # Bot client

# Client events
@client.event
async def on_ready():   # Function to indicate bot is ready
    print("Bot is online.")

# Client commands
@client.command()
async def ping(ctx):    # Ping command
    await ctx.send(f"{round(client.latency * 1000)}ms")

@client.command()
async def load(ctx, extension):    # Command to load cogs
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):    # Command to unload cogs
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

# Load all cogs in cogs folder upon startup
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
