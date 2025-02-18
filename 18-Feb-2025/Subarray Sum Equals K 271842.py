# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        count = 0
        res = defaultdict(int)

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum == k:
                count += 1
            if curr_sum - k in res:
                count += res[curr_sum - k]
            res[curr_sum] += 1
        return count 