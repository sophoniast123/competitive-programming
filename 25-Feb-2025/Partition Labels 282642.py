# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}

        for i, char in enumerate(s):
            hmap[char] = i

        res = []
        size, end = 0, 0

        for i, char in enumerate(s):
            size += 1
            end = max(end, hmap[char])

            if i == end:
                res.append(size)
                size = 0
        return res