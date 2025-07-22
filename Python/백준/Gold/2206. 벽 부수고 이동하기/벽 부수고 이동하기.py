import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = set()
distance = float(1e9)


def dfs(start):
  global distance
  q = deque()
  start_h, start_w, broke, dist = start
  q.append((start_h, start_w, broke, dist))
  visited.add((start_h, start_w, broke))

  while q:
    h, w, broke, dist = q.popleft()
    #찾았다면
    if h == n - 1 and w == m - 1:
      distance = min(distance, dist)
      continue
    #순회 dfs
    for dh, dw in moves:
      new_h, new_w = h+dh, w+dw
      if 0<=new_h<n and 0<=new_w<m:
        #지나갈 수 있다면 지나가기
        if maze[new_h][new_w] == 0:
          if (new_h, new_w, broke) not in visited:
            q.append((new_h, new_w, broke, dist + 1))
            visited.add((new_h, new_w, broke))
        else:
          #지나갈 수 없는데 부수는거 사용 안 했다면
          if not broke and (new_h, new_w) not in visited:
            q.append((new_h, new_w, True, dist + 1))
            visited.add((new_h, new_w, True))


dfs((0, 0, False, 1))
if distance == float(1e9):
  print(-1)
else:
  print(distance)
