import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import asyncio


#changes the value of the level setting to whatever is passed as an argument
def changeLevel(status, serverID):
    with open('settings.json') as data:
        settings = json.load(data) 
    for x in settings['servers']:
        currID = x['id']
        if currID == serverID:
            x['level'] = status
            with open('settings.json', "w") as f:
                f.write(json.dumps(settings, indent=4, sort_keys=True)) 

class settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#check settings
    @commands.command()
    async def settings(self, ctx, argument = None):
        if ctx.message.author.guild_permissions.administrator:
            with open('settings.json') as data:
                settings = json.load(data)

            if argument == None:
                embed=discord.Embed(name="Settings for " + str(ctx.message.guild.name), description="Settings for " + str(ctx.message.guild.name))
                for x in settings['servers']:
                    currID = x['id']
                    if currID == ctx.message.guild.id:
                        embed.add_field(name="Level Messages", value=x['level'], inline=False)
                await ctx.send(embed=embed)
            if argument.lower() == 'level':
                await ctx.send("Please react with <:no:791842503849410590> to disable, react with <:yes:791842528366034954> to enable, and react with <:cancel:791842537877930004> to cancel.")
                embed=discord.Embed(name="Disable/Enable Level Up Messages", description="Disable/Enable Level Up Messages")
                for x in settings['servers']:
                    currID = x['id']
                    if currID == ctx.message.guild.id:
                        embed.add_field(name="Level Messages", value=x['level'], inline=False)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction(emoji = "no:791842503849410590")
                await msg.add_reaction(emoji = "yes:791842528366034954")
                await msg.add_reaction(emoji = "cancel:791842537877930004")
                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) in ['<:yes:791842528366034954>', '<:no:791842503849410590>', '<:cancel:791842537877930004>']
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    await ctx.send('👎')
                else:

                    if str(reaction.emoji) == '<:yes:791842528366034954>':
                        changeLevel("on", ctx.message.guild.id)
                        print("changed status to ON")
                        await ctx.send("Changed to **On**")
                    if str(reaction.emoji) == '<:no:791842503849410590>':
                        changeLevel("off", ctx.message.guild.id)
                        await ctx.send("Changed to **Off**")
                    if str(reaction.emoji) == '<:cancel:791842537877930004>':
                        await ctx.send("Cancelled.")
                        


            
def setup(bot):
    bot.add_cog(settings(bot))