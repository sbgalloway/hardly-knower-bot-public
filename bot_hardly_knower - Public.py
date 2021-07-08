import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Botter?')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  x = msg.split()
  y = [] 
  z = 0
  longest = ""
  for word in x:
    if(word.endswith('er')):
      y.append(word)
  for word in y:
    print(word + str(len(word)) + " > " + str(z))
    if(len(word) > z):
      z = len(word)
      longest = word
      print(longest)

  if(longest != ""):
    await message.channel.send(longest + "? I hardly know her! @" + str(message.author))

client.run('your token here')