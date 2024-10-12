import sys
from  collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
for _ in range(n):
	graph.append(list(map(int, input().strip())))

moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x_s,y_s):
	q = deque()
	q.append((x_s,y_s))
	while q:
		x,y = q.popleft()
		for move in moves:
			xx = x+move[0]
			yy = y+move[1]
			if(0<=xx<n and 0<=yy<m and graph[xx][yy]==1):
				graph[xx][yy] = graph[x][y]+1
				q.append((xx,yy))
	return graph[n-1][m-1]

result = bfs(0,0)
print(result)
		


	