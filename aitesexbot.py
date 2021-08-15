import discord


client = discord.Client()
Token =


@client.event
async def on_ready():
    print('we have logged in as(0.user)'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('aite'):
        await message.channel.send("sex")


client.run(Token)
