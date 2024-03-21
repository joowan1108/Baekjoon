
import sys
from collections import deque
height, width = map(int, sys.stdin.readline().rstrip().split())
graph = []
moves = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(height):
    graph.append(list(sys.stdin.readline().rstrip()))

def bfs(graph, start_height, start_width):
    need_visited = set()
    need_visited.add((start_height, start_width, graph[start_height][start_width]))
    result = 1
    while(need_visited):
        h, w, v = need_visited.pop()
        for dx,dy in moves:
            new_h = h+dx
            new_w = w+dy
            if((0<=new_h<height) and (0<=new_w<width)) and (graph[new_h][new_w] not in v):
                need_visited.add((new_h, new_w, v+graph[new_h][new_w]))
                result = max(result, len(v)+1)
    return result

print(bfs(graph, 0,0))
