import sys
input = sys.stdin.readline
INF = int(1e10)
"""
항상 양수가 아니므로 벨만포드 사용해야 한다
O(V*E)

음의 순환 존재하면 -1
distances를 반환할 때 inf로 설정된 애들은 -1로 바꿔야함
"""

def bellman():
  n,m = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  
  for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

  distances = [INF]*(n+1)
  distances[1] = 0

  for _ in range(n-1):
    for mid_node in range(1,n+1):
      for end_node,weight in graph[mid_node]:
        new_distance = distances[mid_node] + weight
        if distances[mid_node]!=INF and new_distance < distances[end_node]:
          distances[end_node] = new_distance

  for mid_node in range(1,n+1):
    for end_node, weight in graph[mid_node]:
      if distances[mid_node] != INF and distances[mid_node] + weight < distances[end_node]:
        return [-1]
  return distances

distances = bellman()
if distances[0] == -1:
  print(-1)
else:  
  for dist in distances[2:]:
    if dist == INF:
      print(-1)
    else:
      print(dist)
  
    





