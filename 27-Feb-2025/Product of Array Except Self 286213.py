# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        for i in range(len(nums)-1):
            left.append(left[-1]*nums[i])

        nums.reverse()
        for i in range(len(nums)-1):
            right.append(right[-1]*nums[i])


        right.reverse()

        res = []
        for i in range(len(left)):
            res.append(left[i]*right[i])
        return res