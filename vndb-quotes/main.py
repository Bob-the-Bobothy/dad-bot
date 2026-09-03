from enum import nonmember

import discord
from discord import app_commands
from pathlib import Path
import random
import asyncio
import os

token: str = os.environ.get("VNDB_BOT_TOKEN")

class Client(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

_quotes = None
_quotes_lock = asyncio.Lock()

def build_quotes():
    quotes = []
    INPUT = Path("quotes")

    with INPUT.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            columns = line.rstrip("\r\n").split("\t")

            if len(columns) >= 5:
                quote = columns[4].strip()

                if quote:
                    quotes.append(quote)

    return quotes

async def get_quotes():
    global _quotes

    if _quotes is None:
        async with _quotes_lock:
            if _quotes is None:
                _quotes = await asyncio.to_thread(build_quotes)

    return _quotes

client = Client()

@client.tree.command(
    name="get",
    description="Get a quote"
)
async def get_quote(interaction: discord.Interaction):
    quotes = await get_quotes()

    await interaction.response.send_message(random.choice(quotes))

client.run(token)
