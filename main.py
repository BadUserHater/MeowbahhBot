import discord
from discord.ext import commands
import datetime
import asyncio
import random
import sys

client = commands.Bot(command_prefix = "++")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"myself be one with the trash"))
    print("Bot Ready")

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title="Meowbahh Bot", description="Hello. Thank you for inviting me to your server. Cant wait to be trash here.", color=(16711839))
            embed.add_field(name="AGREEMENT", value='As you use me, you agree to our Privacy Policy: https://meowbahhbotsite.glitch.me/privacy.html\nAnd our Terms of Service: https://meowbahhbotsite.glitch.me/tos.html', inline=False)
            embed.add_field(name="WARNING", value='This bot has language that may be unsuitable for some people. Please be advised when using the bot and there is no clean mode.', inline=False)
            await channel.send(embed=embed)
        break

@client.command()
async def help(ctx):
    embed = discord.Embed(title="MEOQBAHH BOT", description="++help - This Message\n++ping - Checks my latency\n++botinfo - Information about the bot", color=(16711839))
    embed.add_field(name="MAIN FUN COMMANDS", value='++say - Make me say things\n++askmeow - Ask me anything\n++facereveal - I reveal my face\n++art - See some Bad User art made by our community\n++badusermeme - Get a Meme of a Bad User', inline=False)
    embed.add_field(name="VOICE CHANNEL COMMANDS", value='++stop - Stop my voice channel stuff and make me disconnect from VC\n++play - Play a stupid song\n++listsongs - I list my music for ++play', inline=False)
    embed.add_field(name="OTHER", value='++staffcmds - Commands for Bot Admins cause they need them.', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'My Latency is: {round(client.latency * 1000)}ms')

@client.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Meowbahh Bot Information", description="Below is information about me", color=(16711839))
    embed.add_field(name="CREATION", value='Made with: discord.py\nMade by: Idiot Creature Hater#2255 (Creators ID: 757827467657478245)', inline=False)
    embed.add_field(name="BOT STATS", value='NO STATS TO SHOW RIGHT NOW', inline=False)
    embed.add_field(name="LINKS", value='Invite Me: https://discord.com/api/oauth2/authorize?client_id=972161452133728256&permissions=0&scope=bot\nSupport Server: https://discord.gg/NpRbKaFmJU\nPrivacy Policy: https://meowbahhbotsite.glitch.me/privacy.html', inline=False)
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
    responses = ["I eat Garbage Bags",
                 "Fun Fact about me: My brain is made out of air.",
                 "What are ABCs?",
                 "Help! I don't know what 1+1 equals",
                 "I live in a dumpster. I love digging in trash",
                 "I have 0 iq.",
                 "I am a 5 year old",
                 "Im Cringe",
                 "Yes. I am the queen of Trash",
                 "I wear Trashbags",
                 "I am indeed Stupid",
                 "I am CRINGE!",
                 "Wanna play Trash Can Simulator with me?",
                 "That equals trash ofc.",
                 "I never graduated kindergarden. lol",
                 "I love saying N word slur",
                 "My Music Covers suck",
                 "NO! Animals do NOT belong in a bun",
                 "Yes I am a Male",
                 "I am not trusted with Moderation cause I am a bin.",
                 "Yes?",
                 "No?",
                 "Why you bully me? :(",
                 "UWU",
                 "Yes. I do love trash bins",
                 "PLS MAKE ME TRASH!",
                 "I have 0 friends",
                 "How would I know that? I dont have a brain",
                 "How do I count?",
                 "I support That Vegan Teacher",
                 "NO DONT EAT ANIMALS!!! *cries",
                 "I am a clown. Wanna see me do a clown dance?",
                 "NO!",
                 "YES! UWU",
                 "Can I eat or drink some glue please?",
                 "I LOVE SAYING SLURS!!!!",
                 "Please Make me trash",
                 "YAAAAAAYYY!!!!! Thank you",
                 "PLS MAKE ME A BIN",
                 "I am a clown with idiot clown makeup on",
                 "I will tell you my favorite meals: Trash in a can and Toilet water",
                 "*does a dumb clown dance",
                 "*cries",
                 "*has a stroke",
                 "*Stares into the abyss",
                 "*does the chicken toilet bin dance for no reason",
                 "*stares at some toilet water like it is gonna do something",
                 "*Listens to my trash bin like it is gonna say something",
                 "*cries and makes a river of tears",
                 "*stares into the abyss with an idiot look",
                 "*starts filming toilet water",
                 "*explodes",
                 "*becomes a bin",
                 "*plays with my bin plushie",]
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
async def facereveal(ctx):
    await ctx.send(file=discord.File(f'./facereveal.jpg'))

