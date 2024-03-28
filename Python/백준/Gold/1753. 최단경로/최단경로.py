import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

v,e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance = [inf for _ in range(v+1)]
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
result = dijkstra(k)
for i in range(1, v+1):
    if(result[i]==inf):
        print("INF")
    else:
        print(result[i])
