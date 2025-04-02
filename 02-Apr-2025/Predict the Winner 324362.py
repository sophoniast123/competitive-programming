# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        
        def sol(i, j):
            if i>j:
                return 0
            if i==j:
                return nums[i]
            
            return max(nums[i] + min(sol(i+1, j-1), sol(i+2, j)), nums[j] + min(sol(i+1, j-1), sol(i, j-2)))
        
        sm = sum(nums)
        player = sol(0, len(nums)-1)
        return player >= sm - player