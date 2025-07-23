import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v, e, start = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for node in range(1,v+1):
  graph[node].sort(reverse=True)

order = [0]*(v+1)
visited = set()
iter = 1
def dfs(node):
  global iter
  visited.add(node)
  order[node] = iter
  iter+=1
  for adj_node in graph[node]:
    if adj_node not in visited:
      dfs(adj_node)
  
  

dfs(start)
for i in range(1,v+1):
  print(order[i])



    
  




