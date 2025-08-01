import sys
input = sys.stdin.readline
INF = sys.maxsize

v,e = map(int, input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]
for _ in range(e):
  a,b,c = map(int, input().split())
  graph[a][b] = c

for mid in range(1,v+1):
  for start in range(1,v+1):
    for end in range(1,v+1):
      new_dist = graph[start][mid] + graph[mid][end]
      graph[start][end] = min(graph[start][end], new_dist)


self = [graph[i][i] for i in range(1,v+1)]
ans = min(self)
if ans == INF:
  print(-1)
else:
  print(ans)







