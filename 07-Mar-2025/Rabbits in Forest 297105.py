# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash_map = defaultdict(int)
        res = 0

        for num in answers:
            if hash_map[num] == 0:
                res += num + 1
                hash_map[num] = num
            else:
                hash_map[num] -= 1
        return res
