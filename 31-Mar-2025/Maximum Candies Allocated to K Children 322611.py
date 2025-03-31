# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        l = 1
        r = sum(candies) // k 
        res = 0
        while l <= r:
            mid = (l + r) // 2
            count = 0
            for c in candies:
                count += c // mid

            if count >= k:
                l = mid + 1
            else:
                r = mid - 1
        return r

            
            
            

        

        