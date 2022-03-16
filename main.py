import discord
import os
import aiohttp
import io
from random import randrange, choice
from serpapi import GoogleSearch
import asyncio
import re

base_image_filename = "sad-ramen.jpg"
base_shreck_filename = "shreck.jpg"
rychu_creations = ["https://www.youtube.com/watch?v=M1yBJDNAwsw",
                   "https://www.youtube.com/watch?v=pAC40NDo2yQ",
                   "https://www.youtube.com/watch?v=r4CCReGjWMI",
                   "https://www.youtube.com/watch?v=qP1IfZj3mi8",
                   "https://www.youtube.com/watch?v=tmPr1dSP_hY",
                   "https://www.youtube.com/watch?v=xBs1yi6I5bY"]
ramen_pics = {}
shreck_pics = {}
with open(base_image_filename, "rb") as f:
    ramen_pics[base_image_filename] = f.read()

with open(base_shreck_filename, "rb") as f:
    shreck_pics[base_shreck_filename] = f.read()


def single_letters(s):
    return re.sub(r'(\d)\1+', r'\1', s)


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


async def get_pics_shreck():
    async with aiohttp.ClientSession() as session:
        try:
            search = GoogleSearch({
                "q": "shrek",
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
                        name = "shreck"+str(len(shreck_pics))+"."+ext
                        shreck_pics[name] = data
                except Exception as e:
                    print("failed to download image XD", e)
                if len(shreck_pics) >= 20:
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

    msg_lower = single_letters(message.content.lower())
    if any(s in msg_lower for s in ['ramen', '@r4m3n']):
        c = choice(list(ramen_pics))
        await message.channel.send(file=discord.File(io.BytesIO(ramen_pics[c]), filename=c))
        return

    if any(s in msg_lower for s in ['shreck', 'shrek', 'love']):
        c = choice(list(shreck_pics))
        await message.channel.send(file=discord.File(io.BytesIO(shreck_pics[c]), filename=c))
        return

    if any(s in msg_lower for s in ['bieda', 'biede', 'bogactwo']):
        await message.channel.send(
            "JEBAĆ BIEDE! WSZYSCY ZA JEDNEGO! BIEDA BIEDA BIEDA!")
        await message.channel.send(
            '$botify play https://www.youtube.com/watch?v=fQyg-dk_D94'
        )
        return
    if any(s in msg_lower for s in ['harnold', 'harnaś', 'harnas', 'radler']):
        await message.channel.send(
            "leje harnolda z puchy :axe:\n" +
            "https://www.youtube.com/watch?v=3dHpEfmegOA\n")

    if any(s in msg_lower for s in ['rychu', 'ryszy']):
        await message.channel.send(
            "wszystko na mój koszt panowie!\n" +
            choice(rychu_creations))
asyncio.run(get_pics())
asyncio.run(get_pics_shreck())
client.run(os.getenv('TOKEN'))
