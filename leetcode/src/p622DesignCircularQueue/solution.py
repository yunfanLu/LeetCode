# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 14:44
# @Author  : yunfan

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self._queue = [0 for i in range(k)]
        self._head = 0
        self._tail = 0
        self._len = 0
        self._size = k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull() is True:
            return False
        self._queue[self._tail] = value
        self._tail = (self._tail + 1) % self._size
        self._len += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty() is True:
            return False
        self._head = (self._head + 1) % self._size
        self._len -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty() is True:
            return -1
        return self._queue[self._head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty() is True:
            return -1
        return self._queue[(self._tail - 1 + self._size) % self._size]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self._len == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self._len == self._size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()