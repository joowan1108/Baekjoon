import sys
from collections import deque
n = int(sys.stdin.readline())

regions = []

max_Val=0
min_Val=101
for _ in range(n):
    input_lst = list(map(int, sys.stdin.readline().rstrip().split()))
    new_max = max(input_lst)
    new_min = min(input_lst)
    if(max_Val < new_max):
        max_Val = new_max
    if(min_Val > new_min):
        min_Val = new_min
    regions.append(input_lst)

safety_nums = []

def dfs(region, start_x, start_y, visited):
    need_visited = deque()
    need_visited.append((start_x, start_y))
    while need_visited:
        x,y = need_visited.pop()
        visited[x][y]=1
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            new_x = x+dx
            new_y = y+dy
            if(new_x<0 or new_x>=n or new_y<0 or new_y>=n):
                continue
            if(visited[new_x][new_y]==0 and region[new_x][new_y]==1):
                visited[new_x][new_y]=1
                need_visited.append((new_x,new_y))
    return visited

for k in range(min_Val, max_Val+1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    regions_copy = [row[:] for row in regions]
    for i in range(n):
        for j in range(n):
            if(regions_copy[i][j]>k):
                regions_copy[i][j]=1
            else:
                regions_copy[i][j]=0
    safety_num = 0
    
    for i in range(n):
        for j in range(n):
            if(visited[i][j]==0 and regions_copy[i][j]==1):
                visited = dfs(regions_copy,i,j, visited)
                safety_num+=1

    safety_nums.append(safety_num)
safety_nums.append(1)

print(max(safety_nums))
            




    
