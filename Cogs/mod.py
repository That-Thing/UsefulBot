import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random


class mod:
    def __init__(self, bot):
        self.bot = bot


    #kick
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def kick(self, ctx, userName: discord.User):
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == 'Your User ID':
            try:
                await self.bot.kick(userName)
                embed=discord.Embed(title="Kick", description="{} Has been kicked from {}.".format (userName.name, ctx.message.server.name), color=random.choice(colors))
                embed.set_footer(text="Requested by {}".format(ctx.message.author))
                await self.bot.say(embed=embed)
            except discord.Forbidden:
                await self.bot.say("I don't have perms for that  ")
        else:
            await self.bot.say('Fuck outta here without admin you cunt.')

    #ban
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def ban(self, ctx, userName: discord.User, member: discord.Member=None):
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        
        # if not member:
        #     await ctx.send('Specify member')
            # return
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == 'Your User ID':
            try:
                await self.bot.ban(userName)
                embed=discord.Embed(title="Ban", description="{} Has been banned from {}.".format (userName.name, ctx.message.server.name), color=random.choice(colors))
                embed.set_footer(text="Requested by {}".format(ctx.message.author))
                await self.bot.say(embed=embed)
            except discord.Forbidden:
                await self.bot.say("I don't have perms for that  ")
        else:
            await self.bot.say('Fuck outta here without admin you cunt.')







#clear
    @commands.command(pass_context = True)
    @commands.cooldown(rate=1, per=2.0)
    async def clear(self, ctx, number):
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        mgs = [] 
        number = int(number)
        async for x in self.bot.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == 'Your User ID':
            try:
                await self.bot.delete_messages(mgs)
                embed=discord.Embed(title="Clear", description="{} messages have been deleted.".format (number), color=random.choice(colors))
                embed.set_footer(text="Requested by {}".format(ctx.message.author))
                await self.bot.say(embed=embed)
                await asyncio.sleep(3)
                await self.bot.delete_message(embed)
            except discord.Forbidden:
                await self.bot.say("I don't have perms for that  ")
        else:
            pass
            await self.bot.say("Get admin privileges if you want to do that.")




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
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == 'Your User ID':
            try:
                await self.bot.say(embed=embed)
                await asyncio.sleep(3)
                await self.bot.delete_message(ctx.embed)
            except discord.Forbidden:
                await self.bot.say("I don't have perms for that  ")          
        else: 
            pass
            await self.bot.say('Nope, you need admin for that.')
            

    
    @commands.command(pass_context = True)
    @commands.cooldown(rate=1, per=2.0)
    async def mute(self, ctx, member: discord.Member):
        if ctx.message.author.server_permissions.administrator or ctx.message.author.id == 'Your User ID':
            role = discord.utils.get(member.server.roles, name='Muted')
            if not member:
                await ctx.send('Specify member')
                return

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            await self.bot.add_roles(member, role)
            embed=discord.Embed(title="User was Muted!", description="{} was muted by {}!".format(member, ctx.message.author), color=random.choice(colors))
            embed.set_footer(text="Requested by {}".format(ctx.message.author))
            await self.bot.say(embed=embed)
        else:
            embed=discord.Embed(title="You don't have admin", description="Come back with admin privileges you cunt.", color=random.choice(colors))
            embed.set_footer(text="Requested by {}".format(ctx.message.author))
            await self.bot.say(embed=embed)



    @commands.command(pass_context = True)
    @commands.cooldown(rate=1, per=2.0)
    async def nickname(self, ctx, userName: discord.User, *args):
         if ctx.message.author.server_permissions.administrator or ctx.message.author.id == 'Your User ID':
            output = ""
            for word in args:
                output += word
                output += ' '
                try:
                    await self.bot.change_nickname(userName, output)
                except discord.Forbidden:
                    await self.bot.say("I don't have perms for that  ")


#    @commands.command(pass_context = True)
#    @commands.cooldown(rate=1, per=2.0)
#    async def unban(self, ctx, user_id):
#        ban_list = await self.bot.get_bans(ctx.message.server)
#        banned = await client.get_user_info(user_id)
#        
#        
#        
#    @commands.command(pass_context = True)
#    @commands.cooldown(rate=1, per=2.0)
#    async def bans(self, ctx):
#        ban_list = await self.bot.get_bans(ctx.message.server)
#        embed = discord.Embed(title="Banned Members", description=.join([user.name for user in ban_list])
#        await self.bot.say(embed=embed)
    
    
















            









def setup(bot):
    bot.add_cog(mod(bot))
