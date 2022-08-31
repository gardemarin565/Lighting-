from  emailimport message, message_from_binary_file
import discord
from discord.ext import commands
import asyncio
from asyncio import sleep
import json
import requests
import sqlite3
from tabulate import tabulate
import osos
import sys
from discord.utils import get
from asyncio import sleep
from config import settings

client = commands.Bot(command_prefix=settings['prefix'], intents  = discord.Intents.all())
bot = commands.Bot(command_prefix=settings['prefix'], intents  = discord.Intents.all())

Links = ['.com', '.ru', '.рф', '.ua', '.org', ".net", 'http', 'https', '://', '.shop']

Маты = ['хуй', 'блядь', 'блять', 'хуе', 'пидар', 'пидор', 'ебл', 'Муд']

@client.event
async  defon_ready():
     while True:
          await client.change_presence(status =discord.Status.idleidle, activity =discord.Game("Lhelp | Бот сервера Lightning💙"))
          await (15)

@client.command(name ="рофл")
async def  (ctx):
    message: discord.Message = await ctx.send(f"{ctx.author.mention}, тебе бан <:Ban:1008448762907201626>")
    await .add_reaction("<:LT_lubimyi_pin_Argona:1004645774912671824>")

@client.command(name = "Лис")
async def fox (ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xF3A016, title = 'Лис')
    embed.set_image(url = json_data['link'])
    await ctx send (embed  = embed)

@client.command(name="Кот")
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)

    embed = discord.Embed (color  = 0xb5b8a5, title  = 'Кот')
    embed.set_image(url = json_data['link'])
    await ctx send(embed = embed)

@client.command(name="Птица")
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/bird')
    json_data = json.loads(response.text)

    embed = discord.Embed (color  = 0x76756D, title = 'Птица')
    embed.set_image(url = json_data['link'])
    await ctx send(embed = embed)

@client.command(name="Панда")
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/panda')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0x8C9394, title = 'Панда') 
    embed.set_image(url = json_data['link']) 
    await ctx send(embed = embed)

client.run(settings ['token'])
