import discord
from discord import app_commands
from discord.ext import commands
from .utils.check import slash_check 
from .utils.embed import Embed


class Message(commands.Cog):
    def __init__(self, client):
        self.client = client
    
        
    @app_commands.command(name="purge", description="purge the amount of messages")
    @app_commands.check(slash_check)
    async def purge(self, interaction: discord.Interaction, num: int):
        channel = interaction.channel
        user = interaction.user
        await interaction.response.defer()
        await channel.purge(limit=num+1)
        self.client.log.info(f"[Slash command] purges {num} messages in {channel.name} by {user}")
        embed = Embed()
        embed.add(name="/purge", value=f"purges {num} messages in {channel.name}")
        embed = embed.get()
    
        await channel.send(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(Message(client), guilds=client._guilds)