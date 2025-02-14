# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
 
for _ in range (t):
    size = int(input())
    nums = list(map(int, input().split()))
    prev = nums[0]
    summ = prev
 
    for i in range(1, len(nums)):
        if nums[i] > 0:
            if prev > 0 and nums[i] >= prev:
                summ -= prev
                prev = nums[i]
                summ += prev
            elif prev < 0:
                prev = nums[i]
                summ += prev
        else:
            if prev < 0 and nums[i] >= prev:
                summ -= prev
                prev = nums[i]
                summ +=prev
            elif prev > 0:
                prev = nums[i]
                summ += prev
 
    print(summ) 