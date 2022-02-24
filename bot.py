import os
import random
import discord
from discord.ext import commands
from keepalive import keepAlive
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="b", description='lol', help_command=None, intents=intents)
messages = [
    "Stop playing genshin impact",
    "Take a shower",
    "Go touch some grass",
    "what, you love an image bro ?? Cringe."
]
@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')
    print(bot.guilds)
    await bot.change_presence(activity=discord.Game(name=f"{random.choice(messages)}"))
    members = 0
    for guild in bot.guilds:
        for member in guild.members:
            members += 1
    with open("members.txt", "w") as f:
         f.write(str(members))
@bot.event
async def on_member_update(before, after):
        if after.activity != None:
            print(after.name)
        if len(after.activities) > 1:
            print(after.activities[1].name)
            if str(after.activities[1].name).lower() == "genshin impact":
                print("banning")
                try:
                    with open("hall-of-shame.txt", "a+") as f:
                        f.write(after.name)


                    await after.send(random.choice(messages))
                    await after.ban(reason='Playing Gayshit Impact')
                except discord.errors.Forbidden:
                    print("Not valid permissions")
                    after.send("")
            if str(after.activities[1].name).lower() == "league of legends":
                print("banning")
                try:
                    with open("hall-of-shame.txt", "a+") as f:
                        f.write(after.name)
                    await after.send(random.choice(messages))
                    await after.ban(reason='Playing league')
                except discord.errors.Forbidden:
                    print("Not valid permissions")
                    after.send("")
keepAlive()
bot.run(os.environ['TOKEN'])