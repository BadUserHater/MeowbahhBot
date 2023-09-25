import revolt
from revolt.ext import commands
import random
import asyncio
import aiohttp
import requests

class Client(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "++"

    @commands.command()
    async def help(self, ctx):
        await ctx.send("Here are my commands\n++help - This message\n++say - Make me say stuff\n++esay - Make me say things in a embed\n++askmeow - Ask me anything\n++baduserfact - Learn a fact about a Bad User\n++askidiotai - Ask the Idiot AI ChatBot API")

    @commands.command()
    async def say(self, ctx, *, arg):
        await ctx.send(arg)
        await ctx.message.delete()

    @commands.command()
    async def esay(self, ctx, *, arg):
        embed = revolt.SendableEmbed(description=arg)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def askmeow(self, ctx: commands.Context, *, question):
        responses = ["Yes. I am the queen of Trash",
                     "Yes?",
                     "No?",
                     "NO!",
                     "YES! UWU",
                     "Yes. I do love trash bins",
                     "YAAAAAAYYY!!!!! Thank you",
                     "Why you bully me? :(",
                     "UWU",
                     "I eat Garbage Bags",
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

    @commands.command()
    async def askidiotai(self, ctx: commands.Context, question):
        url = f"https://idiotcreaturehater.pythonanywhere.com/api?input={question}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        await ctx.send(f"Question: {question}\nResponse: {response.text}")

    @commands.command()
    async def baduserfact(self, ctx: commands.Context):
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



async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, "BOTTOKENHERE")
        await client.start()

asyncio.run(main())


