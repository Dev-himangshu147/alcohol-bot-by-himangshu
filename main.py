import discord
from discord.ext import commands

import colorama
from colorama import Fore
#bot by HIMANGSHU#7120
from config import token, prefix

intents = discord.Intents.all()

bot = commands.AutoShardedBot(command_prefix = prefix,
                              intents = intents,
                              help_command = None,
                              description="desi daru",
                              activity=
                              discord.Activity
                              (type=discord.ActivityType.playing,
                               name="₹ 150 rupia dega"))

@bot.event
async def on_ready():
    print(Fore.CYAN + f"logged in as {bot.user}")
    print("----------------")

events = ["events.command_error"]

if __name__ == "__main__":
    for events in events:
        bot.load_extension(events)
        print(Fore.YELLOW + f"loaded : {events}")
        print("-------|--------")

extensions = ["cogs.misc", "cogs.developer", "cogs.modartion", "cogs.mathe", "cogs.help", "cogs.fun"]
        
if __name__ == "__main__":
    for ext in extensions:
        bot.load_extension(ext)
        print(Fore.GREEN + f"loaded : {ext}")
        print("-------|--------")
        
bot.run(token, reconnect=True)