# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        

        res = [0]*(len(nums) + 1)

        for i,j in requests:
            res[i] += 1
            res[j + 1] -=1
        print(res)

        prefix = [res[0]]*len(res)

        for i in range(1,len(res)):
            prefix[i] = prefix[i-1] + res[i]
        prefix.pop()
        nums.sort()
        prefix.sort()

        result = 0
        for i in range(len(nums)):
            result = (result + nums[i]*prefix[i]) % MOD
        return result