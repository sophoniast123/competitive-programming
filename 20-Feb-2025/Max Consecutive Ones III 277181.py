# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        max_ones=0
        count=0

        for r in range(len(nums)):
            if nums[r]==0:
                count+=1
            while count>k:
                if nums[l]==0:
                    count-=1
                l+=1
            max_ones=max(max_ones, r-l+1)
        return max_ones

