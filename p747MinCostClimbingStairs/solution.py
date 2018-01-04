class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        res = [0 for i in range(len(cost))]
        res[0] = cost[0]
        res[1] = cost[1]
        for i in range(2,len(cost)):
            res[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        return min(res[-1], res[-2])

s = Solution()
ans = s.minCostClimbingStairs([10,15,20])
print(ans)
