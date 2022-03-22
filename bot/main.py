import json
import discord


def main():
    token = None

    # Read discord bot token
    with open('./config.json', 'r') as file:
        config = json.load(file)
        token = config['token']

    client = MyBot()
    client.run(token)


class MyBot(discord.Client):

    # Bot startup event
    async def on_ready(self):
        print(f'We have logged in as {self.user}!')

    # Message event
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == 'Hello':
            await message.channel.send('Hello')

if __name__ == '__main__':
    main()