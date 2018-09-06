# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 08:37
# @Author  : yunfan

class MyStack:
    """
    ONLY CAN USE APPEND AND POP(0), Time COMPE IS TOO HIGHT
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._a = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._a.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        t = self._a[-1]
        self._a.pop()
        return t

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._a[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._a) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()