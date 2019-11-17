import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import praw

reddit = praw.Reddit(
       client_id='f7HwhXzMPI6oLQ',
       client_secret='rb2AyXMM5BVE_sY9hsMCsS8cRgw',
       user_agent='discord:com.sen.usefulbot:v1 (by Sen)')

class images:
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def meme(self):
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        embed=discord.Embed(description='Meme:')
        embed.set_image(url=submission.url)
        await self.bot.say(embed=embed)

    @commands.command()
    async def cat(self):
        cats_submissions = reddit.subreddit('cats').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in cats_submissions if not x.stickied)
        embed=discord.Embed(description='Cat:')
        embed.set_image(url=submission.url)
        await self.bot.say(embed=embed)

    @commands.command()
    async def dog(self):
        rarepuppers_submissions = reddit.subreddit('rarepuppers').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in rarepuppers_submissions if not x.stickied)
        embed=discord.Embed(description='Dog:')
        embed.set_image(url=submission.url)
        await self.bot.say(embed=embed)

    @commands.command()
    async def snek(self):
        Sneks_submissions = reddit.subreddit('Sneks').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in Sneks_submissions if not x.stickied)
        embed=discord.Embed(description='snek:')
        embed.set_image(url=submission.url)
        await self.bot.say(embed=embed)





#weebshit

    @commands.command()
    async def senko(self):
        Sneks_submissions = reddit.subreddit('SewayakiKitsune').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in Sneks_submissions if not x.stickied)
        embed=discord.Embed(description='Senko:')
        embed.set_image(url=submission.url)
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(images(bot))