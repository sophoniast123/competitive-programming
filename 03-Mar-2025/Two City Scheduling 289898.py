# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = sorted(costs, key=lambda x:x[1]-x[0])
        l = 0
        r = len(costs)-1

        run_sum = 0
        while l < r:
            run_sum += res[l][1] + res[r][0]
            l += 1
            r -= 1
        return run_sum
        