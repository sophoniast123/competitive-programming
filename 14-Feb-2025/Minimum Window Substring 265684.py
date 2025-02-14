# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        min_range = [float('-inf'), float('inf')]
        count_t = Counter(t)
        count = 0

        for right in range (len(s)):
            if s[right] in count_t:
                count_t[s[right]] -= 1
                if count_t[s[right]] >= 0:
                    count += 1
            
            while count == len(t):
                if right - left < min_range[1] - min_range[0]:
                    min_range = [left, right]

                if s[left] in count_t:
                    count_t[s[left]] += 1

                    if count_t[s[left]] > 0:
                        count -= 1
                left += 1

        if (min_range[0]==float('-inf') or min_range[1]==float('inf')):
            return ''
        return s[min_range[0] : min_range[1] + 1]
        
            

            





        
