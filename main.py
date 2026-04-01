import discord
import os
import datetime
from colorama import Fore
from commands import parse_dad_joke_trigger

token: str = os.environ.get('BOT_TOKEN')

client = discord.Client(intents=discord.Intents.all())

TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@client.event
async def on_ready():
    print(Fore.LIGHTBLACK_EX + f'{TIMESTAMP}', Fore.LIGHTBLUE_EX + "INFO    ", Fore.WHITE + "Logged in as", Fore.BLUE + f'{client.user}' + Fore.RESET + "!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return None
    
    parsed = parse_dad_joke_trigger(message.content)
    if parsed:
        await message.reply(f"Hi **{parsed.title()}**, I\'m Dad!")

client.run(token)