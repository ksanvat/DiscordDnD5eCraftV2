import os

import discord

try:
    from core import business
    from core import command
    FATAL_STATE = False
except:
    FATAL_STATE = True


TOKEN = os.getenv('DISCORD_TOKEN')


class Client(discord.Client):
    async def on_ready(self) -> None:
        pass

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return

        if FATAL_STATE:
            await message.reply('Критическая ошибка(')
            return

        try:
            cmd = command.parse(message.content)
            if cmd is not None:
                answer = cmd.run(business.Context())
                await message.reply(answer)
        except business.LogicError as exc:
            await message.reply(str(exc))
        except:
            await message.reply('Я сломался(')


if __name__ == '__main__':
    Client().run(TOKEN)
