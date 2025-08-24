import sys
input = sys.stdin.readline

"""
dp에는 각 길이에서 각 숫자를 골랐을 때의 오르막 수를 저장하면 된다
"""

n = int(input())
dp = [[0]*(n+1) for _ in range(10)]

for i in range(10):
  dp[i][1] = 1

for i in range(2,n+1):
  dp[0][i] = dp[0][i-1]%10007
  for j in range(1,10):
    s = 0
    for k in range(j+1):
      s += (dp[k][i-1]%10007)
    dp[j][i] = s%10007

ans = 0
for i in range(10):
  ans += dp[i][n]%10007
print(ans%10007)


    
