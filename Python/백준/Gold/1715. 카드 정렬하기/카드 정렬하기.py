import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
  heapq.heappush(nums, int(input()))
"""
제일 작은 애들부터 더해나간다면 비교 횟수가 최소이다
--> greedy
"""

ans = 0

if len(nums) == 1:
  print(0)
else:
  while len(nums) >=2 :
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    ans += (a+b)
    heapq.heappush(nums, a+b)
  print(ans)
  



  