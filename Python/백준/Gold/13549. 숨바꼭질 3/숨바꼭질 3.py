import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline

n, k = map(int, input().split())

def get_moves(node):
    return [(node-1,1), (node+1,1), (node*2,0)]
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance = [inf for _ in range(200001)]
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if(distance[node] < dist):
            continue
        moves = get_moves(node)
        for move,cost in moves:
            if(move<0 or move>200000):
                continue
            new_dist = dist+cost
            if(new_dist< distance[move]):
                distance[move] = new_dist
                heapq.heappush(q, (new_dist, move))
    return distance

result = dijkstra(n)
print(result[k])
