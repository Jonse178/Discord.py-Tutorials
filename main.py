'''
This is the IDE you will be using, it is called Replit.
This is an online ide where if you have insufficient space in your local PC you can use this to code.
Also it has other cool features!
'''
#first import the discord.py library module
#it also requires pip install
import os#A really helpful module especisally rlly useful when usning replit with api keys,token etc which you want to hide
import discord#pip install discord

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
    #since we are using bot.user.id, you can use this same code for a different bot and still get the correct invite link, else if you use the id by itself and u use this code for a different bot it will still give you the invite link for this bot

#for saftey reason use the os module to get the token from an env file(secret variables)
token = os.getenv('token')#get this from developer portal
bot.run(token)#run the bot

#Episode 2 I will teach you how to host this bot
#As Currently bot will go offline if you close this tab
#Thanks for watching!