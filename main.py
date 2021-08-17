import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

import blackjack
import bank
import checkbalance

def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    GUILD = os.getenv("DISCORD_GUILD")

    client = commands.Bot(command_prefix = "$")

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name = GUILD)
        print(
            f"{client.user} is connected to the following guild:\n"
            f"{guild.name} (id: {guild.id})"
        )

    @client.command()
    async def bjhelp(ctx):
        bot_help = open("help.txt", "r")
        await ctx.send(bot_help.read())

    @client.command()
    async def register(ctx):
        bank.register(ctx.author, ctx.author.name, ctx.author.id)

    @client.command()
    async def money(ctx):
        money = bank.money(ctx.author)
        await ctx.channel.send("<@" + str(ctx.author.id) + ">\nCurrently you have: " + str(money) + "$")

    @client.command(name = "blackjack")
    async def blackjack_func(ctx, arg1):
        if checkbalance.check(ctx.author, arg1) == True:
            blackjack.play(ctx.author, arg1)
        else:
            await ctx.channel.send("I'm sorry, but your balance seems to be to low")

    client.run(TOKEN)

if __name__ == "__main__":
    main()
