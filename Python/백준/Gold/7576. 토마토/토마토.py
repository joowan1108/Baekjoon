import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int, input().split())

box = []
for _ in range(n):
	box.append(list(map(int, input().split())))

start_points = []

for i in range(n):
	for j in range(m):
		if box[i][j]==1:
			start_points.append((i,j))

visited = [[False]*(m) for _ in range(n)]
for i,j in start_points:
	visited[i][j]=True

moves = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs(start):
	q = deque(start)
	while q:
		y,x = q.popleft()
		for dy,dx in moves:
			new_y = y+dy
			new_x = x+dx
			if(0<=new_y<n and 0<=new_x<m and not visited[new_y][new_x] and box[new_y][new_x]!=-1):
				q.append((new_y, new_x))
				box[new_y][new_x] = box[y][x]+1
				visited[new_y][new_x]=True

bfs(start_points)

not_able = False
for i in range(n):
	for j in range(m):
		if box[i][j]>=0 and not visited[i][j]:
			not_able = True

if not_able:
	print(-1)
else:
	max_ = 0
	for i in range(n):
		for j in range(m):
			max_ = max(box[i][j], max_)
	
	print(max_-1)

	