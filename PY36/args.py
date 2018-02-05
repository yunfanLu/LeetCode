# -*- coding: utf-8 -*-
# @Time    : 08/01/2018 23:16
# @Author  : yunfan

import numpy

numpy.array()

def fun(a=2,b=3,c=4):
    print(a)
    print(b)
    print(c)

def goo(c,* li,** args):
    print(li)
    print(args['a'])
    print(args['b'])
    print(c)
