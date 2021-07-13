
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

__auhoor__='chai'

import asyncio
import orm
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='123', database='awesome')
    a = User(name='Test2', email='test2@example.com', passwd='222222', image='about:blank')
    x = User(name='xian_wen', email='xian_wen@example.com', passwd='1234567890', image='about:blank')
    t = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await a.save()
    await x.save()
    await t.save()
    
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()