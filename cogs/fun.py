import discord
from discord.ext import commands
import random
import traceback
import asyncio
from asyncio import sleep

class Fun():
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def choose(self, ctx, *choices):
        """Make me choose something
Ex:
!?choose Facebook Twitter Instagram"""
        if len(choices) == 1:
            return await ctx.send('Give me more choices dude')
        await ctx.send(f':thinking: | I\'ll choose **' + random.choice(choices) + '**!')



    @commands.command()
    async def space(self, ctx, *, context):
        """Space your text
Ex:
!?space How Does This Command Work"""
        await ctx.send(' '.join(context))


    @commands.command()
    async def poll(self, ctx, *, question):
        """Make a poll about something
Ex:
!?poll Should i start youtube?"""
        em = discord.Embed(color=discord.Colour.blurple())
        em.add_field(name='Question:', value=question)
        em.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        hey = await ctx.send(embed=em)
        await hey.add_reaction('\N{THUMBS UP SIGN}')
        await hey.add_reaction('\N{THUMBS DOWN SIGN}')


    @commands.command()
    async def say(self, ctx, *, message):
        """Make me say something
Ex:
!?say Hello World"""
        await ctx.send(message)







def setup(bot):
        bot.add_cog(Fun(bot))
