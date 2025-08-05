import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

min_road = sys.maxsize

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]



#가장자리 
coords = []


visited = set()
island_id = 2
for i in range(n):
  for j in range(n):
    #아직 bfs가 진행되지 않은 육지 찾기
    if graph[i][j] == 1 and (i, j) not in visited:
      is_edge = False
      visited.add((i,j))
      graph[i][j] = island_id
      q = deque()
      q.append((i, j))
      while q:
        h, w = q.popleft()
        for dh, dw in moves:
          new_h, new_w = h + dh, w + dw
          if 0 <= new_h < n and 0 <= new_w < n:
            if graph[new_h][new_w] == 1:
              q.append((new_h, new_w))
              visited.add((new_h, new_w))
              graph[new_h][new_w] = island_id
            elif graph[new_h][new_w] == 0:
              is_edge = True
        if is_edge:
          coords.append((h, w, island_id))
      island_id += 1

#island id가 다른 가장자리 좌표들끼리의 거리의 최솟값 구하기


combs = combinations(coords, 2)
for c1, c2 in combs:
  h1,w1,id1 = c1
  h2,w2,id2 = c2
  if id1==id2:
    continue
  min_road = min(min_road, abs(h1-h2)+abs(w1-w2))

print(min_road-1)