import pycoingecko
import discord
import os
import asyncio

from discord.ext import commands
from setup_test import BOT_TOKEN

class ZaturiClient(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="$",
            intents=discord.Intents.all()
        )
        self.cg = pycoingecko.CoinGeckoAPI()

    async def on_ready(self):
        """check if bot is ready to use"""
        print(f'We have logged in as {client.user}')

client = ZaturiClient()

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start(BOT_TOKEN)

asyncio.run(main())
