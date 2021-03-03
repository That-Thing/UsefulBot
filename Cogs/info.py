import discord
from discord.ext import commands
from discord.ext.commands import Bot
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
 
class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



#server info
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def sinfo(self, ctx):

        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]


        online = 0
        for i in ctx.message.guild.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1
    

        emoji_count = len(ctx.message.guild.emojis)

        embed = discord.Embed(name="{}'s Information".format(ctx.message.guild.name), description="Here is this guild's info.", color=random.choice(colors))
        embed.set_author(name="Server Information")
        embed.add_field(name="Name of server", value=ctx.message.guild.name, inline=True)
        embed.add_field(name='Owner', value=ctx.message.guild.owner, inline=True)
        embed.add_field(name='Members', value=ctx.message.guild.member_count, inline=True)
        embed.add_field(name='Members Online', value=online)
        embed.add_field(name="Roles in Server", value=len(ctx.message.guild.roles), inline=True) 
        embed.add_field(name='Highest role', value=ctx.message.guild.roles[0])
        embed.add_field(name='Number of Emojis', value=str(emoji_count))
        embed.add_field(name='Server Created', value='{}'.format(ctx.message.guild.created_at.strftime('%m/%d/%Y %H:%M:%S')))
        embed.add_field(name='Verification Level', value=str(ctx.message.guild.verification_level), inline=True)
        embed.add_field(name="ID of Server", value=ctx.message.guild.id, inline=True)
        embed.set_footer(text="Requested by {}".format(ctx.message.author))
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        await ctx.send(embed=embed)


#user info
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
        await ctx.send(embed=embed)  

    
    
    
    
#user pfp
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def pfp(self, ctx, user: discord.Member):
        embed = discord.Embed()
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    
    
    
    
    
#url to user pfp
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def pfpurl(self, ctx, user: discord.Member):
        await ctx.send(user.avatar_url)



#info on the bot
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def botinfo(self, ctx):

        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

        embed = discord.Embed(title="Information on Useful Bot", description="Here's the bot info", color=random.choice(colors))
        embed.add_field(name="Name of Bot", value='<@509012657890918430>', inline=True)
        embed.add_field(name="Name of Programmer", value='<@204721061411946496>', inline=True)
        embed.add_field(name="Library", value='Discord.py Rewrite', inline=True)
        embed.add_field(name="Avatar URL", value=self.bot.user.avatar_url, inline=True)
        embed.add_field(name="Bot User ID", value=self.bot.user.id, inline=True)
        embed.set_footer(text="Requested by {}".format(ctx.message.author))


        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)



#time in EST
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def time(self, ctx):
        await ctx.send('Date is: **{0}**\nTime is: **{1}**'.format(time.strftime("%A, %B %d, %Y"), time.strftime("%I:%M:%S %p")))


#list banned users in the server
    @commands.command(pass_context=True, aliases=['lb', 'listban'])
    @commands.cooldown(rate=1, per=2.0)
    async def listbans(self, ctx):
        guild = ctx.message.guild
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        bans = await guild.bans()
        embed = discord.Embed(title="List of Banned Members", description=guild.name, colour=random.choice(colors))
        for i in bans:
            embed.add_field(name="Name", value=i[1].name, inline=False)
            embed.add_field(name="ID", value=i[1].id, inline=False)
            embed.add_field(name="** **", value="** **", inline=False)
        return await ctx.send(embed=embed)

#list how many servers the bot is in
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def servers(self, ctx):
        await ctx.send("Being useful on " + str(len(self.bot.guilds)) + " servers.")



#send a link to the emoji
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def emoji(self, ctx, emoji: discord.Emoji):
        embed=discord.Embed()
        embed.set_image(url=emoji.url)
        await ctx.send(embed=embed)
        










    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def define(self, ctx, *args): #defines from urban dictionary
        output = ""
        for word in args:
            word = str(word)
            output += word
            output += ' '
            output = output
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
            await ctx.send(embed=embed)
        else:
            try:
                embed = discord.Embed(description=output, color=0x00ff00)
                embed.add_field(name='Defenition: ', value=deflist[0], inline=False)
                embed.add_field(name='Usage: ', value=uselist[0], inline=False)
                #embed.set_footer(text="upvotes: "+ upvotelist[0] + " | downvotes: " + downvotelist[0])
                await ctx.send(embed=embed)
            except Exception:
                try:
                    embed = discord.Embed(description=output, color=0x00ff00)
                    embed.add_field(name='Defenition: ', value=deflist[1], inline=False)
                    embed.add_field(name='Usage: ', value=uselist[1], inline=False)
                    #embed.set_footer(text="upvotes: "+ upvotelist[0] + " | downvotes: " + downvotelist[0])
                    await ctx.send(embed=embed)
                except Exception:
                    embed = discord.Embed(description=output, color=0x00ff00)
                    embed.add_field(name='Defenition: ', value=deflist[2], inline=False)
                    embed.add_field(name='Usage: ', value=uselist[2], inline=False)
                    #embed.set_footer(text="upvotes: "+ upvotelist[0] + " | downvotes: " + downvotelist[0])
                    await ctx.send(embed=embed)


    @commands.command(pass_context=True, aliases=['imin', 'iminfo'])
    async def imginfo(self, ctx, user: discord.Member):
        img = Image.open("bg.png")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("MavenPro-Bold.ttf", 25)
        fontbig = ImageFont.truetype("yeyey.otf", 150)
        fillColor = 102,165,106
        strokeColor = 7,7,7
        #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ 
        if len(user.name) > 9:
            fontbig = ImageFont.truetype("yeyey.otf", 70)
            draw.text((20, 0), user.name, fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=fontbig)
        else:
            fontbig = ImageFont.truetype("yeyey.otf", 150)
            draw.text((20, 0), user.name, fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=fontbig) #draws Information
        draw.text((50, 150), '{}'.format( '(a bot)' if user.bot else '(not a bot)'),  fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=font)
        draw.text((50, 200), "Username: {}".format(user.name), fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=font)
        draw.text((50, 250), "ID:  {}".format(user.id), fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=font)
        draw.text((50, 300), "User Status:{}".format(user.status), fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=font)
        draw.text((50, 350), "Account created: {}".format(user.created_at), fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=font)
        draw.text((50, 400), "Nickname:{}".format(user.display_name), fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=font) 
        draw.text((50, 450), "User's Top Role:{}".format(user.top_role), fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=font) 
        draw.text((50, 500), "User Joined:{}".format(user.joined_at), fill=fillColor, stroke_width=1, stroke_fill=strokeColor,  font=font) 
        img.save('tmp.png')
        await ctx.send(file=discord.File("tmp.png", user.name+".png"))



    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def catfact(self,ctx):
        url = "https://some-random-api.ml/facts/cat"
        response = requests.get(url)
        data = response.json()
        embed = discord.Embed(description="Cat Fact")
        embed.add_field(name="Cat Fact", value=data["fact"])
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def dogfact(self,ctx):
        url = "https://some-random-api.ml/facts/dog"
        response = requests.get(url)
        data = response.json()
        embed = discord.Embed(description="Dog Fact")
        embed.add_field(name="Dog Fact", value=data["fact"])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def fortune(self,ctx):
        url = "https://api.neko.airforce/api/fortune"
        response = requests.get(url)
        data = response.json()
        embed = discord.Embed(description="Fortune")
        embed.add_field(name="Fortune", value=data["fortune"])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(info(bot))
