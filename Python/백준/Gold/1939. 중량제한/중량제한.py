import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
max_w = 0
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
  max_w = max(max_w, c)

start, end = map(int, input().split())

"""
start에서 특정 무게 제한은 지닌채로 bfs를 진행
bfs를 진행하면서 물품 무게가 중량제한 때문에 목적지에 도달하지 못한다면 물품 무게를 바꿈

100000*log(100000)*log(1000000000) = 4500000
"""

def bfs(start, end, weight):
  q = deque([start])
  visited = set()
  visited.add(start)
  while q:
    s = q.popleft()
    if s==end:
      #더 큰 범위 탐색해보기
      return weight+1
    for adj,limit in graph[s]:
      if adj not in visited and limit >= weight:
        q.append(adj)
        visited.add(adj)
  #범위 더 줄이기
  return weight-1
      
def binary_search(min_, max_, start, end):
  while min_ <= max_:
    mid = (min_+max_)//2
    new_mid = bfs(start, end, mid)
    #범위를 작은 쪽으로 옮겨야 한다면
    if new_mid == mid-1:
      max_ = mid-1
    else:
      min_ = mid+1
  return max_

ans = binary_search(0, max_w, start, end)
print(ans)
  
  

  
    


    
        
    
  


  
    
  



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  