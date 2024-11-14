import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int, input().split())

box = []
for _ in range(h):
	layer = []
	for _ in range(n):
		tmp = list(map(int, input().split()))
		layer.append(tmp)
	box.append(layer)


moves = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]

visited = [[[False]*m for _ in range(n)] for _ in range(h)]
def bfs(start_points):
	q = deque(start_points)
	while q:
		z,y,x = q.popleft()
		for move in moves:
			new_z,new_y, new_x = z+move[0], y+move[1], x+move[2] 
			if(0<=new_z<h and 0<=new_y<n and 0<=new_x<m and box[new_z][new_y][new_x]!=-1 and not visited[new_z][new_y][new_x]):
				visited[new_z][new_y][new_x]=True
				q.append((new_z,new_y,new_x))
				box[new_z][new_y][new_x] = box[z][y][x]+1



start = []
for i in range(h):
	for j in range(n):
		for k in range(m):
			if box[i][j][k]==1:
				start.append((i,j,k))
				visited[i][j][k]=True

bfs(start)

not_able = False

for i in range(h):
	for j in range(n):
		for k in range(m):
			if box[i][j][k]>=0 and not visited[i][j][k]:
				not_able = True

if not_able:
	print(-1)

else:
	max_ = 0
	for i in range(h):
		for j in range(n):
			for k in range(m):
				max_ = max(max_, box[i][j][k])
	print(max_-1)
				
				
	
	
	