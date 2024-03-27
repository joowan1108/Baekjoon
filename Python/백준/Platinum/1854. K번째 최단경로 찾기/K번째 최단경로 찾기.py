import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

n,m,k = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[inf for _ in range(k)] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    distance[1][0] = 0
    while q:
        dist, node = heapq.heappop(q)
        for place, cost in graph[node]:
            new_dist = dist + cost
            if(distance[place][k-1] > new_dist):
                distance[place][k-1] = new_dist
                distance[place].sort()
                heapq.heappush(q, (new_dist, place))
                
dijkstra()

for i in range(1, n+1):
    if distance[i][k-1] == inf:
        print(-1)
    else:
        print(distance[i][k-1])
