# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    max_inv = 0
    count = 0
    for num in arr:
        if max_inv > num:
            count += 1
            max_inv = 0
        else:
            max_inv = max(max_inv,num)
    print(count)
        