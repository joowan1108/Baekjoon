import sys
from collections import deque

t = int(input())
moves = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(graph, visited, start_w, start_h):
    need_visited = deque()
    need_visited.append((start_h, start_w))
    while need_visited:
        node_height, node_width = need_visited.popleft()
        if(visited[node_height][node_width]==0 and graph[node_height][node_width]==1):
            visited[node_height][node_width]=1
            for dx, dy in moves:
                new_height = node_height+dy
                new_width = node_width + dx
                if(0<=new_height<height and 0<=new_width<width):
                    need_visited.append((new_height, new_width))
                    
    return visited
    
    
    
for _ in range(t):
    worms = 0
    width, height, vegs = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0 for _ in range(width)] for _ in range(height)]
    visited = [[0 for _ in range(width)] for _ in range(height)]
    for _ in range(vegs):
        w, h = map(int, sys.stdin.readline().rstrip().split())
        graph[h][w]=1
    for i in range(height):
        for j in range(width):
            if(graph[i][j]==1 and visited[i][j]==0):
                visited = bfs(graph, visited, j, i)
                worms+=1
        
    print(worms)
        
