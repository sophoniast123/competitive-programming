# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat or not mat[0]:
            return []
    
        rows, cols = len(mat), len(mat[0])

        diagonals = [[] for _ in range(rows + cols -1)]
        
        for i in range(rows):
            for j in range(cols):
                diagonals[i + j].append(mat[i][j])
    
        res = diagonals[0]

        for x in range(1, len(diagonals)):
            if x % 2 == 0:
                res.extend(diagonals[x] [::-1])
            else:
                res.extend(diagonals[x])
        return res
        