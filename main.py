import os

import discord

from core import command


TOKEN = os.getenv('DISCORD_TOKEN')


class Client(discord.Client):
    async def on_ready(self) -> None:
        pass

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return

        try:
            cmd = command.parse(message.content)
            answer = cmd.run()
            await message.reply(answer)
        except:
            await message.reply('Я сломался(')


if __name__ == '__main__':
    Client().run(TOKEN)
