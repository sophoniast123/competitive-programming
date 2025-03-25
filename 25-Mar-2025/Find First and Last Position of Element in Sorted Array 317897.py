# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = 0 
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                gg = mid
                while mid > 0 and nums[mid - 1] == target:
                    mid -= 1
                while gg < len(nums) - 1 and nums[gg + 1] == target:
                    gg += 1
                return [mid, gg]

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return [-1,-1]

