import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
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
'invite', 
'fun', 
'info',
'tagfun',
'gif',
'text',
'images'
]

print('loading')





@bot.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    await bot.change_presence(game=discord.Game(name='Being useful | !!help', url='https://www.twitch.tv/monstercat',type=1))
    print("  ")
    print("                  ██╗   ██╗███████╗███████╗███████╗██╗   ██╗██╗         ██████╗  ██████╗ ████████╗")
    print("                  ██║   ██║██╔════╝██╔════╝██╔════╝██║   ██║██║         ██╔══██╗██╔═══██╗╚══██╔══╝")
    print("                  ██║   ██║███████╗█████╗  █████╗  ██║   ██║██║         ██████╔╝██║   ██║   ██║   ")
    print("                  ██║   ██║╚════██║██╔══╝  ██╔══╝  ██║   ██║██║         ██╔══██╗██║   ██║   ██║   ")
    print("                  ╚██████╔╝███████║███████╗██║     ╚██████╔╝███████╗    ██████╔╝╚██████╔╝   ██║   ")
    print("                   ╚═════╝ ╚══════╝╚══════╝╚═╝      ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   ")
    print(" ")
    print("                                        Currently active on " + str(len(bot.servers)) + " servers.")

@bot.command(pass_context=True)
async def cls(ctx):
    if ctx.message.author.id == '204721061411946496':
        await bot.say(":ballot_box_with_check: **Console cleared!**")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("                  ██╗   ██╗███████╗███████╗███████╗██╗   ██╗██╗         ██████╗  ██████╗ ████████╗")
        print("                  ██║   ██║██╔════╝██╔════╝██╔════╝██║   ██║██║         ██╔══██╗██╔═══██╗╚══██╔══╝")
        print("                  ██║   ██║███████╗█████╗  █████╗  ██║   ██║██║         ██████╔╝██║   ██║   ██║   ")
        print("                  ██║   ██║╚════██║██╔══╝  ██╔══╝  ██║   ██║██║         ██╔══██╗██║   ██║   ██║   ")
        print("                  ╚██████╔╝███████║███████╗██║     ╚██████╔╝███████╗    ██████╔╝╚██████╔╝   ██║   ")
        print("                   ╚═════╝ ╚══════╝╚══════╝╚═╝      ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   ")
        print(" ")
        print("                                                     Console Cleared")



#user = 'osmSj0PjSRPKI6fp'
#key = 'wRQRzsdhgrvo27b6QftQioU9hBais3Lr'




#cleverbot
#@bot.event
##async def on_message(message):

#    if message.content.startswith('<@509012657890918430>'):
#        if message.author.id == '402237660648964096':
#            pass
#        elif message.author.id == '347066550098067457':
#            pass
#        else:
#            await bot.send_typing(message.channel)
#            txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
#            r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'Useful Bot', 'text':txt}).text)
#            if r['status'] == 'success':
#                embed = discord.Embed(description=r['response'])
#                await bot.send_message(message.channel, embed=embed)
#            
#    else:
#        await bot.process_commands(message)
    
            












@bot.command(hidden=True, pass_context=True)
async def load(ctx, extension):
    """Loads a module."""
    if ctx.message.author.id == '204721061411946496':
        try:
            bot.load_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Loaded', color=random.choice(colors))
            embed.add_field(name='Loaded', value='Loaded {}'.format(extension))
            await bot.say(embed=embed)
        except Exception as error:
            print("{} Can't be fucking loaded. [{}]".format(extension, error))

@bot.command(hidden=True, pass_context=True)
async def unload(ctx, extension):
    """Unloads a module."""
    if ctx.message.author.id == '204721061411946496':
        try:
            bot.unload_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Unloaded', color=random.choice(colors))
            embed.add_field(name='Unloaded', value='Unloaded {}'.format(extension))
            await bot.say(embed=embed)
        except Exception as error:
            print("{} Can't be fucking unloaded. [{}]".format(extension, error))

@bot.command(hidden=True, pass_context=True)
async def reload(ctx, extension):
    """Reloads a module."""
    if ctx.message.author.id == '204721061411946496':
        try:

            bot.unload_extension(extention)
            bot.load_extension(extension)

            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Reloaded', color=random.choice(colors))
            embed.add_field(name='Reloaded', value='Reloaded {}'.format(extension))
            await bot.say(embed=embed)
        except Exception as error:
            print("{} Can't be fucking reloaded. [{}]".format(extension, error))









if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as error:
            print("{} couldn't be loaded, something fucked up! [{}]".format(extention, error))







#requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'Useful Bot'})
bot.run('TOKEN HERE')
