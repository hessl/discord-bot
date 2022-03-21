import json
import discord

client = discord.Client()
token = None

# Read discord bot token
with open('./config.json', 'r') as file:
	config = json.load(file)
	token = config['token']

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

if __name__ == '__main__':
	client.run(token)