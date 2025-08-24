import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

m,n = map(int, input().split())
graph = []
for _ in range(m):
  graph.append(list(map(int, input().split())))

moves = [(0,1), (0,-1), (1,0), (-1,0)]

"""
dfs를 진행
방문하지 않은 곳이라면 계속 간다 -> 목적지에 도착하면 경로 수 + 1
방문했던 곳이라면 그 경로의 개수를 목적지 경로 수에 더한다

dp: a->b,c일 때 a에서 목적지로 가는 경우의 수는 b에서 목적지로 가는 경우의 수 + c에서 목적지로 가는 경우의 수

-1로 초기화하는 이유는 0으로 방문했는데 경로가 없는 경우를 나타내기 위해서이다.
"""

visited = [[-1]*(n) for _ in range(m)]

def dfs(h,w):
  ways = 0
  #이미 거쳐간 경로라면
  if visited[h][w] != -1:
    return visited[h][w]
  #거쳐가지 않은 경로로 도착지에 도달했다면 +1
  elif h == m-1 and w == n-1:
    return 1
  #거쳐가지 않은 경로로 가고 있다면 탐색
  else:
    visited[h][w] = 0
    for dh, dw in moves:
      new_h, new_w = h+dh, w+dw
      #dp의 점화식: dp: a->b,c일 때 a에서 목적지로 가는 경우의 수는 b에서 목적지로 가는 경우의 수 + c에서 목적지로 가는 경우의 수
      if 0<=new_h<m and 0<=new_w<n and graph[new_h][new_w] < graph[h][w]:
        ways += dfs(new_h, new_w)
  visited[h][w] = ways
  return ways
        
print(dfs(0,0))
    
      


  
      
        
    
  
