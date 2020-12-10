import os
import discord
from discord.ext import commands, tasks

token = os.getenv('token')

helptext = open('help.txt', 'r').read()



bot = commands.Bot(command_prefix='TB')

bot.remove_command('help')

global typing
typing = 0

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
    global typing
    typing = 1
    while typing == 1:
        ctx.channel.trigger_typing()

@bot.command()
async def stop(ctx):
    global typing
    typing = 0

@bot.command()
async def name(ctx, name):
    ctx.guild.me.edit(nick=name)

    
    
bot.run(token)
