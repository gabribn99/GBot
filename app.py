from nextcord import Intents
from nextcord.ext import commands
import requests
import json
import random
import os

links = json.load(open("gifs.json"))

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='--', intents=intents)


@bot.command(name='ayuda')
async def help(ctx):
    await ctx.send(
        '```'
        '    Los comandos se realizan con la extension: --\n'
        '_____________________________________________________________\n'
        'saluda            >>    Realiza un saludo\n'
        'perro             >>    Envía una foto de un perro\n'
        'perrocomiendo     >>    Envía un gif de un perro comiendo\n'
        'perrojugando      >>    Envía un gif de un perro jugando\n'
        'perrodurmiendo    >>    Envía un gif de un perro durmiendo\n'
        '_____________________________________________________________```')


@bot.command(name="saluda")
async def SendMessage(ctx):
    await ctx.send('¡Hola! Soy GBot, y estoy aquí para ayudarte.')


@bot.command(name='perro')
async def sendRandomDog(ctx):
    response = requests.get("http://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)


@bot.command(name="gifs", aliases=["perrocomiendo", "perrojugando", "perrodurmiendo"])
async def Gifs(ctx):
    await ctx.send(random.choice(links[ctx.invoked_with]))


@bot.command(name='suma')
async def Sumar(ctx, a, b):
    result = int(a) + int(b)
    await ctx.send(f'El resultado de la suma {a} + {b} es: {result}')


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])
