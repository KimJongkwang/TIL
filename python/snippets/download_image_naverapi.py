import os
import time
import sys
import asyncio
import aiohttp
import aiofiles

from config import get_secret # json KEY loader

"""
env: python3.7, aiohttp: 3.7.3, aiofiles: 0.7.0

execute: python3 download_image_naverapi.py "keyword" "Number of Pages"
"""


async def img_downloader(session, img):
    img_name = img.split('/')[-1].split('?')[0]

    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    async with session.get(img) as response:
        if response.status == 200:
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                img_data = await response.read()
                await file.write(img_data)

async def fetch(session, url):
    headers = {
        "X-Naver-Client-Id": get_secret('NAVER_API_ID'), # NAVER API ID
        "X-Naver-Client-Secret": get_secret('NAVER_API_SECRET') # NAVER API KEY
        }
    async with session.get(url, headers=headers) as response:
        result = await response.json()
        items = result['items']
        images = [item['link'] for item in items]
        await asyncio.gather(*[img_downloader(session, img) for img in images])

async def main(keyword, pagenum):
    BASE_URL = "https://openapi.naver.com/v1/search/image"

    urls = [f"{BASE_URL}?query={keyword}&display=20&start={(i*20)+1}" for i in range(pagenum)]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


if __name__ == "__main__":
    start = time.time()
    keyword, page = sys.argv[1:]
    asyncio.run(main(keyword, int(page)))

    print(round(time.time() - start, 2), "seconds")