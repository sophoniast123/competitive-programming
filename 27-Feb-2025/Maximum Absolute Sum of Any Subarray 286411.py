# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return abs(nums[0])

        max_sum = cur_min =  cur_max = nums[0]

        for i in range(1, len(nums)):
            
            cur_min = min(nums[i], cur_min+nums[i])
            cur_max = max(nums[i], cur_max+nums[i])

            max_sum = max(max_sum, abs(cur_max), abs(cur_min))
        return max_sum