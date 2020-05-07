import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random


class gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def btfo(self, ctx):

        btfo = ['https://i.imgur.com/1iNbYzK.gif', 'https://i.imgur.com/kGuGQBh.gif', 'https://i.imgur.com/ken93BF.gif', 'https://i.imgur.com/RLpF0J8.gif']
        
        embed = discord.Embed(description="**iTODDLERS BTFO**", color=0xff0000) 
        embed.set_image(url = random.choice(btfo))  
        await ctx.send(embed=embed)






def setup(bot):
    bot.add_cog(gif(bot))