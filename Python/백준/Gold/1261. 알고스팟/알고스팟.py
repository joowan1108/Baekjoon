import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline
width,height = map(int, input().split())

graph = []
moves = [(1,0),(-1,0),(0,1),(0,-1)]
distance = [[inf for _ in range(width)] for _ in range(height)]


for _ in range(height):
    graph.append(list(map(int,list(input().rstrip()))))

def dijkstra():
    q = []
    heapq.heappush(q, (0, (0,0)))
    distance[0][0]=0
    while q:
        dist, node = heapq.heappop(q)
        if(node[0]==height-1 and node[1]==width-1):
            break
        if(distance[node[0]][node[1]] < dist):
            continue
        for dh, dw in moves:
            new_h = node[0] + dh
            new_w = node[1] + dw
            if(new_h<0 or new_h>=height or new_w<0 or new_w>=width):
                continue
            new_dist = graph[new_h][new_w] + dist
            if(new_dist < distance[new_h][new_w]):
                distance[new_h][new_w] = new_dist
                heapq.heappush(q, (new_dist, (new_h, new_w)))

dijkstra()
print(distance[height-1][width-1])


