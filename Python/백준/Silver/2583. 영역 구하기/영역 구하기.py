import sys
from collections import deque
width,height,k = map(int, sys.stdin.readline().rstrip().split())


graph = [[1 for _ in range(width)] for _ in range(height)]
areas = []
moves = [(0,1),(0,-1),(1,0),(-1,0)]
visited = set()
def bfs(i,j):
    global areas
    area = 1
    need_visited = deque()
    need_visited.append((i,j))
    visited.add((i,j))
    while need_visited:
        x,y = need_visited.popleft()
        for dx,dy in moves:
            new_x = x+dx
            new_y = y+dy
            if(0<=new_x<height and 0<=new_y<width and graph[new_x][new_y]==1 and (new_x, new_y) not in visited):
                visited.add((new_x, new_y))
                need_visited.append((new_x, new_y))
                area +=1
    areas.append(area)
                
    
    
for _ in range(k):
    x,y,xx,yy = map(int, sys.stdin.readline().rstrip().split())
    for i in range(x, xx):
        for j in range(y, yy):
            graph[i][j] = 0

for i in range(height):
    for j in range(width):
        if(graph[i][j]==1 and (i,j) not in visited):
            bfs(i,j)

print(len(areas))
areas.sort()
for a in areas:
    print(a, end=' ')
