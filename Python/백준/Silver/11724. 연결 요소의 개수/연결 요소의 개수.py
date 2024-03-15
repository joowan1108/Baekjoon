import sys
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
count = 0

def dfs(graph, start, visited):
    need_visit = deque()
    need_visit.append(start)
    while need_visit:
        node = need_visit.pop()
        if(visited[node]==0):
            visited[node]=1
            need_visit.extend(graph[node])
    return 1
    
for i in range(n):
    if(visited[i+1]!=1):
        count+=dfs(graph, i+1, visited)
print(count)


    
        
        
    
