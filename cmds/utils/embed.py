import discord
import datetime
from .date import get_date


class Embed:
    def __init__(self):
        self.embed = discord.Embed(color=discord.Colour.blurple())
        self.embed.set_author(name="NCKUCS potato", url="https://youtu.be/dQw4w9WgXcQ",
                    icon_url="https://cdn.discordapp.com/emojis/905814312252215356.png?size=128")
        self.embed.set_thumbnail(
        url="https://cdn.discordapp.com/emojis/897077370530431026.png?size=128")
        self.embed.set_footer(text=get_date())
        
    def add(self, name: str, value: str, inline: bool=False):
        self.embed.add_field(name=name, value=value, inline=inline)
    
    def get(self):
        return self.embed
        