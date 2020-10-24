import os

import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='source')
async def bot_source(ctx):
    source_str = """
    Issues can be submitted at https://github.com/CodyConstine/Adventure_Bot/issues)
    Contributions can be made at https://github.com/CodyConstine/Adventure_Bot"""

    await ctx.send(source_str)

bot.run(TOKEN)
