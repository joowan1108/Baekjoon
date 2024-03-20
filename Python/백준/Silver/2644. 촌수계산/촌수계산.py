import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())
target_1, target_2 = map(int, sys.stdin.readline().rstrip().split())
relate_num = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]

moves_num = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(relate_num):
    input_1, input_2 = map(int, sys.stdin.readline().rstrip().split())
    graph[input_1].append(input_2)
    graph[input_2].append(input_1)



def bfs(graph, start, end, visited):
    need_visited = deque()
    need_visited.append(start)
    while need_visited:
        node = need_visited.popleft()
        if(visited[node]==0):
            visited[node]=1
            for neighbor in graph[node]:
                if (visited[neighbor]==0):
                    moves_num[neighbor] = moves_num[node]+1
                    if(neighbor==end):
                        return moves_num[neighbor]
                    need_visited.append(neighbor)
    return -1

print(bfs(graph, target_1, target_2, visited))
