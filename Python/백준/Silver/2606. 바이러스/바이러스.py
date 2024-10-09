import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(list)
stack = deque()
for _ in range(m):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False]*(n+1)

def dfs(start):
    stack.append(start)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v]=True
            for u in graph[v]:
                stack.append(u)

dfs(1)
print(visited.count(True)-1)
    
    
    