import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import pyfiglet
from pyfiglet import figlet_format, FontNotFound
import json
import utils
import fortune
import subprocess

#os.environ['FORTUNE_FILE'] = "/home/pi/Desktop/UB/FORTUNE_FILE/fortunes.txt"
 
class fun:
    def __init__(self, bot):
        self.bot = bot


    # async def randomimageapi(self, ctx, url, endpoint):
    #     try:
    #         r = await http.get(url, res_method="json", no_cache=True)
    #     except json.JSONDecodeError:
    #         return await ctx.send("Nothing from the API. fuck.")

    #     await ctx.send(r[endpoint])






        #send the whatthefuck image              
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def wtf(self, ctx):
        embed = discord.Embed(name='WTF')
        embed.set_image(url = 'https://i.imgur.com/fKg52jo.png')
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def maga(self, ctx):
        embed = discord.Embed(name='Praise Trump')
        embed.set_image(url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/MAGA.svg/1280px-MAGA.svg.png')
        await self.bot.say(embed=embed)





    @commands.command(name='randomcolor', aliases=['randcolor', 'rc'])
    async def randomcolor(self, message):

        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4, 0x00ff92, 0xfd00ff, 0xffffff, 0x000000, 0xa1a1a1, 0x8ae7f4, 0x6200fd]


        embed = discord.Embed(name="\u200b", color=random.choice(colors))
        await self.bot.say(embed=embed)




#repeat command
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def say(self, *args):   
        output = ""
        for word in args:
            output += word
            output += ' '
        await self.bot.say(output)




    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def rate(self, *args):
        num = random.randint(0, 100)
        deci = random.randint(0, 9)
        output = ""
        for word in args:
            output += word
            output += ' '
        if num == 100:
            deci = 0
        embed = discord.Embed(title='Rate', description=f"{output} is a **{num}.{deci} / 100**")
        await self.bot.say(embed=embed)





        
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def egg(self, ctx):
        embed = discord.Embed(title='You found an easter egg, congrats!')
        embed.set_image(url = 'http://clipart-library.com/data_images/360077.png')
        await self.bot.say(embed=embed)

    
    
    

        




def setup(bot):
    bot.add_cog(fun(bot))
