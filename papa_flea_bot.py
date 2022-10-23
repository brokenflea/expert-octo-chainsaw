import discord
import os
from dotenv import load_dotenv
import time
from discord.ext import tasks
import random

def main():

    load_dotenv()
    bot = discord.Bot()


    @tasks.loop(seconds=60.00)
    async def my_background_task():
        status_list = [
            "The Shining",
            "The Thing",
            "Hot Shots Part Deux",
            "Son of Rambow",
            "Tropic Thunder",
            "The Hidden Fortress",
            "Across the Badlands",
            "The Bandit Queen",
            "The Breaking Point",
            "Champagne for Caesar",
            "Cyrano de Bergerac",
            "Dynamite Pass",
            "Edge of Doom",
            "Fancy Pants",
            "Federal Man",
            "The File on Thelma Jordon",
            "The Girl from San Lorenzo",
            "The Great Plane Robbery",
            "Gunmen of Abilene",
            "Hit Parade of 1951",
            "I Killed Geronimo",
            "The Iroquois Trail",
            "The Jackie Robinson Story",
            "Johnny One-Eye",
            "King of the Bullwhip",
            "The Lawless",
            "Ma and Pa Kettle Go to Town",
            "The Milkman",
            "My Friend Irma Goes West",
            "No Way Out",
            "Once a Thief",
            "The Outriders",
            "Panic in the Streets",
            "Prisoners in Petticoats",
            "Radar Secret Service",
            "Rocky Mountain",
            "Rustlers on Horseback",
            "Six Gun Mesa",
            "The Sound of Fury",
            "Stage to Tucson",
            "Surrender",
            "The Tattooed Stranger",
            "The Tougher They Come",
            "Tyrant of the Sea",
            "Under Mexicali Stars",
            "Vigilante Hideout",
            "Wabash Avenue",
            "West of Wyoming",
            "Wyoming Mail",
            "Young Man with a Horn",
        ]

        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name=random.choice(status_list))) 

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready and online!")
        my_background_task.start()

    @bot.slash_command(name = "hello", description = "Say hello to PapaFleaBot")
    async def hello(ctx):
        await ctx.respond("Eyes up Guardian!")
        
    bot.run(os.getenv('DISCORD_TOKEN'))

if __name__ == "__main__":
    main()
