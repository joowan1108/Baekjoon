import sys
import heapq

input = sys.stdin.readline
n = int(input())
rooms= []
for _ in range(n):
	rooms.append(list(map(int, input().strip())))
for i in range(n):
	for j in range(n):
		if rooms[i][j]==1:
			rooms[i][j]=0
		else:
			rooms[i][j]=1
moves = [(-1,0),(1,0),(0,-1),(0,1)]
def dijkstra(start_y, start_x):
	min_cost=[[float("inf") for _ in range(n)] for _ in range(n)]
	min_cost[start_y][start_x]=0
	q=[]
	heapq.heappush(q, (0,start_y,start_x))
	while q:
		cost, y, x = heapq.heappop(q)
		if min_cost[y][x]<cost:
			continue
		for dy,dx in moves:
			new_y,new_x = y+dy, x+dx
			if(0<=new_y<n and 0<=new_x<n):
				tmp_cost=cost+rooms[new_y][new_x]
				if tmp_cost<min_cost[new_y][new_x]:
					min_cost[new_y][new_x]=tmp_cost
					heapq.heappush(q,(tmp_cost, new_y, new_x))
	return min_cost[n-1][n-1]

print(dijkstra(0,0))