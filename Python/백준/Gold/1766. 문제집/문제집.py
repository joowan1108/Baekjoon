import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  indegree[b]+=1

q = []
result = []

for i in range(1,n+1):
  if indegree[i]==0:
    heapq.heappush(q, i)

"""
q에는 순서가 다 다가온 애들이 들어간다
이 중에서도 숫자가 제일 작은 애를 풀어야 하므로 priority queue를 쓰면 간편함
"""
while q:
  cur = heapq.heappop(q)
  result.append(cur)
  for adj in graph[cur]:
    indegree[adj]-=1
    if indegree[adj]==0:
      heapq.heappush(q, adj)

for r in result:
  print(r, end=' ')

    
    
    




  
    