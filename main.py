#import os
import tracemalloc
import discord
from discord.ext import commands, tasks
import configparser as cfg
tracemalloc.start()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="~", intents= intents, case_insensitive=True)

parser = cfg.RawConfigParser()
FILE = "config.ini"
parser.read(FILE)
token=parser.get("Info", "TOKEN")
bot.run(token)
