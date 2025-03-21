# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import *
t = int(input())

for _ in range(t):
    n,k,d = map(int, input().split())
    arr = list(map(int, input().split()))

    l = 0
    r = 0
    min_len = float('inf')
    dicts = defaultdict(int)
    while r < len(arr):
        dicts[arr[r]] += 1

        if r - l + 1 >= d:
            min_len = min(min_len, len(dicts))
            dicts[arr[l]] -= 1
            if dicts[arr[l]] == 0:
                del dicts[arr[l]]
            l += 1
        r += 1
        
    print(min_len)