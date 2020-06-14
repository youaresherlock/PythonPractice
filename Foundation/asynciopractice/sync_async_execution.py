#!usr/bin/python
# -*- coding:utf8 -*-
import asyncio


async def foo():
    print('Running in foo')
    await asyncio.sleep(0)
    print('Explicit context switch to foo again')


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Implicit context switch back to bar')


async def main():
    tasks = [foo(), bar()]
    await asyncio.gather(*tasks)


asyncio.run(main())
"""
Running in foo
Explicit context to bar
Explicit context switch to foo again
Implicit context switch back to bar
"""



























































