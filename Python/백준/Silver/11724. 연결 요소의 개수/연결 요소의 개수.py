import sys
from collections import defaultdict, deque
 
input = sys.stdin.readline
graph = defaultdict(list)
 
n,m = map(int, input().split())
 
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
visited = [False]*(n+1)
 
def bfs(start):
    q=deque()
    q.append(start)
    visited[start]=True
    while q:
        node = q.popleft()
        for tmp in graph[node]:
            if not visited[tmp]:
                q.append(tmp)
                visited[tmp]=True
result = 0
for g in range(1,n+1):
    if not visited[g]:
        bfs(g)
        result+=1
print(result)