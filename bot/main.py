import discord

client = discord.Client()

# My discord bot token. Token is in .gitignore.
f = open('./token.txt', 'r')
token = f.read()
f.close()

# Bot startup event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Message event
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'Hello':
        await message.channel.send('Hello')

client.run(token)