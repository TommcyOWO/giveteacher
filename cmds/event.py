import discord
from discord.ext import commands
from core.classes import Core

class Event(Core):

 @commands.Cog.listener()
 async def on_message(self,msg):
    if msg.content=="CH":
     await msg.channel.send("CH")
 @commands.Cog.listener()
 async def on_message(self,msg):
    if msg.content=="守則":
     await msg.channel.send("1.禁止引戰/謾罵/洗頻\n2.減少不雅用詞\n3.尊重與遵從管理員指示\n4.保持頻道主題相符話題")
 @commands.command()
 async def sayed(self,ctx,*,msg):
    await ctx.message.delete()
    await ctx.send(msg)
 @commands.command()
 async def cleam(self,ctx,num:int):
    await ctx.channel.purge(limit=num+1)
 @commands.Cog.listener()
 async def on_raw_reaction_add(self,data):
    if str(data.emoji)=="<:OurAfterLife:977520492913242112>":
       guild =self.bot.get_guild(data.guild_id)
       role =guild.get_role(977522981448319026)
       await data.member.add_roles(role)

 @commands.Cog.listener()
 async def on_raw_reaction_add(self,data):
    if str(data.emoji)=="<:__:978272832456900628>":
       guild = self.bot.get_guild(data.guild_id)
       overwrites = {
       guild.default_role: discord.PermissionOverwrite(read_messages=False),
       guild.me: discord.PermissionOverwrite(read_messages=True)
       }
       channel = await data.member.guild.create_text_channel('Tickets', overwrites=overwrites,position=1)
       return channel
 @commands.Cog.listener()
 async def on_reaction_add(self,user,reaction):
  print(user)
  print(reaction)
def setup(bot):
    bot.add_cog(Event(bot))