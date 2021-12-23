import discord
import os
import aiohttp
import io
from random import randrange, choice
from serpapi import GoogleSearch
import asyncio

base_image_filename = "sad-ramen.jpg"
ramen_pics = {}
with open(base_image_filename, "rb") as f:
    ramen_pics[base_image_filename] = f.read()


async def get_pics():
    async with aiohttp.ClientSession() as session:
        try:
            search = GoogleSearch({
                "q": "ramen",
                "api_key": os.getenv('SERAPI_SECRET'),
                "tbm": "isch",
                "jin": randrange(2137)
            })
            for image_result in search.get_dict()['images_results']:
                url = image_result["original"]
                ext = url.split(".")[-1].split("?")[0]
                if len(ext) > 4:
                    continue
                try:
                    async with session.get(url) as resp:
                        if resp.status != 200:
                            continue
                        data = await resp.read()
                        name = "ramen"+str(len(ramen_pics))+"."+ext
                        ramen_pics[name] = data
                except Exception as e:
                    print("failed to download image XD", e)
                if len(ramen_pics) >= 20:
                    break
        except Exception as e:
            print("failed search images", e)

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(s in message.content.lower() for s in ['ramen', '@r4m3n']):
        # async with aiohttp.ClientSession() as session:
        #      async with session.get("https://www.kwestiasmaku.com/sites/v123.kwestiasmaku.com/files/tantanmen-ramen-00.jpg") as resp:
        #         if resp.status != 200:
        #             return
        #         data = io.BytesIO(await resp.read())
        c = choice(list(ramen_pics))
        await message.channel.send(file=discord.File(io.BytesIO(ramen_pics[c]), filename=c))
        return

    if any(s in message.content.lower() for s in ['bieda', 'biede', 'bogactwo']):
        await message.channel.send(
            "JEBAĆ BIEDE! WSZYSCY ZA JEDNEGO! BIEDA BIEDA BIEDA!")
        await message.channel.send(
            '$botify play https://www.youtube.com/watch?v=fQyg-dk_D94'
        )
        return

asyncio.run(get_pics())
client.run(os.getenv('TOKEN'))
