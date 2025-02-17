# Problem: Shifting Letters - https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ''
        suffix_sum = [shifts[-1]]

        for i in range(len(shifts)-2, -1, -1):
            suffix_sum.append(suffix_sum[-1] + shifts[i])

        suffix_sum.reverse()

        for i in range(len(s)):
            char=chr(ord("a") + ((ord(s[i]) + suffix_sum[i]) - ord("a")) % 26)
            res += char
        return res