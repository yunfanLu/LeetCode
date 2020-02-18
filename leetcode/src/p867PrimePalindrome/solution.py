# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 20:24
# @Author  : yunfan

"""
Find the smallest prime palindrome greater than or equal to N.
Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.
For example, 2,3,5,7,11 and 13 are primes.
Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.
For example, 12321 is a palindrome.

Example 1:
Input: 6
Output: 7

Example 2:
Input: 8
Output: 11

Example 3:
Input: 13
Output: 101

Note:
1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""


class Solution:
    def __get_prime_palindrome(self):
        ii = []
        for i1 in range(10):
            for i2 in range(10):
                for i3 in range(10):
                    for i4 in range(10):
                        b = 0
                        if i1 != 0:
                            b = (((((((i1 * 10 + i2) * 10 + i3) * 10 + i4) * 10 + i4) * 10 + i3) * 10 + i2) * 10 + i1)
                        elif i1 == 0 and i2 != 0:
                            b = ((((((i2) * 10 + i3) * 10 + i4) * 10 + i4) * 10 + i3) * 10 + i2)
                        elif i1 == 0 and i2 == 0 and i3 != 0:
                            b = ((((i3) * 10 + i4) * 10 + i4) * 10 + i3)
                        elif i1 == 0 and i2 == 0 and i3 == 0 and i4 != 0:
                            b = ((i4) * 10 + i4)
                        if b != 0:
                            ii.append(b)
                        print("\nb ", len(str(b)), b)
                        for i5 in range(10):
                            a = 0
                            if i1 != 0:
                                a = ((((((((i1 * 10 + i2) * 10 + i3) * 10 + i4) * 10 + i5) * 10 + i4) * 10 + i3) * 10 + i2) * 10 + i1)
                            elif i1 == 0 and i2 != 0:
                                a = (((((((i2) * 10 + i3) * 10 + i4) * 10 + i5) * 10 + i4) * 10 + i3) * 10 + i2)
                            elif i1 == 0 and i2 == 0 and i3 != 0:
                                a = (((((i3) * 10 + i4) * 10 + i5) * 10 + i4) * 10 + i3)
                            elif i1 == 0 and i2 == 0 and i3 == 0 and i4 != 0:
                                a = (((i4) * 10 + i5) * 10 + i4)
                            print("a ", len(str(a)), a)
                            if a != 0:
                                ii.append(a)
        res = []
        for i in ii:
            if self.isPrime(i):
                res.append(i)
        return sorted(res)

    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2,n):
            if i * i > n:
                return True
            if n % i == 0:
                return False
        return True

    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        prime_palindrome_list = []
        if len(prime_palindrome_list) == 0:
            prime_palindrome_list = self.__get_prime_palindrome()
        print(len(prime_palindrome_list))
        print(prime_palindrome_list)


if __name__ == '__main__':
    print(Solution().primePalindrome(10))
