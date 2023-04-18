import discord
from discord.ext import commands
import datetime
import asyncio
import random
import sys

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "++", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"my trash bin"))
    print("Bot Ready")
    try:
        synced = await client.tree.sync()
        print(f"{len(synced)} Slash Commands successfully Synced")
    except Exception as e:
        print(e)

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Idiot Bot", description="**help** - This Message\n**ping** - Checks my latency\n**botinfo** - Information about the bot", color=(16711839))
    embed.add_field(name="MAIN FUN COMMANDS", value="**say** - Make me say things\n**askmeow** - Ask me anything\n**art** - See some Bad User art made by our community\n**badusermeme** - Get a Meme of a Bad User", inline=False)
    embed.add_field(name="VOICE CHANNEL COMMANDS", value="**stop** - Stop my voice channel stuff and make me disconnect from VC\n**play** - Play a stupid song\n**listsongs** - I list my music for ++play", inline=False)
    embed.add_field(name="STAFF COMMANDS", value="**watchstatus** - Set a watching status\n**listenstatus** - Set a Listening status\n**playstatus** - Set a playing status", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'My Latency is: {round(client.latency * 1000)}ms')

@client.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Meowbahh Bot Information", description="Below is information about me", color=(16711839))
    embed.add_field(name="CREATION", value='Made with: discord.py\nMade by: Idiot Creature Hater#2255 (Creators ID: 757827467657478245)', inline=False)
    embed.add_field(name="BOT STATS", value='NO STATS TO SHOW RIGHT NOW', inline=False)
    embed.add_field(name="LINKS", value='Invite Me: https://discord.com/api/oauth2/authorize?client_id=972161452133728256&permissions=0&scope=bot\nSupport Server: https://discord.gg/nVs4rCNwyc\nPrivacy Policy: https://meowbahhbotsite.glitch.me/privacy.html', inline=False)
    embed.add_field(name="CREDITS", value='Orignal Bot: https://discord.com/api/oauth2/authorize?client_id=972161452133728256&permissions=0&scope=bot\nSOURCE CODE: https://github.com/BadUserHater/Meowbahh-Bot', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def say(ctx, *, question: commands.clean_content):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="SOMETHING WENT WRONG", description="HUH???????", color=(16711839))
        embed.set_footer(text="You did not provide a text for me say. Example: ++say Hi")
        await ctx.send(embed=embed)
    else:
        raise error

@client.command()
async def askmeow(ctx, *, question):
    responses = ["Yes. I am the queen of Trash",
                 "Yes?",
                 "No?",
                 "NO!",
                 "YES! UWU",
                 "Why you bully me? :(",
                 "Fun Fact about me: My brain is made out of air and idiotism.",
                 "What are ABCs?",
                 "Help! I don't know what 1+1 equals",
                 "I live in a dumpster. I love digging in trash",
                 "Wanna play Trash Can Simulator with me?",
                 "That equals trash ofc.",
                 "PLS MAKE ME TRASH!",
                 "I have 0 friends",
                 "How would I know that? I dont have a brain",
                 "How do I count?",
                 "I am a clown. Wanna see me do a clown dance?",                     
                 "Can I eat or drink some glue please?",
                 "Please Make me trash",
                 "YAAAAAAYYY!!!!! Thank you",
                 "I am a clown with idiot clown makeup on",
                 "I will tell you my favorite meals: Trash in a can and Toilet water",
                 "I am a cocomelon and bin lover",
                 "I love hugging trash cans",
                 "I am as worthless as a tin can",
                 "Wanna smoke Bin flavoured weed with me?",
                 "ALPHABET BOOK IS BEST BOOK IN UNIVERSE",
                 "Im sorry my brain has no signal for me to answer that",
                 "I dont know how to use the potty",
                 "*does a dumb clown dance",
                 "*has a stroke",
                 "*does the chicken toilet bin dance for no reason",
                 "*stares at some toilet water like it is gonna do something",
                 "*Listens to my trash bin like it is gonna say something",
                 "*cries and makes a river of tears",
                 "*stares into the abyss with an idiot look",
                 "*explodes",
                 "*becomes a bin",
                 "*plays with my bin plushie",
                 "*attempts to eat squeaky chicken",
                 "*eats toilet paper",
                 "*becomes a tin can",
                 "*smokes bin flavoured weed",
                 "*throws a tantrum",
                 "*stares at a wall like an idiot"]
    await ctx.send(f'Meowbahh\n\nQuestion: {question}\nAnswer: {random.choice(responses)}')

@askmeow.error
async def askmeow_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="SOMETHING WENT WRONG", description="HUH???????", color=(16711839))
        embed.set_footer(text="You did not add a question to ask meowbahh. Example: ++askmeow Are you dumb?")
        await ctx.send(embed=embed)
    else:
        raise error

