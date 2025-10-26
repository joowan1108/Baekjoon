import sys
from collections import deque
input = sys.stdin.readline

'''

'''


n,m = map(int, input().split())
maps = []
for _ in range(n):
  mapp = list(input().rstrip())
  line = []
  for ma in mapp:
    line.append(int(ma))
  maps.append(line)

moves = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(i,j):
  all_zeros = set()
  all_zeros.add((i,j))
  q = deque()
  visited = set()
  q.append((i,j))
  visited.add((i,j))
  cnt = 1
  while q:
    h,w = q.popleft()
    for dh,dw in moves:
      new_h, new_w = h+dh, w+dw
      if 0<=new_h<n and 0<=new_w<m and maps[new_h][new_w]==0 and (new_h, new_w) not in visited:
        cnt+=1
        visited.add((new_h, new_w))
        q.append((new_h, new_w))
        all_zeros.add((new_h, new_w))
  return cnt, all_zeros
        

group = -1
groups = dict()
grouped = set()
for i in range(n):
  for j in range(m):
    if maps[i][j] == 0 and (i,j) not in grouped:
      cnt, zeros = bfs(i,j)
      groups[group] = cnt
      for h,w in zeros:
        grouped.add((h,w))
        maps[h][w] = group
      group-=1
        
# blood fill을 다 한 상태에서 1들에 대해서 각 group의 이어진 0 개수 네 방향으로 더하기

for h in range(n):
  for w in range(m):
    if maps[h][w] == 1:
      nearby = set()
      cnt = 1
      for dh,dw in moves:
        new_h,new_w = h+dh, w+dw
        #그룹된 애들
        if 0<=new_h<n and 0<=new_w<m and maps[new_h][new_w] < 0:
          nearby.add(maps[new_h][new_w])
      for near in nearby:
        cnt += groups[near]
      maps[h][w] = cnt

#0이었던 곳들 다시 0으로 표시
for h,w in grouped:
  maps[h][w] = 0

for mapp in maps:
  for ma in mapp:
    print(ma%10,end='')
  print()
          
      

      
        
        
    

        
      
    
    
  

  
