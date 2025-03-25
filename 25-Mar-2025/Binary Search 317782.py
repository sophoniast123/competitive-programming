# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = len(nums) // 2

        

        while l <= r:
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                l = mid + 1
                mid = (l + r) // 2
            else:
                r = mid - 1
                mid = (l + r) // 2
        return -1


        
