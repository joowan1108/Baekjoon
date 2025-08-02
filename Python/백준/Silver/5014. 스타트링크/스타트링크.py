import sys
from collections import deque

input = sys.stdin.readline

total, start, target, u, d = map(int, input().split())
d = -d

q = deque()
q.append((start, 0))
visited = set()
visited.add(start)
ans = -1

while q:
  s, buttons = q.popleft()
  if s==target:
    ans = buttons
    break
  for move in [u,d]:
    new_s = s + move
    if 1<=new_s<=total and new_s not in visited:
      q.append((new_s, buttons+1))
      visited.add(new_s)

if ans!=-1:
  print(ans)
else:
  print("use the stairs")




      
  
  