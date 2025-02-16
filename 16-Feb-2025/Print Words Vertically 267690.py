# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        n = len(max(s, key=len))

        ans = []

        for i in range(n):
            words = ''
            for char in s:
                if len(char) > i:
                    words += char[i]
                else:
                    words += ' '
            ans.append(words.rstrip())

        return ans
        