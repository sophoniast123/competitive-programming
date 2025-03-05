# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        non_zero = 0
        res = []
        for i in range(len(s)):
            res.append(s[i])
            if res[i] != '1':
                res[i], res[non_zero] = res[non_zero], res[i]
                non_zero +=1

        for i in range(len(res)-1):
            if res[-1] == '1':
                a = res.pop()
                res.reverse()
                res.append(a)
                break
        return ''.join(res)
