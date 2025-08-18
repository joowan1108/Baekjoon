import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

seen = set()
count = 0

for a in nums:
    if x - a in seen:
        count += 1
    seen.add(a)

print(count)
