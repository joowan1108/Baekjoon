import sys
from collections import deque

input = sys.stdin.readline
"""
1000000 -> bfs 두번 가능
불 위치에서 bfs를 진행해서 각 칸에 걸리는 시간을 구한다.
그 다음 J 위치에서 bfs를 진행해서 벽이 아니면서 불이 도달한 시간보다 작은 곳들만 가면서 시간을 재면 된다.
"""

n, m = map(int, input().split())
maze = []
j_h, j_w = 0, 0
fires = []
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for h in range(n):
  row = list(input().rstrip())
  maze.append(row)
  for w in range(len(row)):
    if row[w] == 'J':
      j_h, j_w = h, w
    elif row[w] == 'F':
      fires.append((h,w))

#불이 여러개일 수 있다
fire_time = [[-1]*m for _ in range(n)]
for h,w in fires:
  fire_time[h][w] = 0


j_time = [[-1]*m for _ in range(n)]
j_time[j_h][j_w] = 0


def bfs(fires, j_h, j_w):
  min_dist = -1
  for f_h, f_w in fires:
    q = deque([(f_h, f_w)])
    while q:
      h,w = q.popleft()
      for dh, dw in moves:
        new_h, new_w = h+dh, w+dw
        #index 맞고 벽 아니고 방문한 적 없거나 이전 불 위치가 간 시간보다 짧을 때만 update
        if 0<=new_h<n and 0<=new_w<m and (maze[new_h][new_w]!="#" and maze[new_h][new_w]!='F') and (fire_time[new_h][new_w] == -1 or fire_time[h][w]+1 < fire_time[new_h][new_w]):
          fire_time[new_h][new_w] = fire_time[h][w]+1
          q.append((new_h, new_w))

  
  q = deque()
  q.append((j_h, j_w))
  while q:
    h,w = q.popleft()
    if (h==n-1 or w==m-1 or h==0 or w==0) and j_time[h][w]!=-1:
      min_dist = j_time[h][w]
      break
    for dh, dw in moves:
      new_h, new_w = h+dh, w+dw
      if 0<=new_h<n and 0<=new_w<m and maze[new_h][new_w]=='.' and j_time[new_h][new_w] == -1:
        #불이 지나간 시간보다 짧을 때거나 불이 도달하지 못한 곳이면 이동
        if j_time[h][w]+1 < fire_time[new_h][new_w] or fire_time[new_h][new_w]==-1:
          j_time[new_h][new_w] = j_time[h][w]+1
          q.append((new_h,new_w))

  return min_dist

ans = bfs(fires, j_h, j_w)
if ans >= 0:
  print(ans+1)
else:
  print("IMPOSSIBLE")
