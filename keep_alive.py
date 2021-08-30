#This is the webserver code to host the bot
from flask import Flask
from threading import Thread

app = Flask('')
port = 8080
host = "0.0.0.0"

@app.route('/')
def main():
  return "Bot is Alive"

def run():
  app.run(host=host,port=port)

def keep_alive():
  server = Thread(target=run)
  server.start()