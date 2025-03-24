# Problem: Combination Sum III - https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []
        def backtrack(ind,arr,target):
            if len(arr) == k:
                if target == n:
                    ans.append(arr[:])
                return 

            if target > n:
                return  

            for i in range(ind,9+1):
                arr.append(i)
                backtrack(i+1,arr,target+i)
                arr.pop()
            
        backtrack(1,[],0)
        return ans


