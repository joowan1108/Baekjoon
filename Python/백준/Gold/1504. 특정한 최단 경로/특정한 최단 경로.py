import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

#start -> v1, v1->v2, v2->end
#start -> v2, v2 -> v1, v1->end
#v1와 v2를 잇는게 없다면, -1

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance = [inf for _ in range(n+1)]
    distance[start]=0
    while q:
        dist, node = heapq.heappop(q)
        if(distance[node] < dist):
            continue
        for nod, cost in graph[node]:
            new_dist = cost + dist
            if(new_dist < distance[nod]):
                distance[nod] = new_dist
                heapq.heappush(q, (new_dist, nod))
    return distance

#case 1
case_1 = 1
result1, result2, result3 = dijkstra(1), dijkstra(v1), dijkstra(v2)
start_to_v1, v1_to_v2, v2_to_end = result1[v1], result2[v2], result3[n]
if inf in [start_to_v1, v1_to_v2, v2_to_end]:
    case_1 = 0
compare_1 = start_to_v1 + v1_to_v2 + v2_to_end

#case 2
case_2 = 1
result1, result2, result3 = dijkstra(1), dijkstra(v2), dijkstra(v1)
start_to_v2, v2_to_v1, v1_to_end = result1[v2], result2[v1], result3[n]
if inf in [start_to_v2, v2_to_v1, v1_to_end]:
    case_2 = 0
compare_2 = start_to_v2 + v2_to_v1 + v1_to_end

if(case_1==0 and case_2==1):
    print(compare_2)
elif(case_1==1 and case_2==0):
    print(compare_2)
elif(case_1==1 and case_2==1):
    print(min(compare_1, compare_2))
else:
    print(-1)
    
