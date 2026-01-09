import sys
import heapq
from collections import deque
input = sys.stdin.readline

"""
지금까지 포장한 도로의 수를 state으로 저장하면서 DP를 해야 할 거 같음

dp[n][k] : n에 오면서 k개의 도로를 포장했을 때의 최소 거리

"""

n,m,k = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

def dijkstra():
  q = []
  INF = float('inf')
  heapq.heappush(q, (0,1,0))
  dp = [[INF]*(k+1) for _ in range(n+1)]

  for i in range(k+1):
    dp[1][i] = 0

  while q:
    mid_dist, mid_node, nums = heapq.heappop(q)
    if dp[mid_node][nums] < mid_dist:
      continue

    for end_node, end_dist in graph[mid_node]:
      if nums < k:
        new_dist = mid_dist
        if new_dist < dp[end_node][nums+1]:
          dp[end_node][nums+1] = new_dist
          heapq.heappush(q, (new_dist, end_node, nums+1))
      new_dist = mid_dist+end_dist
      if new_dist < dp[end_node][nums]:
        dp[end_node][nums] = new_dist
        heapq.heappush(q, (new_dist, end_node, nums))
        

  
  return dp

dp = dijkstra()

print(min(dp[n]))
      
  
