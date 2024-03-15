import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

pairs = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n+1)]

for _ in range(pairs):
    i,j = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)
    
def dfs(graph, start_node):
    result = 0
    visited = [0]*(n+1) #방문 여부 확인하기 위한 것
    need_visited = deque() #dfs를 하기 위해 필요한 stack
    
    need_visited.append(start_node) #시작
    while need_visited:
        node = need_visited.pop() #방문해야 할 node 가져오기
        if visited[node]==0: #방문한 노드가 아니라면
            result+=1 #바이러스 추가 감염
            visited[node]=1#방문 처리
            need_visited.extend(graph[node]) #방문해야 할 node들 추가
    return result
result = dfs(graph,1)
print(result-1)
        
        
    

    




