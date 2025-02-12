# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()
        count=0
        prefixSum=[0]*len(costs)
        prefixSum[0] = costs[0]

        for i in range(1, len(costs)):
            prefixSum[i] = prefixSum[i - 1] + costs[i]


        for i in range(len(prefixSum)):
            if prefixSum[i]<=coins:
                count+=1
        return count
        