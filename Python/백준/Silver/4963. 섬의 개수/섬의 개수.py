import sys
from collections import deque

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if(w==0 and h==0):
        break
    graph = []
    cnt = 0
    for _ in range(h):
        input_row = list(map(int, sys.stdin.readline().rstrip().split()))
        graph.append(input_row)
        
    visited = [[0 for _ in range(w)] for _ in range(h)]
    
    def dfs(graph, start_x, start_y, visited):
        need_visited = deque()
        need_visited.append((start_x, start_y))
        while need_visited:
            x,y = need_visited.pop()
            for i,j in [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1), (1,-1), (1,1)]:
                new_x = x+i
                new_y = y+j
                if(new_x<0 or new_x>=h or new_y<0 or new_y>=w):
                    continue
                if(visited[new_x][new_y]==0 and graph[new_x][new_y]==1):
                    visited[new_x][new_y]=1
                    need_visited.append((new_x, new_y))
        return visited
    for i in range(0,h):
        for j in range(0, w):
            if(graph[i][j]==1 and visited[i][j]==0):
                visited = dfs(graph, i, j, visited)
                cnt+=1
            
    print(cnt)
                        
    
            
            
        
    
    
        
        
    

    
    
            




    
