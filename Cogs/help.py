import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random




class help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
        )


        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

        embed = discord.Embed(title="Useful Bot Commads", colour=random.choice(colors))
        embed.set_author(name='Command List 1: Mod Commands')
        embed.add_field(name='!!ping', value='Pong!', inline=True)   
        embed.add_field(name='!!kick', value='Kicks a member', inline=True)
        embed.add_field(name='!!ban', value="Bans a member", inline=True)
        embed.add_field(name='!!clear *value*', value="Clears desired ammount of messages", inline=True)
        embed.add_field(name='!!announce *text*', value="Creates a red embed with your desired text", inline=True)
        embed.add_field(name='!!nickname *user* *nickname*', value="Changes a user's nickname", inline=True)
        await self.bot.send_message(author, embed=embed)

        embed = discord.Embed(title="Command List 2: Info Commands", colour=random.choice(colors))

        embed.add_field(name='!!info @*someone*', value='Gives you the info on a member', inline=True)
        embed.add_field(name='!!sinfo', value='Gives you the info on a server', inline=True)
        embed.add_field(name='!!botinfo', value='Shows info on bot', inline=True)
        embed.add_field(name='!!pfp @*someone*', value="Sends the user's profile picture", inline=True)
        embed.add_field(name="!!pfpurl @*someone*", value="Sends a link to the user's profile picture", inline=True)
        embed.add_field(name='!!listbans', value="Lists all the banned users in the server", inline=True)
        embed.add_field(name='!!servers', value="Shows how many servers the bot is on", inline=True)
        embed.add_field(name='!!define', value="Get a defenition of a word from Urban Dictionary", inline=True)
        embed.add_field(name='!!iminfo', value="Information about a user put nicely in an image", inline=True)
        await self.bot.send_message(author, embed=embed)
        embed = discord.Embed(title="Command List 3: @user Commands", colour=random.choice(colors))
        embed.add_field(name='!!hug *user*', value='Hugs someone') 
        embed.add_field(name='!!kiss *user*', value='Kisses someone')
        embed.add_field(name='!!slap *user*', value='Slaps someone')
        embed.add_field(name='!!shoot @*someone*', value='Shoots someone', inline=True)
        embed.add_field(name='!!stab @*someone*', value='Stabs someone', inline=True)  
        await self.bot.send_message(author, embed=embed)    
        embed = discord.Embed(title="Command List 4: Text Commands", colour=random.choice(colors))
        embed.add_field(name='!!fancy *text*', value='Makes the text fancy', inline=True)
        embed.add_field(name='!!big *text*', value='Makes the text big', inline=True)
        embed.add_field(name='!!bigchief *text*', value='Turns your text into the bigcheiffont', inline=True)
        embed.add_field(name='!!block *text*', value='Turns your text into the block font', inline=True)
        embed.add_field(name='!!broadway *text*', value='Turns your text into the broadway font', inline=True)
        embed.add_field(name='!!bubble *text*', value='Turns your text into the bubble font', inline=True)
        embed.add_field(name='!!cyberlarge *text*', value='Turns your text into the cyberlarge font', inline=True)
        embed.add_field(name='!!cybersmall *text*', value='Turns your text into the cybersmall font', inline=True)
        embed.add_field(name='!!doom *text*', value='Turns your text into the doom font', inline=True)
        await self.bot.send_message(author, embed=embed)
	
        embed = discord.Embed(title="Command List 5: Images", colour=random.choice(colors))
        embed.add_field(name='!!cat', value='Sends a cat', inline=True)
        embed.add_field(name='!!dog', value='Sends a dog', inline=True)
        embed.add_field(name='!!snek', value='Sends a snek', inline=True)
        embed.add_field(name='!!meme', value='Sends a meme', inline=True)
        embed.add_field(name='!!senko', value='Sends a senko', inline=True)
        await self.bot.send_message(author, embed=embed)

        embed = discord.Embed(title="Command List 6: Misc Commands", colour=random.choice(colors))
        embed.add_field(name='!!btfo', value='Sends iToddlers BTFO and a Satania gif', inline=True)
        embed.add_field(name='!!maga', value='Make America Great Again!', inline=True)
        embed.add_field(name='!!wtf', value='Sends a picture', inline=True)
        embed.add_field(name='!!randcolor', value="Sends a random color", inline=True)
        embed.add_field(name='!!say *text*', value='The bot repeats after you', inline=True)
        embed.add_field(name='!!rate *something/someone*', value='Rate something or someone', inline=True)
        embed.add_field(name='!!invite', value="Sends an invite to the bot's support server", inline=True)
        await self.bot.send_message(author, embed=embed)


       
        await self.bot.say('{}, look in your fucking DMs'.format(author.mention))

def setup(bot):
    bot.add_cog(help(bot))
