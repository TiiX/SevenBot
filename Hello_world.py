import discord
import asyncio
ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
guess_url = 'https://guess-it.scoder12.repl.co/guess'

client = discord.Client()

@client.event
async def on_ready():
    print("Seven Loaded.")

@client.event
async def on_message(message):
    if message.content == "!hello":
        await message.channel.send("Hey Humain.")

client.run("NjkzMTE4NTI0NjU4NDE3NzU1.Xn4jng._2ywmiNcH9DHiwDGAptLzfD72h0")
