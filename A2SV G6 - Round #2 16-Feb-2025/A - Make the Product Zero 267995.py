# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

t=int(input())
nums=list(map(int, input().split()))

minimum=[]
for num in nums:
    minimum.append(abs(num))
print(min(minimum))