# Problem: Books - https://codeforces.com/contest/279/problem/B

n,m=map(int, input().split())
nums = list(map(int, input().split()))

summ = 0
left = 0
res = 0
for right in range (len(nums)):
    summ += nums[right]

    if summ > m:
        summ -= nums[left]
        left +=1
    res = max(res, right - left + 1 )
print(res)