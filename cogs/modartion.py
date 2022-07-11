import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

from config import color

class modartion(commands.Cog):
    """cogs/modartion.py"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help = "delete message")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title = f"{ctx.author} cleared {amount} messages", color = color)
        await ctx.send(embed=embed, delete_after = 3)

    @commands.command(name='kick', help="kicks user")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed=discord.Embed(title=f'{member.mention} has been kicked for: "{reason}"', color=color)
        await ctx.send(embed=embed)
  
def setup(bot):
    bot.add_cog(modartion(bot))