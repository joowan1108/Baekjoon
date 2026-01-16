import sys
from collections import deque
input = sys.stdin.readline

"""
bfs를 하면 한 점에서 다른 점으로 갈 수 있다면 양수로, 가능하지 않다면 0으로 나올 것이다.

 bfs의 시작점은 여행 계획의 첫 도시로 한다.
"""

n = int(input())

m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
  connects = list(map(int, input().split()))
  for j in range(len(connects)):
    if connects[j]==1:
      graph[i].append(j+1)
      graph[j+1].append(i)
  

travel = list(map(int, input().split()))

def bfs(start):
  visited = set()
  q = deque()
  q.append(start)
  visited.add(start)
  while q:
    tmp = q.popleft()
    for b in graph[tmp]:
      if b not in visited:
        q.append(b)
        visited.add(b)
  return visited

        
avail_cities = bfs(travel[0])

avail = True

for i in range(1,len(travel)):
  if travel[i] not in avail_cities:
    avail = False

if avail:
  print("YES")
else:
  print("NO")
    
        

  
  
  
    
    
    
  
  

      
  















