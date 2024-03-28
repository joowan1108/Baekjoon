import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

s, e = map(int, input().split())

def dijkstra(start):
    q = []
    path = [0 for _ in range(n+1)]
    #e가 어느 노드로부터 왔는지, 또 그 노드는 어디서부터 왔는지,,,,,
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
                path[nod] = node
                
    return distance, path

result, path = dijkstra(s)
print(result[e])

path_result = []
def print_path(dest):
    if(dest==s):
        path_result.append(dest)
        return 0
    path_result.append(dest)
    print_path(path[dest])

print_path(e)
path_result.reverse()

print(len(path_result))
for p in path_result:
    print(p, end=' ')
    
    

