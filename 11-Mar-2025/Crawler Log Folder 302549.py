# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        directories = 0

        for dir in logs:
            if dir == '../':
                if directories > 0:
                    directories -= 1
            elif dir != './':
                directories += 1
        return directories