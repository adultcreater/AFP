from discord.ext import commands
from discord import Embed
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.helps = {
            '**王様ゲーム**':
                '王様ゲームを開始します',
            '**trans**[before laung] [after laung]':
                '指定された言語から指定された言語へ翻訳します',
            '**launglist**':
                '使用できる言語を表示します',
            '**join**':
                'メンバーをVCに参加させます',
            '**play** [url or title]':
                'プレイリストに曲を追加し、指定された音楽を再生します',
            '**pause**':
                '現在再生中の曲をスキップします',
            '**resume**':
                '曲の再生を再開にします',
            '**stop**':
                '現在再生中の曲をストップしVCから退出します',
            '**playlist**':
                'subcommand: shuffle, remove, repeat',
            '**clear**':
                'プレイリストをクリアします',
            '**status**':
                '現在再生中の曲を表示します',
            '**skip**':
                '現在再生中の曲をスキップする投票をします。',
            '**set_volume**':
                'ボリュームを設定します'
        }


    @commands.command()
    async def help(self, ctx):
        embed = Embed(
            title = self.bot.user.name,
            url = 'https://github.com/adultcreater/AFP',
            description = 'This is AFP-Bot',
            colour = ctx.author.color
        )
        embed.set_thumbnail(
            url = self.bot.user.avatar_url
        )
        for k, v in self.helps.items():
            embed.add_field(
                name = k,
                value = v,
                inline = False
            )
        await ctx.send(embed= embed)


def setup(bot):
    bot.add_cog(Help(bot))