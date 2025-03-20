# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans= []
        def combination(ind, arr, target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(arr[:])
                    return
                
                if ind >= len(candidates): 
                    return
            
            if candidates[ind] <= target:
                arr.append(candidates[ind])
                combination(ind, arr, target - candidates[ind])
                arr.pop()
            
            combination(ind + 1, arr, target)

        combination(0,[],target)
        return ans
        