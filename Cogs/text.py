import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import pyfiglet
from pyfiglet import figlet_format, FontNotFound



class text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot







    @commands.command()
    async def big(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="big") + "```")

    @commands.command()
    async def banner(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="banner") + "```")


    @commands.command()
    async def bigchief(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="bigchief") + "```")


    @commands.command()
    async def block(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="block") + "```")



    @commands.command()
    async def broadway(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="broadway") + "```")



    @commands.command()
    async def bubble(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="bubble") + "```")


    @commands.command()
    async def cyberlarge(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="cyberlarge") + "```")

    @commands.command()
    async def cybersmall(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="cybersmall") + "```")


    @commands.command()
    async def doom(self, ctx, *, text):
            await ctx.send("```fix\n" + figlet_format(text, font="doom") + "```")






    @commands.command()
    async def fancy(self, text, ctx):

            def strip_non_ascii(string):
                stripped = (c for c in string if 0 < ord(c) < 127)
                return ''.join(stripped)

            text = strip_non_ascii(text)
            if len(text.strip()) < 1:
                return await ctx.send("Only use ASCII characters.")
            output = ""
            for letter in text:
                if 65 <= ord(letter) <= 90:
                    output += chr(ord(letter) + 119951)
                elif 97 <= ord(letter) <= 122:
                    output += chr(ord(letter) + 119919)
                elif letter == " ":
                    output += " "
            await ctx.send(str(output))




def setup(bot):
    bot.add_cog(text(bot))
