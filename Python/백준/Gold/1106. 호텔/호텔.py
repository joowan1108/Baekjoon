import sys
input = sys.stdin.readline

c,n = map(int, input().split())
costs = []
ppl = []
for _ in range(n):
  cost, p = map(int, input().split())
  costs.append(cost)
  ppl.append(p)

max_cost = 100*1000 + 1
dp = [0]*(max_cost+1)
#초기화
for i in range(n):
  dp[costs[i]] = ppl[i]

for cost, p in zip(costs, ppl):
  for i in range(cost, max_cost+1):
    dp[i] = max(dp[i], dp[i-cost]+p)


ans = 0
for i in range(1,max_cost+1):
  if dp[i] >= c:
    ans = i
    break
print(ans)
    
  
  
  

  

    




  
  

