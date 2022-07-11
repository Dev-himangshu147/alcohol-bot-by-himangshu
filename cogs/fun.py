import discord
import aiohttp
import random
from discord.ext import commands

from config import color

class fun(commands.Cog):
    """fun commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed = discord.Embed(title = res['data']['children'][random.randint(0,25)]["data"]["title"], color=color)
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(fun(bot))