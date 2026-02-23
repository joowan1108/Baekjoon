import sys
from collections import deque

input = sys.stdin.readline

'''
각 플레이어마다 확장을 한번 하고 난 뒤의 queue을 저장해놓고 다시 자기의 턴이 되면 그 queue을 그대로 bfs
'''
n,m,p = map(int, input().split())

s = [0] + list(map(int, input().split()))
maps = []

for _ in range(n):
  maps.append(list(input().rstrip()))

moves = [(0,1),(0,-1),(1,0),(-1,0)]

is_placed = [[0]*m for _ in range(n)]

#각 플레이어들의 queue
queues = [deque() for _ in range(p+1)]

#각 플레이어가 확장한 수
placed_nums = [0]*(p+1)

for i in range(n):
  for j in range(m):
    if maps[i][j]!='#' and maps[i][j]!='.':
      queues[int(maps[i][j])].append((i,j,0))
      is_placed[i][j] = int(maps[i][j])
      placed_nums[int(maps[i][j])] += 1

# for place in is_placed:
#   print(place)

# print('=========')
      
'''
expand 만큼 확장하고 끝내기. 남은 지점들은 queue에 저장
확장된 곳은 is_placed에 저장
하나도 확장을 하지 못한다면 0, 확장이 가능하다면 1을 출력
'''

def bfs(player, queue, expand, turn):
  q = deque(queue)
  expanded_once = False
  while q:
    h,w,times = q.popleft()
    #expand 만큼 확장해서 생긴 castle이 존재하게 된다면 끝내기
    if times == expand*turn:
      q.appendleft((h,w,times))
      break
    for dh,dw in moves:
      new_h, new_w = h+dh, w+dw
      #벽이 아니고 빈 곳일 때만 확장이 가능
      if 0<=new_h<n and 0<=new_w<m and (maps[new_h][new_w]=='.' and is_placed[new_h][new_w]==0):
        q.append((new_h, new_w, times+1))
        is_placed[new_h][new_w] = player
        placed_nums[player]+=1
        expanded_once = True
        
  queues[player] = q
  # for place in is_placed:
  #   print(place)
  # print('=========')
  if expanded_once:
    return 1

  else:
    return 0
  
    
        
    
turns = 1 # turn 수
did_expand = 0 # 모든 플레이어들이 확장했는지 확인
expanded = [True]*(p+1) #전 turn에 확장했는지 확인

while True:
  for player in range(1,p+1):
    #전에 확장하지 못했다면 넘기기
    if not expanded[player]:
      continue
    
    result = bfs(player, queues[player], s[player], turns)
    if result == 1:
      did_expand+=1
      expanded[player] = True
    else:
      expanded[player] = False
  
  #확장이 아무도 안 되었다면
  if did_expand == 0:
    break
  #한명이라도 확장이 되었다면
  else:
    turns+=1
    did_expand = 0

print(*placed_nums[1:])


  

 
        
      
  
      
    
  
  
        
    

  
  
      