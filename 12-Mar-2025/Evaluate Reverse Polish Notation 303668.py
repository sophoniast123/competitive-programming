# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif char == '-':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif char == '/':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(b /a))
            elif char == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            else:
                stack.append(char)
        return int(stack[0])