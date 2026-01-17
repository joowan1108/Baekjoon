import sys
from collections import deque

input = sys.stdin.readline
"""

0,0에서 0에서만 움직이면서 bfs를 하여 1을 발견하면, 그 치즈는 이제 없어질 치즈이기에 이 좌표들을 저장하여 bfs가 끝나면 0으로 바꿈

이 과정을 발견한 치즈가 없을 때까지 반복

이 과정을 반복한 횟수가 답이다.

"""

n,m = map(int,input().split())

maps = []
for _ in range(n):
  maps.append(list(map(int, input().split())))

moves = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs():
  q = deque([(0,0)])
  visited = [[False]*(m) for _ in range(n)]
  visited[0][0] = True

  melts = []
  while q:
    h,w = q.popleft()
    for dh, dw in moves:
      new_h, new_w = h+dh, w+dw
      if 0<=new_h<n and 0<=new_w<m and not visited[new_h][new_w]:
        #치즈 아니라면
        if maps[new_h][new_w]==0:
          visited[new_h][new_w] = True
          q.append((new_h, new_w))
        #치즈라면
        else:
          visited[new_h][new_w] = True
          melts.append((new_h, new_w))

  return melts

time = 0
befores = []
while True:
  melts = bfs()
  if melts:
    time+=1

    before=0
    for h,w in melts:
      maps[h][w] = 0
      before += 1

    befores.append(before)

  else:
    break

print(time)
print(befores.pop())
      
        
    
  