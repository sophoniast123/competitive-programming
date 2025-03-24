# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
        count = Counter(cand)
        cand = sorted(count)
        pref = cand[:]
        for i in range(len(pref) - 2,-1,-1):
            pref[i] += pref[i+1]
        ans = set()
        def b_t(ind, arr, total):
            # print(ind, arr, total)
            if ind == len(pref):
                if total == target:
                    ans.add(tuple(arr))
                return
            if total > target:
                return
            
            # if total + pref[ind] < target:
            #     return
            # arr.append(cand[ind])
            for c in range(count[cand[ind]]+1):
                # arr.append(cand[ind])
                b_t(ind+1, arr[:], total)
                total += cand[ind]
                arr.append(cand[ind])
                # arr.pop()
                # b_t(ind + 1, arr, total)
        b_t(0,[],0)
        return list(ans)

            