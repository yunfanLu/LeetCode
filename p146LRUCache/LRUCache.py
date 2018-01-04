class LRUCache:
    class Node:
        def __init__(self, k=None, v=None, l=None, r=None):
            '''
            :param v: value of this node
            :param l: left node
            :param r: right node
            '''
            self.k = k
            self.l = l
            self.r = r
            self.v = v

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.map = {}

        self.beg = self.Node()
        self.end = self.Node()
        self.beg.r = self.end
        self.end.l = self.beg

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if (key in self.map) is False: return -1
        node = self.map[key]

        node.l.r = node.r
        node.r.l = node.l

        node.l = self.beg
        node.r = self.beg.r
        node.l.r = node
        node.r.l = node

        return node.v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            node = self.map[key]
            node.v = value
            node.l.r = node.r
            node.r.l = node.l
            node.l = self.beg
            node.r = self.beg.r
        else:
            node = self.Node(k=key, v=value, l=self.beg, r=self.beg.r)
            self.size += 1

        node.l.r = node
        node.r.l = node
        self.map[key] = node

        if self.size > self.capacity:
            self.delete_end(self.end.l)
            self.size -= 1

    def delete_end(self, node):
        node.l.r = node.r
        node.r.l = node.l
        del self.map[node.k]

    def printf(self):
        print("*" * 10 + ' size : {}'.format(self.size))
        node = self.beg.r
        while node != self.end:
            print(node.k, " : ", node.v)
            node = node.r

    def clear(self):
        self.map.clear()
        item = self.beg.r

        while item != self.end:
            del_item = item
            item = item.r
            del del_item

        self.beg.r = self.end
        self.end.l = self.beg
        self.size = 0


if __name__ == '__main__':
    '''
    ["LRUCache","put","put","put","put","get","get"]
    [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
    '''

    ca = LRUCache(2)
    ca.put(2,1)
    ca.printf()
    ca.put(1,1)
    ca.printf()
    ca.put(2,3)
    ca.printf()
    ca.put(4,1)
    ca.printf()
    print(ca.get(1))
    print(ca.get(2))

    # '''
    # ["LRUCache","get","put","get","put","put","get","get"]
    # [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
    # '''
    #
    # ca = LRUCache(2)
    # ca.printf()
    # print(ca.get(2))
    # ca.put(2,6)
    # ca.printf()
    # print(ca.get(1))
    # ca.put(1,5)
    # ca.printf()
    # ca.put(1,2)
    # ca.printf()
    # print(ca.get(1))
    # print(ca.get(2))


    # ca = LRUCache(2)
    # ca.put(1, 1)
    # ca.printf()
    # ca.put(2, 2)
    # ca.printf()
    # ca.get(2)
    # ca.printf()
    # ca.get(1)
    # ca.printf()
    # ca.put(3, 3)
    # ca.printf()
    # ca.put(4, 4)
    # ca.printf()
    # print(ca.get(1))
    #
    # print('-' * 10)
    # ca.clear()
    # ca.printf()
    # ca.put(2, 1)
    # ca.printf()
    # ca.put(2, 2)
    # ca.printf()
    # print(ca.get(2))
    # ca.printf()
    # ca.put(1, 1)
    # ca.printf()
    # ca.put(4, 1)
    # ca.printf()
    # print(ca.get(2))
    # ca.printf()
