import discord
import os
client = discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('!hello'):
    await msg.channel.send('Hello!')

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('!youtube'):
    await msg.channel.send('https://www.youtube.com/channel/UC0pBDD3DkwE-G7efI8lZLdQ')

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('!twitch'):
    await msg.channel.send('https://www.twitch.tv/gilvincible')

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('!insta'):
    await msg.channel.send('https://www.instagram.com/gilvinchy')

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('!twitter'):
    await msg.channel.send('https://twitter.com/gilvinchy')

client.run(os.getenv('BOT'))