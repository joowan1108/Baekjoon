import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
place = []
moves = [(1,0), (-1,0), (0,1), (0,-1)]


for i in range(n):
	row = list(map(int, input().split()))
	place.append(row)
	if 2 in row:
		h = i
		w = row.index(2)

m

def bfs(place, start_h, start_w):
	distance = [[0]*(m) for _ in range(n)]
	q = deque()
	q.append((start_h, start_w))
	visited = [[False]*(m) for _ in range(n)]
	visited[start_h][start_w]=True
	while q:
		h_, w_ = q.popleft()
		for move_h, move_w in moves:
			new_h = h_ + move_h
			new_w = w_ + move_w
			if(0<=new_h<n and 0<=new_w<m and visited[new_h][new_w]==False and place[new_h][new_w]==1):
				visited[new_h][new_w]=True
				q.append((new_h, new_w))
				distance[new_h][new_w]=distance[h_][w_]+1
	return distance



dist = bfs(place, h, w)
for i in range(n):
	for j in range(m):
		if(place[i][j]==1 and dist[i][j]==0):
			dist[i][j]=-1

for i in range(n):
	for j in range(m):
		print(dist[i][j], end=' ')
	print()

	
