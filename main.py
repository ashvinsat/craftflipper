# pylint: disable=consider-using-f-string
# pylint: disable=trailing-newlines
# pylint: disable=unused-import
# pylint: disable=missing-module-docstring
import os
import tracemalloc
import configparser as cfg
import discord
from discord.ext import commands, tasks
tracemalloc.start()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="~", intents= intents, case_insensitive=True)

parser = cfg.RawConfigParser()
FILE = "config.ini"
parser.read(FILE)
token=parser.get("Info", "TOKEN")
bot.run(token)

@bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)

