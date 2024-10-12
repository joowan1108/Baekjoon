import sys
from  collections import deque

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
	graph.append(input().strip())

moves=[(1,0),(-1,0),(0,1),(0,-1)]

# 색맹 처리한 graph 따로 만들기
graph_weird = [list(row) for row in graph]
for i in range(n):
	for j in range(n):
		if(graph_weird[i][j]=='G'):
			graph_weird[i][j]='R'
			
#bfs			
def bfs(i,j,c,visited,g):
	q = deque()
	q.append((i,j))
	visited[i][j]=1
	while q:
		x,y = q.popleft()
		for move in moves:
			xx = x+move[0]
			yy = y+move[1]
			if(0<=xx<n and 0<=yy<n and g[xx][yy]==c and visited[xx][yy]==0):
				q.append((xx,yy))
				visited[xx][yy]=1
	return visited
			
colors = ['R', 'G', 'B']
cnt_normal=0

for color in colors:
	visited_normal = [[0 for _ in range(n)] for _ in range(n)]
	for a in range(n):
		for b in range(n):
			if(graph[a][b]==color and visited_normal[a][b]==0):
				visited_normal = bfs(a,b,color,visited_normal, graph)
				cnt_normal+=1


print(cnt_normal, end=' ')

colors_weird= ['R','B']
cnt_weird = 0

for color in colors_weird:
	visited_weird = [[0 for _ in range(n)] for _ in range(n)]
	for a in range(n):
		for b in range(n):
			if(graph_weird[a][b]==color and visited_weird[a][b]==0):
				visited_weird = bfs(a,b,color, visited_weird, graph_weird)
				cnt_weird+=1

print(cnt_weird)
				
			
			
	
		


	