@client.command()
async def art(ctx):
    responses = ["meowbahh1.jpg",
                 "meowbahh2.jpg",
                 "meowbahh3.jpg",
                 "meowbahh4.png",
                 "meowbahh5.png",
                 "meowbahh6.jpg",
                 "meowbahh7.jpg",
                 "meowbahh8.jpg",
                 "meowbahh9.png",
                 "lisagaming1.jpg",
                 "lisagaming2.jpg",
                 "lisagaming3.jpg",
                 "lisagaming4.jpg",
                 "lisagaming5.png",
                 "lisagaming6.jpg",
                 "lisagaming7.jpg",
                 "lisagaming8.png",
                 "anna1.jpg",
                 "anna2.jpg",
                 "anna3.png",
                 "anna4.jpg",
                 "anna5.jpg",
                 "other1.png",
                 "other2.jpg",
                 "other3.jpg",
                 "other4.jpg",
                 "other5.jpg",
                 "other6.png",
                 "other7.jpg",
                 "other8.jpg",
                 "other9.jpg",
                 "other10.jpg",
                 "other11.jpg",]
    await ctx.send(file=discord.File(f'./resources/{random.choice(responses)}'))

@client.command()
async def badusermeme(ctx):
    responses = ["meme1.jpg",
                 "meme2.jpg",
                 "meme3.jpg",
                 "meme4.jpg",
                 "meme5.jpg",
                 "meme6.jpg",
                 "meme7.jpg",
                 "meme8.jpg",
                 "meme9.jpg",
                 "meme10.jpg",
                 "meme11.jpg",
                 "meme12.jpg",
                 "meme13.jpg",
                 "meme14.jpg",
                 "meme15.png",
                 "meme16.jpg",
                 "meme17.png",
                 "meme18.png",
                 "meme19.jpg",
                 "meme20.jpg",
                 "meme21.jpg",
                 "meme22.jpg",
                 "meme23.png",
                 "meme24.jpg",
                 "meme25.jpeg",
                 "meme26.jpg",
                 "meme27.jpg",
                 "meme28.jpg",
                 "meme29.png",
                 "meme30.jpg",
                 "meme31.jpg",]
    await ctx.send(file=discord.File(f'./resources/{random.choice(responses)}'))

@client.command()
async def play(ctx, *, songid):
    if(ctx.author.voice is None):
        await ctx.send("But you need to join a VC to do that")
        return
    if ctx.guild.voice_client in  client.voice_clients:
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(f'./resources/{songid}.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            await ctx.send(f"Hope you enjoy this stupid song")
    else:
        await ctx.author.voice.channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(f'./resources/{songid}.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            await ctx.send(f"Hope you enjoy this stupid song")

@client.command()
async def listsongs(ctx):
    embed = discord.Embed(title="Meowbahh Bot Information", description="Here are a list of songs you can play in me", color=(16711839))
    embed.add_field(name="By The Idiot Creature Hater", value='++play onelittlepieceofsh\n++play onelittlepieceofshext\n++play tvthadash\n++play rhyslufflovespieceofsh\n++play imastupidpieceofsh\n++play musicalmessagetobadusers\n++play bahbahpinksh', inline=False)
    embed.add_field(name="By WDNEBUTE", value='++play idiotcreaturesstroke', inline=False)
    embed.add_field(name="By Anna - Lets Be Idiots/A Demon on YT", value='++play rhysluffsong\n++play annalgasong\n++play 3littlepieceofshs', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def stop(ctx):
    if(ctx.author.voice is None):
        await ctx.send("You need to be in a VC to disconnect me from the Voice Channel")
        return
    server = ctx.message.guild.voice_client
    await server.disconnect()
    await ctx.send("Successfully put away (disconnected from VC)")




botadmin = [757827467657478245]

@client.command()
async def watchstatus(ctx, *, question):
    if ctx.author.id in botadmin:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{question}"))
        await ctx.send("My Status is Successfully Changed")
    else:
        await ctx.send("This command can only be used by the bot admins")
        return

@client.command()
async def listenstatus(ctx, *, question):
    if ctx.author.id in botadmin:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{question}"))
        await ctx.send("My Status is Successfully Changed")
    else:
        await ctx.send("This command can only be used by the bot admins")
        return

@client.command()
async def playstatus(ctx, *, question):
    if ctx.author.id in botadmin:
        await client.change_presence(activity=discord.Game(name=f"{question}"))
        await ctx.send("My Status is Successfully Changed")
    else:
        await ctx.send("This command can only be used by the bot admins")
        return





client.run("BOTTOKENHERE")
