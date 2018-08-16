#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cocomilk'



import orm,asyncio
from models import User,Blog,Comment

async def test(loop):
    await orm.create_pool(loop,user='cocomilk',password='123123',db='awesome')
    u=User(name='Test',email='test@example.com',passwd='123456789',image='about:blank')
    await u.save()

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop),]))
loop.run_forever()