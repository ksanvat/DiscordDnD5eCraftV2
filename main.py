import os

import discord


TOKEN = os.getenv('DISCORD_TOKEN')


class Client(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')


if __name__ == '__main__':
    Client().run(TOKEN)
