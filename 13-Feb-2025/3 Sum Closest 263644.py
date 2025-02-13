# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n=len(nums)
        result=[]

        for i in range(n):
            low,high=1+i, n-1
            while low<high:
                summ= nums[i]+nums[low]+nums[high]
                diff = target - summ
                result.append((abs(diff), summ))
                if summ > target :
                    high -= 1
                else:   
                    low += 1
        result.sort()
        return result[0][1]