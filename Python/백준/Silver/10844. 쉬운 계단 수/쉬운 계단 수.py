import sys
input = sys.stdin.readline

n = int(input())

if n==1:
  print(9)

else:
  dp = [[0]*n for _ in range(10)]
  dp[0][0] = 0
  for i in range(1,10):
    dp[i][0] = 1
  for i in range(1,n):
    for num in range(10):
      if num==0:
        dp[num][i] = dp[num+1][i-1]%1000000000
      elif num==9:
        dp[num][i] = dp[num-1][i-1]%1000000000
      else:
        dp[num][i] = (dp[num-1][i-1] + dp[num+1][i-1])%1000000000
        
  print(sum(dp[i][n-1] for i in range(10))%1000000000)
  

  
