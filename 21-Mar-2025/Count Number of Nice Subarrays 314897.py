# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dicts = defaultdict(int)
        l = 0
        r = 0 
        summ = 0

        count = 0
        for r in range(len(nums)):
            summ += nums[r] % 2
            
            if summ == k:
                count += 1

            if summ - k in dicts:
                count += dicts[summ - k]
            dicts[summ] += 1

        return count