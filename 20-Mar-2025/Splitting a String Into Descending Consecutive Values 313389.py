# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        
        def split(path,i):
            if i == len(s):
                return len(path)>= 2
            
            for j in range(i, len(s)):
                num = int(s[i:j+1])
                if not path or path[-1] - num == 1:
                    path.append(num)
                    if split(path, j + 1):
                        return True
                    path.pop() 
            return False
        return split([], 0)
                

