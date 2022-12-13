import discord
from discord import app_commands
from discord.ext import commands
import datetime
import json
from .utils.embed import Embed

with open("database/birth.json", 'r') as DataFiles:
    data = json.load(DataFiles)


class Birth(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="addbirth", description="tell your birthday to bot.")
    async def addbirth(self, interaction: discord.Interaction, input_date: str):
        """ tell your birthday to bot.

        Args:
            input_date (str): format: yyyy/mm/dd
        """
        try:
            _ = datetime.datetime.strptime(input_date, "%Y/%m/%d")
            user = interaction.user.name
            userid = interaction.user.id
            data[userid] = input_date
            with open("database/birth.json", 'w', encoding='utf8') as dataFile:
                json.dump(data, dataFile, ensure_ascii=False, indent=4)
            await interaction.response.send_message("adding birthday successfully!", ephemeral=True)
            self.client.log.info(f"[Slash commands] adding {user}'s birthday into database.")
        except Exception as e:
            self.client.log.error(e)
            await interaction.response.send_message("your input format is wrong, plz type it again in the correct format.", ephemeral=True)
        


async def setup(client: commands.Bot):
    await client.add_cog(Birth(client), guilds=client._guilds)
