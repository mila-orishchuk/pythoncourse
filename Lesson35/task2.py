'''
Requests using asyncio and aiohttp

Download all comments from a subreddit of your choice using URL:
https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and 
dump it to a file. For this task use asyncio and aiohttp libraries
for making requests to Reddit API.'''


from time import time
import os
import asyncio
import aiohttp
import aiofiles
import requests

URL = 'https://api.pushshift.io/reddit/comment/search'
FILE = 'comments.json'

time_per_subr = {}
subreddits = ['politics', 'teenagers']
loop = asyncio.get_event_loop()


async def proceed_subredit(subreddit):
    async with aiohttp.TCPConnector(ssl=False, loop=loop) as connector:
        params = {'size': 5, 'subreddit': subreddit,
                  'fields': ('author', 'body', 'created_utc', 'subreddit')}
        async with aiohttp.ClientSession(loop=loop, connector=connector).get(
                URL, params=params) as response:
            data = await response.text()
            async with aiofiles.open(FILE, 'a') as file:
                await file.write(data)
                await file.write(',\n')


async def main():
    args = [proceed_subredit(subreddit) for subreddit in subreddits]
    await asyncio.gather(*args, loop=loop)


if __name__ == '__main__':
    loop.run_until_complete(main())
    loop.close()
