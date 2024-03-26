import sys
import heapq
inf = int(1e9)
input = sys.stdin.readline
moves = [(0,1), (0,-1), (1,0), (-1,0)]
problem =1
def dijkstra(n, graph):
    q = []
    heapq.heappush(q, (0,(0, 0)))
    distance = [[inf for _ in range(n)] for _ in range(n)]
    distance[0][0]=graph[0][0]
    while q:
        dist, node = heapq.heappop(q)
        if(distance[node[0]][node[1]] < dist):
            continue
        for dh, dw in moves:
            new_h = node[0]+dh
            new_w = node[1]+dw
            if(new_h<0 or new_h>=n or new_w<0 or new_w>=n):
                continue
            new_dist = distance[node[0]][node[1]] + graph[new_h][new_w]
            if(new_dist < distance[new_h][new_w]):
                distance[new_h][new_w] = new_dist
                heapq.heappush(q, (new_dist, (new_h, new_w)))
    return distance[n-1][n-1]

while True:
    n = int(input())
    if(n==0):
        break
    graph = []
    for _ in range(n):
        input_lst = map(int, input().split())
        graph.append(list(input_lst))
    print("Problem {}: {}".format(problem,dijkstra(n, graph)))
    problem+=1


