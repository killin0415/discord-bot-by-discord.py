import discord
from discord import app_commands
from discord.ext import commands
import json
import logging
import datetime
import os

with open("data.json", 'r') as DataFiles:
    data = json.load(DataFiles)
 


log = logging.getLogger("main")
 
class aclient(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix='=', intents=discord.Intents.all())
        self.synced=False
        self.initial_extensions = []
        
        date = datetime.date.today().strftime("%Y.%m.%d")
        self.path = f"logs/{date}/"
        
        self._guilds = [discord.Object(id=i) for i in data["guilds"]]
        
        folder = [filename for filename in os.listdir("./cmds")]
        for filename in folder:
                if filename.endswith('.py'):
                    cog = f"cmds.{filename[:-3]}"
                    self.initial_extensions.append(cog)
                    log.info(f"[Loading] found {cog} in cmds")
    
    async def setup_hook(self) -> None:
        try:
            for extension in self.initial_extensions:
                await self.load_extension(extension)
                log.info(f"[Loading] loaded {extension}")           
        except Exception as e:
            log.error(e)
    

    async def on_ready(self):
        await self.wait_until_ready()  
        try:                 
            if not self.synced:
                for i in self._guilds:
                    await self.tree.sync(guild=i)
                    guild = self.get_guild(i.id)
                    log.info(f"synced with {guild.name}")  
                self.synced = True
            logged = f"[Login] Bot has been login as {self.user}."
            log.info(logged)
        except Exception as e:
            log.error(e)
        

TOKEN = data["token"]
client = aclient()
tree = client.tree

main_log_path = client.path + "main.log"
logging.basicConfig(filename=main_log_path,level=logging.INFO, encoding='utf-8', filemode='w',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if not os.path.exists(client.path):
    os.mkdir(client.path)

@tree.command(name="hello", description="say hello to the user", guilds=client._guilds)
async def self(interaction: discord.Integration):
    msg = f"hello, {interaction.user.name}."
    log.info("[Slash commands] " + msg)
    await interaction.response.send_message(f"hello, {interaction.user.name}.")

                
if __name__ == "__main__":
    try:
        client.run(TOKEN)
    except RuntimeError:
        log.info("[Server] server closed")
    except Exception as e:
        log.error(f"[error] {e}")

    
