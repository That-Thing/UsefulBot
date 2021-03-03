import requests
import json
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


#boobis
    @commands.command()
    async def boobs(self,ctx):
        urls = ["https://nekos.life/api/v2/img/boobs","https://nekos.life/api/v2/img/tits"]
        response = requests.get(random.choice(urls))
        data = response.json()
        embed = discord.Embed(description="Boobs")
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
#lewd nekos
    @commands.command()
    async def nekolewd(self,ctx):
        response = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
        data = response.json()
        embed = discord.Embed(description="Lewd Neko")
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)
#she's 18 i swear
    @commands.command()
    async def hentai(self,ctx):
        urls = ["https://nekos.life/api/v2/img/tits","https://nekos.life/api/v2/img/pussy_jpg","https://nekos.life/api/v2/img/bj", "https://nekos.life/api/v2/img/Random_hentai_gif", "https://nekos.life/api/v2/img/cum", "https://nekos.life/api/v2/img/anal"]
        response = requests.get(random.choice(urls))
        data = response.json()
        embed = discord.Embed(description="Hentai")
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)

    @commands.command()
    async def ecchi(self,ctx):
        response = requests.get('https://api.neko.airforce/api/ecchi')
        data = response.json()
        embed = discord.Embed(description="Ecchi")
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(nsfw(bot))
