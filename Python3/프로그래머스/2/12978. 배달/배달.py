import heapq
from collections import defaultdict, deque
INF = int(1e9)
def solution(N, road, K):
    graph = [[500005]*(N+1) for _ in range(N+1)]
    for r in road:
        from_node, to_node, weight = r
        if weight < graph[from_node][to_node] or weight < graph[to_node][from_node]:
            graph[from_node][to_node] = weight
            graph[to_node][from_node] = weight
            
    distance = [INF]*(N+1)
    visited = [False] * (N+1)
    distance[1] = 0
    q = [(0,1)]
    
    while q:
        current_weight, current_node = heapq.heappop(q)
        if visited[current_node]:
            continue
        visited[current_node] = True
        for to_node, weight in enumerate(graph[current_node]):
            new_distance = distance[current_node] + weight
            if new_distance < distance[to_node]:
                distance[to_node] = new_distance
                heapq.heappush(q, (new_distance, to_node))
    ans = [d for d in distance if d<=K]
    return len(ans)
        
    
    