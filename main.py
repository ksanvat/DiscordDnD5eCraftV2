import os

import discord


TOKEN = os.getenv('DISCORD_TOKEN')


class Client(discord.Client):
    async def on_ready(self) -> None:
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return

        print(f'Echo "{message.content}"')


if __name__ == '__main__':
    Client().run(TOKEN)
