# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n,k = map(int, input().split())
arr = list(map(int, input().split()))


difference = []
for i in range(1, n):
    difference.append(arr[i]-arr[i-1])

difference.sort()

print(sum(difference[:n - k]))