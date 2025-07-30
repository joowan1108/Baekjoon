import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0



for _ in range(m):
  start, end, cost = map(int, input().split())
  graph[start][end] = min(cost, graph[start][end])

for mid_node in range(1,n+1):
  for start_node in range(1,n+1):
    for end_node in range(1,n+1):
      graph[start_node][end_node] = min(graph[start_node][end_node], graph[start_node][mid_node] + graph[mid_node][end_node])

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == INF:
      print(0, end=' ')
    else:
      print(graph[i][j], end=' ')
  print()

  
    





