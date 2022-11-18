from discord.ext import commands
import discord
from discord import app_commands
import logging
import os



class Log(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
    
    @app_commands.command(name="log", description="get the bot's log.", )
    async def log(self, interaction: discord.Interaction):
        file_path = f"./logs/main.log"
        user = interaction.user
        guild = interaction.guild
        
        await interaction.response.send_message("here you are.", file=discord.File(file_path), ephemeral=True)
        self.client.log.info(f"[slash command] sending logs to {user} in {guild.name}")
        
async def setup(client):
    await client.add_cog(Log(client), guilds=client._guilds)
                 
        
        
    
    