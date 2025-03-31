# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = float('inf')

        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                r = mid - 1
                ans = min(ans, nums[mid])
        return ans 
