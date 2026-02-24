import sys
from collections import deque

input = sys.stdin.readline


moves = [(1,0), (-1,0),(0,1),(0,-1)]
r,c = map(int, input().split())
maps = []
for _ in range(r):
  maps.append(list(input().rstrip()))

gooses = deque()
waters = deque()


water_visited = [[False]*c for _ in range(r)]
goose_visited = [[False]*c for _ in range(r)]

gooses_place = []
for i in range(r):
  for j in range(c):
    if maps[i][j] == 'L':
      gooses_place.append((i,j))
      #거위도 물
      waters.append((i,j))
      water_visited[i][j] = True

    elif maps[i][j] == '.':
      waters.append((i,j))
      water_visited[i][j] = True
      

"""
물에서 bfs해서 녹을 애들을 저장 -> 이 애들에서 bfs 다시 시작

하나의 L에서 시작해서 벽에 닿아서 끝난 애들 저장 -> 이 애들에서 bfs 다시 시작
"""


def bfs_water():
  global waters
  will_melt = deque()
    
  while waters:
    h,w = waters.popleft()
    for dh, dw in moves:
      new_h,new_w = h+dh, w+dw
      if 0<=new_h<r and 0<=new_w<c and not water_visited[new_h][new_w]:
        #벽이라면 얘네들은 이제 녹을 애들
        if maps[new_h][new_w] == 'X':
          will_melt.append((new_h, new_w))
          water_visited[new_h][new_w] = True

  waters = will_melt
  return will_melt
  

gooses.append(gooses_place[0])
goose_visited[gooses_place[0][0]][gooses_place[0][1]] = True
def bfs_goose():
  global gooses
  will_goose = deque()

  while gooses:
    h,w = gooses.popleft()
    if (h,w) == gooses_place[1]:
      return deque()
    for dh, dw in moves:
      new_h,new_w = h+dh, w+dw
      if 0<=new_h<r and 0<=new_w<c and not goose_visited[new_h][new_w]:
        #물이라면 계속 지나감, 벽에 닿는 애들에서 bfs을 다시 하도록 저장
        if maps[new_h][new_w] == '.':
          gooses.append((new_h, new_w))
          goose_visited[new_h][new_w] = True
        elif maps[new_h][new_w] == 'X':
          will_goose.append((new_h, new_w))
          goose_visited[new_h][new_w] = True
        #goose을 만났다면
        else:
          return deque()
          

  gooses = will_goose
  return will_goose



days = 0

while True:
  will_goose = bfs_goose()
  #지금 만날 수 있다면
  if not will_goose:
    break

  #지금 못 만나면 녹을 얼음 있는지 확인
  will_melt = bfs_water()

  if not will_melt:
    break
  #녹여
  for i,j in will_melt:
    maps[i][j] = '.'
    
  days+=1

print(days)
    




          
 

        
          
          
          
      
  


  

 
        
      
  
      
    
  
  
        
    

  
  
      