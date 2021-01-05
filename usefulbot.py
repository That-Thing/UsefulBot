import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import os 
import random
import requests







    

#bot prefix
bot = commands.Bot(command_prefix = '!!')
bot.remove_command('help')




extentions = [
'ping', 
'mod', 
'help',  
'fun', 
'info',
'tagfun',
'gif',
'text',
'images',
'nsfw',
'level',
'settings'
]

print('loading')





@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    await bot.change_presence(activity=discord.Game(name='Being useful | !!help', url='https://www.twitch.tv/monstercat',type=1))
    print("  ")
    print("                  ██╗   ██╗███████╗███████╗███████╗██╗   ██╗██╗         ██████╗  ██████╗ ████████╗")
    print("                  ██║   ██║██╔════╝██╔════╝██╔════╝██║   ██║██║         ██╔══██╗██╔═══██╗╚══██╔══╝")
    print("                  ██║   ██║███████╗█████╗  █████╗  ██║   ██║██║         ██████╔╝██║   ██║   ██║   ")
    print("                  ██║   ██║╚════██║██╔══╝  ██╔══╝  ██║   ██║██║         ██╔══██╗██║   ██║   ██║   ")
    print("                  ╚██████╔╝███████║███████╗██║     ╚██████╔╝███████╗    ██████╔╝╚██████╔╝   ██║   ")
    print("                   ╚═════╝ ╚══════╝╚══════╝╚═╝      ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   ")
    print(" ")
    print("                                        Currently active on " + str(len(bot.guilds)) + " servers.")

@bot.command(pass_context=True)
async def cls(ctx):
    if ctx.message.author.id == 204721061411946496:
        await ctx.send(":ballot_box_with_check: **Console cleared!**")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("                  ██╗   ██╗███████╗███████╗███████╗██╗   ██╗██╗         ██████╗  ██████╗ ████████╗")
        print("                  ██║   ██║██╔════╝██╔════╝██╔════╝██║   ██║██║         ██╔══██╗██╔═══██╗╚══██╔══╝")
        print("                  ██║   ██║███████╗█████╗  █████╗  ██║   ██║██║         ██████╔╝██║   ██║   ██║   ")
        print("                  ██║   ██║╚════██║██╔══╝  ██╔══╝  ██║   ██║██║         ██╔══██╗██║   ██║   ██║   ")
        print("                  ╚██████╔╝███████║███████╗██║     ╚██████╔╝███████╗    ██████╔╝╚██████╔╝   ██║   ")
        print("                   ╚═════╝ ╚══════╝╚══════╝╚═╝      ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   ")
        print(" ")
        print("                                                     Console Cleared")




@bot.command(hidden=True, pass_context=True)
async def load(ctx, extension):
    """Loads a module."""
    if ctx.message.author.id == 204721061411946496:
        try:
            bot.load_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Loaded', color=random.choice(colors))
            embed.add_field(name='Loaded', value='Loaded {}'.format(extension))
            await ctx.send(embed=embed)
        except Exception as error:
            print("{} Can't be fucking loaded. [{}]".format(extension, error))

@bot.command(hidden=True, pass_context=True)
async def unload(ctx, extension):
    """Unloads a module."""
    if ctx.message.author.id == 204721061411946496:
        try:
            bot.unload_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Unloaded', color=random.choice(colors))
            embed.add_field(name='Unloaded', value='Unloaded {}'.format(extension))
            await ctx.send(embed=embed)
        except Exception as error:
            print("{} Can't be fucking unloaded. [{}]".format(extension, error))

@bot.command(hidden=True, pass_context=True)
async def reload(ctx, extension):
    """Reloads a module."""
    if ctx.message.author.id == 204721061411946496:
        try:

            bot.unload_extension(extention)
            bot.load_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Reloaded', color=random.choice(colors))
            embed.add_field(name='Reloaded', value='Reloaded {}'.format(extension))
            await ctx.send(embed=embed)
        except Exception as error:
            print("{} Can't be fucking reloaded. [{}]".format(extension, error))





if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as error:
            print("{} couldn't be loaded, something fucked up! [{}]".format(extention, error))

bot.run('Token')
