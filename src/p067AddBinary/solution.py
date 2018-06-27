"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a, b):
        return bin(eval("0b" + a) + eval("0b" + b))[2:]

class Solution1:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_l = list(a)
        b_l = list(b)
        a_l.reverse()
        b_l.reverse()
        i_a, l_a = 0, len(a_l)
        i_b, l_b = 0, len(b_l)
        tag = 0
        res = []
        while (i_a < l_a) or (i_b < l_b) or (tag != 0):
            if i_a < l_a:
                tag += int(a_l[i_a])
                i_a += 1
            if i_b < l_b:
                tag += int(b_l[i_b])
                i_b += 1
            res.append(str(tag % 2))
            tag //= 2
        res.reverse()
        return ''.join(res)


if __name__ == '__main__':
    print (Solution().addBinary("11", "1"))
    print (Solution().addBinary("110", "1"))
    print (Solution().addBinary("110", "11"))
