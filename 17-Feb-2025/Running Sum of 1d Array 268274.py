# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        List = [nums[0]]
        for i in range(1,len(nums)):
            List.append(nums[i]+List[i-1])

        return List
            