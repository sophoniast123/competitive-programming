# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        track = {}

        for num in nums2:
            while stack and stack[-1] < num:
                a = stack.pop()
                track[a] = num
            stack.append(num)
        
        res = []
        for i in range(len(nums1)):
            if nums1[i] in track:
                res.append(track[nums1[i]])
            else:
                res.append(-1)
        
        return res