@client.command()
async def art(ctx):
    responses = ["meowbahh1.jpg",
                 "meowbahh2.png",
                 "meowbahh3.jpg",
                 "meowbahh4.png",
                 "meowbahh5.jpg",
                 "meowbahh6.jpg",
                 "meowbahh7.jpg",
                 "lisagaming1.jpg",
                 "lisagaming2.jpg",
                 "lisagaming3.jpg",
                 "lisagaming4.jpg",
                 "lisagaming5.jpg",
                 "lisagaming6.jpg",
                 "lisagaming7.jpg",
                 "lisagaming8.png",
                 "narayan1.png",
                 "narayan2.png",
                 "narayan3.jpg",
                 "anna1.jpg",
                 "anna2.jpg",
                 "anna3.png",
                 "other1.png",
                 "other2.jpg",
                 "other3.jpg",]
    await ctx.send(file=discord.File(f'./otherimage/{random.choice(responses)}'))

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
                 "meme28.jpg"]
    await ctx.send(file=discord.File(f'./otherimage/{random.choice(responses)}'))

@client.command()
async def play(ctx, *, songid):
    if(ctx.author.voice is None):
        await ctx.send("But you need to join a VC to do that")
        return
    if ctx.guild.voice_client in  client.voice_clients:
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(f'./audio/{songid}.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            await ctx.send(f"Hope you enjoy this stupid song")
    else:
        await ctx.author.voice.channel.connect()
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio(f'./audio/{songid}.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
            await ctx.send(f"Hope you enjoy this stupid song")

@client.command()
async def listsongs(ctx):
    await ctx.send('Here are a list of songs you can play in me\n\n++play rhysluffsong\n++play gummybear\n++play annalgasong\n++play onelittlepieceofsh\n++play lisagamingrobloxintro\n++play tvthadash\n++play rhyslufflovespieceofsh\n++play imastupidpieceofsh\n++play musicalmessagetobadusers\n++play idiotcreaturesstroke\n++play bahbahpinksh\n\n++play buildatrash\n++play octobershort\n++play untitled\n++play kingsandqueensshort')

@client.command()
async def stop(ctx):
    if(ctx.author.voice is None):
        await ctx.send("You need to be in a VC to (disconnect me from the Voice Channel)")
        return
    server = ctx.message.guild.voice_client
    await server.disconnect()
    await ctx.send("Successfully put away (disconnected from VC)")








leaders = [757827467657478245]

@client.command()
async def staffcmds(ctx):
    embed = discord.Embed(title="MEOQBAHH BOT", description="These are the Commands for my Bot Admins cause we need them. (Public cant use these commands.", color=(16711839))
    embed.add_field(name="UTILITY", value='++watchstatus - Set a watching status\n++listenstatus - Set a Listening status\n++playstatus - Set a playing status', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def watchstatus(ctx, *, question):
    if ctx.author.id in leaders:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{question}"))
        await ctx.send("My Status is Successfully Changed")
    else:
        await ctx.send("This command can only be used by the bot admins")
        return

@client.command()
async def listenstatus(ctx, *, question):
    if ctx.author.id in leaders:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{question}"))
        await ctx.send("My Status is Successfully Changed")
    else:
        await ctx.send("This command can only be used by the bot admins")
        return

@client.command()
async def playstatus(ctx, *, question):
    if ctx.author.id in leaders:
        await client.change_presence(activity=discord.Game(name=f"{question}"))
        await ctx.send("My Status is Successfully Changed")
    else:
        await ctx.send("This command can only be used by the bot admins")
        return





client.run("BOT TOKEN")
