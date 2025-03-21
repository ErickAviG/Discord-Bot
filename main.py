import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from flask import Flask

# Carga el archivo .env
load_dotenv()

# Crea el bot con prefijo "!"
intents = discord.Intents.default()
intents.message_content = True  # Habilita el intent de contenido de mensajes
bot = commands.Bot(command_prefix="!", intents=intents)

# Crea una aplicación Flask para monitorear con UptimeRobot
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot está en línea!'

@app.route('/ping')
def ping():
    return 'Pong! 🏓'

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

# Comando !ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Iniciar el bot con el token y el servidor Flask
if __name__ == "__main__":
    from threading import Thread

    # Inicia Flask en un hilo separado
    def run_flask():
        app.run(host="0.0.0.0", port=5000)

    thread = Thread(target=run_flask)
    thread.start()

    # Inicia el bot de Discord
    TOKEN = os.environ.get("TOKEN")
    bot.run(TOKEN)
