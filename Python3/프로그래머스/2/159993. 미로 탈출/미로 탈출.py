from collections import deque

moves = [(0,1), (0,-1), (1,0), (-1,0)]
def bfs(graph, start_h, start_w, target):
    visited = [[False]*len(graph[0]) for _ in range(len(graph))]
    q = deque([(start_h, start_w, 0)])
    visited[start_h][start_w] = True
    while q:
        h,w, time = q.popleft()
        if graph[h][w] == target:
            return time, h, w
        for move in moves:
            new_h, new_w, new_time = h+move[0], w+move[1], time+1
            if 0<=new_h<len(graph) and 0<=new_w<len(graph[0]) and (graph[new_h][new_w] != 'X'):
                if not visited[new_h][new_w]:
                    visited[new_h][new_w]=True
                    q.append((new_h, new_w, new_time))
    return -1,-1,-1

def solution(maps):
    graph = []
    for map in maps:
        graph.append([m for m in map])
    
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]=='S':
                start_h, start_w = i,j
    
    time_lever, lever_h, lever_w = bfs(graph, start_h, start_w, "L")
    if time_lever == -1:
        return -1
    time_exit, exit_w, exit_lever = bfs(graph, lever_h, lever_w, "E")
    if time_exit == -1:
        return -1
    return time_lever + time_exit
    