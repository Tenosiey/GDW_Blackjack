import os
import discord

import blackjack

from dotenv import load_dotenv

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == '99!':
            response = "99!"
            await message.channel.send(response)

    client.run(TOKEN)

if __name__ == "__main__":
    main()
