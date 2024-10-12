import sys
from  collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
visited = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
	graph.append(list(map(int, input().strip())))

moves=[(1,0),(-1,0),(0,1),(0,-1)]
num_houses = []

def bfs(x,y):
	houses=1
	q = deque()
	q.append((x,y))
	visited[x][y]=1
	while q:
		a,b = q.popleft()
		for move in moves:
			aa = a + move[0]
			bb = b+move[1]
			if(0<=aa<n and 0<=bb<n and graph[aa][bb]==1 and visited[aa][bb]==0):
				q.append((aa,bb))
				visited[aa][bb]=1
				houses+=1
	num_houses.append(houses)
	
cnt = 0
for i in range(n):
	for j in range(n):
		if(graph[i][j]==1 and visited[i][j]==0):
			bfs(i,j)
			cnt+=1

print(cnt)
num_houses.sort()

for h in num_houses:
	print(h)
			
		


	