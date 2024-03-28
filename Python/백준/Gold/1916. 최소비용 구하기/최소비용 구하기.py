import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance = [inf for _ in range(n+1)]
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if(distance[node]<dist):
            continue
        for nod, cost in graph[node]:
            new_dist = cost + dist
            if(distance[nod] > new_dist):
                distance[nod] = new_dist
                heapq.heappush(q, (new_dist, nod))
    return distance
    
result = dijkstra(start)
print(result[end])