# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
arr1 = list(map(int, input().split()))

pre1 = [0]*len(arr1)
pre1[0] = arr1[0]
for i in range(1,len(arr1)):
    pre1[i] = pre1[i-1] + arr1[i]

arr1.sort()
pre2 = [0]*len(arr1)
pre2[0] = arr1[0]
for i in range(1,len(arr1)):
    pre2[i] = pre2[i-1] + arr1[i]


m = int(input())
for _ in range(m):
    type,l,r = map(int, input().split())

    l -= 1
    r -= 1
    if type == 1:
        if l == 0:
            print(pre1[r])
        else:
            print(pre1[r] - pre1[l - 1])

    elif type == 2:
        if l == 0:
            print(pre2[r])
        else:
            print(pre2[r] - pre2[l - 1])
        