import sys
import copy
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = []

for _ in range(n):
    input_lst = list(sys.stdin.readline().rstrip())
    graph.append(input_lst)

weird_graph = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if(weird_graph[i][j]=='G'):
            weird_graph[i][j]='R'
    
visited_weird = [[0 for _ in range(n)] for _ in range(n)]
visited_normal = [[0 for _ in range(n)] for _ in range(n)]
num_of_areas_weird = 0
num_of_areas = 0

def dfs(dfs_graph,x,y, visited):
    start = dfs_graph[x][y]
    need_visit = deque()
    need_visit.append((x,y))
    
    while need_visit:
        node = need_visit.pop()
        if(visited[node[0]][node[1]]==0 and dfs_graph[node[0]][node[1]]==start):
            visited[node[0]][node[1]]=1
            for dx,dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                new_x = node[0]+dx
                new_y = node[1]+dy
                if(new_x<0 or new_x>=n or new_y<0 or new_y>=n):
                    continue
                else:
                    need_visit.append((new_x, new_y))
    return visited
                

for i in range(n):
    for j in range(n):
        if(visited_weird[i][j]==0):
            visited_weird = dfs(weird_graph,i,j, visited_weird)
            num_of_areas_weird+=1

for i in range(n):
    for j in range(n):
        if(visited_normal[i][j]==0):
            visited_normal = dfs(graph,i,j, visited_normal)
            num_of_areas+=1
            
print("{} {}".format(num_of_areas, num_of_areas_weird))




    
        
        
    
