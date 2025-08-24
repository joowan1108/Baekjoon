import sys
input = sys.stdin.readline

"""
dp[i]에는 가치 i를 이루는 가짓수를 저장함
이때 가치 i에서부터 모든 coin들을 더해서 가짓수를 update하면 중복이 생긴다.

각 index에서 쓸 수 있는 코인을 하나로 제한해서 풀면 중복이 안된다.
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