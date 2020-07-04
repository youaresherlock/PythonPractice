import asyncio
import aiohttp
import time


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = [
        'http://www.zongheng.com/category/1.html',
        'http://www.zongheng.com/category/3.html',
        'http://www.zongheng.com/category/6.html',
        'http://www.zongheng.com/category/9.html',
        'http://www.zongheng.com/category/15.html',
        'http://www.zongheng.com/category/18.html',
        'http://www.zongheng.com/category/21.html',
        'http://www.zongheng.com/category/40.html',
        'http://www.zongheng.com/rank.html',
        'http://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html',
        'http://search.zongheng.com/s?keyword=%E9%9B%AA%E4%B8%AD%E6%82%8D%E5%88%80%E8%A1%8C'
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()

