import sys
from collections import deque
input = sys.stdin.readline

max_area = 0
paints = 0 

moves = [(1,0), (0,1), (-1,0), (0,-1)]

n,m = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

ones = set()
lst = deque()

def bfs(start_h, start_w, ones):
  q = deque([(start_h, start_w)])
  visited = set()
  visited.add((start_h, start_w))
  area = 1
  while q:
    h, w = q.popleft()
    for dh, dw in moves:
      new_h = h + dh
      new_w = w + dw
      if 0<=new_h<n and 0<=new_w<m and graph[new_h][new_w]==1:
        if (new_h, new_w) not in visited:
          q.append((new_h, new_w))
          visited.add((new_h, new_w))
          ones.remove((new_h, new_w))
          area += 1

  return ones, area
  
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      ones.add((i,j))
      lst.append((i,j))

#1이 존재하지 않을 때
if len(lst)==0:
  print(0)
  print(0)
  

else:
  #모든 1에 대해 bfs한다. --> return 되는 횟수 = 그림의 수, 넓이는 bfs 할 때마다 갱신
  for h,w in lst:
    if (h,w) not in ones:
      continue
    ones, area = bfs(h, w, ones)
    paints += 1
    max_area = max(area, max_area)

  print(paints)
  print(max_area)
  
      








