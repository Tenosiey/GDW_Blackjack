import os
import discord

import blackjack
import bank

from dotenv import load_dotenv

def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    GUILD = os.getenv("DISCORD_GUILD")

    client = discord.Client()

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f"{client.user} is connected to the following guild:\n"
            f"{guild.name}(id: {guild.id})"
        )

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == "$register":
            bank.register(message.author, message.author.name, message.author.id)

    client.run(TOKEN)

if __name__ == "__main__":
    main()
