import sys
input = sys.stdin.readline

"""
각 자리가 0일 때랑 1일 때랑 구분해서 모든 경우의 수를 구해야한다.

dp를 2차원 배열로 2*n으로 만든다
"""

n = int(input())

dp = [[0]*(2) for _ in range(n+1)]
dp[1][1] = 1
for i in range(2, n+1):
  if dp[i-1][1]>0:
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
  else:
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]

print(dp[n][1]+dp[n][0])



