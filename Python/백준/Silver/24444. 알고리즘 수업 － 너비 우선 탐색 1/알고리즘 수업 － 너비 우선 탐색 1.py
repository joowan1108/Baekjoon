import sys
from collections import deque
input = sys.stdin.readline

v, e, start = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for node in range(1,v+1):
  graph[node].sort()

order = [0]*(v+1)

def bfs(node):
  iter=1
  visited = set([node])
  q = deque([node])
  order[node] = iter
  while q:
    t = q.popleft()
    for adj_node in graph[t]:
      if adj_node not in visited:
        visited.add(adj_node)
        q.append(adj_node)
        iter+=1
        order[adj_node] = iter

bfs(start)
for i in range(1,v+1):
  print(order[i])
  




    
  




