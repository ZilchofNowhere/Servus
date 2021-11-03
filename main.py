import discord
import random
import time
from discord.ext import commands
import datetime
import os

client = discord.Client()
client = commands.Bot(command_prefix=",", case_insensitive=True)

#kümeler
sad_words = ["sad", "niye ben"]
starter_encouragements = [
    "Mutlu olmanızı emrediyorum",
    "Mutsuz olmanız yasaklanmıştır",
    "Üzülme"
]
insults = ["noob", "çomar", "newi"]
hatır = ["nasılsın", "ne yapıyon","napıyon"]
ölüm = ["öl", "vefat", "geber"]
gay = [
    "how gay is aek",
    "how gay is arda eren",
    "how gay is @Chancelier Palpatine", #bozuk
    "how gay is arda",   
]
smart = [
    "how smart is aek",
    "how smart is arda eren",
    "how smart is @Chancelier Palpatine", #bozuk
    "how smart is arda",
]
evalarray = ["sfac"]

#botun hazır olduğunu belirten şey
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Domino ei bonus servus esse"))
    print("We have logged in as {0.user}".format(client))

#eventler
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    yaz = message.channel.send

    async def filter(x, y):
        if msg.startswith(x):
            await message.channel.send(y)

    if msg.startswith("$hello"):
        await message.channel.send("Hello!")
    
    if message.author.id == 643477588022657035:
        return

    if any(word in msg for word in insults):
        await message.channel.send("Mazlumlar korumam altındadır :angry: (uğur hariç, uğur gerçek bir noobtur)")
    
    if msg.startswith("hoş geldin bot"):
        await message.channel.send("Hoş buldum")
    
    if any(word in msg for word in hatır):
        await message.channel.send("İyiyim elhamdülillah")
    
    if message.channel.id == 796626374181388308: 
        await message.channel.send('<@634136510375002143>')
    
    await(filter("yaşasın", f"Heeey, sevindiğinize çok sevindim <@{message.author.id}>!"))
    
    if any(word.lower() in msg for word in ölüm):
        await message.channel.send("RIP :pensive:")
    
    n = random.randint(0, 100)
    if any(word in msg for word in gay):
        await message.channel.send("Sorduğunuz kişi %0 gay")
    elif msg.startswith("how gay is"):
        await message.channel.send(f"Sorduğunuz kişi %{n} gay")

    iq = random.randint(10, 300)
    if any(word in msg for word in smart):
        await message.channel.send("Sorduğunuz kişinin iqsu 300 puan")
    elif msg.startswith("how smart is"):
        await message.channel.send(f"Sorduğunuz kişinin iqsu {iq} puan")

    if msg.startswith("hack"):
        mesaj = await message.channel.send("Belirlenen kurbanın hacki başlatıldı")
        time.sleep(2)
        await mesaj.edit(content="Banka hesapları ele geçirildi ve parası Çiftlikbank'a yatırıldı")
        time.sleep(2)
        await mesaj.edit(content="Steam hesabı sıfırlandı")
        time.sleep(2)
        await mesaj.edit(content="Son oynadığı oyunda herkesten küfür yediği belirlendi")
        time.sleep(2)
        await mesaj.edit(content="Bilgisayarına Creeper virüsü yüklendi ve antivirüsü devre dışı bırakıldı")
        time.sleep(2)
        await mesaj.edit(content="Hack tamamlandı")

    await(filter("ayb", "Ayıp tabi"))
    await(filter("günaydın", f"Sağ ol <@{message.author.id}>"))
    
    if message.channel.id == 834836887998169118 and message.author.id == 751512679394312313:
        return
        await message.channel.purge(limit=1)
    elif message.channel.id == 834836887998169118 and message.author.id == 634136510375002143:
        return
        await message.channel.purge(limit=1)
    elif message.channel.id == 834836887998169118 and msg == "":
        return
    elif message.channel.id == 834836887998169118:
        await message.channel.send(msg)  

    if msg.startswith("del"):
        await message.channel.purge(limit=2)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))    
   
    """
    if any(word in msg for word in evalarray) and message.author.id != 789137363346784306:
        return
    elif msg.startswith("sfac"):
        await message.channel.send(eval(msg.lstrip("sfac")))
"""

    await(filter("!crusade", "Sorry, MEE6 is dead :pensive:\nBut maybe <@484438480773054485> could give you the role"))
    await(filter("favori charın ne", "Tabii ki Kartheon"))
    await(filter("ping", f"Pinginiz {round(client.latency * 1000)} ms"))

    await client.process_commands(message)
    
#komutlar
@client.command()
async def beep(ctx):
    await ctx.send("Boop!")

@client.command(name="servushelp")
async def _help(ctx):
    embedVar = discord.Embed(title="İşte mevcut komutlar", description="Daha fazla komut için takip edip like atmayı unutmayın", color=0x00c18e)
    embedVar.add_field(name="how gay", value="Arkadaşınız ne kadar gay :rainbow_flag:", inline=False)
    embedVar.add_field(name="how smart", value="Arkadaşınız ne kadar akıllı :brain:", inline=False)
    embedVar.add_field(name="hack", value="Sunucudakilere küçük ve tatsız sürprizler yapın :keyboard:", inline=False)
    embedVar.add_field(name="bot rickroll", value="We do a little trolling :slight_smile:", inline=False)
    embedVar.add_field(name="del", value="Mesaj silmek için butona gerek yok artık", inline=False)
    embedVar.add_field(name="crusade", value="Kutsal topraklara bir yolculuk... :sword:", inline=False)
    embedVar.add_field(name="ping", value="Gecikmenizi öğrenin", inline=False)
    embedVar.add_field(name="bot beep", value="Botun hayatta olduğundan emin olun :heart:", inline=False)
    embedVar.add_field(name="bot parrot", value="Botunuz niye bir papağan olmasın ki :parrot:", inline=False)
    embedVar.add_field(name="bot info", value="Sunucunuz hakkında biraz bilgi edinin", inline=False)
    await ctx.send(embed=embedVar)

@client.command()
async def rickroll(ctx):
    await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO")

@client.command()          #birden fazla kelimeyse tırnakla
async def parrot(ctx, arg):
    await ctx.send(arg)

@client.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="İşte bulunduğunuz server hakkında bilgiler ", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/823498531728785418/0d53ca06a4afb085ba7fb6b712e65164.png?size=128")
    await ctx.send(embed=embed)
    
    
@client.command()
async def exec(ctx, *, arg):
    os.system(f"{arg} > ./exec.txt")
    with open("./exec.txt", "r") as exec:
        await ctx.send(exec.read())


#bitiş
client.run("ODIzNDk4NTMxNzI4Nzg1NDE4.YFhsxQ.uIrEf-YC0FAZG5_c9m_C3mm75Y4")
