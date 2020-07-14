import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import praw
import requests
import json
#god i hate reddit
reddit = praw.Reddit(
       client_id='f7HwhXzMPI6oLQ',
       client_secret='SECRET HERE',
       user_agent='discord:com.sen.usefulbot:v1 (by Sen)')

class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def meme(self, ctx):
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        embed=discord.Embed(description='Meme:')
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        embed=discord.Embed(description='Cat:')
        embed.set_image(url=data[0]["url"])
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        embed=discord.Embed(description='Dog:')
        embed.set_image(url=data["message"])
        await ctx.send(embed=embed)

    @commands.command()
    async def neko(self,ctx):
        urls  = ["https://nekos.life/api/v2/img/ngif", "https://nekos.life/api/v2/img/neko"]
        response = requests.get(random.choice(urls))
        data = response.json()
        embed = discord.Embed(description="Neko")
        embed.set_image(url=data["url"])
        await ctx.send(embed=embed)


    @commands.command()
    async def snek(self, ctx):
        Sneks_submissions = reddit.subreddit('Sneks').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in Sneks_submissions if not x.stickied)
        embed=discord.Embed(description='snek:')
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)





#weebshit

    @commands.command()
    async def senko(self, ctx):
        Sneks_submissions = reddit.subreddit('SewayakiKitsune').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in Sneks_submissions if not x.stickied)
        embed=discord.Embed(description='Senko:')
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)




#remove background from image
    @commands.command(alias=["removebg"])
    async def removeBG(self, ctx):
        url = "https://removal.ai/wp-admin/admin-ajax.php"
        headers = {
            "referer":"https://removal.ai/upload/"
        }
        imageUrl = ctx.message.attachments[0].url
        data = {
            "link":imageUrl,
            "action":"file_upload_url"
        }
        r = requests.post(url, data=data, headers=headers).json()
        embed = discord.Embed()
        embed.set_image(url=r["download"])
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(images(bot))