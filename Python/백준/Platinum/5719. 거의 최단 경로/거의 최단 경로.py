import sys
import heapq
from collections import deque
input = sys.stdin.readline

"""
거의 최단 경로를 구하기 위해서는 최단 경로를 구성하는 간선들을 모두 제거해야 한다.

간선들을 제거하기 위해서는 그래프를 인접 행렬로 하는 것이 나아보임
"""

while True:
  n,m = map(int,input().split())
  if n==0 and m==0:
    break

  graph = [[0]*(n) for _ in range(n)]
  
  start,dest = map(int,input().split())
  
  for _ in range(m):
    u,v,p = map(int,input().split())
    graph[u][v] = p

  def dijkstra(s,d):
    q = []
    heapq.heappush(q, (0,s))
    distances = [int(1e9)]*n
    distances[s] = 0

    while q:
      mid_dist, mid = heapq.heappop(q)
      if distances[mid] < mid_dist:
        continue

      for i in range(n):
        if graph[mid][i]!=0:
          end_dist = graph[mid][i]
          end = i
          new_dist = mid_dist + end_dist
          
          if new_dist < distances[end]:
            distances[end] = new_dist
            heapq.heappush(q, (new_dist, end))
            
    return distances
    
  fastest = dijkstra(start, dest)

  #역추적: fastest[end] = fastest[other] + graph[other][end] 라면 그 경로는 최단 경로
  def bfs(s):
    q = deque()
    visited = set()
    visited.add(s)
    q.append(s)
    while q:
      node = q.popleft()
      for i in range(n):
        #i -> node 경로가 존재할 때
        if graph[i][node] != 0 and fastest[node] == fastest[i] + graph[i][node]:
          # 이게 최단 경로라면
          #이 간선 제거
          graph[i][node] = 0

          if i not in visited:
            q.append(i)
            visited.add(i)

  bfs(dest)
  
  #다시 최단 경로 구하기 -> 이 경로가 거의 최단 경로
  almost_fastest = dijkstra(start, dest)
  if almost_fastest[dest]!=int(1e9):
    print(almost_fastest[dest])
  else:
    print(-1)
  
    
  
  
   

  
        
        
  
    


