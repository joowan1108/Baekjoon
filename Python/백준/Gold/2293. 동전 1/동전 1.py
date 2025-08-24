import sys
input = sys.stdin.readline

"""
dp[i]에는 가치 i를 이루는 가짓수를 저장함
"""

n,k = map(int, input().split())
dp = [0]*(k+1)
coins = []
for _ in range(n):
  coin = int(input())
  coins.append(coin)


dp[0] = 1
for coin in coins:
  for i in range(k):
    if i+coin <= k:
      dp[i+coin] += dp[i]

print(dp[k])