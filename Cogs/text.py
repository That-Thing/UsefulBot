import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import pyfiglet
from pyfiglet import figlet_format, FontNotFound



class text:
    def __init__(self, bot):
        self.bot = bot







    @commands.command()
    async def big(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="big") + "```")

    @commands.command()
    async def banner(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="banner") + "```")


    @commands.command()
    async def bigchief(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="bigchief") + "```")


    @commands.command()
    async def block(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="block") + "```")



    @commands.command()
    async def broadway(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="broadway") + "```")



    @commands.command()
    async def bubble(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="bubble") + "```")


    @commands.command()
    async def cyberlarge(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="cyberlarge") + "```")

    @commands.command()
    async def cybersmall(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="cybersmall") + "```")


    @commands.command()
    async def doom(self, *, text):
            await self.bot.say("```fix\n" + figlet_format(text, font="doom") + "```")























    @commands.command()
    async def fancy(self, *, text):

            def strip_non_ascii(string):
                stripped = (c for c in string if 0 < ord(c) < 127)
                return ''.join(stripped)

            text = strip_non_ascii(text)
            if len(text.strip()) < 1:
                return await self.bot.say("Use only ASCII characters.")
            output = ""
            for letter in text:
                if 65 <= ord(letter) <= 90:
                    output += chr(ord(letter) + 119951)
                elif 97 <= ord(letter) <= 122:
                    output += chr(ord(letter) + 119919)
                elif letter == " ":
                    output += " "
            await self.bot.say(output)




def setup(bot):
    bot.add_cog(text(bot))
