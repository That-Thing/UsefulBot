import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random


class tagfun:
    def __init__(self, bot):
        self.bot = bot



#shoot someone
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def shoot(self, ctx, user: discord.Member):  

        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

        embed = discord.Embed(name="You've been shot.", color=random.choice(colors))
        embed.add_field(name="{}:gun:   you were shot, you will probably bleed out and die.".format(user.name), value='shot by {}'.format(ctx.message.author.name), inline=True) 
        await self.bot.say(embed=embed)


#shoot someone
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def stab(self, ctx, user: discord.Member):  

        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

        embed = discord.Embed(name="You've been shot.", color=random.choice(colors))
        embed.add_field(name=":dagger:{}  You were stabbed. Go to a hospital.".format(user.name), value= 'stabbed by {}'.format(ctx.message.author.name), inline=True) 
        await self.bot.say(embed=embed)







def setup(bot):
    bot.add_cog(tagfun(bot))