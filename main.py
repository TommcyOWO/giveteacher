import discord
from discord.ext import commands
from core.classes import Core
import json
import random, os, asyncio

with open("botjson.json","r",encoding="utf8")as jfile:
 jdata=json.load(jfile)

intents = discord.Intents.all()

bot=commands.Bot(command_prefix='!',intents=intents)



@bot.event
async def on_member_remove(member):
 channel =bot.get_channel(int(jdata["LEAVE"]))
 await channel.send(F"{member} 很遺憾您離開......")

@bot.event
async def on_member_join(member):
 channel =bot.get_channel(int(jdata["WECOM"]))
 await channel.send(F"{member} 歡迎來到Our AfterLife伺服器\n請遵守以上守則!!\n1.禁止引戰/謾罵/洗頻\n2.減少不雅用詞\n3.尊重與遵從管理員指示\n4.保持頻道主題相符話題")



@bot.event
async def on_ready():
 print(">> Bot is online <<")

for filename in os.listdir('./cmds'):
 if filename.endswith('.py'):
   bot.load_extension(f'cmds.{filename[:-3]}')
if __name__ == "__main__":
 bot.run(jdata['TOKEN'])