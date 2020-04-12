# -*- coding: utf-8 -*-

"""Discord bot Douili main entry point."""
import os
from random import randint

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
BOT_ID = os.getenv("DISCORD_BOT_ID")
bot = commands.Bot(command_prefix=BOT_ID)


@bot.command(name=" 99", help="Douili douili douili")
async def douili(ctx):
    """Test Discord command."""
    response = randint(1, 8) * "douili "
    await ctx.send(response)


@bot.command(name=" minecraft", help="Minecraft server")
async def create_minecraft(ctx):
    """Test Discord command."""
    response = randint(1, 8) * "douili "
    await ctx.send(response)


bot.run(TOKEN)
