
import sys
from collections import deque
import copy

n,m,v = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    i,j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)
graph_dfs = copy.deepcopy(graph)

for i in range(1, n+1):
    graph[i].sort()
    graph_dfs[i].sort(reverse=True)

def bfs(graph, start):
    visited = set()
    need_visited = deque()
    need_visited.append(start)
    while need_visited:
        node = need_visited.popleft()
        if(node not in visited):
            visited.add(node)
            need_visited.extend(graph[node])
            print(node, end= ' ')

def dfs(graph, start):
    visited = set()
    need_visited = deque()
    need_visited.append(start)
    while need_visited:
        node = need_visited.pop()
        if(node not in visited):
            visited.add(node)
            need_visited.extend(graph[node])
            print(node, end= ' ')

dfs(graph_dfs, v)
print()
bfs(graph, v)
