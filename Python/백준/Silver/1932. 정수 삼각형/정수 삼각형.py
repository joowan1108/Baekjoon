import sys
import heapq
input = sys.stdin.readline

n = int(input())

triangle = [[] for _ in range(n)]
for i in range(n):
	triangle[i] = list(map(int, input().split()))
	


# for i in range(n):
# 	for j in range(len(triangle[i])):
# 		triangle[i][j]=-triangle[i][j]
		
# moves = [(1,0),(1,1)]

# def dijkstra(start_y, start_x):
# 	q=[]
# 	heapq.heappush(q, (triangle[start_y][start_x], start_y, start_x))
# 	distance = [[float("inf")]*n for _ in range(n)]
# 	distance[start_y][start_x]=0
# 	while q:
# 		dist, y,x = heapq.heappop(q)
# 		if distance[y][x]<dist:
# 			continue
# 		for dy,dx in moves:
# 			new_y, new_x = y+dy, x+dx
# 			if 0<=new_y<n and 0<=new_x<n:
# 				if triangle[new_y][new_x]+dist < distance[new_y][new_x]:
# 					distance[new_y][new_x] = triangle[new_y][new_x]+dist
# 					heapq.heappush(q, (distance[new_y][new_x], new_y, new_x))
# 	return distance
# distance = dijkstra(0,0)

# min_ = min(distance[-1])
# print(-min_)

for i in range(1,n):
	for j in range(len(triangle[i])):
		if j==0:
			triangle[i][j]+=triangle[i-1][j]
		elif j==len(triangle[i])-1:
			triangle[i][j]+=triangle[i-1][len(triangle[i-1])-1]
		else:
			triangle[i][j]=max(triangle[i-1][j], triangle[i-1][j-1])+triangle[i][j]

print(max(triangle[-1]))	
		
	