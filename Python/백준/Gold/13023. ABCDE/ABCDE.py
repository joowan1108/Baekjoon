import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)] 
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


visited = [False] * n

def dfs(node, depth):
  if depth == 4:
    return True
  visited[node] = True
  for neighbor in graph[node]:
    if not visited[neighbor]:
      if dfs(neighbor, depth + 1):
        return True
  visited[node] = False
  return False

result = False
for i in range(n):
  if graph[i]:
    result = result | dfs(i,0)
    if result:
      break

if result:
  print(1)
else:
  print(0)
