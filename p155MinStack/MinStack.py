class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)        
        self.size += 1
        i = self.size - 1
        while i >= 1 and self.stack[i] < self.stack[i - 1]:
            self.stack[i], self.stack[i - 1] = self.stack[i - 1], self.stack[i]
            i -= 1
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop(self.size - 1)
        
    def top(self):
        """
        :rtype: int
        """
        if self.size == 0: return 0
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.size == 0: return 0
        return self.stack[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

ms = MinStack()
ms.push(-3)
ms.push(0)
ms.push(-2)
print(ms.getMin())
print(ms.pop())
print(ms.top())