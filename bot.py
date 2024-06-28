# bot.py
import discord
import config
import math
from discord.ext import commands


botdescription = "A mostly harmless bot used for trying things out"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, description=botdescription)


# Message is displayed after connection when bot is ready to accept commands
# This also has another example of native config file being used to obfuscate information.
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to the discord.')
    await bot.wait_until_ready()
    # Channel ID is pulled from another file via Import config
    channel = bot.get_channel(int(config.generalchat))
    # The double tile here (~~) format part of this line as a strikethrough on discord.
    if channel:
        await channel.send(f'{bot.user} has connected to the botnet and is ~~ready to hack the world~~ '
                           f'ready to follow orders.')


# The original code takes an 11 character string in the format 'XXX-XXX-XXX' as a seed, removes the '-', then converts
#   the string into a long. The conversion is simple and is shown below. I translated this into python to work with my
#   bot. The ord() function I use below takes a character and returns the unicode integer value for that character.
#   long result = 0;
# 		for (int i = 8; i >= 0; i--) {
# 			char c = code.charAt(i);
# 			if (c > 'Z' || c < 'A')
# 				throw new IllegalArgumentException("codes must be 9 A-Z characters.");
#
# 			result += (c - 65) * Math.pow(26, (8 - i));
# 		}
# 		return result;
@bot.command(name="reverseSeed")
async def reverse_seed(ctx, seedstring: str):
    seedstring.upper()
    if len(seedstring) != 9:
        response = 'wrong number of characters in seed, please try again.'
        await ctx.send(response)
    seedint = 0
    for x in range(0, len(seedstring)):
        seedint += (ord(seedstring[x])-65) * math.pow(26, 8-x)
    await ctx.send(f'{int(seedint)}')
    await ctx.send(f'{seedint} is the long conversion of the given string.')


# Token is stored in a native config file
bot.run(config.bot_token)

