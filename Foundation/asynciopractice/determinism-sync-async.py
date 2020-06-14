#!usr/bin/python
# -*- coding:utf8 -*-
import time
import random
import asyncio


def task(pid):
    """Synchronous non-deterministic task"""
    time.sleep(random.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


async def task_coro(pid):
    """Coroutine non-deterministic task"""
    await asyncio.sleep(random.randint(0, 2) * 0.01)
    print('Task %s done' % pid)


async def asynchronous():
    tasks = [task_coro(i) for i in range(1, 10)]
    await asyncio.gather(*tasks)


print('Synchronous')
synchronous()

print('Asynchronous')
asyncio.run
"""
Synchronous:
Task 1 done
Task 2 done
Task 3 done
Task 4 done
Task 5 done
Task 6 done
Task 7 done
Task 8 done
Task 9 done
Asynchronous:
Task 4 done
Task 9 done
Task 2 done
Task 3 done
Task 5 done
Task 6 done
Task 8 done
Task 1 done
Task 7 done
"""





















