import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(46)
dp[1] = 1

"""
예외처리 귀찮음
"""
for i in range(2,46):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

