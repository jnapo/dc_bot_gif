import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix="+")
client.remove_command('help')

# embed for command help
embed = discord.Embed(title="Available commands", color=0x0000ff)
embed.add_field(name="+gif", value="I will send you a gif with your text", inline=False)


# Bot is running properly
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Hello there"))
    print("Bot is ready")


# Wrong command
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=embed)
        await ctx.message.delete()
    else:
        print(str(error))


# Help command
@client.command()
async def help(ctx):
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def gif(ctx):
    pass

client.run('TOKEN')