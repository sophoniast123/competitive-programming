# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        prefix = [0]*(len(s) + 1)

        for start,end,direction in shifts:
            if direction == 1:
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end + 1] += 1

        for i in range(1,len(prefix)):
            prefix [i] += prefix[i-1]
        prefix.pop()

        res = []
        for i, char in enumerate(s):
            chars = chr((ord(char) - ord('a') + prefix[i]) % 26 + ord('a'))
            res.append(chars)
        return''.join(res)