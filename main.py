#############################################################################
#                                                                           #                                                                                                            #                                                                          #
# Basic Status Bot, Based on Discord.py                                     #
# Created by Rhys!                                                          #
#                                                                           #
#############################################################################


import discord # importing discord module
from discord.ext import commands

client = discord.Client() 

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='#')) # Change Status Here - Check Github For More Status's
    
    print('Connected to bot: {}'.format(client.user.name))  # Console log

client.run('') # put your token here
