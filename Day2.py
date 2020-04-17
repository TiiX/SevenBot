import discord
import asyncio
import CobraMusic

from discord_token import *
import ban_words as b_w
from discord_xp import *
from discord_admins import *

#Token
print(token_id)

##ws_url = 'ws://Guesser-Cluster.scoder12.repl.co'
##guess_url = 'https://guess-it.scoder12.repl.co/guess'

client = discord.Client()

print("Initial XP")
print(xp)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("!help if you need"))
    print("Seven Loaded.")  
    
@client.event
async def on_message(message):

    #Create Admins
    if message.author != client.user and message.author.id == admins[0]:
        if message.content.startswith("!admin"):
            if message.content.split()[1] == "add":
                admins.append(message.content.split()[2])

    if message.author.id in admins and message.content == "!blue":
        await message.channel.send("Blue is Life.")

    #Ban words
    if message.author != client.user and message.author.id in admins:
        if message.content.startswith("!admin"):
            if message.content.split()[1] == "ban" and message.content.split()[2] == "word":
                ban_w = b_w.BAN_WORDS
                if message.content.split()[3] in ban_w:
                    pass
                else:
                    ban_w.append(message.content.split()[3])
                    f = open("ban_words.py","w")
                    f.write("BAN_WORDS = {}".format(ban_w))
                    f.close()
                    
            #ADMIN HELP
            if message.content.split()[1] == "help":
                em = discord.Embed(title="ADMIN COMMANDS",color = 0x424242)
                em.add_field(name="!admin ban word [word]",value="Add the word to the BAN_WORDS list",inline=False)
                em.add_field(name="!admin add [id]",value="Add an admin",inline=False)
                em.add_field(name="!bark",value="BAAAARK !!!",inline=False)
                em.add_field(name="!ntm",value="Notre chere marine...",inline=False)
                em.add_field(name="!saad",value="SO SAAAD.",inline=False)
                em.add_field(name="!daah",value="FUS ROH DAH !!",inline=False)
                em.add_field(name="!elevator",value="God power.",inline=False)
                em.add_field(name="!punch",value="Just a 'Thank you'",inline=False)
                em.add_field(name="!blyaat",value="My dear ears. Good luck...",inline=False)
                em.add_field(name="!crickets",value="...",inline=False)
                em.add_field(name="!one punch",value="Did i really need to explain ?",inline=False)
                em.add_field(name="!directed by",value="Directed by Robert B. Weide.",inline=False)
                await message.author.send(embed=em)

        #Sound Bank
        if message.content == "!bark":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://youtu.be/qMPpnCvCZvw")
            await message.channel.send("BAAAAAARK !!!")

        if message.content == "!ntm":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://www.youtube.com/watch?v=YlXBpLjSSMc")

        if message.content == "!saad":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://www.youtube.com/watch?v=BfyXK4KwyYA&")

        if message.content == "!daah":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://youtu.be/zzH_Wn0R-yo")

        if message.content == "!elevator":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://www.youtube.com/watch?v=xy_NKN75Jhw&")

        if message.content == "!punch":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://www.youtube.com/watch?v=OZdIbJZdSZw&")

        if message.content == "!blyaat":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://youtu.be/9nQ-PXHV6nw")

        if message.content == "!crickets":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://www.youtube.com/watch?v=CpGtBnVZLSk&")

        if message.content == "!one punch":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://www.youtube.com/watch?v=qVdo8C8HWRo")

        if message.content == "!directed by":
            music_client = await CobraMusic.get_client(message, client)
            await message.channel.send("Directed by Robert B. Weide")
            await music_client.play("https://www.youtube.com/watch?v=X-KwYX2u8e4")

        if message.content == "!crab rave":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://www.youtube.com/watch?v=1IY9lRTGaYE")

        if message.content == "!im blue":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play("https://www.youtube.com/watch?v=NNvuHltfTWo")

        
    

    #print(message.author.id)

    #Presentation
    if message.author != client.user:
        if message.content == "!hello":
            member_name = message.author.name
            guild_name = message.guild.name
            new_msg = await message.channel.send("Bonjour "+member_name+" et bienvenue sur "+guild_name+".")

    
    if message.content.startswith("!why seven") and message.author.id in admins:
        if message.content.split()[2] == "42":
            if message.content.split()[3] == "help":
                await message.channel.send("")
            em = discord.Embed(Title="Ya claime the first one !", description="First step. Good. Now, what is the next one ?", inline=False)
            em.add_field(name="Need Help ?", value="Then type !why seven 42 help", inline=False)
            await message.channel.send(embed=em)
        
        else:
            await message.channel.send("I'm a secret. So find why. (Hint : Division and Hexcolor)")

    if message.author != client.user:    
        if message.content == "!me":
            member_name = message.author.name

            for member in xp:
                member_id = message.author.id
                if member[0] == member_id:
                    member_xp = member[1]
            if message.author.id == admins[0]:
                deos_color = 0x424242            
                em = discord.Embed(title=member_name.upper(), color=deos_color)
            else:
                em = discord.Embed(title=member_name, color=0xFF0000)
            if message.author.id == admins[0]:
                em.add_field(name="Ton Niveau :", value="dieu.", inline=True)
            else:
                em.add_field(name="Ton Niveau :", value=str(member_xp//42), inline=True)
                em.add_field(name="XP :", value=str(member_xp), inline=False)
            
            await message.channel.send(embed=em)
            
    if message.author != client.user:
        for word in b_w.BAN_WORDS:
            if word in message.content.lower():
                print("WARNING : Ban Word Detected.")
                await message.channel.send("WARNING : Ban Word Detected for "+message.author.name)
                await message.delete()
                await message.author.send("Ban Word Detected. => "+word+" <=\nThe Previous Message :\n"+message.content)

    #Help
    if message.content.startswith("!help"):
        em = discord.Embed(title="Help !", color = 0x424242)
        em.add_field(name="!hello", value="Say hi to Seven !", inline=False)
        em.add_field(name="!play [URL]", value="Playing the music", inline=False)
        em.add_field(name="!stop", value="Stop the music", inline=False)
        em.add_field(name="!resume", value="Restart the music from where he was stopped", inline=False)
        em.add_field(name="BECARFUL !",value="Wait for the current music playing until his stop to start another one !", inline = False)
        em.add_field(name="!me", value="Show me how ya get with talking !", inline=False)
        em.add_field(name="!xp", value="Level Up !", inline=False)
        if message.author.id in admins:
            em.add_field(name="!admin help", value="Only for the family ~")
            em.add_field(name="Secret 1 :", value="!why seven", inline=False)
        await message.author.send(embed=em)
        await message.channel.send("The list of commands you have access to has been sent to your DMs.")

    #Music
    if message.author != client.user and message.author.id in admins:
        if message.content.startswith("!play"):
            music_client = await CobraMusic.get_client(message, client)
            await music_client.play(message.content.split()[1])
            await message.channel.send("Music started ~")

        if message.content.startswith("!stop"):
            music_client = await CobraMusic.get_client(message, client)
            await music_client.pause()
            await message.channel.send("Music stopped.")

        if message.content == "!resume":
            music_client = await CobraMusic.get_client(message, client)
            await music_client.resume()
            await message.channel.send("Music resumed ~")
            
    #XP +1
    member_find = 0
    for member in xp:
        member_id = message.author.id
        if member[0] == member_id:
            member[1] += 1
            member_find = 1
            
    if member_find == 0:
        xp.append([member_id, 1])

    #Debug
    #print(xp)

    #Fct XP
    if message.author != client.user:
        if message.content == "!xp":
            member_name = message.author.name

            for member in xp:
                member_id = message.author.id
                if member[0] == member_id:
                    member_xp = member[1]
                            
            em = discord.Embed(title="Ton Nom", description=member_name, color=0xFF0000,
                               timestamp=message.created_at)
            
            em.add_field(name="XP :", value=str(member_xp), inline=True)
            
            await message.channel.send(embed=em)

    #Save for the XP
    f = open("discord_xp.py","w")
    f.write("xp = {}".format(xp))
    f.close()
        
    
client.run(token_id)
