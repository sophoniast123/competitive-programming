# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k %= n
        nums.reverse()


        start , end = 0 , k-1
        while start < end:
            nums[start],nums[end]=nums[end],nums[start]
            end-=1
            start+=1

        start,end=k, n-1
        while start < end:
            nums[start],nums[end]=nums[end],nums[start]
            end-=1
            start+=1

        