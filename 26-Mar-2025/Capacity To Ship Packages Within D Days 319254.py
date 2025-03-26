# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(weights, capacity, days):
            load = 0
            days_count = 1

            for wt in weights:
                load = load + wt
                if load > capacity:
                    load = wt
                    days_count += 1
                    
                    if days_count > days:
                        return False
            
            return True
            
        start = max(weights)
        end = sum(weights)

        while start < end:
            mid = start + (end - start) // 2

            if canShip(weights, mid, days):
                end = mid
            else:
                start = mid + 1

        return start