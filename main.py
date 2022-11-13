import discord

import modules.cLogger as cLog

from dotenv import dotenv_values

cLog.new_log()

TOKEN = dotenv_values(".env")["TOKEN"]

class AurobotClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

intents = discord.Intents.default()
intents.message_content = True

client = AurobotClient(intents=intents)
client.run(TOKEN, log_handler=None)