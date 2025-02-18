# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

import sys
n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

if sum(nums1) != sum(nums2):
    print(-1)
    sys.exit(0)

count = 0
prefix_1 = [nums1[0]]*len(nums1)
prefix_2 = [nums2[0]]*len(nums2)

for i in range(1,len(nums1)):
    prefix_1 [i] = prefix_1[i - 1] + nums1 [i]

for i in range(1,len(nums2)):
    prefix_2 [i] = prefix_2[i - 1] + nums2 [i]

l, r = 0, 0
while l < len(prefix_1) and r < len(prefix_2):
    if prefix_1[l] == prefix_2[r]:
        l += 1
        r += 1
        count += 1
    elif prefix_1[l] < prefix_2[r]:
        l += 1
    else:
        r += 1
if count > 0:
    print(count)
else:
    print(-1)