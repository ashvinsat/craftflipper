# pylint: disable=consider-using-f-string
# pylint: disable=pylint(trailing-newlines)
# pylint: disable=pylint(unused-import)
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
async def ping(ctx):
    """do stuff"""
    await ctx.send(f"pong {round(bot.latency * 1000)}ms")

