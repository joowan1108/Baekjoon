from collections import deque
import sys

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)] 

for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
    
visited= [0 for _ in range(n+1)]

record = [0 for _ in range(n+1)]

def dfs(graph, start):
    need_visited = deque()
    visited= [0 for _ in range(n+1)]
    need_visited.append(start)
    while need_visited:
        node = need_visited.pop()
        for nod in graph[node]:
            if(visited[nod]==0):
                visited[nod]=1
                record[nod]=node
                need_visited.append(nod)

dfs(graph, 1)
for i in range(2, n+1):
    print(record[i])
    
