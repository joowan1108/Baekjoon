import sys
input = sys.stdin.readline


n,k = map(int, input().split())
coins = set()
for _ in range(n):
  coins.add(int(input()))

"""

dp[i]에는 가치 i가 되는 동전 최소 개수가 들어감

"""

dp = [sys.maxsize]*(k+1)
dp[0] = 0

for c in coins:
  for i in range(k):
    if i+c < k+1:
      dp[i+c] = min(dp[i]+1, dp[i+c])

if dp[k] == sys.maxsize:
  print(-1)
else:
  print(dp[k])