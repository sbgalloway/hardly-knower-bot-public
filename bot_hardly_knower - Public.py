import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Botter?')

@client.event
async def on_reaction_add(reaction, user):
  print('reaction seen')
  print(reaction.emoji == '🍆')
  if(reaction.emoji == '🍆'):
    if reaction.message.author == client.user:
      return

    msg = reaction.message.content

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
      await reaction.message.reply(longest + "? I hardly know her!")
    else:
      reacters = await reaction.users().flatten()
      first = reacters[0]
      await reaction.message.reply(first.mention + ' at least one word in the message needs to end in \'er\' for this joke to work dumbass.', mention_author=False)

client.run('your token here')