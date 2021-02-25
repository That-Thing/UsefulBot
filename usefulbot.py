import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
import os 
import random
import requests
import time
import asyncio

intents = discord.Intents.default()
intents.members = True

#bot prefix
bot = commands.Bot(command_prefix = '!!', case_insensitive=True, intents=intents)
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

def checkExisting(serverID):
    with open('settings.json') as data:
        servers = json.load(data)
    idCheck = False
    for x in servers["servers"]:
        currID = x['id']
        if currID == serverID:
            idCheck = True
    return idCheck

#Every time the bot joins a new server the bot checks if the server config already exists and if not, creates a new config. 
@bot.event
async def on_guild_join(guild):
    with open('settings.json') as data:
        Jsettings = json.load(data)
    if checkExisting(guild.id) == False:
        toAppend = {
            "id":guild.id,
            "level":"on"
        }
        Jsettings["servers"].append(toAppend)
        with open('settings.json', "w") as f:
            f.write(json.dumps(Jsettings, indent=4, sort_keys=True))
    else:
        pass


@bot.command()
async def check(ctx):
    if ctx.message.author.id == 204721061411946496:
        with open('settings.json') as data:
            Jsettings = json.load(data)
        Jsettings["servers"][0].append("x")   
        with open('settings.json', "w") as f:
            f.write(json.dumps(Jsettings, indent=4, sort_keys=True))
        print(Jsettings["servers"][0])

@bot.command()
async def addservers(ctx):
    if ctx.message.author.id == 204721061411946496:
        with open("settings.json") as data:
            Jsettings = json.load(data)
        serverCheck = False
        for x in bot.guilds:
            if checkExisting(x.id) == False:
                guildID = x.id
                toAppend = {
                    "id":guildID,
                    "level":"on"
                }
                Jsettings["servers"].append(toAppend)
                with open('settings.json', "w") as f:
                    f.write(json.dumps(Jsettings, indent=4, sort_keys=True))
        print("servers added.")
        with open('settings.json', "w") as f:
            f.write(json.dumps(Jsettings, indent=4, sort_keys=True))


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
            bot.unload_extension(extension)
            print("Unloaded")
            bot.load_extension(extension)
            print("Loaded")
            colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

            embed = discord.Embed(name='Reloaded', color=random.choice(colors))
            embed.add_field(name='Reloaded', value='Reloaded {}'.format(extension))
            await ctx.send(embed=embed)
        except Exception as error:
            print("{} Can't be fucking reloaded. [{}]".format(extension, error))



snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]


#not my code lol. 
@bot.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")


#If the bot sends the embed, but it's empty, it simply means that the deleted message was either a media file or another embed.










if __name__ == "__main__":
    for extention in extentions:
        try:
            bot.load_extension(extention)
        except Exception as error:
            print("{} couldn't be loaded, something fucked up! [{}]".format(extention, error))

bot.run('TOKEN')
