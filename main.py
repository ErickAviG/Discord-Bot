import discord
from discord.ext import commands
import os

# Crea el bot con prefijo "!"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

# Comando !ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Iniciar el bot con el token
TOKEN = os.getenv("MTEyMTg0NjM3MjUzOTMxNDIxNg.Gz71dz.dX502m5KjacaBNIlxX-jcQGW_jQmvdN2AzKOKY")  # Toma el token desde una variable de entorno
bot.run(TOKEN)
