# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, temp = [], []

        def recursion():
            if len(temp) == n:
                res.append(temp[:])
                return 
            
            for i in nums:
                if i not in temp:
                    temp.append(i)
                    recursion()
                    temp.pop()
        
        recursion()
        return res
        