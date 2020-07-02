#!usr/bin/python
# -*- coding:utf8 -*-
"""
python3.5用于定义协程的关键字async/await,async定义一个协程, await用于
挂起阻塞的异步调用接口
"""
"""
import time
import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    for url in urls:
        # await是同步调用, crawl_page(url)在当前的调用结束之前, 是不会触发下一次调用的
        await crawl_page(url)

start = time.perf_counter()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
end = time.perf_counter()
print(end - start)
"""
import time
import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # *tasks解包列表, 将列表变成了函数的参数
    await asyncio.gather(*tasks)
    # for task in tasks:
    #     await task

start = time.perf_counter()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
end = time.perf_counter()
print(end - start)
























