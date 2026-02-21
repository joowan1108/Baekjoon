import sys
from collections import deque

input = sys.stdin.readline

"""
불로 먼저 bfs해서 각 칸에 도달하는 시간 기록

그 다음 사람이 불보다 먼저 도착하는 칸 + 벽이 아닌 공간에만 도달할 수 있게 bfs

100*1000*1000*2

200000000

isinstance 함수가 시간이 오래 걸리낭.

"""

moves = [(1,0),(-1,0),(0,1),(0,-1)]
T = int(input())

for _ in range(T):
  w,h = map(int, input().split())
  maps = []
  for _ in range(h):
    maps.append(list(input().rstrip()))

  # 탈출 위치 + 불, 사람 시작 위치
  ends = set()
  fires = []
  start_h, start_w = 0,0
  fire_t = [[-1]*w for _ in range(h)]
  person_t = [[-1]*w for _ in range(h)]
  for i in range(h):
    for j in range(w):
      if maps[i][j] == '@':
        start_h, start_w = i,j
        person_t[start_h][start_w] = 1
      elif maps[i][j] == '*':
        fires.append((i,j))
        fire_t[i][j] = 1

  # 불 먼저 bfs해서 각 가능한 칸에 도달하는 최소 시간 기록
  q = deque(fires)
  while q:
    fire_h, fire_w = q.popleft()
    for dh, dw in moves:
      new_h, new_w = fire_h+dh, fire_w+dw
      if 0<=new_h<h and 0<=new_w<w and maps[new_h][new_w]!="#":
        #빈 곳이라면
        if (maps[new_h][new_w] == '.' or maps[new_h][new_w] == '@') and fire_t[new_h][new_w] == -1:
          #이전 불 위치보다 1 증가
          fire_t[new_h][new_w] = fire_t[fire_h][fire_w] + 1
          q.append((new_h, new_w))

    
  #사람 bfs
  q = deque([(start_h, start_w)])
  found = False
  while q:
    cur_h, cur_w = q.popleft()
    #탈출 지점에 도착했다면
    if cur_h==h-1 or cur_h==0 or cur_w == 0 or cur_w == w-1:
      found = True
      print(person_t[cur_h][cur_w])
      break
    for dh, dw in moves:
      new_h, new_w = cur_h + dh, cur_w + dw
      if 0<=new_h<h and 0<=new_w<w and maps[new_h][new_w]!="#" and person_t[new_h][new_w] == -1:
        #사람이 도달하는 시간이 불 도달 시간보다 빠르다면 이동
        if fire_t[new_h][new_w] == -1 or fire_t[new_h][new_w] > person_t[cur_h][cur_w]+1:
          q.append((new_h, new_w))
          person_t[new_h][new_w] = person_t[cur_h][cur_w]+1
          
  if not found:
    print("IMPOSSIBLE")
  
  
        
    

  
  
      