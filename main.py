import discord
import os
import aiohttp
import io


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(s in message.content.lower() for s in ['ramen','@r4m3n']):
        async with aiohttp.ClientSession() as session:
             async with session.get("https://www.kwestiasmaku.com/sites/v123.kwestiasmaku.com/files/tantanmen-ramen-00.jpg") as resp:
                if resp.status != 200:
                    return
                data = io.BytesIO(await resp.read())
                await message.channel.send(file=discord.File(data, filename="tantanmen-ramen-00.jpg"))
    if 'bieda' in  message.content or 'biede' in  message.content or 'bogactwo' in  message.content:
        await message.channel.send(
            "JEBAĆ BIEDE! WSZYSCY ZA JEDNEGO! BIEDA BIEDA BIEDA!")
        await message.channel.send(
            '$botify play https://www.youtube.com/watch?v=fQyg-dk_D94'
        )

client.run(os.getenv('TOKEN'))