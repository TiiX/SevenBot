import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("Seven Loaded.")

@client.event
async def on_message(message):
    print(message.content)

client.run("NjkzMTE4NTI0NjU4NDE3NzU1.Xn4bsg.743IZIpQ_bLW5GQTh8lo07HBces")
