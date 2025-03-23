# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())


for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    cur_sum1 = 0
    max_sum1 = 0

    for i in range(len(arr1)):
        cur_sum1 += arr1[i]
        max_sum1 = max(cur_sum1,max_sum1)    
    
    cur_sum2 = 0
    max_sum2 = 0

    for i in range(len(arr2)):
        cur_sum2 += arr2[i]
        max_sum2 = max(cur_sum2,max_sum2)
    maxx= max_sum1 + max_sum2
    print(max(maxx,0))