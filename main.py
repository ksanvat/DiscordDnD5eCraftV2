import os

import discord


TOKEN = os.getenv('DISCORD_TOKEN')


class Client(discord.Client):
    async def on_ready(self) -> None:
        pass

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return

        await message.channel.send(f'Echo "{message.content}"')


if __name__ == '__main__':
    Client().run(TOKEN)
