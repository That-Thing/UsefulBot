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
import urbandictionary as ud
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
 
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
        embed.add_field(name='Server Created', value='{}'.format(ctx.message.server.created_at.strftime('%m/%d/%Y %H:%M:%S')))
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
        # embed.add_field(name="People Who Helped", value='<@368860954227900416>', inline=True)
        embed.add_field(name="Library", value='Discord.py', inline=True)
        #embed.add_field(name="Support Server", value='https://discord.gg/PEqVQCu', inline=True)
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


    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def youtube(self, ctx, *, name):

            data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+ 'AIzaSyB6Y8CrhCv6fCLaBn3x4lkUqPPgrdxIR0g').read()
            subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
            views = json.loads(data)["items"][0]["statistics"]["viewCount"]
            vids = json.loads(data)["items"][0]["statistics"]["videoCount"]

            # Generate embed and say
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Subscribers:", value="{:,d}".format(int(subs)), inline=False)
            embed.add_field(name="Total views:", value="{:,d}".format(int(views)), inline=False)
            embed.add_field(name="Total videos:", value="{:,d}".format(int(vids)), inline=False)
            embed.set_thumbnail(url="https://s.ytimg.com/yts/mobile/img/apple-touch-icon-144x144-precomposed-vflopw1IA.png")
            embed.set_footer(text="requested by {}".format(ctx.message_author))
            await self.bot.say(embed=embed)



    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def emoji(self, emoji: discord.Emoji):
        embed=discord.Embed()
        embed.set_image(url=emoji.url)
        await self.bot.say(embed=embed)
        










    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def define(self, *args): #defines from urban dictionary
        output = ""
        for word in args:
            output += word
            output += ' '
        defined = ud.define(output)
        deflist = []
        uselist = []
        upvotelist = []
        for d in defined:
            deflist.append(d.definition)
            uselist.append(d.example)
            upvotelist.append(d.upvotes)
        if len(deflist) == 0:
            embed = discord.Embed(description=output, color=0xff0000)
            embed.add_field(name='Not Found ', value="Try checking your spelling or something")
            await self.bot.say(embed=embed)
        else:
            try:
                embed = discord.Embed(description=output, color=0x00ff00)
                embed.add_field(name='Defenition: ', value=deflist[0], inline=False)
                embed.add_field(name='Usage: ', value=uselist[0], inline=False)
                #embed.set_footer(text="upvotes: "+ upvotelist[0] + " | downvotes: " + downvotelist[0])
                await self.bot.say(embed=embed)
            except Exception:
                try:
                    embed = discord.Embed(description=output, color=0x00ff00)
                    embed.add_field(name='Defenition: ', value=deflist[1], inline=False)
                    embed.add_field(name='Usage: ', value=uselist[1], inline=False)
                    #embed.set_footer(text="upvotes: "+ upvotelist[0] + " | downvotes: " + downvotelist[0])
                    await self.bot.say(embed=embed)
                except Exception:
                    embed = discord.Embed(description=output, color=0x00ff00)
                    embed.add_field(name='Defenition: ', value=deflist[2], inline=False)
                    embed.add_field(name='Usage: ', value=uselist[2], inline=False)
                    #embed.set_footer(text="upvotes: "+ upvotelist[0] + " | downvotes: " + downvotelist[0])
                    await self.bot.say(embed=embed)


    @commands.command(pass_context=True, aliases=['imin', 'iminfo'])
    async def imginfo(self, ctx, user: discord.Member):
        img = Image.open("bg.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("MavenPro-Bold.ttf", 25)
        fontbig = ImageFont.truetype("yeyey.otf", 150)
 
        #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ 
        if len(user.name) > 9:
            fontbig = ImageFont.truetype("yeyey.otf", 70)
            draw.text((20, 0), user.name, (255, 249, 173), font=fontbig)
        else:
            fontbig = ImageFont.truetype("yeyey.otf", 150)
            draw.text((20, 0), user.name, (255, 249, 173), font=fontbig) #draws Information
        draw.text((50, 150), '{}'.format( '(a bot)' if user.bot else '(not a bot)'),  (255, 249, 173), font=font)
        draw.text((50, 200), "Username: {}".format(user.name), (255, 249, 173), font=font)
        draw.text((50, 250), "ID:  {}".format(user.id), (255, 249, 173), font=font)
        draw.text((50, 300), "User Status:{}".format(user.status), (255, 249, 173), font=font)
        draw.text((50, 350), "Account created: {}".format(user.created_at), (255, 249, 173), font=font)
        draw.text((50, 400), "Nickname:{}".format(user.display_name), (255, 249, 173), font=font) 
        draw.text((50, 450), "User's Top Role:{}".format(user.top_role), (255, 249, 173), font=font) 
        draw.text((50, 500), "User Joined:{}".format(user.joined_at), (255, 249, 173), font=font) 
        img.save('tmp.png')
        await self.bot.upload("tmp.png")









def setup(bot):
    bot.add_cog(info(bot))
