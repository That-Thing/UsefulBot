import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import os 
import random
import datetime
import time
import platform
import sys
import requests
import urllib.request
from discord import Member
from discord.ext.commands import has_permissions
 
class info:
    def __init__(self, bot):
        self.bot = bot




    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def sinfo(self, ctx):

        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]


        online = 0
        for i in ctx.message.server.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
    

        emoji_count = len(ctx.message.server.emojis)

        embed = discord.Embed(name="{}'s Information".format(ctx.message.server.name), description="Here is this server's info.", color=random.choice(colors))
        embed.set_author(name="Server Information")
        embed.add_field(name="Name of Server", value=ctx.message.server.name, inline=True)
        embed.add_field(name='Owner', value=ctx.message.server.owner, inline=True)
        embed.add_field(name='Members', value=ctx.message.server.member_count, inline=True)
        embed.add_field(name='Members Online', value=online)
        embed.add_field(name="Roles in Server", value=len(ctx.message.server.roles), inline=True) 
        embed.add_field(name='Highest role', value=ctx.message.server.role_hierarchy[0])
        embed.add_field(name='Number of Emojis', value=str(emoji_count))
        embed.add_field(name='Verification Level', value=str(ctx.message.server.verification_level), inline=True)
        embed.add_field(name="ID of Server", value=ctx.message.server.id, inline=True)
        embed.set_footer(text="Requested by {}".format(ctx.message.author))
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)



    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def info(self, ctx, user: discord.Member):

        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        
        embed = discord.Embed(title="{}'s Information".format(user.name), description="Here's the info.", color=random.choice(colors))

        embed.add_field(name="Name of User", value=user.name, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="** **Joined", value='{}'.format(user.joined_at.strftime('%m/%d/%Y %H:%M:%S')))
        embed.add_field(name="Is user a robot", value='{}'.format( 'Yes' if user.bot else 'No'))
        embed.add_field(name='User Created', value='{}'.format(user.created_at.strftime('%m/%d/%Y %H:%M:%S')))
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.set_footer(text="Requested by {}".format(ctx.message.author))
        embed.set_thumbnail(url=user.avatar_url)
        await self.bot.say(embed=embed)  

    
    
    
    
    
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def pfp(self, ctx, user: discord.Member):
        embed = discord.Embed()
        embed.set_image(url=user.avatar_url)
        await self.bot.say(embed=embed)

    
    
    
    
    
    
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def pfpurl(self, ctx, user: discord.Member):
        await self.bot.say(user.avatar_url)




    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def botinfo(self, ctx):

        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

        embed = discord.Embed(title="Information on Useful Bot", description="Here's the bot info", color=random.choice(colors))
        embed.add_field(name="Name of Bot", value='<@509012657890918430>', inline=True)
        embed.add_field(name="Name of Programmer", value='<@204721061411946496>', inline=True)
        embed.add_field(name="Library", value='Discord.py', inline=True)
        embed.add_field(name="Avatar URL", value=self.bot.user.avatar_url, inline=True)
        embed.add_field(name="Bot User ID", value=self.bot.user.id, inline=True)
        embed.set_footer(text="Requested by {}".format(ctx.message.author))


        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await self.bot.say(embed=embed)




    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def time(self, ctx):
        await self.bot.say('Date is: **{0}**\nTime is: **{1}**'.format(time.strftime("%A, %B %d, %Y"), time.strftime("%I:%M:%S %p")))



    @commands.command(pass_context=True, aliases=['lb', 'listban'])
    @commands.cooldown(rate=1, per=2.0)
    async def listbans(self, ctx):
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        x = await self.bot.get_bans(ctx.message.server)
        x = '\n'.join([y.name for y in x])
        embed = discord.Embed(title="List of Banned Members", description=x, colour=random.choice(colors))
        return await self.bot.say(embed=embed)

                
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def servers(self):
        await self.bot.say("Being useful on " + str(len(self.bot.servers)) + " servers.")





    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def emoji(self, emoji: discord.Emoji):
        embed=discord.Embed()
        embed.set_image(url=emoji.url)
        await self.bot.say(embed=embed)
        







    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: str):
        if not permissions.can_embed(ctx):
            return await ctx.send("I need permissions to send embeds.")

        url = await http.get(f'http://api.urbandictionary.com/v0/define?term={search}', res_method="json")

        if url is None:
            return await ctx.send("The API doesn't work.")

        count = len(url['list'])
        if count == 0:
            return await ctx.send("Couldn't find that, try checking your spelling.")
        result = url['list'][random.randint(0, count - 1)]

        definition = result['definition']
        if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(' ', 1)[0]
                definition += '...'

        embed = discord.Embed(colour=0xC29FAF, description=f"**{result['word']}**\n*by: {result['author']}*")
        embed.add_field(name='Definition', value=definition, inline=False)
        embed.add_field(name='Example', value=result['example'], inline=False)
        embed.set_footer(text=f"👍 {result['thumbs_up']} | 👎 {result['thumbs_down']}")
        await ctx.send(embed=embed)
#This shit broken ^















def setup(bot):
    bot.add_cog(info(bot))
