#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'cocomilk'


import orm
from models import User,Blog,Comment

def test():
    yield from orm.create_pool(user='cocomilk',password='123123',database='awesome')
    u=User(name='Test',email='test@example.com',passwd='123456789',image='about:blank')
    yield from u.save()

for x in test():
    pass