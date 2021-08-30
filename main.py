#Welcome to Episode 5!
#Here you will learn to make Moderation Commands!

import os
import discord#pip install discord
from discord.ext import commands
from keep_alive import keep_alive

prefix = '!'
#commands.when_mentioned_or makes the bot respond to mentions and it's commands!
bot = commands.Bot(  command_prefix = commands.when_mentioned_or(prefix)#Set the command_prefix
                    ,case_insensitive=True#Make commands case insensitive
                    )

#When bot is ready
@bot.event
async def on_ready():
  print(f"Logged in as {bot.user.name} - {bot.user.id}")
bot.remove_command('help')#removes the default help command

@bot.command()
async def hello(ctx):
  embed = discord.Embed(title = f'Hello {ctx.author.name}',description = f"I am {bot.user.name}!\nI am a bot created by Jonse for the new Discord.py Yotube Tutorial Series!",color = discord.Color.blue())

  await ctx.send(embed=embed) 

@bot.command()
async def help(ctx):
  help_em = discord.Embed(description=f"{bot.user.name}'s Commands!\nHelp - Shows this message\nHello - Bot says Hello Back!",color = discord.Color.blurple())
  await ctx.send(embed=help_em)

@bot.command()
@commands.has_permissions(kick_members = True)#Checks whether the command user has permissions to kick in the server
async def kick(ctx,user:discord.Member,*,reason = 'no reason provided'):
  if reason == 'no reason provided':
    pass
  else:
    reason = reason

  kick_msg = discord.Embed(title= f"{ctx.author.name} kicked {user.name}",description = f"Reason: {reason}")#Just to be clear ctx.author.name is the person using the command
  try:
    await user.kick(reason=reason)
    await ctx.send(embed = kick_msg)
  except:
    await ctx.send(f'{ctx.author.mention} I do not have the permission to kick the user!\nPlease ask an admin or someone else with a high enough permissions to give me kick perms!')
    #no errors shown in the console
  

#We are getting this error in the console because the bot doesn't have the kick Permission
#ban command
@bot.command()
@commands.has_permissions(ban_members = True)#Checks whether the command user has permissions to kick in the server
async def ban(ctx,user:discord.Member,*,reason = 'no reason provided'):
  if reason == 'no reason provided':
    pass
  else:
    reason = reason

  ban_msg = discord.Embed(title= f"{ctx.author.name} baned {user.name}",description = f"Reason: {reason}")#Just to be clear ctx.author.name is the person using the command
  try:
    await user.ban(reason=reason)
    await ctx.send(embed = ban_msg)
  except:
    await ctx.send(f'{ctx.author.mention} I do not have the permission to ban the user!\nPlease ask an admin or someone else with a high enough permissions to give me ban perms!')
    #Easy game:D
  

token = os.getenv('token')
keep_alive()
bot.run(token)

#Thanks for watching
#See you in the next Episode :D