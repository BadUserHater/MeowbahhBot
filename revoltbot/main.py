import voltage
from voltage.ext import commands
import random
import asyncio
import aiohttp
import requests

client = commands.CommandsClient("++")

@client.listen("ready")
async def ready():
    print("Meowbahh Bot is Online and Ready")
    await client.set_status(text="Listening to my Trash Can")

@client.command(description="View Information about the bot + Invite Links")
async def botinfo(ctx):
    embed = voltage.SendableEmbed(title="Meowbahh Bot Information", description=f"Servers Im in: {len(client.servers)}\nMade with: Voltage (A Python Package for Revolt Bots)\nInvite Me: https://app.revolt.chat/bot/01GQ6RADXPSXPF6NW4CBXXE0VV\nSupport Server: https://rvlt.gg/sRTVE2sV\nWebsite: https://idiotcreaturehater.glitch.me", color="#FF009F")
    await ctx.send(embed=embed)

@client.command(description="Make me say things. Example: ++say hi")
async def say(ctx, *, question):
    await ctx.send(f'{question}')
    await ctx.message.delete()

@client.command(description="Make me say things in a embed. Example: ++esay hi")
async def esay(ctx, *, question):
    embed = voltage.SendableEmbed(description=f'{question}', color="#FF009F")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(description="Ask me anything. Example: ++askmeow hi")
async def askmeow(ctx, *, question):
    responses = ["Yes. I am the queen of Trash",
                 "Yes?",
                 "No?",
                 "NO!",
                 "YES! UWU",
                 "Yes. I do love trash bins",
                 "YAAAAAAYYY!!!!! Thank you",
                 "Why you bully me? :(",
                 "UWU",
                 "Fun Fact about me: My brain is made out of air and idiotism.",
                 "What are ABCs?",
                 "Help! I don't know what 1+1 equals",
                 "I live in a dumpster. I love digging in trash",
                 "I have 0 iq.",
                 "I am indeed Stupid",
                 "I am CRINGE!",
                 "That equals trash ofc.",
                 "I never graduated kindergarden. lol",
                 "I love saying N word slur",
                 "My Music Covers suck",
                 "I am not trusted with Moderation because I am a bin.",
                 "PLEASE MAKE ME TRASH!",
                 "How would I know that? I dont have a brain",
                 "How do I count?",
                 "I support That Vegan Teacher",
                 "I am a clown. Wanna see me do a clown dance?",                     
                 "Can I eat or drink some glue please?",
                 "Please Make me trash",
                 "I am a clown with idiot clown makeup on",
                 "I will tell you my favorite meals: Trash in a can and Toilet water",
                 "Does 1+1 equal 3?",
                 "Wanna play Trash Can Simulator with me?",
                 "Wanna see me unleash my bin form?",
                 "I am a cocomelon and bin lover",
                 "I love hugging trash cans",
                 "I am as worthless as a tin can",
                 "Wanna smoke Bin flavoured weed with me?",
                 "ALPHABET BOOK IS BEST BOOK IN UNIVERSE",
                 "Im sorry my brain has no signal for me to answer that",
                 "Let me get a Childrens book because I want a childrens book",
                 "I dont know how to use the potty",
                 "I'm too scared of the potty",
                 "Help. I dont know my shapes",
                 "What are shapes?",
                 "*prays to my bin",
                 "*does a dumb clown dance",
                 "*has a stroke",
                 "*does the chicken toilet bin dance for no reason",
                 "*stares at some toilet water like it is gonna do something",
                 "*Listens to my trash bin like it is gonna say something",
                 "*cries and makes a river of tears",
                 "*stares into the abyss with an idiot look",
                 "*starts filming toilet water",
                 "*explodes",
                 "*becomes a bin",
                 "*becomes a tin can",
                 "*plays with my bin plushie",
                 "*attempts to eat squeaky chicken",
                 "*eats toilet paper",
                 "*smokes bin flavoured weed",
                 "*throws a tantrum",
                 "*stares at a wall like an idiot"]
    await ctx.send(f'Meowbahh\n\nQuestion: {question}\nAnswer: {random.choice(responses)}')

