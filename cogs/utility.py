import discord
from discord.ext import commands
import random
import traceback
import asyncio
from asyncio import sleep

class Utility():
    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=['calc'])
    async def calculate(self, ctx, left: int, type, right: int):
        '''Calculate an equation
Ex:
!?calculate [number] [ + | * | - | ^ | / ] [number]'''
        if type == '*':
            return await ctx.send(left * right)
        if type == '+':
            return await ctx.send(left + right)
        if type == '-':
            return await ctx.send(left - right)
        if type == '/':
            return await ctx.send(left / right)
        if type == '^':
            return await ctx.send(left ^ right)
        await ctx.send('Invalid equation')




    @commands.command()
    async def avatar(self, ctx, user: discord.Member=None):
        '''Get a member's avatar
Ex:
!?avatar @kian_8x'''
        if user is None:
            user = ctx.author

        e = discord.Embed(description=f'[{user}\'s avatar]( {user.avatar_url} )', color=discord.Colour.blurple())
        e.set_image(url=user.avatar_url)
        await ctx.send(embed=e)


    @commands.command()
    async def roles(self, ctx):
        '''Get the server roles'''
        a = discord.Embed(color=discord.Colour.blurple())
        a.add_field(name=f'Server roles [{len(ctx.guild.roles)}]', value=', '.join(g.name for  g in ctx.guild.roles))
        await ctx.send(embed=a)


    @commands.command(aliases=['memberoles'])
    async def userroles(self, ctx, user: discord.Member=None):
        '''Get a user's roles
Ex:
!?userroles @luke'''
        if user is None:
            user = ctx.author

        a = discord.Embed(color=discord.Colour.blurple())
        a.add_field(name=f'{user}\'s roles [{len(ctx.author.roles)}]', value=', '.join(g.name for g in ctx.author.roles))
        await ctx.send(embed=a)


    @commands.command()
    async def userinfo(self, ctx, user: discord.Member=None):
        '''Get a user's info
Ex:
!?userinfo @magazinsnow'''
        if user is None:
            user = ctx.author

        a = discord.Embed(color=discord.Colour.blurple())
        a.add_field(name='Name:', value=f'{user.name}')
        a.add_field(name='ID:', value=f"{user.id}")
        a.add_field(name='Bot:', value=f'{user.bot}')
        a.add_field(name='Discrim:', value=f'{user.discriminator}')
        a.add_field(name='Top Role', value=f'{user.top_role}')
        a.add_field(name=f'Roles [{len(user.roles)}]', value=', '.join(g.name for g in user.roles))
        a.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=a)
            






def setup(bot):
        bot.add_cog(Utility(bot))
