# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        count = 0
        res = defaultdict(int)

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum % k == 0:
                count += 1
            if curr_sum % k in res:
                count += res[curr_sum % k]
            res[curr_sum % k] += 1
        return count