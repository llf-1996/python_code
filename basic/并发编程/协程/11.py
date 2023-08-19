# -*- coding: utf-8 -*-
"""
@Author: llf
@Email: linfeng@karboncard.com
@Time: 2023/08/04
@desc: 
"""
import time
import asyncio

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        return await fetch(session, "http://httpbin.org/headers")


if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    res1 = loop.run_until_complete(main())
    print(res1)
    print(time.time() - t1)
