import sys
import heapq

input = sys.stdin.readline

n,d = map(int, input().split())
graph = [[] for _ in range(d+1)]
for i in range(d):
	graph[i].append((i+1,1))

for _ in range(n):
	start, end, cost = map(int, input().split())
	if end<=d:
		graph[start].append((end, cost))

def dijkstra(start):
	min_cost = [float("inf") for _ in range(d+1)]
	min_cost[start]=0
	q = []
	heapq.heappush(q, (0,start))
	while q:
		cost, node = heapq.heappop(q)
		if min_cost[node]<cost:
			continue
		for connected, distance in graph[node]:
			tmp_cost = cost + distance
			if tmp_cost < min_cost[connected]:
				min_cost[connected]=tmp_cost
				heapq.heappush(q, (tmp_cost, connected))
	return(min_cost[d])

print(dijkstra(0))
			