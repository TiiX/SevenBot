import discord
import asyncio
ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
guess_url = 'https://guess-it.scoder12.repl.co/guess'

BAN_WORDS = ["AI","Cheese"]

client = discord.Client()

@client.event
async def on_ready():
    print("Seven Loaded.")

@client.event
async def on_message(message):
    if message.content == "!hello":
        member_name = message.author.name
        guild_name = message.guild.name
        new_msg = await message.channel.send("Bonjour "+member_name+" et bienvenue sur "+guild_name+".")
        await new_msg.pin()
        
    if message.content == "!why seven":
        await message.channel.send("I'm a secret. So find why.")
        
    if message.content == "!me":
        member_name = message.author.name
        em = discord.Embed(title="Ton Nom", description=member_name, color=0xFF0000,
                           timestamp=message.created_at)
        em.add_field(name="Un Field", value="Ton value", inline=True)
        await message.channel.send(embed=em)
    for word in BAN_WORDS:
        if word in message.content:
            print("WARNING : Ban Word Detected.")
            await message.delete()
            await message.channel.send("Ban Word Detected.")

client.run("NjkzMTE4NTI0NjU4NDE3NzU1.Xn4jng._2ywmiNcH9DHiwDGAptLzfD72h0")
