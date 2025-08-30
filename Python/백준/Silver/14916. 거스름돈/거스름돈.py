import sys
input = sys.stdin.readline

n = int(input())

dp = [sys.maxsize]*(100000+1)
coins = [2,5]
dp[2] = 1
dp[5] = 1
for i in range(2,n+1):
  if dp[i]!=sys.maxsize:
    for coin in coins:
      if i+coin < n+1:
        dp[i+coin] = min(dp[i+coin], dp[i]+1)
if dp[n] == sys.maxsize:
  print(-1)
else:
  print(dp[n])
  

    
        
    
  


  
    
  



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  