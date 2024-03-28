import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

item_lst = list(map(int, input().split()))

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

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
            new_dist = dist +  cost
            if(new_dist < distance[nod]):
                distance[nod] = new_dist
                heapq.heappush(q, (new_dist, nod))
    return distance

#i가 start 지점
max_value = 0
for i in range(1, n+1):
    distance = dijkstra(i)
    val_sum=0
    for index in range(1, len(distance)):
        if(distance[index]<=m):
            val_sum+=item_lst[index-1]
    max_value = max(max_value, val_sum)

print(max_value)
    
