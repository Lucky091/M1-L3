import discord
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Привет'):
        await message.channel.send('Привет!')
    elif message.content.startswith('Пока'):
        await message.channel.send('Пока')
    elif message.content.startswith('Смайлик'):
        await message.channel.send(gen_smilik())
    elif message.content.startswith('Подбросить монетку'):
        await message.channel.send(flip_monetka())
    elif message.content.startswith('Пароль'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Я не знаю такого!")

client.run("Токен")