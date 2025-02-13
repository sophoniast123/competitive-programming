# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left = 0
        right = len(skill) - 1
        summation = skill[left] + skill[right]
        res=0

        while left < right:
            if skill[left] + skill[right] != summation:
                return -1
            

            res+= (skill[left]*skill[right])
            left+=1
            right-=1
        return res