from core.classes import Cog_Extention
import discord
from discord.ext import commands, tasks
import datetime 
from datetime import timedelta, timezone, time, date

class Event(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        msg = message.content
        if message.author != self.client.user:
            if "早ㄤ" in msg:
                await message.channel.send("早ㄤ")
            elif "早安" in msg:
                await message.channel.send("早ㄤ")

async def setup(client: commands.Bot):
    await client.add_cog(Event(client), guilds=client._guilds)