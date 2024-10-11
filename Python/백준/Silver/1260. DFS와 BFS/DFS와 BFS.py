from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n,m,v = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    graph[g].sort()

visited_dfs = [0 for _ in range(n+1)]
dfs_result = []
def dfs(start):
    visited_dfs[start]=1
    dfs_result.append(start)
    for i in graph[start]:
        if visited_dfs[i]!=1:
            dfs(i)
        
dfs(v)

visited_bfs = [0 for _ in range(n+1)]
bfs_result = []
def bfs(start):
    q = deque()
    visited_bfs[start]=1
    q.append(start)
    while q:
        tmp = q.popleft()
        bfs_result.append(tmp)
        for t in graph[tmp]:
            if visited_bfs[t]!=1:
                q.append(t)
                visited_bfs[t]=1

bfs(v)

for i in range(len(dfs_result)-1):
    print(dfs_result[i], end=' ')
print(dfs_result[-1])

for i in range(len(bfs_result)-1):
    print(bfs_result[i], end=' ')
print(bfs_result[-1])
    

    