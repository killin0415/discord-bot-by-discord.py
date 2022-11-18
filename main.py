import discord
from discord import app_commands
from discord.ext import commands
import json
import logging
import os
import asyncio
import sys
import datetime
from datetime import timedelta, timezone
import shutil

if not os.path.exists("logs/"):
    os.mkdir("logs/")
if not os.path.exists("logs/history/"):
    os.mkdir("logs/history/")

with open("data.json", 'r') as DataFiles:
    data = json.load(DataFiles)


 
class aclient(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix='=', intents=discord.Intents.all())
        self.synced=False
        self.initial_extensions = []
        self.log = logging.getLogger("main")
        self.path = f"logs/"
        
        self._guilds = [discord.Object(id=i) for i in data["guilds"]]
        self.tree.copy_global_to(guild=self._guilds[0])
        folder = [filename for filename in os.listdir("./cmds")]
        for filename in folder:
                if filename.endswith('.py'):
                    cog = f"cmds.{filename[:-3]}"
                    self.initial_extensions.append(cog)
                    self.log.info(f"[Loading] found {cog} in cmds")
    
    async def setup_hook(self) -> None:
        try:
            for extension in self.initial_extensions:
                await self.load_extension(extension)
                self.log.info(f"[Loading] loaded {extension}")           
        except Exception as e:
            self.log.error(e)
    

    async def on_ready(self):
        await self.wait_until_ready()  
        self.uptime = datetime.datetime.now()
        try:                 
            if not self.synced:
                for i in self._guilds:
                    await self.tree.sync(guild=i)
                    guild = self.get_guild(i.id)
                    self.log.info(f"synced with {guild.name}")  
                self.synced = True
            logged = f"[Server] Bot has been login as {self.user}."
            self.log.info(logged)
        except Exception as e:
            self.log.error(e)
        

TOKEN = data["token"]
client = aclient()
tree = client.tree

main_log_path = client.path + "main.log"
logging.basicConfig(filename=main_log_path,level=logging.INFO, encoding='utf-8', filemode='w',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
client.log.addHandler(handler)

if not os.path.exists(client.path):
    os.mkdir(client.path)

@tree.command(name="hello", description="say hello to the user", guilds=client._guilds)
async def self(interaction: discord.Integration):
    msg = f"hello, {interaction.user.name}."
    client.log.info("[Slash commands] " + msg)
    await interaction.response.send_message(f"hello, {interaction.user.name}.")


@tree.command(name="shutdown", guilds=client._guilds)
@commands.is_owner()
async def shutdown(interaction: discord.Interaction):
    try:
        await interaction.response.send_message("bot has logged out successfully.", ephemeral=True)
        
        client.log.info("[Server] server closed")
        newfilename = datetime.datetime.now(tz=timezone(offset=timedelta(hours=8))).strftime("%Y.%m.%d.%H.%M")
        client.log.info(f"[Server] server closed in {newfilename}.")
        shutil.copyfile("logs/main.log", f"logs/history/{newfilename}.log")
        
        await asyncio.sleep(1)
        await client.close()
    except Exception as e:
        await interaction.response.send_message("error.", ephemeral=True)
        client.log.error(e)
        exit()
          
if __name__ == "__main__":
    client.run(TOKEN)
    