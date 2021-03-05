# bot.py
import sys, os
from numpy import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#current size 15
gifs = ['https://media1.giphy.com/media/W5TEa73iw1fnSVjjZZ/200w.webp?cid=ecf05e47draafxxzqp7jmcz4w4nkghh3mp7dbmt0shog8isa&rid=200w.webp',
        'https://media4.giphy.com/media/PnaSw04C4NoTuxuJXg/200w.webp?cid=ecf05e47draafxxzqp7jmcz4w4nkghh3mp7dbmt0shog8isa&rid=200w.webp',
        'https://media0.giphy.com/media/Jmg0OCeHfE2YUb88ct/200w.webp?cid=ecf05e47draafxxzqp7jmcz4w4nkghh3mp7dbmt0shog8isa&rid=200w.webp',
        'https://media4.giphy.com/media/xUySTOUTA1QrQOEeje/200w.webp?cid=ecf05e4765shpyv7jze7pg59o6vyapv6pn2rtpjhmz01fzhm&rid=200w.webp',
        'https://media0.giphy.com/media/Zd5UEe6YXuPbtfqKHJ/200.webp?cid=ecf05e47hhr29o9nkez81pijpkszqbfr3ol3t6d09knuz92e&rid=200.webp',
        'https://media0.giphy.com/media/gJnKkHxaHifu1uQjvz/200w.webp?cid=ecf05e47amukxwfygf0vjcnt7mnr33mvhdq5gc7j1k7t0p74&rid=200w.webp',
        'https://media2.giphy.com/media/3ofT5yrCK8VM6rATZe/200w.webp?cid=ecf05e47amukxwfygf0vjcnt7mnr33mvhdq5gc7j1k7t0p74&rid=200w.webp',
        'https://media0.giphy.com/media/3ohuPy9tCuGoHxOumk/200w.webp?cid=ecf05e47amukxwfygf0vjcnt7mnr33mvhdq5gc7j1k7t0p74&rid=200w.webp',
        'https://media2.giphy.com/media/Xeee4HKAFTOwT8eLU4/200w.webp?cid=ecf05e47ommluca13ouilqwrx4j87dhdigp227zzj9j2gl5c&rid=200w.webp',
        'https://media2.giphy.com/media/BIslp4EBz762k/giphy.webp?cid=ecf05e47giypmn6cvzaat4x2149xjhcmk1itrvmporudytwh&rid=giphy.webp',
        'https://media1.giphy.com/media/f94G8pwmmtHkztedwd/200w.webp?cid=ecf05e47giypmn6cvzaat4x2149xjhcmk1itrvmporudytwh&rid=200w.webp',
        'https://media0.giphy.com/media/ns4ICutK9rKu1Em3md/200w.webp?cid=ecf05e47giypmn6cvzaat4x2149xjhcmk1itrvmporudytwh&rid=200w.webp',
        'https://media1.giphy.com/media/QvqnK8LfwTEnatCyTt/200w.webp?cid=ecf05e47giypmn6cvzaat4x2149xjhcmk1itrvmporudytwh&rid=200w.webp',
        'https://media0.giphy.com/media/YMN3au52fbXi44lI81/200.webp?cid=ecf05e47o4u7s4t7qii44yq4e47dcbznh8dcd6rowjj7wh27&rid=200.webp',
        'https://media2.giphy.com/media/W02KJMd0xRj21zeq3K/200w.webp?cid=ecf05e478sq4now4fkgouv6omqrjsydqdv9yhy01ss0o5y8c&rid=200w.webp']

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    print(
        f'{message.author} sent a message\n'
    )
    if message.author == client.user:
        return
    elif "dad bot" in str(message.author).lower():
        return
         
    twice_response = "DID SOMEBODY SAY TWICE?!"

    if "twice" in message.content.lower():
        x = random.randint(15)
        await message.channel.send(twice_response)
        await message.channel.send(gifs[x])
        
client.run(TOKEN)