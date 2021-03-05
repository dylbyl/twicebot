# bot.py
import sys, os
from numpy import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#current size 39
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
        'https://media2.giphy.com/media/W02KJMd0xRj21zeq3K/200w.webp?cid=ecf05e478sq4now4fkgouv6omqrjsydqdv9yhy01ss0o5y8c&rid=200w.webp',
        'https://media.giphy.com/media/eLXadZuZ1hN8AOclZR/giphy.gif',
        'https://media.tenor.com/images/bb5ae136c9dc3de7b9757cf2a156b460/tenor.gif',
        'https://media.giphy.com/media/kEoguATlRXPLHRTaY8/giphy.gif',
        'https://media.giphy.com/media/xLI6yofqY6hzO/giphy.gif',
        'https://media.giphy.com/media/l1Asyt8E4bw5zAZS8/giphy.gif',
        'https://media.giphy.com/media/3ofT5YwTXNXZJDlS5a/giphy.gif',
        'https://media.giphy.com/media/3ofT5YKxH7fS4vsNQk/giphy.gif',
        'https://media.giphy.com/media/hqm43RkgSjWin0KkO3/giphy.gif',
        'https://media.giphy.com/media/U6e8oEzVPH8j01UUiD/giphy.gif',
        'https://media.giphy.com/media/Qrcs9WG2ZlPvOdNSqO/giphy.gif',
        'https://media.giphy.com/media/lmuX8VzZqm2Ostyh7b/giphy.gif',
        'https://media.giphy.com/media/xUySTtPKh79lZVQ93i/giphy.gif',
        'https://media.giphy.com/media/hWGi1kHpWycSSpfTmu/giphy.gif',
        'https://media.giphy.com/media/3ofT5VgD5NOgKbYlna/giphy.gif',
        'https://media.giphy.com/media/JsQX89yt6toWPFHrb8/giphy.gif',
        'https://media.giphy.com/media/hV6z5HJfJ14VjGKwSt/giphy.gif',
        'https://media.giphy.com/media/Kb5AssJPAutnvwwpbV/giphy.gif',
        'https://media.giphy.com/media/xUySTXCrUBCNEA5lGE/giphy.gif',
        'https://media.giphy.com/media/UWmerXS1W8h7CML7tG/giphy.gif',
        'https://media.giphy.com/media/JsKdu4ikYSoxaAhJOB/giphy.gif',
        'https://media.giphy.com/media/TIFCfyNwKlus4oGzuk/giphy.gif',
        'https://media.giphy.com/media/c8En1CeEuqRri/giphy.gif',
        'https://media.giphy.com/media/eLXadZuZ1hN8AOclZR/giphy.gif',
        'https://media.giphy.com/media/eMgVjuhiwq5USE3icW/giphy.gif',]

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

    if "twice" in message.content.lower():
        x = random.randint(39)
        twice_response = f'DID SOMEBODY SAY TWICE?!\n{gifs[x]}'
        await message.channel.send(twice_response)
        
client.run(TOKEN)
