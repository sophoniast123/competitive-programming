# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set()
        
        for num in nums:
            if num in sett:
                return num
            sett.add(num)
            

