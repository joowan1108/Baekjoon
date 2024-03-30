import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

test = int(input())

def dijkstra(start, graph):
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
            if(new_dist < distance[nod]):
                distance[nod] = new_dist
                heapq.heappush(q, (new_dist, nod))
    return distance

for _ in range(test):
    n,m,t = map(int, input().split())
    
    s,g,h = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d= map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    suspects = []
    for _ in range(t):
        suspects.append(int(input()))
    distance_1 = dijkstra(s, graph)
    if(distance_1[g]!=inf):
        d1_1 = distance_1[g] #s->g
    if(distance_1[h]!=inf):
        d1_2 = distance_1[h] #s->h
    
    distance_2 = dijkstra(g, graph)
    connect = distance_2[h] #g<->h
    
    distance_3 = dijkstra(h, graph)
    result = []
    
    s_h = d1_1 + connect #s->g->h
    s_g = d1_2 + connect #s->h->g
    #목적지들끼리 비교
    for dest in suspects:
        d2 = distance_2[dest]
        d3 = distance_3[dest]
        if(d3!=inf):
            res1 = s_h + d3 #s->g->h->d
        if(d2!=inf):
            res2 = s_g + d2 #s -> h-> g->d
        res3 = distance_1[dest]
        if(res3==res1 or res3==res2):
            result.append(dest)
    result.sort()
    for r in result:
        print(r, end=' ')
    print()
    
        
        
    
