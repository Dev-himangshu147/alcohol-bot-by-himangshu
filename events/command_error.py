import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

from config import color

class command_error(commands.Cog, command_attrs=dict(hidden=True)):
    """events/command_error.py"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="<:requirements:995957813958410302> please pass in all requirements", color=color)
            await ctx.send(embed=embed, delete_after = 5)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="<:permissions:995957625768378491> you don't have permission to use this", color=color)
            await ctx.send(embed=embed, delete_after = 5)
            
def setup(bot):
    bot.add_cog(command_error(bot))