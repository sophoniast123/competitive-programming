# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        output = []
        while len(arr) > 1:
            idx = arr.index(max(arr))
            if idx == len(arr) - 1:
                arr = arr[:idx]
            else:
                output.append(idx + 1)
                output.append(len(arr))
                arr = arr[idx + 1:][::-1] + arr[:idx]
        return output