import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = []
num_of_houses = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
    
def bfs(graph, start_node):
    need_visited = deque() #dfs를 하기 위해 필요한 stack
    need_visited.append((start_node[0],start_node[1])) #시작
    graph[start_node[0]][start_node[1]] = 0
    sum=1
    while need_visited:
        node = need_visited.popleft() #방문해야 할 node 가져오기
        for k in range(4):
            new_x = node[0]+dx[k]
            new_y = node[1]+dy[k]
            if(new_x<0 or new_x>=n or new_y<0 or new_y>=n):
                continue
            if(graph[new_x][new_y]==1):
                sum+=1
                graph[new_x][new_y]=0
                need_visited.append((new_x, new_y))
    return sum

for i in range(n):
    for j in range(n):
        if(graph[i][j]==1):
            num_of_houses.append(bfs(graph,(i,j)))

num_of_houses.sort()

print(len(num_of_houses))
for num in num_of_houses:
    print(num)
        
    

    




