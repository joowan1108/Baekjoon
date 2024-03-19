import sys
from collections import deque

test = int(sys.stdin.readline().rstrip())

moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1, -2),(-2,-1)]

def bfs(start_x, start_y, end_x, end_y, graph, visited, size):
    need_visited = deque()
    need_visited.append((start_x, start_y))
    visited[start_x][start_y]=1
    while need_visited:
        loc_x, loc_y = need_visited.popleft()
        if(loc_x == end_x and loc_y == end_y):
            return graph[loc_x][loc_y]
        for dx,dy in moves:
            new_x = loc_x + dx
            new_y = loc_y + dy
            if(new_x<0 or new_x>=size or new_y<0 or new_y>=size):
                continue
            if(visited[new_x][new_y]==0):
                need_visited.append((new_x, new_y))
                visited[new_x][new_y]=1
                graph[new_x][new_y] = graph[loc_x][loc_y] + 1

for _ in range(test):
    size = int(sys.stdin.readline().rstrip())
    graph = [[0 for _ in range(size)] for _ in range(size)]
    
    visited = [[0 for _ in range(size)] for _ in range(size)]
    start_x, start_y = map(int, sys.stdin.readline().rstrip().split())
    end_x, end_y = map(int, sys.stdin.readline().rstrip().split())
    result = bfs(start_x, start_y, end_x, end_y, graph, visited, size)
    print(result)
                
    
            
    

            
            
        
    
    
        
        
    

    
    
            




    
