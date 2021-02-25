import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


#I'm here to chew ass and kick bubblegum
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, userName: discord.User):
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        guild = ctx.message.guild
        try:
            await guild.kick(userName)
            embed=discord.Embed(title="Kick", description="{} Has been kicked from {}.".format (userName.name, ctx.message.guild.name), color=random.choice(colors))
            embed.set_footer(text="Requested by {}".format(ctx.message.author))
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have perms for that")

#I'm here to chew ass and ban bubblegum
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, userName: discord.User):
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        guild = ctx.message.guild
        try:
            await guild.ban(userName)
            embed=discord.Embed(title="Ban", description="{} Has been banned from {}.".format (userName.name, ctx.message.guild.name), color=random.choice(colors))
            embed.set_footer(text="Requested by {}".format(ctx.message.author))
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have perms for that")







#clear
    @commands.command(pass_context = True)
    @commands.cooldown(rate=1, per=2.0)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, arg1):
        number = int(arg1)
        try:
            channel = ctx.message.channel
            await channel.purge(limit=number)
            embed = discord.Embed(description = "Deleted {} messages".format(number))
            embed.add_field(name="Channel: ", value=channel, inline=False)
            await ctx.send(embed=embed)
        except discord.Forbidden:
            await ctx.send("I don't have perms for that")



#announcement
    @commands.command(pass_context = True, name = 'announce', aliases = ['announcement'])
    @commands.cooldown(rate=1, per=2.0)
    async def announce(self, ctx, *args):
        output = ""
        for word in args:
            output += word
            output += ' '
            embed = discord.Embed(title="Announcement", description=output, color=0xfd0000)
            embed.set_footer(text="Requested by {}".format(ctx.message.author))
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '204721061411946496':
            try:
                await ctx.send(embed=embed)
                await asyncio.sleep(3)
                await self.bot.delete_message(ctx.embed)
            except discord.Forbidden:
                await ctx.send("I don't have perms for that  ")          
        else: 
            pass
            await ctx.send('Nope, you need admin for that.')
            

    


#change user nickname
    @commands.command(pass_context = True)
    @commands.cooldown(rate=1, per=2.0)
    async def nickname(self, ctx, userName: discord.User, *args):
         if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 204721061411946496:
            output = ""
            for word in args:
                output += word
                output += ' '
                try:
                    await self.bot.change_nickname(userName, output)
                except discord.Forbidden:
                    await ctx.send("I don't have perms for that  ")















            









def setup(bot):
    bot.add_cog(mod(bot))
