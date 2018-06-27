"""
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""


class Solution1:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n > 0:
            res.append(chr(((n - 1) % 26) + ord('A')))
            n = (n - 1) // 26
        res.reverse()
        return "".join(res)

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return '' if n == 0 else self.convertToTitle((n - 1) // 26) + \
                                chr((n - 1) % 26 + ord('A'))

if __name__ == '__main__':
    print (Solution().convertToTitle(1))
    print (Solution().convertToTitle(2))
    print (Solution().convertToTitle(26))
    print (Solution().convertToTitle(27))
    print (Solution().convertToTitle(701))