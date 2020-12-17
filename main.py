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
    bot.change_presence(activity=discord.Game('TBhelp'))

@bot.command()
async def help(ctx):
    await ctx.send(helptext)

@bot.command()
async def start(ctx):
    global typing
    typing = 1
    await ctx.channel.send("starting typing, may take a up to 30 seconds")
    while typing == 1:
        await ctx.channel.trigger_typing()

@bot.command()
async def stop(ctx):
    global typing
    typing = 0
    await ctx.channel.send("stopping typing, may take a up to 30 seconds")

@bot.command()
async def name(ctx, name):
    await ctx.guild.me.edit(nick=name)
    await ctx.channel.send(f"typing-bot's name will now appear as {name}")

    
    
bot.run(token)
