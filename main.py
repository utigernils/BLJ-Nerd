import discord
import AI

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

async def smartBot(text, message):
    await message.reply(AI.talkWithBot(str(message.author) + ": " + str(text), 0))

async def dumbBot(text, message):
    await message.reply(AI.talkWithBot(str(message.author) + ": " + str(text), 1))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?S'):
        await smartBot(message.content[2:], message)

    if message.content.startswith('?B'):
        await dumbBot(message.content[2:], message)

client.run('Discord Token')
