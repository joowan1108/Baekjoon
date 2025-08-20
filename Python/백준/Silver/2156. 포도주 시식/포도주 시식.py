import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
wines = [0]
for _ in range(n):
  wines.append(int(input()))

"""
dp[i][0] = 현재부터  연속으로 마신 개수 0
-> max(dp[i-1][0], dp[i-1][1], dp[i-1][2])

dp[i][1] = 현재부터 연속으로 마신 개수 1
-> dp[i-1][0] + wines[i]

dp[i][2] = 현재부터 연속으로 마신 개수 2
-> dp[i-1][1] + wines[i]
"""

dp = [[0]*(3) for _ in range(n+1)]
for i in range(n+1):
  dp[i][0] = max([dp[i-1][0], dp[i-1][1], dp[i-1][2]])
  dp[i][1] = dp[i-1][0] + wines[i]
  dp[i][2] = dp[i-1][1] + wines[i]

print(max(dp[n]))
  
