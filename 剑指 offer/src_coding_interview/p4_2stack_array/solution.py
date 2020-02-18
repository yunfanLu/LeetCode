# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 13:02
# @Author  : yunfan

class Solution:

    def __init__(self):
        self.__push_stake = []
        self.__pop_stake = []

    def push(self, node):
        self.__push_stake.append(node)

    def pop(self):
        if len(self.__pop_stake) == 0:
            ll = len(self.__push_stake)
            for _ in range(ll):
                self.__pop_stake.append(self.__push_stake.pop())
        return self.__pop_stake.pop()

