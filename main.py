import discord
from discord.ext import commands
from dotenv import load_dotenv
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

TOKEN = os.environ.get("TOKEN")
bot.run(TOKEN)
