import json
from discord import Interaction

with open("database/data.json", 'r') as DataFiles:
    data = json.load(DataFiles)

def slash_check(interaction: Interaction):
    return interaction.user.id in data['administrators']
        