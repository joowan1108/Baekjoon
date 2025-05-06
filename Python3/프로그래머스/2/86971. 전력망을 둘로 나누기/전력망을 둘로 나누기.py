from collections import deque, defaultdict

cnt = 0
def dfs(graph, start, visited):
    global cnt
    visited.add(start)
    cnt+=1
    for adj in graph[start]:
        if adj not in visited:
            dfs(graph, adj, visited)
    
    
def solution(n, wires):
    global cnt
    result = []
    for i in range(n-1):
        graph = defaultdict(list)
        visited = set()
        for j in range(n-1):
            if j==i:
                continue
            start = wires[j][0]
            graph[wires[j][0]].append(wires[j][1])
            graph[wires[j][1]].append(wires[j][0])
        dfs(graph, start, visited)
        result.append(abs(n-2*cnt))
        cnt = 0
    return min(result)
        
        
        
        