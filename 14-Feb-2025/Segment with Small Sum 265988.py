# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,m = map(int, input().split())
nums = list(map(int, input().split()))


l = 0
res = 0
sum = 0

for i in range(len(nums)):
    sum+=nums[i]

    if sum > m:
        sum-=nums[l]
        l+=1
    res=max(res,i-l+1)
print(res)