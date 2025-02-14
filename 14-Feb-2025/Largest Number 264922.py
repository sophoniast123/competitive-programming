# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strings=[]
        for num in nums:
            strings.append(str(num))

        for i in range (len(strings)):
            for j in range(len(strings)-1-i):
                if int(strings[j]+strings[j+1]) < int(strings[j+1]+strings[j]):
                    strings[j],strings[j+1]=strings[j+1],strings[j]



        return str(int(''.join(strings)))