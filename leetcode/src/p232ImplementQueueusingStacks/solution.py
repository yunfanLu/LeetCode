# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 08:36
# @Author  : yunfan

class MyQueue:
    """
    ONLY CAN USE APPEND AND POP
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.a.append(x)

    def _a_to_b(self):
        if len(self.b) == 0:
            for i in range(len(self.a)):
                t = self.a[-1]
                self.a.pop()
                self.b.append(t)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self._a_to_b()
        r = self.b[-1]
        self.b.pop()
        return r

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self._a_to_b()
        return self.b[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.a) + len(self.b) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()