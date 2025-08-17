import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  indegree[b]+=1

result = []
q = deque()
for i in range(1,n+1):
  if indegree[i]==0:
    q.append(i)
    
while q:
  cur = q.popleft()
  result.append(cur)
  for adj in graph[cur]:
    indegree[adj]-=1
    if indegree[adj]==0:
      q.append(adj)

for i in range(n):
  print(result[i], end=' ')


  
    