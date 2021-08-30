#Welcome to Episode 4!
#Learn how to use Embeds!
import os
import discord#pip install discord
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(  command_prefix = '!'#Set the command_prefix
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
  help_em = discord.Embed(description=f"{bot.user.name}'s Commands!\nHelp - Shows this message\nHello - Bot says Hello Back!",color = discord.Color.blurple())#only can have these 3 parameters, title,description and color

  await ctx.send(embed=help_em)#for embed it is same as sending a message but you need to include embed= follow by the variable you assigned for your embed message



token = os.getenv('token')
keep_alive()
bot.run(token)

#Right now all the commands are Basic and not really useful
#Thanks for watching see you in next episode!
#:D
