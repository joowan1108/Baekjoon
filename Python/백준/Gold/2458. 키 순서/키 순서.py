import sys
from collections import deque

input = sys.stdin.readline

"""
전체 node들에 대해서 bfs
자기한테 오는 노드 수 + 다른 노드로 가는 개수 == n-1 이라면 앞뒤로 몇명인지 알 수 있음
"""

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
reversed_graph = [[] for _ in range(n+1)]

for _ in range(m):
  start, end = map(int, input().split())
  graph[start].append(end)
  reversed_graph[end].append(start)

def bfs(s, graph):
  q = deque()
  q.append(s)
  visited = set()
  visited.add(s)
  while q:
    node = q.popleft()
    for adj in graph[node]:
      if adj not in visited:
        q.append(adj)
        visited.add(adj)
  return len(visited)-1
ans = 0
for s in range(1,n+1):
  num1 = bfs(s, graph)
  num2 = bfs(s, reversed_graph)
  if num1 + num2 == n-1:
    ans+=1

print(ans)
    
    