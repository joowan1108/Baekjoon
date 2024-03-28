import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance = [inf for _ in range(n+1)]
    distance[start]=0
    
    while q:
        dist, node = heapq.heappop(q)
        if(distance[node] < dist):
            continue
        for nod, cost in graph[node]:
            new_dist = dist + cost
            if(new_dist < distance[nod]):
                distance[nod] = new_dist
                heapq.heappush(q, (new_dist, nod))
    return distance
distance = dijkstra(x)
result = []
for i in range(len(distance)):
    if(distance[i] == k):
        result.append(i)

if(len(result)==0):
    print(-1)
else:
    for res in result:
        print(res)
