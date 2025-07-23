import sys
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

k = int(input())


def bfs(start, num):
  q = deque([start])
  bipartite[start] = num
  while q:
    node = q.popleft()
    for adj_node in graph[node]:
      if bipartite[adj_node] == 0:
        bipartite[adj_node] = -1*bipartite[node]
        q.append(adj_node)
      elif bipartite[node] == bipartite[adj_node]:
        return False
  return True


for _ in range(k):
  is_bi = True
  v,e = map(int, input().split())
  graph = defaultdict(list)
  bipartite = [0]*(v+1)
  
  for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  for s in range(1, v+1):
    if bipartite[s] == 0:
      if not bfs(s, 1):
        is_bi = False
        break
  print("YES" if is_bi else "NO")
  
  
  





