import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())

"""
 물건을 담았을 때 가능한 무게들을 index로 하는 dp 배열을 만든다.

 각 무게에서의 가치의 최대값을 구하면 결국 무게가 k일 때의 가치의 최대값을 구할 수 있다 
"""
        
items = deque()
dp = [0 for _ in range(k+1)]

for _ in range(n):
  w,v = map(int, input().split())
  items.append([w,v])

while items:
  w,v = items.popleft()
  for w_idx in range(k,w-1,-1):
    if w_idx >= w:
      #현재 무게에서의 최대값과 (최대무게 - 현재 무게)에서의 최대값 + 현재 item의 가치를 계속 비교하면 된다. 
      dp[w_idx] = max(dp[w_idx], dp[w_idx-w]+v)

print(dp[-1])




  
  

  


