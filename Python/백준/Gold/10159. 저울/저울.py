import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
graph_reversed = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph_reversed[b].append(a)


"""
양쪽으로 bfs를 하여 앞뒤로 연결된 개수를 확인한다

결과를 알 수 없는 물건 수는 전체-자기자신-bfs-bfs_reversed 이다.
"""
def bfs(g, start):
  q = deque([start])
  visited = set([start])
  while q:
    s = q.popleft()
    for adj in g[s]:
      if adj not in visited:
        visited.add(adj)
        q.append(adj)
  return len(visited)-1

for i in range(1,n+1):
  bfs_ = bfs(graph, i)
  bfs_reversed = bfs(graph_reversed, i)
  print(n-bfs_-1-bfs_reversed)






    
    
  
      