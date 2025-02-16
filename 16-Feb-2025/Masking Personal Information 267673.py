# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            i = s.index('@')

            res = s[0] + '*'*5 + s[i-1] + s[i:]

        else:
            phone=''
            for c in s:
                if c.isdigit():
                    phone += c
            n = len(phone)

            if n == 10:
                res = '*'*3 + '-' + '*'*3 + '-' + phone[6:]
            elif n == 11:
                res = '+' + '*' + '-' + '*'*3 + '-' + '*'*3 + '-' + phone[7:]
            elif n == 12:
                res = '+' + '*'*2 + '-' + '*'*3 + '-' + '*'*3 + '-' + phone[8:]
            elif n == 13:
                res = '+' + '*'*3 + '-' + '*'*3 + '-' + '*'*3 + '-' + phone[9:]
        return res

            
