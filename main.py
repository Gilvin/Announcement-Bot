import discord

client = discord.Client()
@client.event
async def on_ready():
  print('We hacve logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('$hello'):
    await msg.channel.send('Hello!')

client.run()