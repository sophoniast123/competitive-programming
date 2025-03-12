# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        final =[[1]]

        for i in range(34 - 1):
            temp = [0] + final[-1] + [0]
            res = []
            for j in range(len(final[-1]) + 1):
                res.append(temp[j] + temp[j+1])
            final.append(res)
        return final[rowIndex]