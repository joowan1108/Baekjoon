import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split())
nums = deque([i for i in range(1,n+1)])
yosepus = []

while (len(nums)>=1):
    for _ in range(k-1):
        nums.append(nums.popleft())
    tmp=nums.popleft()
    yosepus.append(tmp)

print('<', end='')
for i in range(len(yosepus)-1):
    print(f"{yosepus[i]}, ",end='')
print(f"{yosepus[-1]}>")
    





    