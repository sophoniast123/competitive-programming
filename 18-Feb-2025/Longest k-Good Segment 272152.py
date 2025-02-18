# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

n,m=map(int, input().split())
nums = list(map(int, input().split()))

hmap=defaultdict(int)

l = 0
max_len = 0

arr = []

for r in range(len(nums)):
    hmap[nums[r]] += 1
    while len(hmap) > m:
        
        hmap[nums[l]] -= 1
        if hmap[nums[l]] == 0:
            del hmap[nums[l]]
        l+=1
    if max_len < r - l + 1:
        max_len = max(max_len, r - l + 1)
        arr = [l+1,r+1]

print(*arr)



    
    