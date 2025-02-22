# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:

        ones_count = 0  
        swaps = 0  

        for char in s:
            if char == '1':
                ones_count += 1
            elif char == '0':
                swaps += ones_count  

        return swaps
