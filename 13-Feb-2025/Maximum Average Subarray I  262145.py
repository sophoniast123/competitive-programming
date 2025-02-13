# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        l=0
        total = sum(nums[:k - 1])

        for r in range(k - 1, len(nums)):
            total+=nums[r]

            res = max(total, res)

            total-=nums[l]
            l+=1
        return res / k