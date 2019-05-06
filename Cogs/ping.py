import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

class ping:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, aliases=['Ping'])
    @commands.cooldown(rate=1, per=2.0)
    async def ping(self, ctx):
        pingtime = time.time()
        pingms = await self.bot.say("*Pinging...*")
        ping = (time.time() - pingtime) * 1000
        await self.bot.edit_message(pingms, "**Pong!** :ping_pong:  ``%dms``" % ping)
        




def setup(bot):
    bot.add_cog(ping(bot))