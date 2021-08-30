#Welcome to Episode 3!
#Introduction to commands!
import os
import discord#pip install discord
from discord.ext import commands
from keep_alive import keep_alive#import the webserver file

bot = commands.Bot(  command_prefix = '!'#Set the command_prefix
                    ,case_insensitive=True#Make commands case insensitive
                    )

#When bot is ready
@bot.event
async def on_ready():
  print(f"Logged in as {bot.user.name} - {bot.user.id}")

@bot.event
async def on_message(message):
  if message.content.startswith('hello'):#when we send hello
    await message.channel.send(f'Hello I am `{bot.user.name}`')#bot replies with this
  elif message.content.startswith('invite'):
    await message.channel.send(f'https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=0&scope=bot')#bot's invite from developer portal

  await bot.process_commands(message)#This fixes the bug

#I forgot to mention when using on_message with commands there is a small bug. The on_message stops the commands.
bot.remove_command('help')#removes the default help command

@bot.command()
async def hello(ctx):
  await ctx.send('Hi')  

@bot.command()
async def help(ctx):
  await ctx.send(f"{bot.user.name}'s Commands!\nHelp - Shows this message\nHello - Bot says Hello Back!")

token = os.getenv('token')
keep_alive()#call the webserver function
bot.run(token)#run the bot

#Next episode I will teach on Embeds