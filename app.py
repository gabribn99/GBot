from nextcord import Intents
from nextcord.ext import commands
import requests
import json
import random
import os

links = json.load(open("gifs.json"))

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='defcon ', intents=intents)


@bot.cammand(name='ayuda')
async def help(ctx):
    await ctx.send(
        '```'
        '    Los comandos se realizan con la extension: defcon'
        '_____________________________________________________________'
        'saluda            >>    Realiza un saludo'
        'perro             >>    Envía una foto de un perro'
        'perrocomiendo     >>    Envía un gif de un perro comiendo'
        'perrojugando      >>    Envía un gif de un perro jugando'
        'perrodurmiendo    >>    Envía un gif de un perro durmiendo'
        '_____________________________________________________________```')


@bot.command(name="saluda")
async def SendMessage(ctx):
    await ctx.send('¡Hola!, soy Bad Def, y estoy aquí para ayudarte.')


@bot.command(name='perro')
async def sendRandomDog(ctx):
    response = requests.get("http://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)


@bot.command(name="gifs", aliases=["perrocomiendo", "perrojugando", "perrodurmiendo"])
async def Gifs(ctx):
    await ctx.send(random.choice(links[ctx.invoked_with]))


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])
