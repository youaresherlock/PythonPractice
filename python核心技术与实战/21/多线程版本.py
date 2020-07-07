#!usr/bin/python
# -*- coding:utf8 -*-
"""
Python实现多线程/多进程，大家常常会用到标准库中的threading和multiprocessing模块。
但从Python3.2开始，标准库为我们提供了concurrent.futures模块，它提供了ThreadPoolExecutor
和ProcessPoolExecutor两个类，实现了对threading和multiprocessing的进一步抽象，
使得开发者只需编写少量代码即可让程序实现并行计算
1. Futures 中的 Executor 类，当我们执行 executor.submit(func) 时，它便会安排里面的 func() 函数执行，并返回创建好的 future 实例，以便你之后查询调用
2. Futures 中的方法 done()，表示相对应的操作是否完成——True 表示完成，False 表示没有完成。不过，要注意，done() 是 non-blocking 的，会立即返回结果。
相对应的 add_done_callback(fn)，则表示 Futures 完成后，相对应的参数函数 fn，会被通知并执行调用
3. Futures 中还有一个重要的函数 result()，它表示当 future 完成后，返回其对应的结果或异常。
4. 而 as_completed(fs)，则是针对给定的 future 迭代器 fs，在其完成后，返回完成后的迭代器
"""
import time
import requests
import concurrent.futures


def download_one(url):
    resp = requests.get(url)  # 线程安全的,不会出现race condition
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    """
    多线程并行方式:
    max_workers = min(32, (os.cpu_count() or 1) + 4)
    os.cpu_count()==8 max_workers==12 线程的创建、维护和删除也会有一定的开销
    executor.map()表示对sites中的每一个元素,并发的调用函数download_one()
    """
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     executor.map(download_one, sites)
    """
    多进程并发方式: 
    并行的方式一般用在CPU heavy的场景中,下面的程序并不会提升效率 
    """
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     executor.map(download_one, sites)
    """
    方式三:
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
        for future in concurrent.futures.as_completed(to_do):
            future.result()


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
    ] * 10
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()






























