import discord
from discord.ext import commands

from config import color

class mathe(commands.Cog):
    """cogs/mathe.py"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "add", help="<:replyL:995703923539193917> .add <num1> <num2>")
    async def add(self, ctx, arg1: int, arg2: int):
        embed=discord.Embed(title = f"{arg1} + {arg2} = {arg1 + arg2}", color = color)
        await ctx.send(embed = embed)

    @commands.command(name = "subs", help="<:replyL:995703923539193917> .subs <num1> <num2>")
    async def subs(self, ctx, arg1: int, arg2: int):
        embed=discord.Embed(title = f"{arg1} - {arg2} = {arg1 - arg2}", color = color)
        await ctx.send(embed = embed)

    @commands.command(name = "mul", help="<:replyL:995703923539193917> .mul <num1> <num2>")
    async def mul(self, ctx, arg1: int, arg2: int):
        embed=discord.Embed(title = f"{arg1} * {arg2} = {arg1 * arg2}", color = color)
        await ctx.send(embed = embed)
         
    @commands.command(name = "div", help = "<:replyL:995703923539193917> .div <num1> <num2>")
    async def div(self, ctx, arg1: int, arg2: int):
        embed=discord.Embed(title = f"{arg1} ÷ {arg2} = {arg1 / arg2}", color = color)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(mathe(bot))