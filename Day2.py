import discord
import asyncio
import CobraMusic

import discord_token as tk
import ban_words as b_w

token = tk.token_id

##ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
##guess_url = 'https://guess-it.scoder12.repl.co/guess'

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
    if message.author != client.user:
        for word in b_w.BAN_WORDS:
            if word in message.content.lower():
                print("WARNING : Ban Word Detected.")
                await message.delete()
                await message.author.send("Ban Word Detected. => "+word+" <=\nThe Previous Message :\n"+message.content)
    if message.content.startswith("!play"):
        music_client = await CobraMusic.get_client(message, client)
        await music_client.play(message.content.split()[1])


client.run(token)
