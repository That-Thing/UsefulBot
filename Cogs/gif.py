import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random


class gif:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def hug(self, ctx, user: discord.Member):

        hug = ['https://i.imgur.com/hejbwuS.gif', 'https://i.imgur.com/56OCPoy.gif', 'https://i.imgur.com/bCnrjAe.gif', 'https://i.imgur.com/DDl2DjX.gif', 'https://i.imgur.com/qQkY8VP.gif', 'https://i.imgur.com/hD5pZrs.gif', 'https://i.imgur.com/0PZiCCX.gif', 'https://i.imgur.com/AZCevvt.gif', 'https://i.imgur.com/BdGIkOM.gif', 'https://i.imgur.com/QG7xFge.gif', 'https://i.imgur.com/ybXSvPc.gif', 'https://i.imgur.com/Y6srht4.gif', 'https://i.imgur.com/fpT2uFh.gif', 'https://i.imgur.com/hdFQjqr.gif', 'https://i.imgur.com/IMtQjgT.gif', 'https://i.imgur.com/RLxvnXQ.gif', 'https://i.imgur.com/vsuKYAh.gif', 'https://i.imgur.com/e1ofXDH.gif', 'https://i.imgur.com/g2bvb0d.gif', 'https://i.imgur.com/8Efj2gb.gif']
        colors = [0xff00e7, 0xff00c1, 0xe141ff, 0xf417d5, 0xff0074, 0xbd00ff]
        
        embed = discord.Embed(description="{} was hugged by {}".format(user.name, ctx.message.author.name), color=random.choice(colors)) 
        embed.set_image(url = random.choice(hug))  
        await self.bot.say(embed=embed)



    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def kiss(self, ctx, user: discord.Member):

        kiss = ['https://i.imgur.com/ukUOotJ.gif', 'https://i.imgur.com/SEHW6HV.gif', 'https://i.imgur.com/mDQ9lau.gif', 'https://i.imgur.com/tHONYnu.gif', 'https://i.imgur.com/RygJxDO.gif', 'https://i.imgur.com/RqZqrd4.gif', 'https://i.imgur.com/12MrqcM.gif', 'https://i.imgur.com/l2ejsp0.gif', 'https://i.imgur.com/8VmMBHA.gif', 'https://i.imgur.com/ZtMRVFF.gif', 'https://i.imgur.com/phQTVnl.gif', 'https://i.imgur.com/2O32yQm.gif', 'https://i.imgur.com/DLGxJVh.gif', 'https://i.imgur.com/l29fhBO.gif', 'https://i.imgur.com/Wih2WjM.gif']
        colors = [0xff00e7, 0xff00c1, 0xe141ff, 0xf417d5, 0xff0074, 0xbd00ff]
        
        embed = discord.Embed(description="{} was kissed by {}".format(user.name, ctx.message.author.name), color=random.choice(colors)) 
        embed.set_image(url = random.choice(kiss))  
        await self.bot.say(embed=embed)


    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def btfo(self):

        btfo = ['https://i.imgur.com/1iNbYzK.gif', 'https://i.imgur.com/kGuGQBh.gif', 'https://i.imgur.com/ken93BF.gif', 'https://i.imgur.com/RLpF0J8.gif']
        
        embed = discord.Embed(description="**iTODDLERS BTFO**", color=0xff0000) 
        embed.set_image(url = random.choice(btfo))  
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def slap(self, ctx, user: discord.Member):

        slap = ['https://i.imgur.com/7CGaETY.gif', 'https://i.imgur.com/2HvqTwW.gif', 'https://i.imgur.com/kH8kMAt.gif', 'https://i.imgur.com/2IRug9R.gif', 'https://i.imgur.com/7NViK03.gif', 'https://i.imgur.com/q33bSxk.gif', 'https://i.imgur.com/AEKSbZV.gif', 'https://i.imgur.com/62UHivx.gif', 'https://i.imgur.com/df66TfG.gif', 'https://i.imgur.com/FNUuBpZ.gif', 'https://i.imgur.com/FNUuBpZ.gif', 'https://i.imgur.com/RLAtotk.gif', 'https://i.imgur.com/RLAtotk.gif', 'https://i.imgur.com/c80nmyM.gif', 'https://i.imgur.com/c80nmyM.gif', 'https://i.imgur.com/b4VlpwP.gif', 'https://i.imgur.com/b4VlpwP.gif', 'https://i.imgur.com/dnB0ol5.gif',]
        colors = [0x2f00ff, 0x70a5ff, 0x6a66d0, 0x496a98, 0x24009a]
        
        embed = discord.Embed(description="{} was slapped by {}".format(user.name, ctx.message.author.name), color=random.choice(colors)) 
        embed.set_image(url = random.choice(slap))  
        await self.bot.say(embed=embed)






def setup(bot):
    bot.add_cog(gif(bot))