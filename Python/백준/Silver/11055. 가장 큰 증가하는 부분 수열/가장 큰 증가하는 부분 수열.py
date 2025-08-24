import sys
input = sys.stdin.readline

"""
dp에 지금까지 가장 큰 수열의 합을 저장하면 된다.
"""

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
  for j in range(i):
    if nums[j] < nums[i]:
      dp[i] = max(dp[i], dp[j]+nums[i])

print(max(dp))
