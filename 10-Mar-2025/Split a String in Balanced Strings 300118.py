# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        hash = defaultdict(int)
        for char in s:
            hash[char] += 1
            if len(hash.values()) > 1 and len(set(hash.values())) == 1:
                count += 1
        return count