import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random
import requests
import json
colors = [0xff00e7, 0xff00c1, 0xe141ff, 0xf417d5, 0xff0074, 0xbd00ff]
class tagfun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



#shoot someone
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def shoot(self, ctx, user: discord.Member):  
        if user.id == 483026011882258446:
            usr = await self.bot.fetch_user(804007711800295506)
            embed = discord.Embed(name="You've been shot.", color=random.choice(colors))
            embed.add_field(name=usr.name + ":gun:   you were shot, you will probably bleed out and die.".format(user.name), value='shot by {}'.format(ctx.message.author.name), inline=True) 
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(name="You've been shot.", color=random.choice(colors))
            embed.add_field(name="{}:gun:   you were shot, you will probably bleed out and die.".format(user.name), value='shot by {}'.format(ctx.message.author.name), inline=True) 
            await ctx.send(embed=embed)


#shoot someone
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def stab(self, ctx, user: discord.Member):  
        if user.id == 483026011882258446:
            usr = await self.bot.fetch_user(804007711800295506)
            embed = discord.Embed(name="You've been shot.", color=random.choice(colors))
            embed.add_field(name=":dagger:"+ usr.name +"  You were stabbed. Go to a hospital.", value= 'stabbed by {}'.format(ctx.message.author.name), inline=True) 
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(name="You've been shot.", color=random.choice(colors))
            embed.add_field(name=":dagger:{}  You were stabbed. Go to a hospital.".format(user.name), value= 'stabbed by {}'.format(ctx.message.author.name), inline=True) 
            await ctx.send(embed=embed)

#and here comes the holy grail of APIs. Thank you nekos.life for making such a wonderful collection of images. 
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def slap(self, ctx, user: discord.Member):
        response = requests.get("https://nekos.life/api/v2/img/slap")
        data = response.json()
        embed = discord.Embed(description="{} was slapped by {}".format(user.name, ctx.message.author.name), color=random.choice(colors))
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def hug(self, ctx, user: discord.Member):
        response = requests.get("https://nekos.life/api/v2/img/hug")
        data = response.json()
        embed = discord.Embed(description="{} was hugged by {}".format(user.name, ctx.message.author.name), color=random.choice(colors))
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def pat(self, ctx, user: discord.Member):
        response = requests.get("https://nekos.life/api/v2/img/pat")
        data = response.json()
        embed = discord.Embed(description="{} was patted by {}".format(user.name, ctx.message.author.name), color=random.choice(colors))
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def kiss(self, ctx, user: discord.Member):
        response = requests.get("https://nekos.life/api/v2/img/kiss")
        data = response.json()
        embed = discord.Embed(description="{} was kissed by {}".format(user.name, ctx.message.author.name), color=random.choice(colors))
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def spank(self, ctx, user: discord.Member):
        fucktonOfLinks = ["https://i.imgur.com/V0LMJkt.gif", "https://i.imgur.com/SnZ8Szh.gif", "https://i.imgur.com/jzJyCJp.gif", "https://i.imgur.com/BZDfN8b.gif", "https://i.imgur.com/9DMPdIV.gif", "https://i.imgur.com/j90b50B.gif", "https://i.imgur.com/JyjwigU.gif"] #God forgive me for this atrocity. 
        embed = discord.Embed(description="{} was spanked by {}".format(user.name, ctx.message.author.name), color=random.choice(colors))
        embed.set_image(url=random.choice(fucktonOfLinks))
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def cuddle(self, ctx, user: discord.Member):
        response = requests.get("https://nekos.life/api/v2/img/cuddle")
        data = response.json()
        embed = discord.Embed(description="{} cuddles with {}".format(ctx.message.author.name, user.name), color=random.choice(colors))
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def poke(self, ctx, user: discord.Member):
        response = requests.get("https://nekos.life/api/v2/img/poke")
        data = response.json()
        embed = discord.Embed(description="{} was poked by {}".format(user.name, ctx.message.author.name), color=random.choice(colors))
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(tagfun(bot))
