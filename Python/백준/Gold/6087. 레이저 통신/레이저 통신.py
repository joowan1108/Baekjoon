import sys
import heapq
from collections import deque
input = sys.stdin.readline

"""
구하는 것은 최단 거리가 아니라 최소 방향 전환 횟수이다.

priority queue의 우선순위를 방향 전환 횟수로..?
"""

w,h = map(int, input().split())

start_h, start_w, dest_h, dest_w = 0,0,0,0
maps = []

first = False

for l in range(h):
  line = list(input().rstrip())
  maps.append(line)
  for i in range(w):
    if line[i] == 'C':
      if first:
        dest_h, dest_w = l, i
      else:
        start_h, start_w = l, i
        first = True

moves = [(0,1), (0,-1), (1,0), (-1,0)]


def dijkstra():
  q = []
  heapq.heappush(q,(-1, start_h, start_w))
  nums_change = [[int(1e9)]*w for _ in range(h)]
  nums_change[start_h][start_w] = 0

  while q:
    mid_change, mid_h, mid_w = heapq.heappop(q)
    if nums_change[mid_h][mid_w] < mid_change:
      continue
    for dh,dw in moves:
      end_h, end_w = mid_h+dh, mid_w+dw
      # valid한 좌표일 때
      while 0<=end_h<h and 0<=end_w<w and maps[end_h][end_w] != '*':
        new_change = mid_change+1
        if new_change < nums_change[end_h][end_w]:
          nums_change[end_h][end_w] = new_change
          heapq.heappush(q, (new_change, end_h, end_w))

        end_h+=dh
        end_w+=dw
        
            
  return nums_change
  
mirrors = dijkstra()
print(mirrors[dest_h][dest_w])

"""
for i in range(h):
  for j in range(w):
    if mirrors[i][j] == int(1e9):
      mirrors[i][j] = 'w'
    
for mirror in mirrors:
  print(mirror)

for mapp in maps:
  print(mapp)

      
"""

