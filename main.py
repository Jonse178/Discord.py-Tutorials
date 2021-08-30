#Time to learn how to host the bot!
import os
import discord#pip install discord
from keep_alive import keep_alive#import the webserver file

bot = discord.Client()

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
    

token = os.getenv('token')
keep_alive()#call the webserver function
bot.run(token)#run the bot

#The webserver alone can keep the bot online for 1 hour
#But how to make it 24/7 online?, you may ask
#To make it 24/7 need to visit uptimerobot.com