@client.command(description="Ask That Vegan Teacher stuff. Example: ++asktvt hi")
async def asktvt(ctx, *, question):
    responses = ["YES",
                 "NO!",
                 "NO NO NO!",
                 "NO! ANIMALS DO NOT BELONG IN A BUN",
                 "WHAT THE HECK IS THAT!?",
                 "Animals are friends. Not food",
                 "Why love one animal but eat the other?",
                 "EATING ANIMALS IS RAPE!",
                 "Be vegan!",
                 "Start being vegan!",
                 "I like Weeeeeeeeeeeeeeeeeeed",
                 "Why would you sexually harras an animal?",
                 "If we stopped eating animals, they will eventually disappear",
                 "And on that farm we have some.... Brocoli?",
                 "NO DONT EAT ANIMALS!!! *cries",
                 "CHEESE IS A POISON",
                 "Sheep do NOT belong on a farm!",
                 "WHAT ARE YOU DOING!?",
                 "WE LIKE bin WEEEEEEEEEEEEEEEED!",
                 "Try drinking Pee. It is really good for you",
                 "*rages at cheese",
                 "*cries",
                 "*starts smoking bin flavoured weed"]
    embed = voltage.SendableEmbed(title="THAT VEGAN TEACHER", description=f"Question: {question}\nAnswer: {random.choice(responses)}", color="#FF009F", icon_url="https://static.wikia.nocookie.net/youtube/images/7/7a/ThatVeganTeacherFace.jpg/revision/latest?cb=20210113090901")
    await ctx.send(embed=embed)

@client.command(description="Ask the IdiotAI Chatbot things. Example: ++askidiotai hi")
async def askidiotai(ctx, question):
    url = f"https://idiotcreaturehater.pythonanywhere.com/api?input={question}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    embed = voltage.SendableEmbed(title=f"IdiotAI API", description=f"Question: {question}\nResponse: {response.text}", color="#FF009F")
    await ctx.send(embed=embed)

@client.command(description="See some Bad User art made by our community")
async def art(ctx):
    responses = ["meowbahh1.jpg",
                 "meowbahh2.jpg",
                 "meowbahh3.jpg",
                 "meowbahh4.png",
                 "meowbahh5.jpg",
                 "meowbahh6.jpg",
                 "meowbahh7.jpg",
                 "meowbahh8.jpg",
                 "meowbahh9.jpg",
                 "meowbahh10.jpg",
                 "lisagaming1.jpg",
                 "lisagaming2.jpg",
                 "lisagaming3.jpg",
                 "lisagaming4.png",
                 "lisagaming5.jpg",
                 "lisagaming6.jpg",
                 "lisagaming7.jpg",
                 "lisagaming8.jpg",
                 "lisagaming9.png",
                 "lisagaming10.jpg",
                 "lisagaming11.png",
                 "anna1.jpg",
                 "anna2.jpg",
                 "anna3.png",
                 "anna4.png",
                 "anna5.jpg",
                 "anna6.jpg",
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
    await ctx.send(attachment=voltage.File(f'./resources/{random.choice(responses)}'))

@client.command(description="Get a Meme of a Bad User")
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
                 "meme32.webp",]
    await ctx.send(attachment=voltage.File(f'./resources/{random.choice(responses)}'))

@client.command(description="Learn a fact about a Bad User")
async def baduserfact(ctx):
    responses = ["Lisa Gaming Roblox started Youtube on Jul 30, 2017",
                 "The main reason Lisa Gaming Roblox has been hated is because she deletes peoples Bloxburg houses in Roblox that the people worked hard on.",
                 "Lisa Gaming Roblox and her discord staff has been exposed by Parlos #lisafiles because they supported illegal stuff like Doxxing people and CP.",
                 "Meowbahh has been hated cause she thinks she (or he) can defeat allah and loves saying slurs",
                 "Alex Gaming Roblox started Youtube at Feb 4, 2021",
                 "Alex Gaming Roblox believes dreamsexual is valid which means he is most likely a Dream stan",
                 "Alex Gaming Roblox thinks Slendersexual is valid",
                 "Alex Gaming Roblox LOVES watching Cocomelon",
                 "Narayan the Video Maker 2000 USED to be a bad user but has changed his ways and is no longer a bad user",
                 "PEKKA is actually owned by Seance the Gacha Archer Boy (Sometimes changes username to something else similar) and Seance offends countries. Watch Idiot Creature Wars Episode 2 to watch the proof.",
                 "Gacha Kitten Lisa thinks eating meat is offensive to everyone.",
                 "Dreamstans are actually weird",
                 "NFTs are causing harm to the environment cause they use cryptocurrencies",]
    await ctx.send(f'**Here is a Random Bad User Fact:** {random.choice(responses)}')



client.run("BOTTOKENHERE")
