# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = deque()

        for i in range(1, n + 1):
            d.append(i)

        while len(d) > 1:
            for i in range(k - 1):
                d.append(d.popleft())
            d.popleft()
        
        return d[0]