# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 07:51
# @Author  : yunfan

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ind_stack= []
        ans = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            temp =  temperatures[i]
            if len(ind_stack) == 0:
                ind_stack.append(i)
            else:
                if temp <=  temperatures[ind_stack[-1]]:
                    ind_stack.append(i)
                else:
                    while len(ind_stack) > 0 and temp > temperatures[ind_stack[-1]]:
                        ans[ind_stack[-1]] = i - ind_stack[-1]
                        ind_stack.pop()
                    ind_stack.append(i)
        return ans