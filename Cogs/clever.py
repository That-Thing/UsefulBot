import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

class clever:
    def __init__(self, bot):
        self.bot = bot
    @bot.event
    async def on_message(self, message):

        if message.content.startswith('<@509012657890918430>'):
            await self.bot.send_typing(message.channel)
            txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
            r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'Useful Bot', 'text':txt}).text)
            if r['status'] == 'success':
                embed = discord.Embed(description=r['response'])
                await self.bot.send_message(message.channel, embed=embed)
                
        else:
            await self.bot.process_commands(message)
        



    requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'Useful Bot'})
def setup(bot):
    bot.add_cog(clever(bot))
