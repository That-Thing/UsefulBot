import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os






class invite:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def invite(self):
        await self.bot.say('An invite to a server')






def setup(bot):
    bot.add_cog(invite(bot))