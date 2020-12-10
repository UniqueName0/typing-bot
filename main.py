import os
import discord
from discord.ext import commands, tasks

token = os.getenv('token')

helptext = open('help.txt', 'r').read()



bot = commands.Bot(command_prefix='TB')

bot.remove_command('help')



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def help(ctx):
    await ctx.send(helptext)

@bot.command()
async def start(ctx):
    await ctx.channel.startTyping(True)

@bot.command()
async def stop(ctx):
    await ctx.channel.stopTyping(True)

@bot.command()
async def name(ctx, name):
    ctx.guild.me.edit(nick=name)

    
bot.run(token)
