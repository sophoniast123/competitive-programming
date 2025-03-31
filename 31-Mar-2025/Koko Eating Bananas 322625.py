# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 10**9

        def good(rate):
            total = 0

            for pile in piles:
                total += math.ceil(pile / mid)
            
            return total <= h

        while l <= r:
            mid = (l + r) // 2

            if good(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
