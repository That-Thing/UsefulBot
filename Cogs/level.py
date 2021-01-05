import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


#checks if the user config exists in the json
def checkExisting(userID):
    with open('users.json') as data:
        users = json.load(data)
    idCheck = False
    for x in users["users"]:
        currID = x['id']
        if currID == userID:
            idCheck = True
    return idCheck

#gets the user's level
def getLevel(userID):
    with open('users.json') as data:
        users = json.load(data)
    for x in users["users"]:
        currID = x['id']
        if currID == userID:
            level = x['level']
            return level
        else:
            print("Not Found")

#checks if the level messages are enabled in the server
def checkSettings(serverID):
    with open('settings.json') as data:
        settings = json.load(data)
    for x in settings['servers']:
        currID = x['id']
        if currID == serverID:
            return x['level']

#checks if the user has enough xp to level up. If the user does, the level gets raised by one
def levelUp(xp, userID):
    with open('users.json') as data:
        users = json.load(data)
    for x in users["users"]:
        currID = x['id']
        if currID == userID:
            level = x['level']
            multiplied = 5*(level**2)+30*level+30
            if xp == multiplied:
                level = level+1
                x['level'] = level
                with open('users.json', "w") as f:
                    f.write(json.dumps(users, indent=4, sort_keys=True)) 
                img = Image.open("levelup.jpg")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Zector.otf", 37)
                draw.text((132, 5), str(level-1) , (39,39,39), font=font)
                draw.text((310, 5), str(level) , (39,39,39), font=font)
                img.save('LevelupTemp.png')
                return True



class level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


#colors for level ups:
    #66a56a - 1-9
    #a0a566 - 10-59
    #7c66a5 - 50-99
    #a5669d - 150+

    @commands.command()
    async def level(self, ctx):
        with open('users.json') as data:
            users = json.load(data)
        for x in users["users"]:
            currID = x['id']
            if currID == ctx.message.author.id:
                level = x['level']
                xp = x['xp']
        color= 102,165,106
        x=0
        #cringe. 
        if level < 10:
            x=235
        elif level >= 50 and level < 100:
            color=160,165,102
            x = 220
        elif level >= 100 and level < 150:
            x = 200
            color=124,102,165
        elif level >= 150:
            color=165,102,157
            x = 200
        img = Image.open("LevelBackground.jpg")
        draw = ImageDraw.Draw(img)
        fontL = ImageFont.truetype("Zector.otf", 60)
        fontS = ImageFont.truetype("Zector.otf", 25)
        text_width, text_height = draw.textsize(str(xp)+"/"+str(level*150), fontS)
        draw.text((x, 150), str(level) , (color), font=fontL)
        draw.text(((500-text_width)/2, 265), str(xp)+"/"+str(level*150) , (39,39,39), font=fontS)
        img.save('Leveltmp.png')
        await ctx.send(file=discord.File("Leveltmp.png", ctx.message.author.name+".png"))


#Using the image level check command because it looks nice(tm)
    # @commands.command()
    # async def level(self, ctx):
    #     with open('users.json') as data:
    #         users = json.load(data)
    #     for x in users["users"]:
    #         currID = x['id']
    #         if currID == ctx.message.author.id:
    #             level = x['level']
    #             xp = x['xp']
    #     embed = discord.Embed(title="Level", description=str(level))
    #     embed.add_field(name="XP", value=str(xp)+"/"+str(level*150))
    #     embed.set_footer(text="Requested by {}".format(ctx.message.author))
    #     await ctx.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        currentID = message.author.id
        with open('users.json') as data:
            users = json.load(data)
        #check if user config exists. If not, create new one. 
        if checkExisting(currentID) == True:
            pass
        else:
            toAppend = {
                "id":currentID,
                "level":1, 
                "xp":1
            }
            users["users"].append(toAppend)
            with open('users.json', "w") as f:
                f.write(json.dumps(users, indent=4, sort_keys=True))            

        #time for the actual leveling stuff
        for x in users["users"]:
            currID = x['id']
            if currID == self.bot.user.id:
                pass
            elif currID == currentID:
                x['xp']+=1
                with open('users.json', "w") as f:
                    f.write(json.dumps(users, indent=4, sort_keys=True))
                if levelUp(x['xp'], currentID) == True:
                    if checkSettings(message.guild.id) == "on":
                        await message.channel.send(file=discord.File("LevelupTemp.png", message.author.name+".png"))

                      

        

            
def setup(bot):
    bot.add_cog(level(bot))