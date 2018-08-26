#=======================IMPORTS===============
import discord
from discord.ext import commands
import logging
import random
from typing import Union
#===========================DEFINING===================
desc = f"""I am kian_8x's Bot! Made by Adytzu96#3030 to keep the server safe and sound"""
bot = commands.Bot(case_insensitive=True, command_prefix='!?', description=desc)
logging.basicConfig(level='INFO')
bot.load_extension('cogs.mod')
bot.load_extension('cogs.fun')
bot.load_extension('cogs.admin')
bot.load_extension('cogs.utility')
blacklist = []

#=============================IDK===================
@bot.event
async def on_ready():
    print(f'Logging in as {bot.user.name}')
    await bot.change_presence(activity=discord.Streaming(name="with Kian | !?help", url='https://www.twitch.tv/kian_8x'))






@bot.check
async def nobots(ctx):
    return not ctx.author.bot


   
@bot.event
async def on_command_error(ctx, error):
    if ctx.author.bot is True:
        return
    return await ctx.send(f'Error : {error}')
    
#============================HANDLERS==========================


@bot.listen()
async def on_member_join(member):
    if member.guild.id != 444774197458239499:
        return
    if member.guild.id == 444774197458239499:
        em = discord.Embed(color=discord.Colour.blurple())
        em.add_field(name=':tada: | Welcome!', value=member.mention, inline=False)
        em.add_field(name=':tools: | Info:', value=f'Welcome! This is {member.guild.owner.mention}\'s server. You can ask the staff for support, for more complex questions ping <@404708655578218511> or <@293825161549840394>')
        em.set_thumbnail(url=member.avatar_url)
        em.set_footer(text='Member Joined!', icon_url=member.avatar_url)
        await bot.get_guild(444774197458239499).get_channel(483343633332961301).send(embed=em)


@bot.event
async def on_member_join(member):
    if member.guild.id != 444774197458239499:
        return
    if member.bot is True:
        bot = discord.utils.get(member.guild.roles, id=447343285409808384)
        return await member.add_roles(bot)
    role = discord.utils.get(member.guild.roles, id=447330927295725568)
    await member.add_roles(role)



        
@bot.event
async def on_member_remove(member):
    if member.guild.id != 444774197458239499:
        return
    if member.guild.id == 444774197458239499:
        em = discord.Embed(color=discord.Colour.blurple())
        em.add_field(name=':cry: | Goodbye!', value=member.mention, inline=False)
        em.add_field(name=':tools: | Info:', value=f'He left us... I hope you\'ll rejoin, you\'re always welcome!')
        em.set_thumbnail(url=member.avatar_url)
        em.set_footer(text='Member Left!', icon_url=member.avatar_url)
        await bot.get_guild(444774197458239499).get_channel(483343633332961301).send(embed=em)



#==============================WHY=ARE=YOU=LOOKING=AT=THIS============
bot.run('NDgyNDMwMDY2MTQwMjUwMTQy.DmEyMA.TZmMiRAWjZPc28HTS_iJyP3sukk')
