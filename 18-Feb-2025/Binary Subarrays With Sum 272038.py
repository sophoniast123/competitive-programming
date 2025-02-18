# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur_sum = 0
        dicts = defaultdict(int)
        count = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            if cur_sum == goal:
                count += 1
            if cur_sum - goal in dicts:
                count += dicts[cur_sum - goal]
            dicts[cur_sum] += 1
        return count