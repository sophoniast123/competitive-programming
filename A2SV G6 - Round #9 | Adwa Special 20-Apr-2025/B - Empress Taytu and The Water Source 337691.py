# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

import math

t = int(input())  
arr = []

for _ in range(t):
    n, k = map(int, input().split()) 
    d = list(map(int, input().split())) 
    a = list(map(int, input().split()))  
    arr.append((n, k, d, a))

def deliver(n, k, d, a, size):
    total_time = 0
    for i in range(n):
       
        trips_needed = math.ceil(d[i] / size)  
        total_time += trips_needed * a[i]
        if total_time > k:  
            return False
    return total_time <= k

def wagon(t, arr):
    for n, k, d, a in arr:
        low, high = 1, max(d)  
        answer = -1
        
        while low <= high:
            mid = (low + high) // 2  
            if deliver(n, k, d, a, mid):
                answer = mid
                high = mid - 1  
            else:
                low = mid + 1  
        
        print(answer)

wagon(t, arr)
