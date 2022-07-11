import discord
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext import commands

from config import color

class misc(commands.Cog):
    """cogs/misc.py"""
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(help="shows bot latency")
    async def ping(self, ctx):
        embed = discord.Embed(title = f"<:latency:995718562532573184> {round(self.bot.latency * 1000)} ms", color = color)
        await ctx.send(embed=embed)
    
    @commands.command(help="bot source code")
    async def src(self, ctx):
        em = discord.Embed(title = "<:github_code:995718034868158595> comming soon", color = color)
        await ctx.send(embed=em)

    @commands.command(help = "report bug")
    async def bug(self, ctx, bug):
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/995696604847804491/-UiMNrj9tt9LVsKh1DFFUP-vEDoKUfjp4QYJIzkcxWyaYB7oQCYVRgb8OW9e4P-F2qi7')
        embed = DiscordEmbed(title=f'{ctx.author} just reported a bug', description=f"Bug : `{bug}`", color=color)
        webhook.add_embed(embed)
        em=discord.Embed(title = "bug submitted", description = f"your bug : {bug}", color=color)
        await ctx.send(embed=em)
        response = webhook.execute()

    @commands.command(help= "invite bot")
    async def invite(self, ctx):
        embed=discord.Embed(title= "invite alcohol to your discord server", description= "[invite](https://discord.com/api/oauth2/authorize?client_id=994523272496554044&permissions=8&scope=bot) | [support](https://discord.gg/CaDpa7bQ8q)")
        await ctx.send(embed=embed)
   
def setup(bot):
    bot.add_cog(misc(bot))