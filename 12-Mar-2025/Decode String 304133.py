# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
            stack = []
            
            for i in s:
                if i == ']':

                    char = []
                    while stack and stack[-1] != '[':
                        char.append(stack.pop())
                    char.reverse()
                    ans = "".join(char)
                    
                    stack.pop()
                
                    num = []
                    while stack and stack[-1].isdigit():
                        num.append(stack.pop())
                    num.reverse()
                    numss = ''.join(num)

                    stack.append(str(int(numss) * ans))
            
                else:
                    stack.append(i)
        
            return ''.join(stack)