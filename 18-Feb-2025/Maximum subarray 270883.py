# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]

        for i in range(1,len(nums)):
            cur_sum = max(nums[i], nums[i] + cur_sum)
            max_sum = max(max_sum, cur_sum)
        return max_sum