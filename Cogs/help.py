import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random




class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=2.0)
    async def help(self, ctx):
        author = ctx.message.author

        #embed = discord.Embed()


        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]

        embed = discord.Embed(title="Useful Bot Commands", colour=random.choice(colors))
        embed.set_author(name='Command List 1: Mod Commands')
        embed.add_field(name='!!ping', value='Pong!', inline=False)   
        embed.add_field(name='!!kick', value='Kicks a member', inline=False)
        embed.add_field(name='!!ban', value="Bans a member", inline=False)
        embed.add_field(name='!!clear *value*', value="Clears desired ammount of messages", inline=False)
        embed.add_field(name='!!announce *text*', value="Creates a red embed with your desired text", inline=False)
        embed.add_field(name='!!nickname *user* *nickname*', value="Changes a user's nickname", inline=False)
        await author.send(embed=embed)

        embed = discord.Embed(title="Command List 2: Info Commands", colour=random.choice(colors))

        embed.add_field(name='!!info @*someone*', value='Gives you the info on a member', inline=False)
        embed.add_field(name='!!sinfo', value='Gives you the info on a server', inline=False)
        embed.add_field(name='!!botinfo', value='Shows info on bot', inline=False)
        embed.add_field(name='!!pfp @*someone*', value="Sends the user's profile picture", inline=False)
        embed.add_field(name="!!pfpurl @*someone*", value="Sends a link to the user's profile picture", inline=False)
        embed.add_field(name='!!listbans', value="Lists all the banned users in the server", inline=False)
        embed.add_field(name='!!servers', value="Shows how many servers the bot is on", inline=False)
        embed.add_field(name='!!define', value="Get a defenition of a word from Urban Dictionary", inline=False)
        embed.add_field(name='!!iminfo', value="Information about a user put neatly in an image", inline=False)
        await author.send(embed=embed)
        embed = discord.Embed(title="Command List 3: @user Commands", colour=random.choice(colors))
        embed.add_field(name='!!hug *user*', value='Hugs someone', inline=False) 
        embed.add_field(name='!!kiss *user*', value='Kisses someone', inline=False)
        embed.add_field(name='!!slap *user*', value='Slaps someone', inline=False)
        embed.add_field(name='!!spank *user*', value='Spanks someone', inline=False)
        embed.add_field(name='!!pat *user*', value='Pats someone', inline=False)
        embed.add_field(name='!!cudde *user*', value='Cuddles someone', inline=False)
        embed.add_field(name='!!poke *user*', value='Pokes someone', inline=False)
        embed.add_field(name='!!shoot @*someone*', value='Shoots someone', inline=False)
        embed.add_field(name='!!stab @*someone*', value='Stabs someone', inline=False)  
        await author.send(embed=embed)    
        embed = discord.Embed(title="Command List 4: Text Commands", colour=random.choice(colors))
        embed.add_field(name='!!fancy *text*', value='Makes the text fancy', inline=False)
        embed.add_field(name='!!big *text*', value='Makes the text big', inline=False)
        embed.add_field(name='!!bigchief *text*', value='Turns your text into the bigcheiffont', inline=False)
        embed.add_field(name='!!block *text*', value='Turns your text into the block font', inline=False)
        embed.add_field(name='!!broadway *text*', value='Turns your text into the broadway font', inline=False)
        embed.add_field(name='!!bubble *text*', value='Turns your text into the bubble font', inline=False)
        embed.add_field(name='!!cyberlarge *text*', value='Turns your text into the cyberlarge font', inline=False)
        embed.add_field(name='!!cybersmall *text*', value='Turns your text into the cybersmall font', inline=False)
        embed.add_field(name='!!doom *text*', value='Turns your text into the doom font', inline=False)
        await author.send(embed=embed)
        embed = discord.Embed(title="Command List 5: Images", colour=random.choice(colors))
        embed.add_field(name='!!cat', value='Sends a cat', inline=False)
        embed.add_field(name='!!dog', value='Sends a dog', inline=False)
        embed.add_field(name='!!snek', value='Sends a snek', inline=False)
        embed.add_field(name='!!neko', value='Sends a neko', inline=False)
        embed.add_field(name='!!meme', value='Sends a meme', inline=False)
        embed.add_field(name='!!senko', value='Sends a senko', inline=False)
        await author.send(embed=embed)
        embed = discord.Embed(title="Command List 6: NSFW", colour=random.choice(colors))
        embed.add_field(name='!!hentai', value='Posts a hentai image/gif', inline=False)
        embed.add_field(name='!!boobs', value='Posts boobs', inline=False)
        embed.add_field(name='!!nekolewd', value='Lewd Nekos', inline=False)
        await author.send(embed=embed)
        embed = discord.Embed(title="Command List 7: Misc Commands", colour=random.choice(colors))
        embed.add_field(name='!!btfo', value='Sends iToddlers BTFO and a Satania gif', inline=False)
        embed.add_field(name='!!randcolor', value="Sends a random color", inline=False)
        embed.add_field(name='!!say *text*', value='The bot repeats after you', inline=False)
        embed.add_field(name='!!rate *something/someone*', value='Rate something or someone', inline=False)
        await author.send(embed=embed)


       
        await ctx.send('{}, look in your fucking DMs'.format(author.mention))

def setup(bot):
    bot.add_cog(help(bot))
