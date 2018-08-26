import discord
from discord.ext import commands
import random
import traceback
import asyncio
from asyncio import sleep



class Moderation():
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx):
        """Manage the server roles
Ex:
!?role [add/remove] [user] [role]"""
        if ctx.invoked_subcommand is None:
            return await ctx.send('Please do `!?role [add/remove] [user] [role]`')

    @role.command()
    @commands.has_permissions(manage_roles=True)
    async def add(self, ctx, target: discord.Member, role: discord.Role):
        """Add a role to a user
Ex:
!?role add Adytzu96 Admin"""
        await target.add_roles(role)
        await ctx.send(f'I gave {target} the role {role}')

    @role.command()
    @commands.has_permissions(manage_roles=True)
    async def remove(self, ctx, target: discord.Member, role: discord.Role):
        """Remove a role from a user
Ex:
!?role remove Adytzu96 Mod"""
        await target.remove_roles(role)
        await ctx.send(f'{target} was removed from {role}')


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def purge(self, ctx, amount: int):
        """Delete a number of messages in a channel
Ex:
!?purge 120"""
        await ctx.message.delete()
        await ctx.message.channel.purge(bulk=True, limit=amount)
        await ctx.send(f'Succesfully deleted {int(amount)} messages', delete_after=5)

 
            
        
        

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, target: discord.Member=None, reason=None):
        """Ban a user
Ex:
!?ban MEE6 Bad bot"""
        if target.id == 404708655578218511:
            return await ctx.send('Can you understand i can\'t ban my creator? (He will delete me if i do)')
        if target is None:
            return await ctx.send('Please provide a user')
        if ctx.author == target:
            return await ctx.send('You can\'t ban yourself!')
        if target == ctx.guild.owner:
            return await ctx.send('Did you know you can\'t ban the owner?')
        if target is not None and reason is None:
            await target.ban(reason=f'No Reason Provided (banned by {ctx.author}')
            return await ctx.send(f'`{target}` was succesfully banned!')
        if target is not None and reason is not None:
            await target.ban(reason=f'{reason} (banned by {ctx.author}')
            return await ctx.send(f'`{target}` was succesfully banned for `{reason}`!')







    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target: discord.Member=None, reason=None):
        """Kick a user
Ex:
!?kick Nightbot We don't need you"""
        if target.id == 404708655578218511:
            return await ctx.send('Can you understand i can\'t kick my creator? (He will delete me if i do)')
        if target is None:
            return await ctx.send('Please provide a user')
        if ctx.author == target:
            return await ctx.send('You can\'t kick yourself!')
        if target == ctx.author.guild.owner:
            return await ctx.send('Did you know you can\'t kick the owner?')
        if target is not None and reason is None:
            await target.kick(reason=f'No Reason Provided (kicked by {ctx.author}')
            return await ctx.send(f'`{target}` was succesfully kicked!')
        if target is not None and reason is not None:
            await target.kick(reason=f'{reason} (kicked by {ctx.author}')
            return await ctx.send(f'`{target}` was succesfully kicked for `{reason}`!')
        
    


    




def setup(bot):
        bot.add_cog(Moderation(bot))
