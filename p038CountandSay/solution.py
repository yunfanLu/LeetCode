'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        foo = '1' + '$'
        for i in range(1,n):
            bar = ''
            cnt = 1
            for j in range(len(foo) - 1):
                if foo[j] == foo[j + 1]:
                    cnt += 1
                else:
                    bar += str(cnt) + foo[j]
                    cnt = 1
            foo = bar + '$'
        return foo[0:-1]

ss = Solution()
print(ss.countAndSay(1))
print(ss.countAndSay(2))
print(ss.countAndSay(3))
print(ss.countAndSay(4))
print(ss.countAndSay(5))
print(ss.countAndSay(6))
