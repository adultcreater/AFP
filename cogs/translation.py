from discord.ext import commands
import discord
import googletrans
class Trans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def trans(self, ctx, src: str, dest: str, *, transword = None):
        if transword is None:
            return
        text = googletrans.Translator().translate(transword, src=src, dest=dest).text
        await ctx.send(text)

    @commands.command(aliases = ['ll'])
    async def launglist(self, ctx):

        e = discord.Embed(
            description = f'[一覧はこちら]({"https://www.benricho.org/translate/languagecode.html"})'
        )
        await ctx.send(embed = e)

def setup(bot):
    bot.add_cog(Trans(bot))
