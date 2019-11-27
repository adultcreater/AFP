from discord.ext import commands
from utils import date
from discord import Embed
from random import shuffle, choice
import discord
import traceback


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.load_ousama = date.load('ousama')
        self.save_ousama = date.save
    
    
    def user_date(self, ctx):
        guild = str(ctx.guild.id)
        voice = str(ctx.author.voice.channel.id)
        if self.load_ousama.get(guild, None) is None:
            self.load_ousama[guild] = {}
            self.save_ousama(self.load_ousama, 'ousama')

        if self.load_ousama[guild].get(voice, None) is None:
            self.load_ousama[guild][voice] = {}
            self.save_ousama(self.load_ousama, 'ousama')

        voice_key = self.load_ousama[guild][voice]
        vmembers = []

        for mem in ctx.author.voice.channel.members:
            
            vmembers.append(mem)
        print(vmembers)
        shuffle(vmembers)
        """
        for member_count in range(len(vmembers) + 1):
            for member in ctx.author.voice.channel.members:
                print(member)
                voice_key[str(member_count)] = str(member)
                self.save_ousama(self.load_ousama, 'ousama')"""

        counter = 0
        while True:
            for member in ctx.author.voice.channel.members:
                voice_key[str(counter)] = str(member)
                self.save_ousama(self.load_ousama, 'ousama')
                counter = counter + 1
            break
        ousama = choice(vmembers)
        print(f'王様-{ousama}')
        self.load_ousama[guild][voice]['ousama'] = str(ousama)
        self.save_ousama(self.load_ousama, 'ousama')


    @commands.command(name = '王様ゲーム')
    async def ousama(self, ctx):
        if not ctx.author.voice:
            return

        VCID = str(ctx.author.voice.channel.id)
        GUIDID = str(ctx.guild.id)
        
        self.user_date(ctx)
        
        embed = Embed(
            title = '王様ゲーム-Info',
            description = ','.join(memb.mention for memb in ctx.author.voice.channel.members),
            colour = ctx.author.color
        )
        
        embed.add_field(
            name = '王様',
            value = self.load_ousama[GUIDID][VCID]['ousama'],
            inline = False
        )

        embed.add_field(
            name = f'1番から{len(ctx.author.voice.channel.members)}の中から番号で誰かを指定して命令してください',
            value = '命令が終わったら必ず**王様**が「王様ゲーム番号」と送信してください',
            inline = False
        )

        embed.set_footer(
            text = '王様ゲームを開始します'
        )

        await ctx.send(embed = embed)


        def start_check(mes):
            return mes.channel == ctx.channel and str(mes.author) == self.load_ousama[GUIDID][VCID]['ousama'] and mes.content == '王様ゲーム番号'


        mes = await self.bot.wait_for('message', check = start_check)


        embed_ = Embed(
            title = '王様ゲーム-Info',
            description = ','.join(memb.mention for memb in ctx.author.voice.channel.members),
            colour = ctx.author.color
        )
    
        for k, v in self.load_ousama[GUIDID][VCID].items():
            embed_.add_field(
                name = k,
                value = v,
                inline = False
            )

        embed_.set_footer(
            text = 'それでは王様ゲームをスタートします'
        )
        
        await ctx.send(embed = embed_)

        self.load_ousama[GUIDID].pop(VCID)
        return self.save_ousama(self.load_ousama, 'ousama')

    @ousama.error
    async def ousama_error(self, ctx, error):
        await ctx.send(f'```py\n{traceback.format_exc()}\n```')

def setup(bot):
    bot.add_cog(Game(bot))