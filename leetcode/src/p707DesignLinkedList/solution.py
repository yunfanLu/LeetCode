# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 23:11
# @Author  : yunfan

'''

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next
is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev
to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion,
the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the
length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the
node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.

唯一需要注意的是，插入的时候在第 i 个节点前插入即可，i 的范围是 [0, len]，删除的时候删除第 i 个节点，i 的范围是 [0, len)
'''


class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def _current_index(self, index):
        return index <= self.len

    def _get_node(self, index):
        """
        起始为 0 ，拿到第 index 个 node，第 self.len 个 node 是 self.tail
        :param index:
        :return:
        """
        node = self.head.next
        for i in range(0, index):
            node = node.next
        return node

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self._current_index(index) is False:
            return -1
        return self._get_node(index).val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.addAtIndex(self.len, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,
        the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if self._current_index(index) is False:
            return
        node = self._get_node(index)
        new_node = Node(val, node, node.prev)
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self.len += 1


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.len:
            return
        node = self._get_node(index)
        print(node.val)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.len -= 1

    def to_string(self):
        res = ''
        node = self.head.next
        while node is not self.tail:
            res += '-' + str(node.val)
            node = node.next
        return res


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
1
13
213
2
13
1
"""
