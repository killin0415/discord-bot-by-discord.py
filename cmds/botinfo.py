import discord
from discord import app_commands
from discord.ext import commands
from .utils.date import get_date, get_time
from datetime import datetime

class Info(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
      
      
        
    @app_commands.command(name="info",description="show the bot's info")
    async def info(self, interaction: discord.Interaction):
        try:
            embed = discord.Embed(color=discord.Colour.blurple(), title="About", 
                                description="this bot is made by 一顆悠閒的麻鈴糬#4852 in discord.py.")
            embed.set_author(name="NCKUCS potato", url="https://youtu.be/dQw4w9WgXcQ",
                        icon_url="https://cdn.discordapp.com/emojis/905814312252215356.png?size=128")
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/emojis/897077370530431026.png?size=128")
            embed.set_footer(text=get_date())
            
            
            
            embed.add_field(name="Link",
                            value="[Github](https://github.com/killin0415/discord-bot-by-discord.py)\n \
                                    [Support Server](https://discord.gg/59s45PYDHD)", inline=True)
            embed.add_field(name="Bot info", value="version: 1.0.0\npackage used: discord.py 2.1", inline=True)
            embed.add_field(name="Uptime", value=f"{get_time(datetime.now()-self.client.uptime)}")
            
            guild = interaction.guild
            channel = interaction.channel
            self.client.log.info(f"[Slash command] sending info in channel {channel.name} in guild {guild.name}")
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            self.client.log.error(e)

async def setup(client: commands.Bot):
    await client.add_cog(Info(client), guilds=client._guilds)