import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def ping(self, ctx):
        pingtime = time.time()
        message = await ctx.send("*Pinging...*")
        ping = (time.time() - pingtime) * 1000
        await message.edit(content="**Pong!** :ping_pong:  ``%dms``" % ping)
        




def setup(bot):
    bot.add_cog(ping(bot))