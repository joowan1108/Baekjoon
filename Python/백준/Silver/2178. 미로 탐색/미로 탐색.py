import sys
from collections import deque
n,m = map(int, sys.stdin.readline().rstrip().split())

graph = []
moves = [(0,1),(0,-1),(1,0),(-1,0)]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

def bfs(start_h, start_w):
    need_visited = deque()
    need_visited.append((start_h, start_w))
    while need_visited:
        h,w= need_visited.popleft()
        for dh, dw in moves:
            new_h = h+dh
            new_w = w+dw
            if(0<=new_h<n and 0<=new_w<m and graph[new_h][new_w]==1):
                need_visited.append((new_h, new_w))
                graph[new_h][new_w] = graph[h][w] + 1
    
    
bfs(0,0)
print(graph[n-1][m-1])

    
