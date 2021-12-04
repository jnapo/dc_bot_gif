import discord
from discord.ext import commands
from get_gif import download_gif
from discord.utils import get

client = commands.Bot(command_prefix="+")
client.remove_command('help')

# embed for command help
embed = discord.Embed(title="Available commands", color=0x0000ff)
embed.add_field(name="+gif",
                value="I will send you a gif with your text and font, "
                      "if you want to send text with spaces surround it with \" \"",
                inline=False)


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
    elif isinstance(error, commands.BadArgument):
        await ctx.send("That's not what I wanted")
    else:
        print(str(error))


# Help command
@client.command()
async def help(ctx):
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def gif(ctx, text="JP2GMD", font=70):
    download_gif(text, font)
    await ctx.send(file=discord.File('text.gif'))


client.run('TOKEN')
