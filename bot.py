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
        'https://media.giphy.com/media/eMgVjuhiwq5USE3icW/giphy.gif',
        'https://64.media.tumblr.com/3720c0649a55983b5b27091baa2b3b80/483f2bd418b6dd35-9b/s400x600/3aae114321e08ea0359f644a7cf3f8cb1b7a26b8.gifv',
        'https://64.media.tumblr.com/f12291e8998fd5d37ada36993eabe8b6/304ab7d9334aa727-34/s1280x1920/ba166de5c3e719ded0b5f96cfe157f24fbede804.jpg',
        'https://64.media.tumblr.com/d6432c1425ed45ac3475894d4c781c49/70b5ac379d0d5f68-20/s400x600/7a4df21aa3866543c543e0da881d9d758fb8d91a.png',
        'https://64.media.tumblr.com/e972fb1cfbe8312007687129dda45852/d15207c9b8b5a99d-4a/s540x810/b76f4e3bbadec14126e57a35db108aba18be62c4.gifv',
        'https://64.media.tumblr.com/f60d04d8cbdb1eea999c1b5b61aa87f5/a5719cdd50b07585-18/s540x810/3030c36c9320640c80b0c912d05c6763621fe24a.gifv',
        'https://64.media.tumblr.com/a7b14f89ca955bee07bf74972b7bd18e/361712c5e589935a-5a/s250x400/01ac777eaa1953777bef9f4091d65e4a01ba7d80.gifv',
        'https://64.media.tumblr.com/43dc22e16228e20ce582196d64b6f966/361712c5e589935a-e8/s250x400/a6f85a745dc2f42945db13c2fb1ee6b20e69ce2a.gifv',
        'https://64.media.tumblr.com/0dade6ce0328344f97b8e594c06d53c7/361712c5e589935a-7f/s250x400/f4eb0805f201d1b28ae10711dec5a4acf959b2b9.gifv',
        'https://64.media.tumblr.com/f063053ba40e2135c8ef1b0acd9cd61f/a9518aed49d88f69-f1/s1280x1920/718f3240a7a48ecb8db5178829eb61a7873e6d67.jpg',
        'https://i.giphy.com/media/UthjTg3TUPDZHFpTVG/200w.webp',
        'https://media3.giphy.com/media/USDLzEBaDObgWuWywy/200w.webp?cid=ecf05e47m3sgtrwfe9ql29ye75pcystc0nnfd0aod13gnmkj&rid=200w.webp&ct=g',
        'https://i.giphy.com/media/L2wFxr0ptAW06oQSlE/200w.webp',
        'https://64.media.tumblr.com/674fec8a19332cdf495a517bf912bab4/8cbd38afb32ebf1a-1c/s540x810/8f112de30862a47cd0a2a164f1dadd735e25c260.gifv',
        'https://media1.giphy.com/media/JOdKVJrzO3KkZXmCKz/200w.webp?cid=ecf05e47k7gx36p0g5eeo5a9zbbgbj8v632q97mq0ou95qd1&rid=200w.webp&ct=g',
        'https://media2.giphy.com/media/g8uAoUma06vpjqqEjZ/200w.webp?cid=ecf05e47k7gx36p0g5eeo5a9zbbgbj8v632q97mq0ou95qd1&rid=200w.webp&ct=g',
        'https://media1.giphy.com/media/lQ7jg6uIclUGTbUQJ8/200w.webp?cid=ecf05e47k7gx36p0g5eeo5a9zbbgbj8v632q97mq0ou95qd1&rid=200w.webp&ct=g',
        'https://media1.giphy.com/media/3ofSBkhaoNiUqSI1y0/200w.webp?cid=ecf05e47k7gx36p0g5eeo5a9zbbgbj8v632q97mq0ou95qd1&rid=200w.webp&ct=g',
        'https://media0.giphy.com/media/vqR16AFKwGMM8jtOa1/200w.webp?cid=ecf05e47k7gx36p0g5eeo5a9zbbgbj8v632q97mq0ou95qd1&rid=200w.webp&ct=g',
        'https://media2.giphy.com/media/G26Ixeq8GrsEmRw37S/200w.webp?cid=ecf05e47k7gx36p0g5eeo5a9zbbgbj8v632q97mq0ou95qd1&rid=200w.webp&ct=g',
        'https://media1.giphy.com/media/MG2yG0e5g42JO8URxP/200w.webp?cid=ecf05e47k7gx36p0g5eeo5a9zbbgbj8v632q97mq0ou95qd1&rid=200w.webp&ct=g',
        'https://media4.giphy.com/media/1LYZH90P7R2SoIYdoM/200w.webp?cid=ecf05e47k7gx36p0g5eeo5a9zbbgbj8v632q97mq0ou95qd1&rid=200w.webp&ct=g',]

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
        x = random.randint(len(gifs))
        twice_response = f'DID SOMEBODY SAY TWICE?!\n{gifs[x]}'
        await message.channel.send(twice_response)
        
client.run(TOKEN)
