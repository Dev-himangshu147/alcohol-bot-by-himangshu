import discord
import platform
from discord.ext import commands
from discord.errors import Forbidden
from config import color, version, prefix, owner

async def send_embed(ctx, embed):
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class help(commands.Cog):
    """cogs/help.py"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *input):
        if not input:
            emb = discord.Embed(title='Commands and modules', color=color,
                                description=f'<:replyL:995703923539193917>  Use `{prefix}help <module>` to gain more information about that module')

            cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'<:replyL:995703923539193917> `{cog}`  \n'#{self.bot.cogs[cog].__doc__}
            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            commands_desc = ''
            for command in self.bot.walk_commands():
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'
                
            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)
            emb.add_field(name="About", value="<:replyL:995703923539193917> `The Bots is developed by` <:py_discord_staff:995705479802130462>[himangshu](https://himangshu147.me), `based on discord.py .`")
            emb.add_field(name="report bug", value=f"<:replyL:995703923539193917> `To report a bug please do` `{prefix}bug <content>`")
            emb.set_footer(text=f"Bot version : {version} | discord.py version : {discord.__version__} | python version : {platform.python_version()}")

        elif len(input) == 1:
            for cog in self.bot.cogs:
                if cog.lower() == input[0].lower():
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                        color=color)
                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    break
            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{input[0]}` before :scream:",
                                    color=color)

   
        elif len(input) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once :sweat_smile:",
                                color=color)

        await send_embed(ctx, emb)

def setup(bot):
    bot.add_cog(help(bot))